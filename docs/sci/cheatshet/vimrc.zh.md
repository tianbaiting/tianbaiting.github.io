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



一个完全不需要插件的vimrc配置

https://github.com/YanivZalach/Vim_Config_NO_PLUGINS/blob/main/.vimrc







## 常用的插件管理库 vim plug


推荐的 vimrc 配置资源

[Amix's Vimrc](https://github.com/amix/vimrc)：一个流行的 Vim 配置仓库，包含丰富的插件和优化。

[Vim Awesome](https://vimawesome.com/)：一个插件资源网站，帮助用户扩展 Vim 的功能。


https://github.com/junegunn/vim-plug



```
// This is a Vim configuration file that sets up basic settings for Vim editor.

:set number


" 示例插件
Plug 'preservim/nerdtree'         " 文件树
Plug 'junegunn/fzf', { 'do': './install --all' } " 模糊搜索
Plug 'vim-airline/vim-airline'    " 状态栏
Plug 'tpope/vim-fugitive'         " Git 集成
Plug 'sheerun/vim-polyglot'       " 多语言支持
Plug 'scrooloose/nerdcommenter'   " 快速注释

call plug#end()

```

neovim与lazyvim详见[[vim_neovim.zh]]