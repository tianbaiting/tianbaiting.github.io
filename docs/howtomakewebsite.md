# how to make a web like this

我采用的是Githubpages. 这样并不需要任何购买服务器,也不需要购买域名. 

然后利用mkdocs,由markdown格式来产生一个静态的HTML网站.(不然直接写前端也蛮麻烦的) 

当代码push到github上,利用github work flow自动部署网页.

## Github Pages介绍

GitHub Pages 是一个静态网站托管服务，您可以直接从 GitHub 仓库中发布网站。它支持与 Jekyll 等静态网站生成器集成，方便地将 Markdown 文件转换为静态网页。

## MkDocs介绍

MkDocs 是一个用于构建静态文档网站的简单且快速的静态站点生成器。它使用 Markdown 编写文档，并生成一个完全静态的 HTML 网站。MkDocs 的主要特点包括：

- **简单易用**：使用简单的命令行工具和配置文件即可生成文档网站。
- **主题支持**：内置多个主题，并支持自定义主题。
- **扩展性强**：支持多种插件，可以扩展 MkDocs 的功能。
- **实时预览**：在本地编写文档时，可以实时预览文档的效果。

通过使用 MkDocs，您可以轻松地将 Markdown 文件转换为美观的静态网站，并将其托管在 GitHub Pages 上。

## GitHub Workflow介绍

GitHub Workflow 是 GitHub Actions 的一部分，它允许您在 GitHub 仓库中定义自动化流程。通过编写 YAML 文件，您可以在特定事件（如代码推送）发生时触发自动化任务，例如构建、测试和部署您的项目。利用 GitHub Workflow，您可以实现持续集成和持续部署（CI/CD），提高开发效率和代码质量。



## 使用步骤

### 第一步：创建 GitHub 仓库

1. 登录 GitHub 并创建一个新的仓库。
2. 将仓库命名为 `username.github.io`，其中 `username` 是您的 GitHub 用户名。

### 第二步：安装 MkDocs

(本地的网页运行是不必需的,可以完全放在github上.)

1. 确保您已经安装了 Python 和 pip。
2. 使用以下命令安装 MkDocs：
    ```bash
    pip install mkdocs
    ```

### 第三步：创建 MkDocs 项目

1. 在本地机器上创建一个新的 MkDocs 项目：
    ```bash
    mkdocs new my-project
    cd my-project
    ```

### 第四步：编写文档

1. 在 `docs` 文件夹中编写您的 Markdown 文件。
2. 更新 `mkdocs.yml` 配置文件以包含您的文档。

### 第五步：本地预览

1. 使用以下命令在本地预览您的网站：
    ```bash
    mkdocs serve
    ```
2. 打开浏览器并访问 `http://127.0.0.1:8000` 查看您的网站。

### 第六步：部署到 GitHub Pages

1. 将您的项目推送到 GitHub 仓库。
2. 在 GitHub 仓库中，设置 GitHub Pages 来源为 `gh-pages` 分支。
3. 使用 GitHub Actions 自动化部署：
    - 创建 `.github/workflows/gh-pages.yml` 文件。
    - 添加以下内容：
      ```yaml
      name: Deploy to GitHub Pages
      on:
         push:
            branches:
              - main
      jobs:
         deploy:
            runs-on: ubuntu-latest
            steps:
              - name: Checkout repository
                 uses: actions/checkout@v2
              - name: Set up Python
                 uses: actions/setup-python@v2
                 with:
                    python-version: '3.x'
              - name: Install dependencies
                 run: |
                    pip install mkdocs
                    pip install mkdocs-material
              - name: Build and deploy
                 run: |
                    mkdocs gh-deploy --force
      ```

完成以上步骤后，您的网站将自动部署到 GitHub Pages，并可以通过 `https://username.github.io` 访问。

