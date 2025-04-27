---
title: vim配置文件
tag:
    - vim
    - vimrc
    - vim配置
---


观前提示：不知道什么是vim的，可以在linux终端输入`vimtutor zh`.

vimrc 文件是 Vim 编辑器的配置文件，用于定义 Vim 的行为、外观和功能。通过编辑 vimrc 文件，用户可以自定义 Vim 的使用体验，例如设置快捷键、启用插件、调整配色方案等。


  Vim 的功能特性要比 Vi 多得多，但其中大部分都没有缺省启用。为了使用更多的
  特性，您得创建一个 vimrc 文件。



## 不需要插件的vimrc

https://github.com/YanivZalach/Vim_Config_NO_PLUGINS/blob/main/.vimrc


这里面定义了这些快捷键


### 常用快捷键

    jj：快速退出插入模式。
    Q：格式化段落为行。
    <leader>：空格键被设置为 Leader 键。

### 文件操作

    <leader>a：选择全文。
    <leader>e：打开文件浏览器（Lexplore）。
    <leader>o：从浏览器中打开文件（Explore）。
    <C-S>：保存文件。
    <C-q>：保存并退出文件。
    <leader>c：在新标签页中打开/创建文件。

###  分屏操作

    <leader>y：水平分屏。
    <leader>x：垂直分屏。
    <C-j>：分屏中向下移动。指光标聚焦点
    <C-k>：分屏中向上移动。
    <C-h>：分屏中向左移动。
    <C-l>：分屏中向右移动。
    <A-Up>：增加分屏高度。
    <A-Down>：减少分屏高度。
    <A-Left>：减少分屏宽度。
    <A-Right>：增加分屏宽度。

### 标签页操作

    <leader>t：切换标签页。
    <leader>c：在新标签页中打开文件。

### 搜索和替换

    <leader>sw：用指定字符包裹单词。
    <leader>rw：替换所有出现的单词。
    <C-z>：打开/关闭拼写检查，默认检查英语（en_us）。

### 终端操作

    <C-t>：打开终端窗口。
    <C-t>（终端模式）：关闭终端窗口。
    <C-i> 或 Esc（终端模式）：使终端窗口可滚动。

### 特殊功能

    <leader>ht：切换希伯来语键盘映射和从右到左的设置。
    <leader>hx：在创建十六进制文件和还原之间切换。
    <leader>r：查看寄存器内容。
    <leader>v：切换块模式（V-Block）。

### 复制与粘贴

    <C-V>：粘贴内容。
    <C-C>：复制内容到系统剪贴板。

### 行操作

    J（可视模式）：将选中的行向下移动。
    K（可视模式）：将选中的行向上移动。





## 常用的插件管理库 vim plug


推荐的 vimrc 配置资源

[Amix's Vimrc](https://github.com/amix/vimrc)：一个流行的 Vim 配置仓库，包含丰富的插件和优化。

[Vim Awesome](https://vimawesome.com/)：一个插件资源网站，帮助用户扩展 Vim 的功能。


https://github.com/junegunn/vim-plug



```


call plug#begin('~/.vim/plugged')

" 示例插件
" Plug 'preservim/nerdtree'         " 文件树
" Plug 'junegunn/fzf', { 'do': './install --all' } " 模糊搜索
" Plug 'vim-airline/vim-airline'    " 状态栏
" Plug 'tpope/vim-fugitive'         " Git 集成
" Plug 'sheerun/vim-polyglot'       " 多语言支持
" Plug 'scrooloose/nerdcommenter'   " 快速注释

Plug 'liuchengxu/vim-which-key'

call plug#end()




set timeoutlen=50

let g:mapleader = "\<Space>"
let g:maplocalleader = ","
nnoremap <silent> <leader> :WhichKey '<Space>'<CR>
nnoremap <silent> <localleader> :WhichKey ','<CR>


" Mouse functionality
	set mouse=a

```

neovim与lazyvim详见[[vim_neovim.zh]]