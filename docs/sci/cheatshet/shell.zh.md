
查看当前目录下所有目录的大小，并限制深度为 1 (以人类可读的格式):
```
du -dh 1 .
```


## how to use

-help  --help

man [command]

TLDR https://tldr.sh


## wget


wget -r -p -np -k https://example.com


1. 从 https://example.com 开始递归下载所有内容；
2. 下载页面所需的所有资源（如图片、CSS 等）；
3. 限制下载范围，不会超出指定目录；
4. 将 HTML 文件中的链接转换为本地链接，便于离线浏览。

## 文本操作

cat ~/Software/setup_zsh.sh | iconv -f utf-8 -t utf-16le | clip.exe

传递给win的剪切板

## 模糊检索

fzf


## 屏幕操作 (screen)

提示：screen 的快捷键以 Ctrl-a 为前缀（可自定义）。部分功能依赖于 screen 版本与配置。

常用命令示例：
```
# 新建会话并命名
screen -S mysession

# 列出会话
screen -ls

# 分离会话（在 screen 中按）
Ctrl-a d

# 重连会话
screen -r mysession

# 在会话中创建新窗口（按）
Ctrl-a c

# 窗口切换：下一个 / 上一个
Ctrl-a n / Ctrl-a p

# 切换到指定窗口编号（按）
Ctrl-a 0..9

# 重命名当前窗口（按）
Ctrl-a A

# 关闭当前窗口（按）
Ctrl-a k

# 分割屏幕（水平）并在分区间切换
Ctrl-a S       # 分割
Ctrl-a Tab     # 切换焦点
Ctrl-a Q       # 关闭其他分区，保留当前

# 复制/粘贴（拷贝模式）
Ctrl-a [       # 进入拷贝模式，移动光标，空格开始选择，回车复制
Ctrl-a ]       # 粘贴
```



## tmux

默认前缀为 Ctrl-b。常用操作示例：
```
# 新建会话并命名
tmux new -s mysession

# 后台新建会话
tmux new -s mysession -d

# 列出会话
tmux ls

# 连接会话
tmux attach -t mysession
tmux a -t mysession

# 分离会话（在 tmux 中按）
Ctrl-b d

# 创建新窗口（按）
Ctrl-b c

# 窗口切换：下一个 / 上一个
Ctrl-b n / Ctrl-b p

# 重命名当前窗口（按）
Ctrl-b ,

# 垂直/水平分割窗格
Ctrl-b %   # 垂直分割（左右）
Ctrl-b "   # 水平分割（上下）

# 在窗格间切换
Ctrl-b o     # 切换到下一个窗格
或使用方向键：Ctrl-b 上/下/左/右

# 调整窗格大小（示例）
Ctrl-b : resize-pane -L 5

# 关闭窗格 / 窗口
Ctrl-b x   # 关闭当前窗格
Ctrl-b &   # 关闭当前窗口

# 拷贝/粘贴（复制模式）
Ctrl-b [   # 进入复制模式，移动光标，空格开始选择，回车复制
Ctrl-b ]   # 粘贴

# 将窗格输出保存到文件
tmux capture-pane -pS -1000 > /tmp/tmux_scrollback.txt

# 在脚本中发送按键到窗格
tmux send-keys -t mysession:0.1 'ls -la' C-m
```

提示：tmux 配置文件 ~/.tmux.conf 可自定义前缀、快捷键和行为；tmux 功能更强、脚本化友好，适合复杂会话管理。



## install sofware / 安装软件

常见场景：系统包管理器优先，其次使用语言/生态专属包管理器；找不到时再考虑从源码构建。

- 在 Debian/Ubuntu 系统：
    - 更新源并安装：
        ```bash
        sudo apt update
        sudo apt install <package>
        ```
    - 搜索包名：
        ```bash
        apt search <name>
        apt show <package>
        ```

- 在 macOS：（linux都能装homebrew）
    - 使用 Homebrew：
        ```bash
        brew update
        brew install <package>
        ```


- 语言/生态工具：
    - Python：pip install --user <pkg> 或使用 pipx
    - Node.js：npm install -g <pkg> 或使用 nvm 管理 Node 版本
    - Rust：cargo install <crate>

- 快速定位“未找到命令”原因：
    - 确认包名拼写；使用 apt/dnf/pacman 的 search 命令查找。
    - 在 Debian/Ubuntu 可参考命令搜索服务（如 command-not-found.com 的线上或系统数据库）。

- 从源码构建（最后手段）：
    1. 获取源码：git clone <repo> && cd repo
    2. 阅读 README / INSTALL 等文档，安装构建依赖。
    3. 常见构建流程：
         - Autotools：
             ```bash
             ./configure --prefix=/usr/local
             make -j$(nproc)
             sudo make install
             ```
         - CMake：
             ```bash
             mkdir build && cd build
             cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local
             cmake --build . -- -j$(nproc)
             sudo cmake --install .
             ```
         - 如果是脚本或 Python 项目：查看是否有 setup.py / pyproject.toml / install.sh 指示安装方法。
    4. 注意事项：尽量避免直接将文件散装到系统路径；可使用 --prefix=/usr/local、checkinstall、stow 或容器/虚拟环境来管理自建软件。

