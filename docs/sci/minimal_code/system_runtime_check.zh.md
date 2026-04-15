# 如何查找当前运行的进程、程序与远程会话

当你问“这台机器现在到底在跑什么”时，通常不要只看一条命令。最稳妥的做法是同时从下面五个角度看：

1. 进程：当前有哪些程序正在运行。
2. 会话：这些程序属于哪个登录会话。
3. 端口：哪些服务在监听，哪些连接已经建立。
4. 资源：谁在占 CPU、内存、运行时间。
5. 数据：模拟任务有没有在持续产出 `.root`、`.csv` 之类的数据文件。

下面这套方法适合 Linux 主机，尤其适合排查：

- SSH 登录之后后台到底还跑着什么
- XRDP 远程桌面里开了哪些程序
- `tmux` 里是否还挂着分析或模拟任务
- Geant4、smsimulator、ROOT、Python 脚本是否还在跑

## 一屏快速看当前运行了什么

先跑下面这一组：

```bash
ps -eo pid,ppid,user,tty,stat,etime,cmd --sort=etime
pgrep -af 'ssh|sshd|xrdp|xrdp-sesman|tmux|python|root|geant4|smsimulator|anaroot|code-tunnel|tailscaled'
ss -tulpn
ss -tnp
loginctl list-sessions
```

这五条命令分别回答：

- `ps -eo ...`：现在有哪些进程，它们是谁启动的，活了多久，完整命令行是什么。
- `pgrep -af ...`：快速按名字抓关键进程。
- `ss -tulpn`：哪些端口在监听。
- `ss -tnp`：哪些 TCP 连接已经建立。
- `loginctl list-sessions`：当前有哪些登录会话。

如果你只想先快速扫一眼，最常用的两条通常是：

```bash
ps -ef
pgrep -af '<关键词>'
```

## 1. 如何按名字找进程

### 最直接的方法：`pgrep -af`

```bash
pgrep -af ssh
pgrep -af xrdp
pgrep -af tmux
pgrep -af python
pgrep -af root
pgrep -af 'smsimulator|geant4|anaroot'
```

这里推荐 `pgrep -af`，因为它会直接显示：

- 进程 PID
- 完整命令行

比起下面这种写法更干净：

```bash
ps -ef | grep ssh
```

因为 `ps | grep` 很容易把 `grep` 自己也匹配出来。

### 查某一类远程相关程序

```bash
pgrep -af '(^|/)(ssh|sshd|sftp|scp|xrdp|xrdp-sesman|xfreerdp|wlfreerdp|remmina|gnome-remote-desktop|krdc)( |$)|sshfs|rdesktop'
```

这条适合一次性扫：

- SSH 客户端/服务端
- XRDP
- 常见 RDP 客户端
- 远程文件系统挂载

## 2. 如何看一个进程到底是谁启动的

推荐用：

```bash
ps -eo pid,ppid,user,tty,stat,etime,cmd --sort=etime
```

各字段含义：

- `PID`：当前进程编号。
- `PPID`：父进程编号，能帮助你看出是谁拉起了它。
- `USER`：属于哪个用户。
- `TTY`：从哪个终端起来的；图形桌面进程通常不是普通 TTY。
- `STAT`：状态，例如 `S`、`R`、`Ss`、`Sl`。
- `ETIME`：已经运行了多久。
- `CMD`：完整命令行。

### 为什么 `PPID` 很重要

如果你看到：

- 一个 `tmux` 挂在 `sshd` 会话下面
- 一个 `i3`、`xrdp-chansrv`、`i3bar` 挂在 XRDP 会话下面

那通常就能推断出：

- 这个任务来自 SSH
- 或者这个任务属于远程桌面

### 只看某个 PID 的详情

```bash
ps -fp 12345
```

如果你已经知道某个 PID，这条最省事。

### 看父子进程树

```bash
ps -eo pid,ppid,user,tty,stat,etime,cmd --forest
```

如果系统装了 `pstree`，也很方便：

```bash
pstree -ap
pstree -ap 12345
```

## 3. 如何看谁最占资源

### 动态查看

```bash
top
```

如果装了 `htop`，交互体验会更好：

```bash
htop
```

### 静态排序查看

按 CPU 排序：

```bash
ps -eo pid,ppid,user,%cpu,%mem,etime,cmd --sort=-%cpu | head -n 20
```

按内存排序：

```bash
ps -eo pid,ppid,user,%cpu,%mem,etime,cmd --sort=-%mem | head -n 20
```

按运行时长排序：

```bash
ps -eo pid,ppid,user,etime,cmd --sort=-etime | head -n 20
```

这几条特别适合找：

- 跑了几天的后台任务
- 吃满 CPU 的模拟程序
- 内存泄漏或异常占用

## 4. 如何看系统服务本身在不在

进程在，不一定代表 systemd 服务正常；反过来，服务显示 active，也不一定代表现在有客户端连接。

### 看正在运行的服务

```bash
systemctl --type=service --state=running
```

### 单独看某个服务

```bash
systemctl status ssh
systemctl status xrdp
systemctl status xrdp-sesman
systemctl status tailscaled
```

