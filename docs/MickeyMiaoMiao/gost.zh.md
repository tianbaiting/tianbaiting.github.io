# gost 代理

## 安装

在 x86_64 Linux 系统下安装 gost 的步骤如下：

```bash
# 创建目录并进入
mkdir -p ~/bin && cd ~/bin

# 下载 gost（示例 v2.11.5）
wget https://github.com/ginuerzh/gost/releases/download/v2.11.5/gost-linux-amd64-2.11.5.gz

# 解压、重命名并赋予执行权限
gunzip gost-linux-amd64-2.11.5.gz
mv gost-linux-amd64-2.11.5 gost
chmod +x gost
```

## 服务器运行

示例：开启一个代理。假设端口为 28888（>1024），账号为 `myuser`，密码为 `mypass`。
也可以不设置密码.

命令格式（示例）：
```bash
# 格式：./gost -L <协议>://<账号>:<密码>@:<端口>
# <协议>可选http、socks5等
./gost -L <protocol>://myuser:mypass@:28888
```


为了后台运行，可以使用 `nohup`：
```bash
nohup ./gost -L <protocol>://myuser:mypass@:28888 > gost.log 2>&1 &
```



也可以使用 tmux、screen 等终端复用工具以便管理后台进程。

## 本地使用

### 建立映射（把远程服务器的 28888 映射到本地 28888）

方式一：在本地运行 gost 将流量转发到远程服务器（示例）：
```bash
./gost -L=:28888 -F=socks5://<服务器IP>:28888
```

方式二：使用 SSH 本地端口转发（将远程 28888 拉到本地）：
```bash
# 格式：ssh -L 本地端口:127.0.0.1:远程gost端口 用户@服务器IP
ssh -L 28888:127.0.0.1:28888 user@server_ip
```

### 设置代理

浏览器单独设置（仅让浏览器走代理，不影响其他应用）：

- 推荐使用 Chrome/Edge 搭配 SwitchyOmega 插件。
- 步骤概述：
    1. 在浏览器扩展商店安装 "Proxy SwitchyOmega"。
    2. 打开插件 -> Options -> 新建情景模式。
    3. 协议选择 SOCKS5（推荐），服务器填写 `127.0.0.1`，端口填写 `28888`。
    4. 如服务端设置了账号密码，点击锁状图标填写；否则跳过。
    5. 保存并启用该情景模式，访问网页时流量将通过本地 127.0.0.1:28888 -> SSH 隧道 -> 远程服务器 -> 目标网站。


全局设置（让整个系统流量走代理）：

Windows：
1. 设置 -> 网络和 Internet -> 代理。
2. 手动设置代理：地址 `127.0.0.1`，端口 `28888`，保存。
3. 注意：Windows 的系统代理通常只对 HTTP/HTTPS 生效。若需对所有应用生效，可使用 Proxifier 等第三方工具，或在“Internet 选项”->“连接”->“局域网设置”->“高级”中在 SOCKS 一栏填写 `127.0.0.1:28888`。

macOS：
1. 系统偏好设置 -> 网络。
2. 选择当前网络 -> 高级 -> 代理。
3. 勾选 SOCKS 代理，服务器 `127.0.0.1`，端口 `28888`，确认并应用。

命令行（Linux / macOS）：

```bash
export http_proxy="http://127.0.0.1:28888"
export https_proxy="http://127.0.0.1:28888"
export all_proxy="socks5://127.0.0.1:28888"
```
