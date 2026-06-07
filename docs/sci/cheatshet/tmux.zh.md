# tmux 常用命令与快捷键速查表

> 默认前缀键：Ctrl + b  
> 以下快捷键均在按下前缀键后触发（除特别说明）

ctrl+b ? 触发帮助显示所有快捷键。
---

```
session（会话）
  └── window（窗口）
        └── pane（面板）
```

## 会话（session）管理

### 会话：命令行

```bash 
tmux new -s name          # 新建会话
tmux attach -t name       # 连接会话
tmux ls                   # 列出会话
tmux kill-session -t name # 删除会话
tmux rename-session -t old new
```

### 会话：快捷键

``` 
Ctrl+b d        # detach 当前会话  
Ctrl+b $        # 重命名当前会话  
Ctrl+b s        # 列出会话并切换
```

---

## 窗口（window）管理

### 窗口：命令行

```bash
tmux new-window -n name
tmux kill-window
tmux rename-window name
tmux select-window -t 1
```

### 窗口：快捷键

``` 
Ctrl+b c        # 新建窗口  
Ctrl+b &        # 关闭窗口  
Ctrl+b ,        # 重命名窗口  
Ctrl+b n        # 下一个窗口  
Ctrl+b p        # 上一个窗口  
Ctrl+b l        # 上一个使用过的窗口  
Ctrl+b w        # 窗口列表  
Ctrl+b 0-9      # 切换窗口编号
```

---

## 面板（pane）管理

### 分割

``` 
Ctrl+b %        # 垂直分割  
Ctrl+b "        # 水平分割
```

### 删除

``` 
Ctrl+b x        # 关闭 pane
```

### 切换 pane

``` 
Ctrl+b 方向键  
Ctrl+b o        # 下一个 pane  
Ctrl+b ;        # 切回上一个 pane
```

### 调整大小

``` 
Ctrl+b Ctrl+方向键  
Ctrl+b Alt+方向键
```

### 最大化

``` 
Ctrl+b z        # 放大/恢复 pane
```

---

## 布局（layout）

``` 
Ctrl+b Space    # 循环布局  
Ctrl+b Alt+1    # even-horizontal  
Ctrl+b Alt+2    # even-vertical  
Ctrl+b Alt+3    # main-horizontal  
Ctrl+b Alt+4    # main-vertical  
Ctrl+b Alt+5    # tiled
```

---

## 复制模式 / 滚动

``` 
Ctrl+b [        # 进入复制模式  
Ctrl+b ]        # 粘贴缓冲区
```

复制模式内：

``` 
Space           # 开始选择  
Enter           # 复制  
q               # 退出  
/               # 搜索  
n               # 下一个匹配  
N               # 上一个匹配
```

滚动：

``` 
PgUp            # 上滚  
PgDn            # 下滚
```

---

## 缓冲区

### 缓冲区：快捷键

``` 
Ctrl+b =        # 列出缓冲区  
Ctrl+b -        # 删除最近缓冲区
```

### 缓冲区：命令行

```bash
tmux show-buffer
tmux save-buffer file
tmux load-buffer file
```

---

## 同步输入

``` 
Ctrl+b : setw synchronize-panes on  
Ctrl+b : setw synchronize-panes off
```

（多个 pane 同时输入）

```

---

## `-t` 目标指定规则

tmux 命令行中的 `-t` 参数用来定位 session / window / pane，格式为：

```
session_name:window_index.pane_index
```

### 怎么查看当前有哪些目标

```bash
tmux list-sessions                        # 列出所有 session
tmux list-windows -t session_name         # 列出某 session 的所有 window
tmux list-panes -t session_name:0         # 列出某 window 的所有 pane
tmux list-panes -t session_name:0.1       # 也可只看某个 pane
```

### 三层定位

```
-t session_name           # 只指定 session
-t session_name:0         # 指定 session + window（按编号）
-t session_name:0.1       # 指定 session + window + pane（按编号）
```

### 简写规则

| 简写 | 含义 | 说明 |
|------|------|------|
| `abc` | session `abc` | 等同于 `-t abc` |
| `abc:2` | session `abc` 的 window 2 | 可用窗口名替代编号 |
| `abc:2.0` | session `abc` 的 window 2 pane 0 | 完整定位 |
| `:2` | 当前 session 的 window 2 | 省略 session 名 = 当前 session |
| `:2.1` | 当前 session 的 window 2 pane 1 | |
| `.3` | 当前 window 的 pane 3 | 省略 session:window = 当前 |
| `={regex}` | 匹配窗口标题的正则 | 如 `-t =log` 匹配标题含 log 的窗口 |
| `%1` | 匹配 pane id | `tmux list-panes` 可看到 `%0` `%1` 等 |

### 实用示例

```bash
# 在指定 pane 执行命令
tmux send-keys -t dev:1.0 'make test' Enter