这里常见的误判是：

- `sshd` 正在运行，只能说明 SSH 服务开着
- `xrdp` 正在运行，只能说明 RDP 服务开着

它们都不等于“现在有人连着”

## 5. 如何看端口和活动连接

### 看谁在监听

```bash
ss -tulpn
```

重点看：

- `22`：SSH
- `3389`：XRDP / RDP
- 其他你自己服务的端口

例如：

- `0.0.0.0:22` 或 `[::]:22` 说明 SSH 在监听
- `*:3389` 说明 XRDP 在监听

### 看哪些连接已经建立

```bash
ss -tnp
```

重点看状态：

- `ESTAB`：连接已建立
- `CLOSE-WAIT`：对端已经发起关闭，本地还没收尾
- `FIN-WAIT-2`：正在关闭

对于 SSH/RDP 排查，最关键的区别是：

- 监听端口：服务开着
- `ESTAB` 连接：此刻真的有人连着

## 6. 如何看登录会话里跑了什么

这一步非常重要，因为“进程存在”不代表你知道它属于哪个登录场景。

### 列出所有会话

```bash
loginctl list-sessions
```

这会列出 session id，例如：

- 本地桌面会话
- SSH 会话
- XRDP 会话
- 正在关闭但还没完全清理掉的残留会话

### 看某个会话的元数据

```bash
loginctl show-session <session-id> -p Id -p User -p Name -p Seat -p Remote -p RemoteHost -p Service -p Type -p Class -p State -p Leader -p Display
```

重点字段解释：

- `Remote=yes`：远程会话
- `Remote=no`：本地会话
- `RemoteHost=`：远程来源地址
- `Service=sshd`：这是 SSH 登录
- `Service=xrdp-sesman`：这是 XRDP 桌面
- `Seat=seat0`：通常表示本地物理桌面
- `State=active`：当前活跃
- `State=closing`：会话正在关闭，但里面可能还有残留进程
- `Display=:10`：图形显示编号，XRDP/X11 常见
- `Leader=`：这个会话的主进程 PID

### 直接看会话里的进程

```bash
loginctl session-status <session-id>
```

这是查“这个桌面里到底开了哪些程序”的最好用方法之一。

## 7. SSH 场景：怎么判断 SSH 断了，但任务还在跑

### 先看 SSH 服务是否在监听

```bash
ss -tulpn | rg ':22'
```

### 再看是否有活动连接

```bash
ss -tnp | rg ':22'
```

如果这里没有 `ESTAB` 的 `:22` 连接，通常说明当前没有活跃 SSH 会话。

### 但 SSH 断了，不代表任务没了

很多时候你会在旧 SSH 会话里启动：

- `tmux`
- `screen`
- `nohup python ...`
- 后台分析脚本

所以还要结合：

```bash
loginctl list-sessions
loginctl session-status <ssh-session-id>
pgrep -af tmux
```

如果某个 SSH session 已经是 `closing`，但里面还挂着 `tmux`，这说明：

- SSH 传输层断了
- 会话残留还在
- 任务可能还在继续跑

### 看 SSH 断开的时间

```bash
journalctl -u ssh --since "2026-03-01"
last -a
```

如果是 `sshd-session` 打出来的超时或读错误日志，通常能看到远端 IP 和断开时间。

## 8. XRDP 场景：怎么查看远程桌面里打开了哪些应用

### 先看 XRDP 服务

```bash
pgrep -af xrdp
systemctl status xrdp
systemctl status xrdp-sesman
ss -tulpn | rg ':3389'
```

### 再看 XRDP 会话本身

```bash
loginctl list-sessions
loginctl show-session <session-id> -p Remote -p RemoteHost -p Service -p Display -p State -p Leader
loginctl session-status <session-id>
```

如果 `Service=xrdp-sesman` 且 `Remote=yes`，那就是 XRDP 会话。

`loginctl session-status <id>` 往往能直接列出：

- 窗口管理器，如 `i3`
- XRDP 通道程序，如 `xrdp-chansrv`
- 托盘程序，如 `pasystray`
- 剪贴板程序，如 `clipit`
- 后台同步程序
- 浏览器、编辑器、文件管理器等 GUI 程序

如果你想看得更细，可以配合 `Leader=` 的 PID，再查进程树：

```bash
ps -eo pid,ppid,user,tty,stat,etime,cmd --forest | less
```

## 9. 如何看模拟任务和分析任务是不是还在跑

### 先按名字扫

```bash
pgrep -af 'smsimulator|geant4|anaroot|root|python|tmux'
```

### 再看完整命令行和运行时长

```bash
ps -eo pid,ppid,user,%cpu,%mem,etime,cmd --sort=-etime | rg 'smsimulator|geant4|anaroot|root|python|tmux'
```

### 如果任务藏在 `tmux` 里

```bash
pgrep -af tmux
tmux ls
```

如果当前用户没有 `tmux` 会话权限或环境不对，先回到对应用户下再查。

### 看输出文件是否还在增长

如果你怀疑某个模拟在持续写数据，可以同时查最近输出：

