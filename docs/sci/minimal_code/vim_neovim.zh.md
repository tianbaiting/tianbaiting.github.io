---
title：vim neovim

---

## 安装步骤


1. **下载 Homebrew**  
   
    apt下载的neovim版本可能过于老旧，无法安装lazyvim.

    打开终端并运行以下命令安装 Homebrew：  
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. **下载 Neovim**  
    使用 Homebrew 安装 Neovim：  
    ```bash
    brew install neovim
    ```

3. **下载 LazyVim**  
    克隆 LazyVim 配置到 Neovim 的配置目录：  
    ```bash
    git clone https://github.com/LazyVim/starter ~/.config/nvim
    ```

4. **启动 Neovim**  
    在终端中运行以下命令启动 Neovim：  
    ```bash
    nvim
    ```

5. **安装插件**  
    启动 Neovim 后，LazyVim 会自动安装所需插件。等待安装完成即可开始使用。