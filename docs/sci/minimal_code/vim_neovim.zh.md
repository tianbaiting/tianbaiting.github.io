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


## vim 基本操作, 使用哲学

三大模式
normal, visual, edit(insert)


### 移动

基础: hjkl  左下上右. j形状像是下箭头.

h l 几乎不用, 而是用 f F 进行精准的行间查找  或者w b e 进行单词移动.

/用于全文查找.  查找后n 继续下一个 N 上一个. 会一直显示高亮直到 :nohl.

### 语法结构

动词+名词

dw 删除一个词语

dp 删除一段

动词+介词+名词

| 按键 | 英文全称 / 助记 | 含义 |
|---|---|---|
| f | Find | 向后查找字符，停在上面 |
| t | Till | 向后查找字符，停在前面（直到…） |
| F | Find (back) | 向前查找字符 |
| T | Till (back) | 向前查找字符 |
| ; | (Repeat) | 重复上一次 f/t |
| , | (Reverse) | 反向重复上一次 f/t |

daw delete around word

dfe f行内查找,删除到下一个e

dte 删除直到下一个e()

动词和名词前可以跟数量

3dw 删除3个词语

d3w 删除3个词语

### 重复

. 重复上一个操作(编辑操作)

n 重复上一个查找操作
N 反向重复上一个查找操作

 重复跳转操作