```bash
find . -type f \( -name '*.root' -o -name '*.ridf' -o -name '*.csv' \) -printf '%TY-%Tm-%Td %TH:%TM %p\n' | sort | tail -n 30
```

如果你知道输出目录，更推荐只查特定路径，避免扫太慢。

## 10. 如何看模拟数据本身包含什么

对于 ROOT 文件，先不要急着写代码；先看结构。

已有两篇相关文档可以一起看：

- [CERN ROOT 数据结构](cernrootData.zh.md)
- [ROOT 可视化 Geant4 数据](root_visual_geant4.zh.md)

如果是 smsimulator 体系，也建议参考仓库内文档：

- `docs/sci/project/samurai/smsimulator/smsimulator.zh.md`

根据现有资料，smsimulator 的输出通常会包含：

- Geant4 步骤
- 参数
- 从 Geant4 步骤转换得到的可观测量

如果觉得文件太大，可以检查是否关闭了步骤存储：

```text
/action/data/NEBULA/StoreSteps false
NEBULASimDatainitializer::SetDataStore(false)
```

### ROOT 文件结构排查常用方法

进入 ROOT 之后，常用的是：

```cpp
TTree::Print()
TTree::Show(0)
TTree::Scan("branch_name")
tree->GetListOfBranches()
```

如果你不清楚分支结构，先用 `TBrowser` 看最省事。

## 11. 常见误判

### 误判 1：服务开着，就以为有人连着

错。

- `sshd` 在监听，只说明 SSH 服务开了
- `xrdp` 在监听，只说明 RDP 服务开了

真正是否有人在连，要看 `ss -tnp` 的 `ESTAB`。

### 误判 2：`w` 没显示，就以为没人

也不一定。

`w` 和 `who` 对 GUI、XRDP、残留会话、某些 systemd session 的表达并不完整。  
排查远程桌面时，`loginctl` 往往更准。

### 误判 3：会话是 `closing`，就以为任务没了

错。

很多时候 `closing` 会话里还残留：

- `tmux`
- 后台 Python 任务
- 分析程序

### 误判 4：只看端口，不看会话

端口只能告诉你“服务是否暴露”，不能告诉你“具体哪个桌面里开了哪些应用”。

### 误判 5：在容器或沙箱里直接跑 `loginctl` / `ss`

如果返回 `Operation not permitted`，通常不是命令错了，而是环境受限。  
这类命令最好直接在宿主机 shell 执行。

## 附录：这台机器在 2026-04-02 的实际检查示例

下面这段不是实时状态，而是一份固定示例，目的是演示上面这些命令怎么组合判断。

### 先看到服务层

已确认：

- SSH 正在监听 `22`
- XRDP 正在监听 `3389`

这说明两项远程服务都开着，但这还不能证明当前真的有活动连接。

### 再看会话层

`loginctl list-sessions` 查到 5 个 session，其中关键的是：

- `82`：本地桌面，会话状态 `active`，`Remote=no`，`Seat=seat0`
- `60`：本地桌面残留，会话状态 `closing`，`Remote=no`，`Seat=seat0`
- `c21`：XRDP 远程桌面，会话状态 `active`
- `181`：旧 SSH 会话，会话状态 `closing`

### XRDP 会话 `c21`

已确认元数据如下：

- `Id=c21`
- `Remote=yes`
- `RemoteHost=::ffff:100.115.0.17`
- `Service=xrdp-sesman`
- `Display=:10`
- `Type=x11`
- `State=active`
- 会话从 `2026-03-26 22:38:55 JST` 开始存在

这个会话里看到的主要程序有：

- `i3`
- `xrdp-chansrv`
- `ssh-agent`
- `xss-lock`
- `i3lock`
- `i3bar`
- `i3status`
- `pasystray`
- `clipit`
- Nutstore 的 Python daemon、Java GUI、WebKit 相关进程

这说明当前确实有一条活动的 XRDP 桌面，而且桌面环境内还有同步和托盘类应用在运行。

### SSH 会话 `181`

已确认元数据如下：

- `Id=181`
- `Remote=yes`
- `RemoteHost=100.92.16.91`
- `Service=sshd`
- `Type=tty`
- `State=closing`
- 会话开始于 `2026-03-06 20:41:33 JST`

虽然这个 SSH 会话已经不活跃，但 `loginctl session-status 181` 里还看到：

```text
tmux new -s nn_train
```

并且日志里记录到：

- `2026-03-07 05:26:05 JST`
- 远端 `100.92.16.91`
- `Read error from remote host ... Connection timed out`

这说明：

- SSH 连接本身早就断了
- 但是会话残留还在
- 至少有一个 `tmux` 任务被留下来了

### 对这台机器的结论

截至 `2026-04-02 18:11 JST` 这次检查：

- 有 1 条明确活动中的 XRDP 远程桌面会话
- 当前没有看到活动中的 SSH `ESTAB` 连接
- 但有 1 条旧 SSH 会话处于 `closing`，里面残留了 `tmux`

此外还额外看到：

- `tailscaled` 正在运行
- `code-tunnel` 存在外连

它们说明这台机器还开着其他远程访问或远程开发能力，但不属于本文主体。
