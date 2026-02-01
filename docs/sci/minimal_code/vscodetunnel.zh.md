#  VS Code Tunnel 


远程电脑下载vscode. 运行
```bash
code tunnel
```
然后github账号登录. 

其他设备就可以通过给出的链接访问远程的 VS Code 了.

## 将 VS Code Tunnel 作为系统服务运行


code tunnel 允许你从本地的 VS Code 连接到远程的 VS Code Server，从而实现远程开发。

如果你直接运行 code tunnel，当你把这个终端窗口（或者 SSH 会话）关掉时，连接就断了。

作为一个 Linux 用户，你肯定希望它像 systemd 服务一样在后台静默运行.

```bash
code tunnel service install
```


```
smsimulator5.5 on  main [$] via △ v4.2.1 via 🅒 anaroot-env took 1h35m41s 
❯ code tunnel service install
*
* Visual Studio Code Server
*
* By using the software, you agree to
* the Visual Studio Code Server License Terms (https://aka.ms/vscode-server-license) and
* the Microsoft Privacy Statement (https://privacy.microsoft.com/en-US/privacystatement).
*
[2026-02-01 22:53:06] info Successfully registered service...
[2026-02-01 22:53:07] info Successfully enabled unit files...
[2026-02-01 22:53:07] info Tunnel service successfully started
Service successfully installed! You can use `code tunnel service log` to monitor it, and `code tunnel service uninstall` to remove it.
```