# Debian 系统连接网络打印机（Fuji Xerox DocuPrint C3360）

本教程说明如何在 Debian 上通过 CUPS 配置内网网络打印机（以 Fuji Xerox DocuPrint C3360 为例）。

https://wiki.debian.org/SystemPrinting

## 一、环境准备

在开始前请确保已安装并启用 CUPS 服务。

1. 安装 CUPS
```bash
sudo apt update
sudo apt install cups
```

2. 启动并启用服务
```bash
sudo systemctl enable cups
sudo systemctl start cups
sudo systemctl status cups   # 检查状态，应显示 active (running)
```

3. 配置权限
```bash
sudo usermod -aG lpadmin $(whoami)
```
> 注意：执行后建议注销并重新登录或重启，使权限生效。

## 二、获取打印机信息

需要知道打印机的内网 IP 地址。示例 IP：`172.27.227.180`

获取方法：
- 在打印机面板的“网络设置”或“TCP/IP 设置”中查看。
- 在路由器管理后台的设备列表中查看。

## 三、通过 CUPS Web 界面添加打印机

1. 打开 CUPS 管理页面：`http://localhost:631`

2. 进入 Administration -> Add Printer（需要系统用户名/密码验证）。

3. 选择连接协议（常用）：
- `AppSocket/HP JetDirect`（最常用）
- `LPD/LPR Host or Printer`

4. 输入连接地址（Connection）：
- AppSocket：`socket://172.27.227.180`
- LPD/LPR：`lpd://172.27.227.180/`

5. 填写打印机信息：
- Name: `DocuPrint_C3360`（不可包含空格）
- Description: `Fuji Xerox DocuPrint C3360`
- Location: 可选（如 `Office`）

## 四、驱动程序选择（关键）

- 情况 A：使用厂商驱动  
    在 Make 列表选择 `Fuji Xerox` 或 `Xerox`，并在型号中选 `DocuPrint C3360`（如有）。

- 情况 B：使用通用驱动（推荐）  
    若找不到准确型号，选择 `Generic` -> `Generic PostScript Printer`（或带 PCL6 的驱动）。此类彩色激光机通常支持 PostScript。

- 情况 C：手动提供 PPD 文件  
    如果有官方 `.ppd` 文件，在上传 PPD 后点击 Add Printer。

## 五、测试与保存设置

1. 设置默认选项（例如纸张 A4，颜色 Color），点击 Set Default Options。  
2. 在打印机详情页的 Maintenance 菜单中选择 Print Test Page。  
3. 如果打印成功，则配置完成。

## 常见问题排查

- 无法访问 `http://localhost:631`：检查 CUPS 是否运行（`sudo systemctl status cups`）。  
- 打印乱码：通常为驱动不匹配，尝试切换到 `Generic PostScript Printer`。  
- 权限不足：确认已执行 `usermod -aG lpadmin $(whoami)` 并重新登录会话。
- 若仍有问题，查看 CUPS 日志：`/var/log/cups/error_log`（可能需要 root 权限）。

