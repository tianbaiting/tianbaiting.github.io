# Zsh 环境一键配置脚本

这是一个用于快速配置 Zsh 开发环境的自动化脚本，包含 oh-my-zsh、starship 提示符、常用插件等。

## 功能特性

- ✅ 自动安装 Zsh 和必要依赖
- ✅ 安装 oh-my-zsh 框架
- ✅ 配置 starship 现代化提示符
- ✅ 安装常用插件（自动补全、语法高亮、模糊搜索）
- ✅ 自动设置为默认 shell
- ✅ 幂等性设计，可重复执行


```bash
cat ~/Software/setup_zsh.sh | iconv -f utf-8 -t utf-16le | clip.exe
```

### 
```
chmod +x ~/Software/setup_zsh.sh
~/Software/setup_zsh.sh
```

## 脚本内容

```bash
#!/usr/bin/env bash
set -e

# =========================
#  Zsh 环境配置脚本
# =========================

# 工具函数：如果没安装就安装
install_if_missing() {
    if ! command -v "$1" &>/dev/null; then
        echo ">>> 安装 $1 ..."
        sudo apt install -y "$1"
    else
        echo ">>> $1 已安装"
    fi
}

echo ">>> 更新系统..."
sudo apt update -y

# 必要工具
install_if_missing git
install_if_missing curl
install_if_missing zsh
install_if_missing fzf

# =========================
#  安装 starship
# =========================
if ! command -v starship &>/dev/null; then
    echo ">>> 安装 starship..."
    curl -sS https://starship.rs/install.sh | sh -s -- -y
else
    echo ">>> starship 已安装"
fi

# =========================
#  安装 oh-my-zsh
# =========================
if [ ! -d "$HOME/.oh-my-zsh" ]; then
    echo ">>> 安装 oh-my-zsh..."
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
else
    echo ">>> oh-my-zsh 已安装"
fi

# =========================
#  安装插件
# =========================
ZSH_CUSTOM=${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}

# autosuggestions
if [ ! -d "$ZSH_CUSTOM/plugins/zsh-autosuggestions" ]; then
    echo ">>> 安装 zsh-autosuggestions..."
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM}/plugins/zsh-autosuggestions
else
    echo ">>> zsh-autosuggestions 已安装"
fi

# syntax-highlighting
if [ ! -d "$ZSH_CUSTOM/plugins/zsh-syntax-highlighting" ]; then
    echo ">>> 安装 zsh-syntax-highlighting..."
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM}/plugins/zsh-syntax-highlighting
else
    echo ">>> zsh-syntax-highlighting 已安装"
fi

# =========================
#  修改 zshrc
# =========================
echo ">>> 配置 .zshrc ..."
# 主题改成 robbyrussell（默认简单主题，starship 会覆盖）
sed -i 's/^ZSH_THEME=.*$/ZSH_THEME="robbyrussell"/' ~/.zshrc || true

# 插件配置
if grep -q "^plugins=" ~/.zshrc; then
    sed -i 's/^plugins=(.*)$/plugins=(git zsh-autosuggestions zsh-syntax-highlighting fzf)/' ~/.zshrc
else
    echo 'plugins=(git zsh-autosuggestions zsh-syntax-highlighting fzf)' >> ~/.zshrc
fi

# starship 初始化
if ! grep -q 'eval "$(starship init zsh)"' ~/.zshrc; then
    echo 'eval "$(starship init zsh)"' >> ~/.zshrc
fi

# =========================
#  切换默认 shell
# =========================
if [ "$SHELL" != "$(which zsh)" ]; then
    echo ">>> 设置 zsh 为默认 shell..."
    chsh -s "$(which zsh)"
fi

echo "===================================="
echo "✅ 安装完成！请运行以下命令立即生效："
echo "   source ~/.zshrc"
echo "   退出并重新登录即可启用 zsh"
echo "===================================="
```

## 安装组件说明

### 核心组件
- **Zsh**: 强大的命令行shell
- **Oh My Zsh**: Zsh配置框架
- **Starship**: 跨shell的现代化提示符

### 插件功能
- **git**: Git命令别名和状态显示
- **zsh-autosuggestions**: 基于历史的命令自动建议
- **zsh-syntax-highlighting**: 命令语法高亮
- **fzf**: 模糊搜索工具

## 使用技巧

### 常用快捷键
- `Ctrl+R`: 搜索历史命令
- `Tab`: 命令补全
- `→`: 接受自动建议
- `Ctrl+T`: fzf文件搜索

### 自定义配置

#### 修改Starship主题
```bash
# 创建配置文件
mkdir -p ~/.config
starship config > ~/.config/starship.toml

# 编辑配置
nano ~/.config/starship.toml
```

#### 添加自定义别名
```bash
# 编辑 ~/.zshrc
echo 'alias ll="ls -la"' >> ~/.zshrc
echo 'alias ..="cd .."' >> ~/.zshrc
source ~/.zshrc
```

## 系统要求

- Ubuntu/Debian 系列 Linux 发行版
- 需要 sudo 权限
- 网络连接（用于下载组件）

## 故障排除

### 1. 权限问题
```bash
# 确保脚本有执行权限
chmod +x setup_zsh.sh

# 检查sudo权限
sudo -v
```

### 2. 网络连接问题
```bash
# 测试网络连接
curl -I https://github.com
ping -c 3 github.com
```

### 3. 插件不生效
```bash
# 重新加载配置
source ~/.zshrc

# 检查插件路径
ls -la ~/.oh-my-zsh/custom/plugins/
```

### 4. Starship不显示
```bash
# 检查starship是否安装
which starship

# 手动添加到.zshrc
echo 'eval "$(starship init zsh)"' >> ~/.zshrc
```

### 5. 恢复默认设置
```bash
# 切换回bash
chsh -s /bin/bash

# 备份并重置zshrc
cp ~/.zshrc ~/.zshrc.backup
rm ~/.zshrc
```

## 卸载方法

```bash
# 删除 oh-my-zsh
rm -rf ~/.oh-my-zsh

# 删除配置文件
rm ~/.zshrc

# 切换回默认shell
chsh -s /bin/bash

# 卸载starship（可选）
sudo rm /usr/local/bin/starship
```

## 更多资源

- [Oh My Zsh 官方文档](https://ohmyz.sh/)
- [Starship 配置指南](https://starship.rs/config/)
- [Zsh 用户指南](http://zsh.sourceforge.net/Guide/)