总之：优先使用系统与生态的包管理器，必要时再从源码构建并按照项目文档安装。


## pipe & Redirect

```
ls | grep "build"
```

重定向 对文件的输出

redirect : > & < 

```ls > ls_out```

把ls的输出stdout 输入到file ls_out里面

```grep build < ls_out```

把ls_out的内容 当作grep的命令的输入stdin



### stdout / stderr / stdin（0, 1, 2）详解

- 0：stdin（标准输入） — 程序从这里读取输入（通常来自键盘或管道）。
- 1：stdout（标准输出） — 程序的正常输出流，默认打印到终端。
- 2：stderr（标准错误） — 错误或诊断信息，默认也打印到终端（与 stdout 分离，便于分别重定向）。

常用重定向示例：
```bash
# 将 stdout 写入文件（覆盖）
cmd > out.txt

# 将 stdout 追加到文件
cmd >> out.txt

# 将 stderr 写入文件
cmd 2> err.txt

# 将 stdout 和 stderr 一起写入同一文件（bash）
cmd &> both.txt        # bash-specific
# 或者更通用的写法
cmd > both.txt 2>&1

# 丢弃输出
cmd > /dev/null 2>&1   # 丢弃 stdout 和 stderr
cmd 2> /dev/null       # 只丢弃 stderr
```

管道只传递 stdout，若要把 stderr 也传给下一个命令：
```bash
# 把 stderr 重定向到 stdout 再通过管道
cmd 2>&1 | less

# 或只把 stderr 通过进程替换传给另一个命令
cmd 2> >(grep -i error > errors.txt)
```

### Here-doc / Here-string（多行输入）

- Here-doc（多行块）：
```bash
cat <<EOF > file.txt
第一行
第二行
EOF
```

- Here-string（短文本作为 stdin）：
```bash
grep foo <<< "one foo two"
```

### tee：同时输出到终端与文件
```bash
ls -la | tee listing.txt    # 将输出写到文件并打印到屏幕
ls -la | tee -a append.txt  # 追加写入
```

### xargs 与 find 的常见搭配
处理大量文件或带空格的文件名时用 -print0 与 -0：
```bash
# 并行压缩找到的文件（对大文件集有效）
find . -type f -name '*.log' -print0 | xargs -0 -n1 -P4 gzip
```

### 进程替换（Process Substitution）
在需要以文件名形式传递命令输出时：
```bash
diff <(ls dir1) <(ls dir2)
```

### 后台运行与作业控制
- 将命令放后台运行：
```bash
sleep 60 &
```
- 查看作业、切后台/前台：
```bash
jobs
fg %1
bg %1
disown %1   # 让作业与当前 shell 分离（可用于关闭终端后继续运行）
```
- 使用 nohup 或 screen/tmux 在会话断开后保持运行：
```bash
nohup longtask &> longtask.log &
```

### 脚本执行与 shebang、权限
- 在脚本顶部加入 shebang：
```bash
#!/usr/bin/env bash
```
- 使脚本可执行并运行：
```bash
chmod +x script.sh
./script.sh
```

### 环境变量与 PATH、别名、函数
- 临时设置并导出变量：
```bash
export MYVAR="value"
echo $MYVAR
```
- 修改 PATH：
```bash
export PATH="$HOME/bin:$PATH"
```
- 常用别名（放入 ~/.bashrc 或 ~/.zshrc）：
```bash
alias ll='ls -la'
unalias ll
```
- 定义简单函数：
```bash
mkcd() { mkdir -p "$1" && cd "$1"; }
```

### 常见小技巧与安全注意
- 使用双引号保护包含空格的文件名或变量： "$var"
- 避免在不受信任的数据上直接使用 eval 或将未过滤输入传给 shell。 （小心注入式攻击）（小心自己把自己注入式攻击了）
- 调试脚本时可用 set -x（显示执行命令）和 set -e（遇错退出）
```bash
set -euo pipefail   # 推荐在脚本顶部开启（严格模式）
```

### 参考常见命令速查（一览）
- 文件与权限：ls, cp, mv, rm, chmod, chown
- 压缩：tar, gzip, bzip2, zip
- 查找与筛选：find, grep, sed, awk
- 网络：curl, wget, ssh, scp
- 进程与性能：ps, top, htop, nice, ionice
- 包管理：apt, yum/dnf, pacman, brew

：掌握 IO 重定向、管道、后台/作业控制与脚本基础，能显著提高在 shell 中的效率。把常用片段放到 shell 配置文件或脚本中以便复用。


### 文本三剑客

#### awk

和c类似

