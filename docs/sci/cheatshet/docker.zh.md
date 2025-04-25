---
title: docker
tag: 
    - docker
    - 打包
    - 依赖
---

## docker 安装

Docker 是一个开源的容器化平台，可以通过以下步骤安装：

1. 更新系统包：
   ```bash
   sudo apt-get update
   ```
2. 安装必要的依赖：
   ```bash
   sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
   ```
3. 添加 Docker 官方 GPG 密钥：
   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```
4. 添加 Docker 仓库：
   ```bash
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```
5. 安装 Docker：
   ```bash
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io
   ```
6. 验证安装：
   ```bash
   docker --version
   ```

## docker 拉取镜像启动容器

使用以下命令从 Docker Hub 拉取镜像：
```bash
docker pull <镜像名称>:<标签>
```
例如，拉取最新的 Ubuntu 镜像：
```bash
docker pull ubuntu:latest
```

## docker 图形化界面 gui

可以使用 Portainer 作为 Docker 的图形化界面管理工具：

1. 拉取 Portainer 镜像：
   ```bash
   docker pull portainer/portainer-ce
   ```
2. 启动 Portainer 容器：
   ```bash
   docker run -d -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
   ```
3. 访问 GUI 界面：
   打开浏览器，访问 `http://localhost:9000`。

## docker 打包

使用以下命令将应用程序打包为 Docker 镜像：

1. 创建一个 `Dockerfile` 文件，定义镜像构建规则。例如：
   ```dockerfile
   FROM node:14
   WORKDIR /app
   COPY . .
   RUN npm install
   CMD ["node", "app.js"]
   ```
2. 构建镜像：
   ```bash
   docker build -t <镜像名称>:<标签> .
   ```
3. 验证镜像：
   ```bash
   docker images
   ```

## 打包程序安装

将打包的镜像运行为容器：

1. 使用以下命令运行容器：
   ```bash
   docker run -d -p 8080:8080 --name=<容器名称> <镜像名称>:<标签>
   ```
2. 验证容器是否运行：
   ```bash
   docker ps
   ```
3. 访问应用程序：
   打开浏览器，访问 `http://localhost:8080`。