# tmux 常用命令与快捷键速查表

> 默认前缀键：Ctrl + b  
> 以下快捷键均在按下前缀键后触发（除特别说明）

---

```
session（会话）
  └── window（窗口）
        └── pane（面板）
```

## 一、会话（session）管理

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

## 二、窗口（window）管理

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

## 三、面板（pane）管理

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

## 四、布局（layout）

``` 
Ctrl+b Space    # 循环布局  
Ctrl+b Alt+1    # even-horizontal  
Ctrl+b Alt+2    # even-vertical  
Ctrl+b Alt+3    # main-horizontal  
Ctrl+b Alt+4    # main-vertical  
Ctrl+b Alt+5    # tiled
```

---

## 五、复制模式 / 滚动

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

## 六、缓冲区

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

## 七、同步输入

``` 
Ctrl+b : setw synchronize-panes on  
Ctrl+b : setw synchronize-panes off
```

（多个 pane 同时输入）

---

## 八、发送命令到 pane

```bash
tmux send-keys -t pane 'cmd' Enter
```

---

## 九、服务器管理

```bash
tmux kill-server                 # 关闭所有 tmux
tmux source-file ~/.tmux.conf    # 重新加载配置
```

---

## 十、帮助与命令模式

``` 
Ctrl+b ?        # 查看所有快捷键  
Ctrl+b :        # 进入命令模式
```

---

## 十一、常见自定义建议

set -g mouse on              # 鼠标支持  
set -g history-limit 10000   # 历史行数  
setw -g mode-keys vi         # vi 风格复制  
bind r source-file ~/.tmux.conf \; display "reloaded"

---

## 十二、个人高频使用 TOP

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

