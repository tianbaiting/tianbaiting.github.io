# FZF 模糊搜索工具完全教程

FZF (Fuzzy Finder) 是一个通用的命令行模糊搜索工具，可以大幅提升命令行操作效率。

## 目录
- [安装配置](#安装配置)
- [基础用法](#基础用法)
- [快捷键操作](#快捷键操作)
- [高级功能](#高级功能)
- [Shell 集成](#shell-集成)
- [实用案例](#实用案例)
- [自定义配置](#自定义配置)

## 安装配置

### Ubuntu/Debian
```bash
sudo apt install fzf
```

### macOS
```bash
brew install fzf
# 安装 shell 集成
$(brew --prefix)/opt/fzf/install
```

### 从源码安装
```bash
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```

### 验证安装
```bash
fzf --version
```

## 基础用法

### 1. 文件搜索
```bash
# 在当前目录搜索文件
fzf

# 搜索并直接编辑选中的文件
vim $(fzf)

# 搜索特定类型文件
find . -name "*.py" | fzf
```

### 2. 历史命令搜索
```bash
# Ctrl+R 搜索历史命令（需要 shell 集成）
history | fzf
```

### 3. 进程搜索
```bash
# 搜索并终止进程
ps aux | fzf | awk '{print $2}' | xargs kill
```

## 快捷键操作

### 基础快捷键
| 快捷键 | 功能 |
|--------|------|
| `Ctrl+J/K` 或 `↓/↑` | 上下移动 |
| `Enter` | 选择当前项 |
| `Esc` | 退出 |
| `Tab` | 多选模式标记/取消标记 |
| `Shift+Tab` | 反向多选 |

### 搜索快捷键
| 快捷键 | 功能 |
|--------|------|
| `Ctrl+A` | 全选 |
| `Ctrl+D` | 取消全选 |
| `Ctrl+T` | 切换全选状态 |
| `Alt+A` | 选择所有匹配项 |
| `Alt+D` | 取消选择所有项 |

### 预览快捷键
| 快捷键 | 功能 |
|--------|------|
| `?` | 切换预览窗口 |
| `Ctrl+U/D` | 预览窗口上下滚动 |

## 高级功能

### 1. 预览模式
```bash
# 预览文件内容
fzf --preview 'cat {}'

# 预览目录结构
fzf --preview 'ls -la {}'

# 动态预览窗口大小
fzf --preview 'cat {}' --preview-window=right:70%:wrap
```

### 2. 多选模式
```bash
# 启用多选
fzf -m

# 多选文件并复制
cp $(fzf -m) /target/directory/
```

### 3. 自定义搜索命令
```bash
# 使用 fd 替代 find
export FZF_DEFAULT_COMMAND='fd --type f --hidden --follow --exclude .git'

# 使用 rg 搜索文件内容
export FZF_DEFAULT_COMMAND='rg --files --hidden --follow --glob "!.git/*"'
```

### 4. 交互式过滤
```bash
# 实时过滤日志
tail -f /var/log/system.log | fzf --no-sort --tac
```

## Shell 集成

### Bash/Zsh 快捷键
安装 shell 集成后可用：

| 快捷键 | 功能 |
|--------|------|
| `Ctrl+T` | 搜索文件并插入路径 |
| `Ctrl+R` | 搜索历史命令 |
| `Alt+C` | 搜索目录并跳转 |

### 配置示例
```bash
# ~/.bashrc 或 ~/.zshrc
export FZF_DEFAULT_OPTS='
  --height 40% 
  --layout=reverse 
  --border
  --preview "cat {}"
  --preview-window=right:60%:wrap'

# 自定义 Ctrl+T 行为
export FZF_CTRL_T_OPTS="
  --preview 'bat --color=always --line-range :500 {}'
  --bind shift-up:preview-page-up,shift-down:preview-page-down"
```

## 实用案例

### 1. 快速文件编辑
```bash
# 创建快捷函数
vf() {
  local file
  file=$(fzf --preview 'bat --color=always --line-range :500 {}') && vim "$file"
}
```

### 2. Git 分支切换
```bash
# 交互式分支切换
fbr() {
  local branches branch
  branches=$(git branch -vv) &&
  branch=$(echo "$branches" | fzf +m) &&
  git checkout $(echo "$branch" | awk '{print $1}' | sed "s/.* //")
}
```

### 3. 进程管理
```bash
# 交互式进程终止
fkill() {
  local pid
  pid=$(ps -ef | sed 1d | fzf -m | awk '{print $2}')
  if [ "x$pid" != "x" ]; then
    echo $pid | xargs kill -${1:-9}
  fi
}
```

### 4. 目录跳转
```bash
# 快速目录跳转
fd() {
  local dir
  dir=$(find ${1:-.} -path '*/\.*' -prune -o -type d -print 2> /dev/null | fzf +m) &&
  cd "$dir"
}
```

### 5. Docker 容器管理
```bash
# 进入 Docker 容器
dexec() {
  local cid
  cid=$(docker ps | sed 1d | fzf -q "$1" | awk '{print $1}')
  [ -n "$cid" ] && docker exec -it "$cid" bash
}
```

### 6. 环境变量查看
```bash
# 搜索环境变量
fenv() {
  env | fzf --preview 'echo {} | cut -d= -f2-'
}
```

## 自定义配置

### 1. 颜色主题
```bash
export FZF_DEFAULT_OPTS='
  --color=fg:#f8f8f2,bg:#282a36,hl:#bd93f9
  --color=fg+:#f8f8f2,bg+:#44475a,hl+:#bd93f9
  --color=info:#ffb86c,prompt:#50fa7b,pointer:#ff79c6
  --color=marker:#ff79c6,spinner:#ffb86c,header:#6272a4'
```

### 2. 布局设置
```bash
export FZF_DEFAULT_OPTS='
  --height 60%
  --layout=reverse
  --border=rounded
  --margin=1
  --padding=1'
```

### 3. 预览设置
```bash
export FZF_DEFAULT_OPTS='
  --preview-window=right:50%:hidden:wrap
  --bind=ctrl-/:toggle-preview
  --bind=ctrl-u:preview-page-up
  --bind=ctrl-d:preview-page-down'
```

### 4. 自定义绑定
```bash
export FZF_DEFAULT_OPTS='
  --bind=ctrl-a:select-all
  --bind=ctrl-d:deselect-all
  --bind=ctrl-t:toggle-all
  --bind=alt-j:jump
  --bind=alt-k:jump-accept'
```

## 高级技巧

### 1. 与其他工具结合

#### 与 ripgrep 结合
```bash
# 搜索文件内容
rg --line-number --no-heading --color=never "search_term" | 
fzf --delimiter : --preview 'bat --color=always --line-range {2}: {1}'
```

#### 与 fd 结合
```bash
# 快速查找文件
alias ff='fd --type f | fzf --preview "bat --color=always --line-range :500 {}"'
```

### 2. 复杂搜索模式
```bash
# 精确匹配
fzf --exact

# 反向搜索
fzf --query="!pattern"

# 多条件搜索
fzf --query="term1 term2"
```

### 3. 自定义启动脚本
```bash
# ~/.fzf_functions.sh
#!/bin/bash

# 搜索并编辑配置文件
fedit() {
  local files
  files=$(find ~/.config -name "*.conf" -o -name "*.cfg" -o -name "*.ini" | fzf -m)
  [[ -n "$files" ]] && ${EDITOR:-vim} $files
}

# 搜索并安装包
finstall() {
  apt list 2>/dev/null | grep -v "WARNING" | 
  fzf --multi --preview 'apt show {1}' | 
  cut -d'/' -f1 | 
  xargs -ro sudo apt install
}
```

## 性能优化

### 1. 缓存搜索结果
```bash
# 使用缓存加速大目录搜索
export FZF_DEFAULT_COMMAND='fd --type f --hidden --follow --exclude .git 2>/dev/null'
```

### 2. 限制搜索深度
```bash
# 限制搜索深度提升性能
fd --max-depth 3 --type f | fzf
```

### 3. 异步预览
```bash
# 异步预览大文件
fzf --preview 'timeout 1 bat --color=always --line-range :100 {}'
```

## 故障排除

### 1. 中文显示问题
```bash
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

### 2. 预览不工作
```bash
# 检查依赖工具
which bat || sudo apt install bat
which fd || sudo apt install fd-find
```

### 3. 快捷键冲突
```bash
# 检查按键绑定
bind -p | grep fzf
```

## 故障排除：关于管道输入与预置查询

如果遇到像下面这样的错误：
```bash
rg --line-number --no-heading '' | fzf "termux"
# 输出：unknown option: termux
```

说明与修正要点：
- 当把其它命令的输出通过管道传给 fzf 时，若想预先设置查询词（initial query），应使用 -q 或 --query 参数；直接把查询词作为位置参数可能被误解析或在某些组合中产生错误。
- 推荐使用方式示例：

正确示例：
```bash
# 使用 -q 指定初始查询（大小写敏感）
rg --line-number --no-heading '' | fzf -q termux

# 使用 --query 指定初始查询（等价）
rg --line-number --no-heading '' | fzf --query=termux

# 忽略大小写
rg --line-number --no-heading '' | fzf -i -q termux

# 带预览的示例（结合 bat）
rg --line-number --no-heading '' | fzf -q termux --preview 'bat --color=always --style=numbers {1}'
```

简短说明：
- -q / --query 用于设置初始过滤关键词；也可以在 fzf 启动后直接输入搜索词。
- 若仍报奇怪的 option 错误，检查 fzf 版本（fzf --version）并确保没有把查询词误写成以 `-` 开头的字符串或放在不恰当的位置。

## 总结

FZF 是一个强大的模糊搜索工具，通过合理配置可以大幅提升命令行工作效率。主要优势：

- 🚀 快速模糊搜索
- 🎨 丰富的自定义选项
- 🔧 与各种工具无缝集成
- ⚡ 高性能和低内存占用
- 🎯 直观的交互体
- 验

建议从基础用法开始，逐步添加自定义配置和函数，根据个人工作流程定制最适合的使用方式。
