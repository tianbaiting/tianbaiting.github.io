# VS Code 插件开发指南

本文介绍如何开发、托管并发布 VS Code 插件。

## 1. 环境准备

首先需要安装 Node.js 和 Git。接着使用 npm 安装 Yeoman 和 VS Code 插件生成器：

```bash
npm install -g yo generator-code
```

## 2. 创建与开发项目

运行以下命令初始化插件项目：

```bash
yo code
```

按照提示选择语言（推荐 TypeScript）和项目名称。完成各步骤后：
1. 使用 VS Code 打开项目文件夹。
2. 按 `F5` 键启动调试，这会打开一个新的“扩展开发宿主”窗口。
3. 修改 `src/extension.ts` 中的代码，然后在调试控制台使用 `Developer: Reload Window` 查看效果。

## 3. 托管至 GitHub

1. 在 GitHub 上创建一个新的仓库。
2. 在本地项目根目录执行：

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <你的仓库地址>
git push -u origin main
```

## 4. 发布到 Marketplace

发布插件需要使用 `vsce` (Visual Studio Code Extensions) 命令行工具。

1. 安装 vsce: `npm install -g vsce`
2. 获取 PAT: 登录 [Azure DevOps](https://dev.azure.com/) 并创建一个 Personal Access Token，权限需选择 `Marketplace (Publish)`。
3. 创建发布者: 在 [Marketplace 管理页面](https://marketplace.visualstudio.com/manage/publishers) 创建发布者账号。
4. 执行发布:

```bash
# 登录发布者账号
vsce login <publisher-name>
# 发布插件
vsce publish
```

更多详细信息可访问 [VS Code 官方文档](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
