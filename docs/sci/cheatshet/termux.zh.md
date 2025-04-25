---
title: termux 运行ubuntu 
tag: 
    - termux
    - anlinux
---

## 使用 Termux 运行 Ubuntu

Termux 是一个强大的 Android 终端模拟器，可以通过 AnLinux 工具在其中运行 Ubuntu。

Termux：地基和工具箱

    Termux 是一个 Android 终端模拟器应用。简单来说，它就像在你的安卓设备上打开了一个命令行界面（CLI），让你能够输入和执行 Linux 命令，而且在大多数情况下不需要你的手机进行 root 操作。
    Termux 自带了一个软件包管理器 (pkg)，并且包含了很多已经适配到安卓系统上运行的 Linux 工具和实用程序。你可以把它想象成一个迷你的 Linux 环境。
    Termux 利用了安卓系统底层的 Linux 内核，但它运行在安卓的安全模型和文件系统权限的限制之内。

Termux 里的 Ubuntu：一个访客环境

    当你在 Termux 里面安装 Ubuntu 时，你实际上是创建了一个 chroot 环境或者使用了像 PRoot 这样的工具。这些技术可以创建一个隔离的文件系统环境，这个环境模仿了一个完整的 Linux 发行版。
    Chroot （change root，改变根目录）是一种更传统的 Unix 机制，它会改变当前进程及其子进程所看到的根目录。要完全使用 chroot 的功能，通常需要你的安卓设备已经 root。
    PRoot 是 chroot、mount --bind 和 binfmt_misc 的用户空间实现。它允许你在不需要 root 权限的情况下运行 Linux 发行版，其原理是拦截系统调用。Termux 经常使用 PRoot 来在未 root 的设备上安装像 Ubuntu 这样的发行版。
    你在 Termux 里安装的 Ubuntu 是一个独立的用户空间环境。 它有自己的文件系统、用户和软件包管理系统（通常是 apt）。然而，它仍然是运行在 Termux 环境和底层的安卓内核之上的。

它们之间的关系：

你可以这样理解：

    安卓系统： 宿主操作系统（就像房子的地基）。
    Termux： 运行在安卓上的一个应用，它提供了一个类似 Linux 的终端和一些基本的工具（就像房子里的工具箱）。
    Ubuntu（在 Termux 里）： 一个运行在 Termux 内部的访客 Linux 发行版，通过 chroot 或 PRoot 技术与主要的安卓和 Termux 系统隔离开（就像在房子里搭建的一个独立的小房间）。

主要的区别和需要考虑的事项：

    内核： 在 Termux 里运行的 Ubuntu 共享安卓系统底层的 同一个 Linux 内核。它没有自己独立的内核。
    硬件访问： 从 Ubuntu 环境中访问硬件（比如 GPU、摄像头等）通常是受限的，或者需要特定的配置和变通方法。
    性能： 由于涉及到模拟或隔离层，在 Termux 里运行一个完整的 Linux 发行版有时会比在专用电脑上运行慢。
    Root 权限： 虽然 Termux 本身通常不需要 root 权限，但使用 chroot 来获得完整的 Ubuntu 体验通常需要 root。PRoot 提供了一个非 root 的替代方案，但可能存在一些限制。
    目的： 人们在 Termux 里运行 Ubuntu 的原因有很多，比如访问特定的 Linux 工具、搭建开发环境或者在安卓设备上学习 Linux 命令。它通常不能完全替代在电脑上安装的完整 Ubuntu 系统。

总而言之，Termux 提供了一个环境和必要的工具，通过像 chroot 或 PRoot 这样的技术，在你的安卓设备上创建并运行一个独立的 Ubuntu 用户空间。这个 Ubuntu 实例是 Termux 里的一个访客，它共享底层的安卓内核，但拥有自己隔离的文件系统和软件生态系统。


以下是步骤：

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

