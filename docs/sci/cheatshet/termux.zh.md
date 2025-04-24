---
title: termux 运行ubuntu 
tag: 
    - termux
    - anlinux
---

## 使用 Termux 运行 Ubuntu

Termux 是一个强大的 Android 终端模拟器，可以通过 AnLinux 工具在其中运行 Ubuntu。以下是步骤：

### 安装 Termux 和 AnLinux
1. 从 [Google Play](https://play.google.com/store/apps/details?id=com.termux) 或 [F-Droid](https://f-droid.org/packages/com.termux/) 安装 Termux。
2. 安装 AnLinux 应用程序，用于简化 Linux 环境的安装。

### 配置 Ubuntu 环境
1. 打开 Termux，更新包管理器：
    ```bash
    pkg update && pkg upgrade
    ```
2. 安装必要的工具：
    ```bash
    pkg install wget proot
    ```
3. 使用 AnLinux 提供的脚本下载并安装 Ubuntu：
    ```bash
    wget https://raw.githubusercontent.com/Neo-Oli/termux-ubuntu/master/ubuntu.sh
    bash ubuntu.sh
    ```

### 启动 Ubuntu
1. 运行以下命令进入 Ubuntu 环境：
    ```bash
    ./start-ubuntu.sh
    ```
2. 现在你可以在 Ubuntu 环境中安装和运行各种工具。

### 注意事项
- 确保你的设备有足够的存储空间。
- 使用 `exit` 命令退出 Ubuntu 环境。

通过以上步骤，你可以在 Termux 中成功运行 Ubuntu。

## 添加图形界面

