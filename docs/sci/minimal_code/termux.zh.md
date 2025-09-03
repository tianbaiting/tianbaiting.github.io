# 在 Termux 中安装 Ubuntu 桌面环境并运行 VS Code 的终极指南

这份文档总结了从零开始，在 Termux 中部署一个完整的 Ubuntu 图形化桌面环境，并成功运行 Visual Studio Code 的所有步骤。本文档包含了针对常见问题（特别是三星设备的后台限制和 VNC 显示问题）的最终解决方案。

---

## 目录
1.  [**第一部分：准备工作**](#part1)
2.  [**第二部分：安装 Ubuntu 和 XFCE 桌面环境**](#part2)
3.  [**第三部分：配置并启动 VNC 图形界面**](#part3)
4.  [**第四部分：连接到 Ubuntu 桌面**](#part4)
5.  [**第五部分：安装并配置 Visual Studio Code**](#part5)
6.  [**第六部分：安卓系统稳定性设置 (防后台查杀)**](#part6)
7.  [**第七部分：日常使用流程备忘录**](#part7)

---

<a name="part1"></a>
## 第一部分：准备工作

1.  **安装 Termux**: 从 F-Droid 或 GitHub 安装最新版的 Termux。
    > **注意**: Google Play 版本的 Termux 已停止更新，不推荐使用。

2.  **安装 AnLinux**: 从 Google Play 商店安装 AnLinux 应用。它能为我们方便地生成安装脚本。

3.  **更换 Termux 软件源 (可选但推荐)**:
    为了提高下载速度，建议更换为国内镜像源。
    ```bash
    termux-change-repo
    ```

---

<a name="part2"></a>
## 第二部分：安装 Ubuntu 和 XFCE 桌面环境

1.  **生成并运行 Ubuntu 安装脚本**:
    * 打开 AnLinux 应用，选择 Ubuntu。
    * 点击“复制”按钮，复制安装命令。
    * 粘贴到 Termux 中并运行。
    ```bash
    # AnLinux 生成的命令示例
    pkg install wget openssl-tool proot -y && hash -r && wget [https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh](https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh) && bash ubuntu.sh
    ```

2.  **启动 Ubuntu**:
    安装完成后，使用以下命令进入 Ubuntu 环境。
    ```bash
    ./start-ubuntu.sh
    ```

3.  **安装 XFCE 桌面环境及必要工具**:
    * 仍在 AnLinux 中，选择 `Desktop Environment -> XFCE`，复制其安装命令。
    * 粘贴到 **Ubuntu 的 shell** 中（提示符为 `root@localhost:~#`）并运行。
    ```bash
    # 进入 Ubuntu 环境后运行
    apt-get update && apt-get install -y xfce4 xfce4-goodies
    ```
    * 我们还需要安装一些其他工具。
    ```bash
    apt-get install -y sudo nano wget curl
    ```

---

<a name="part3"></a>
## 第三部分：配置并启动 VNC 图形界面

这是最关键的一步，我们将直接写入正确的配置，以避免“黑白网格”和“无法启动”等问题。

1.  **安装 VNC 服务器**:
    ```bash
    apt-get install -y tigervnc-standalone-server
    ```

2.  **首次运行 VNC 服务器以生成配置文件**:
    ```bash
    vncserver :1
    ```
    > 系统会提示您设置一个 VNC 连接密码（至少6位）。请设置并记住它。当询问是否设置 view-only 密码时，输入 `n`。

3.  **修复 VNC 启动脚本 (`xstartup`)**:
    默认的 VNC 启动脚本是空的，会导致显示异常。我们需要写入正确的 XFCE 启动命令。
    ```bash
    # 先杀死刚才测试启动的 VNC 服务
    vncserver -kill :1

    # 写入正确的配置
    cat > /root/.vnc/xstartup << EOF
    #!/bin/bash
    unset SESSION_MANAGER
    unset DBUS_SESSION_BUS_ADDRESS
    startxfce4 &
    EOF

    # 赋予脚本执行权限
    chmod +x /root/.vnc/xstartup
    ```

4.  **正式启动 VNC 服务器**:
    ```bash
    vncserver :1
    ```
    > 看到 `New 'X' desktop is localhost:1` 等字样即表示成功。

---

<a name="part4"></a>
## 第四部分：连接到 Ubuntu 桌面

1.  **在安卓手机上安装 VNC 客户端**:
    * 推荐应用: **VNC Viewer** (by RealVNC)，可在各大应用商店下载。

2.  **创建新连接**:
    * 打开 VNC Viewer 应用，点击 `+` 创建新连接。
    * **Address (地址)**: `localhost:1` 或 `127.0.0.1:1`
    * **Name (名称)**: 任意填写，如 `MyUbuntu`
    * 保存并点击连接。

3.  **处理警告并输入密码**:
    * VNC Viewer 会提示“Unencrypted connection”（未加密连接），这是正常的，因为连接在手机内部进行，非常安全。点击 **Continue (继续)**。
    * 输入您在第三部分设置的 VNC 密码。

> 现在，您应该能看到一个完整的 Ubuntu XFCE 桌面了。

---

<a name="part5"></a>
## 第五部分：安装并配置 Visual Studio Code

1.  **添加 VS Code 官方软件源**:
    在 **Ubuntu 的 VNC 桌面终端** 中，执行以下命令。
    ```bash
    # 安装依赖
    apt-get install -y wget gpg apt-transport-https

    # 导入微软 GPG 密钥
    wget -qO- [https://packages.microsoft.com/keys/microsoft.asc](https://packages.microsoft.com/keys/microsoft.asc) | gpg --dearmor > packages.microsoft.gpg
    install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg

    # 添加 VS Code 的 ARM64 软件源
    echo "deb [arch=arm64 signed-by=/etc/apt/keyrings/packages.microsoft.gpg] [https://packages.microsoft.com/repos/code](https://packages.microsoft.com/repos/code) stable main" | tee /etc/apt/sources.list.d/vscode.list > /dev/null
    ```

2.  **安装 VS Code**:
    ```bash
    apt-get update
    apt-get install code -y
    ```

3.  **配置永久运行环境 (最关键)**:
    为了解决 `DISPLAY` 环境变量丢失和每次输入长命令的问题，我们将所有配置写入 `bash` 配置文件。
    ```bash
    # 写入 DISPLAY 环境变量，确保图形程序能找到屏幕
    echo 'export DISPLAY=:1' >> /root/.bashrc

    # 写入 VS Code 启动别名，包含所有修复参数
    echo 'alias vscode="code --no-sandbox --disable-gpu --user-data-dir ./"' > /root/.bashrc

    # 让配置立刻生效
    source /root/.bashrc
    ```

4.  **运行 VS Code**:
    完成以上配置后，在 VNC 桌面的终端里，只需输入我们创建的别名即可：
    ```bash
    vscode
    ```
    > VS Code 窗口现在应该能成功启动了！

---

<a name="part6"></a>
## 第六部分：安卓系统稳定性设置 (防后台查杀)

为了防止 Termux 在运行重度任务时被安卓系统（特别是三星）强制杀死，请务必进行以下设置。

1.  **锁定 Termux 应用**:
    * 打开安卓的“最近应用”界面。
    * 找到 Termux 卡片，点击上方的图标。
    * 选择 **“锁定此应用” (Lock this app) 或 "Keep open"**。

2.  **关闭电池优化**:
    * 长按 Termux 应用图标 -> **(i) (应用信息)**。
    * 进入 **“电池”** -> 设置为 **“不受限制” (Unrestricted)**。

3.  **设为永不休眠**:
    * 进入手机“设置” -> “电池和设备维护” -> “电池” -> “后台使用限制”。
    * 将 **Termux** 添加到 **“从不休眠的应用”** 列表中。

4.  **使用 Termux 唤醒锁**:
    * 在执行 `./start-ubuntu.sh` **之前**，在 Termux 原始 shell 中运行：
    ```bash
    termux-wake-lock
    ```

---

<a name="part7"></a>
## 第七部分：日常使用流程备忘录

1.  **启动**:
    * 关闭手机上其他无关应用。
    * 打开 Termux。
    * （可选但推荐）运行 `termux-wake-lock`。
    * 运行 `./start-ubuntu.sh` 进入 Ubuntu。
    * 运行 `vncserver :1` 启动图形界面。
    * 打开 VNC Viewer 连接。

2.  **工作**:
    * 在 VNC 桌面的终端里，直接使用 `vscode` 命令启动 VS Code。
    * ...进行您的开发工作...

3.  **关闭**:
    * 在 VNC 桌面的终端里，运行 `vncserver -kill :1` 关闭图形服务。
    * 运行 `exit` 退出 Ubuntu。
    * （可选）在 Termux 原始 shell 中按 `Ctrl+C` 停止 `termux-wake-lock`。
    * 彻底关闭 Termux 应用。

---
恭喜！您现在拥有了一个稳定、强大、可随时启动的移动 Linux 开发环境。