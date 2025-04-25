# git 备忘单

## 常用 Git 命令

### 初始化
- `git init`：初始化一个新的 Git 仓库。

### 配置
- `git config --global user.name "你的名字"`：设置全局用户名。
- `git config --global user.email "你的邮箱@example.com"`：设置全局邮箱。

### 基本工作流程
- `git status`：检查工作目录的状态。
- `git add <文件>`：将更改暂存。
- `git commit -m "提交信息"`：提交暂存的更改。

更复杂的工作流详见[[minimal_code/git.zh]]


### 分支管理
- `git branch`：列出分支。
- `git branch <分支名>`：创建新分支。
- `git checkout <分支名>`：切换到某个分支。
- `git merge <分支名>`：将某个分支合并到当前分支。

### 远程仓库
- `git remote add origin <网址>`：添加远程仓库。
- `git push -u origin <分支名>`：将更改推送到远程分支。
- `git pull`：从远程仓库获取并合并更改。

### 日志与历史
- `git log`：查看提交历史。
- `git diff`：显示提交或工作目录之间的更改。

### 撤销更改
- `git reset <文件>`：取消暂存文件。
- `git checkout -- <文件>`：放弃文件中的更改。

### 暂存
- `git stash`：临时保存更改。
- `git stash apply`：重新应用暂存的更改。

### 克隆
- `git clone <网址>`：克隆一个仓库。

### 删除
- `git branch -d <分支名>`：删除分支。
- `git rm <文件>`：从仓库中删除文件。

## 使用 rebase 合并提交
