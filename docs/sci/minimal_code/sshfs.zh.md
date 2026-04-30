# sshfs：把远程目录当本地盘用

`sshfs` 走 SSH/SFTP 协议，把远程主机的某个目录挂到本地一个空目录上。挂上之后用 `ls`、`vim`、`code .`、文件管理器，行为和本地目录几乎没差别——背后每次读写都通过 SSH 连接转发。比 `scp` 来回传方便，比 NFS/Samba 不用动服务端配置。

## 安装

```bash
# Debian / Ubuntu
sudo apt install sshfs

# Fedora / RHEL
sudo dnf install fuse-sshfs

# macOS（需要先装 macFUSE）
brew install --cask macfuse
brew install gromgit/fuse/sshfs-mac
```

挂载靠 FUSE，所以本地内核需要有 `fuse` 模块，普通发行版默认就有。

## 最小用法：mount

```bash
mkdir -p ~/mnt/server                       # 本地挂载点，必须是空目录
sshfs user@host:/remote/path  ~/mnt/server  # 把远程目录挂上来
```

挂载后 `~/mnt/server` 里看到的就是远程 `/remote/path` 的内容。

常用选项：

```bash
sshfs user@host:/data ~/mnt/server \
    -p 2222 \                       # 远程 SSH 端口非 22
    -o reconnect \                  # 网络抖动后自动重连
    -o ServerAliveInterval=15 \     # 每 15s 发一次 keepalive
    -o ServerAliveCountMax=3 \      # 3 次没回应就判死
    -o follow_symlinks \            # 远程符号链接当真实文件穿透
    -o cache=yes \                  # 客户端缓存元数据，减少 RTT
    -o IdentityFile=~/.ssh/id_ed25519
```

挂载点路径：远端只写主机名（`host:`）等价于挂远端家目录；写 `host:/` 挂根；写相对路径以家目录为基准。

## 卸载：unmount

```bash
fusermount -u ~/mnt/server      # Linux 推荐
# 或
umount ~/mnt/server             # 需要 root，或挂载时加了 allow_other
```

macOS 上：

```bash
umount ~/mnt/server
# 或强制
diskutil unmount force ~/mnt/server
```

如果提示 `device is busy`，是有进程还在占用挂载点。要么 `cd` 走开、关掉打开远程文件的编辑器，要么：

```bash
fusermount -uz ~/mnt/server     # 懒卸载，先解绑命名空间，进程退出后再真正释放
```

## 写到 fstab 自动挂载（可选）

```fstab
user@host:/data  /home/me/mnt/server  fuse.sshfs  noauto,x-systemd.automount,_netdev,users,idmap=user,IdentityFile=/home/me/.ssh/id_ed25519,allow_other,reconnect  0  0
```

`x-systemd.automount` 让它按需挂载，避免开机时网络没起来卡住启动。

## 为什么远程 `.bashrc` 第一行就要短路：非交互保护

sshfs 建连时实际上在远端跑一个非交互的 shell 启动 `sftp-server`。SSH 会把远端的启动文件（bash 是 `~/.bashrc`，因为 OpenSSH 对非交互非登录会话默认读 `.bashrc`）执行一遍。

**关键陷阱**：如果 `.bashrc` 里有任何往 stdout/stderr 输出的命令——`echo "welcome"`、`fortune`、`neofetch`、`conda` 的初始化打印、`source` 一个会 echo 的脚本——这些字节会污染 SFTP 协议流，sshfs 直接挂掉，报：

```
read: Connection reset by peer
remote host has disconnected
```

或者挂上但每个操作都报 `Input/output error`。

解决方案：在远端 `.bashrc` **最顶部**加一行守卫，让非交互 shell 立刻返回，跳过后续所有逻辑：

```bash
# ~/.bashrc 第一行
case $- in
    *i*) ;;     # 交互式 shell：$- 包含 'i'，什么都不做，继续往下
    *) return;; # 非交互（sshfs/scp/rsync/ssh host cmd）：直接 return
esac

# ↓ 下面所有 alias / PS1 / source / echo 都只对交互式生效
alias ll='ls -la'
PS1='\u@\h:\w\$ '
# ...
```

`$-` 是 bash 的当前 shell 选项标志。交互式 shell 包含 `i`，非交互式没有。`return` 在被 `source` 的脚本里直接退出当前文件而不退出 shell，正是这里需要的语义。

> Debian/Ubuntu 默认的 `~/.bashrc` 模板第一段就长这样，不是巧合——就是为了不破坏 scp/sshfs/rsync。如果你曾经手贱把它删了，现在加回去。

### 自检：远程的非交互 shell 是不是干净的

从本地跑一发：

```bash
ssh user@host 'true' | xxd | head
```

正常情况是空输出（`true` 不打印任何东西）。如果有任何字节，说明 `.bashrc`（或 `.bash_profile`、`.profile`、系统级 `/etc/profile.d/*.sh`）里有人在非交互路径上 echo，sshfs 一定会出问题。逐个二分注释找出元凶。

## 常见报错速查

| 现象 | 原因 | 处理 |
|---|---|---|
| `read: Connection reset by peer` 一连上就断 | 远端启动文件污染 stdout | 加上面那段 `case $- in` 守卫 |
| `Transport endpoint is not connected` | 网络掉了，挂载点僵死 | `fusermount -uz` 卸掉再挂 |
| `Input/output error` 偶发 | 长连接被中间防火墙 NAT 超时切断 | 加 `-o reconnect -o ServerAliveInterval=15` |
| `fuse: device not found` | 内核没装 fuse 模块 | `modprobe fuse` 或装内核 modules-extra 包 |
| 性能很差（cd / ls 都卡） | 元数据每次都跑一次 RTT | `-o cache=yes -o kernel_cache -o compression=no`（局域网压缩反而更慢） |

## 一句话总结

`sshfs host:path mnt` 挂、`fusermount -u mnt` 卸；远端 `.bashrc` 顶部务必有非交互短路，否则 sshfs/scp/rsync 都会神秘失败。
