# FreeRDP 正确退出

用 `xfreerdp` / `wlfreerdp` 连 Linux 上的 `xrdp` 服务时，关窗口和注销是两件不同的事。混用会留下幽灵进程、占内存，或者反过来——以为只是临时离开，结果上下文全没了。

## 服务端发生了什么

Debian 上 `xrdp` 的默认配置（见 `/etc/xrdp/sesman.ini`）：

```ini
[Sessions]
X11DisplayOffset=10        # 远程会话从 :10 开始
KillDisconnected=false     # 断线后 session 不死
DisconnectedTimeLimit=0    # 不自动定时清理
```

也就是：断线 ≠ 注销。断线只是切掉了 client ↔ xrdp 的 TCP 连接；服务端的 X server、窗口管理器、所有打开的 brave/code/编辑器、private dbus-daemon——全都继续在跑，等你下次连回来 resume。

如果你的 dotfile 里给 XRDP session 配了独立 dbus（例如 `bin/rdp-session-bus`），那个 dbus-daemon 也只在「真正注销」时才被回收。

## 两种正确的退出方式

| 操作 | 服务端结果 | 适用场景 |
|---|---|---|
| Disconnect（断线）：直接关 freerdp 窗口 | session 留着，所有进程继续跑，下次连回来秒恢复 | 绝大多数时候用这个——这是 RDP 的核心价值 |
| Logout（注销）：在远程桌面里执行 WM 退出 | WM 退出 → `.xsession` 退出 → cleanup hook 触发 → dbus-daemon、socket 文件被回收 → xrdp-sesman 收尸整个 X server | 不再需要这个 session；机器要重启；怀疑状态污染想要全新一次 |

### 怎么 logout

i3 用户：

```bash
i3-msg exit
```

或绑定的快捷键（参考 `i3 config`，常见是 `Mod+Shift+E`，会弹一个 `i3-nagbar` 让你二次确认）。

GNOME / KDE 等：从右上角菜单选「注销」。

## 不推荐的几种「退出」

- `kill -9 xfreerdp`：等同 disconnect，只是更粗暴。没必要。
- `Ctrl+Alt+End`：在 Windows 客户端是 `Ctrl+Alt+Del` 的远端等价键，对 Linux/i3 桌面没意义，不会触发任何注销逻辑。
- 直接拔网线 / 关物理机：服务端走 TCP 超时判 disconnect，行为同 disconnect。但本地正在 flush 的进程（同步盘、未保存的编辑器）可能丢数据。少用。

## 边角

### 我想断线一段时间后自动清理

把 `/etc/xrdp/sesman.ini` 改成：

```ini
KillDisconnected=true
DisconnectedTimeLimit=86400   # 24 小时后强制清掉断线 session
```

代价：你以为可以「换地方继续」的远程，超时后变成全新 session，所有上下文丢失。只有当你主要价值在干净状态、不在 session resume 时才开启。

### 我注销了，下次连接会怎样？

`xrdp` 看到没有 disconnected session 留着，会起一个全新 X server，跑你的 `.xsession`，重新启动 i3 + autostart 里所有东西。等同于一次完整登录。

### 我断线了，从另一台机器连接上行不行？

行——`xrdp` 会把那个持久 session 接管给新 client。原来那台 client 即使再连也只能拿到「session 已被接管」提示。所以你不需要先回到原 client 再断线。

### 怎么判断当前 session 是「断线复用」还是「全新」？

```bash
ps -o etime= -p $$
```

在远程桌面里开个终端跑这个，看你的 shell 已经活了多久。如果显示几小时甚至几天 → 是复用的旧 session；如果显示几秒 → 是全新登录。

## 一句话总结

默认 disconnect（关窗口），偶尔 `Mod+Shift+E` 注销做一次大扫除。session resume 是 RDP 区别于 SSH 的核心特性，别因为不熟悉退出语义而错误使用。