# 向另一个 session 的 window 发送命令
tmux send-keys -t build:0 'cargo build' Enter

# 捕获指定 pane 的内容
tmux capture-pane -t dev:1.0 -p

# 关闭指定 session 的某个 window
tmux kill-window -t dev:3

# 选择指定 session 的某个 pane
tmux select-pane -t dev:0.1
```

> **提示**：pane 编号可通过 `tmux list-panes` 查看，或在 tmux 内用 `Ctrl+b q` 短暂显示各 pane 编号。

---

## 发送命令到 pane / 捕获 pane 内容

### send-keys

```bash
tmux send-keys -t 0.1 'ls -la' Enter          # 向 pane 发送命令
tmux send-keys -t dev:2.0 'make' Enter         # 指定 session:window.pane
tmux send-keys -t 0.0 C-c                      # 发送 Ctrl-c（中断）
tmux send-keys -t 0.0 C-l                      # 发送 Ctrl-l（清屏）
```

### capture-pane

```bash
tmux capture-pane -t 0.1                       # 捕获 pane 内容到缓冲区
tmux capture-pane -t 0.1 -p                    # -p 直接打印到 stdout（不存缓冲区）
tmux capture-pane -t 0.1 -p -S -50             # -S -50 捕获最近50行历史
tmux capture-pane -t 0.1 -p -S -               # -S - 捕获全部历史
tmux capture-pane -t 0.1 -p | tail -20         # 配合管道取最后20行
tmux capture-pane -t 0.1 -p -E 30              # -E 30 截止到第30行
```

参数说明：

| 参数 | 含义 |
|------|------|
| `-p` | 打印到 stdout 而非存入缓冲区 |
| `-S -N` | 起始行：从历史第 N 行开始（`-` 表示最开头） |
| `-E N` | 结束行：到第 N 行截止（默认到底部） |
| `-J` | 合并被 wrap 的行 |
| `-e` | 保留转义序列（颜色等） |

### 典型用法

```bash
# 抓取另一个 pane 的输出并判断是否编译成功
if tmux capture-pane -t build:0.0 -p -S -5 | grep -q "error"; then
    echo "编译失败"
fi

# 保存 pane 全部历史到文件
tmux capture-pane -t 0.0 -p -S - > output.log

# 捕获后存入指定缓冲区
tmux capture-pane -t 0.0 -b mybuf
tmux save-buffer -b mybuf output.txt
```

---

## 服务器管理

```bash
tmux kill-server                 # 关闭所有 tmux
tmux source-file ~/.tmux.conf    # 重新加载配置
```

---

## 帮助与命令模式

``` 
Ctrl+b ?        # 查看所有快捷键  
Ctrl+b :        # 进入命令模式
```

---

## 常见自定义建议

set -g mouse on              # 鼠标支持  
set -g history-limit 10000   # 历史行数  
setw -g mode-keys vi         # vi 风格复制  
bind r source-file ~/.tmux.conf \; display "reloaded"

---

## 个人高频使用 TOP

``` 
Ctrl+b c        # 新窗口  
Ctrl+b %        # 垂直分割  
Ctrl+b "        # 水平分割  
Ctrl+b z        # 最大化 pane  
Ctrl+b d        # detach  
Ctrl+b [        # 滚动查看  
Ctrl+b s        # 会话切换  
Ctrl+b w        # 窗口切换  
Ctrl+b :        # 命令模式
```

---

## 结束

