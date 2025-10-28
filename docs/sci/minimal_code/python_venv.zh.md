---
title: Python 虚拟环境
slug: python-venv
tags: [sci, python]
summary: 在 Python 中使用虚拟环境来隔离项目依赖。
---

# Python 虚拟环境

在 Python 开发中，虚拟环境（virtual environment）是一种用于隔离项目依赖的工具。它允许你为每个项目创建独立的环境，从而避免不同项目之间的依赖冲突。
## 创建虚拟环境
要创建一个新的虚拟环境，可以使用 `venv` 模块。以下是创建虚拟环境的步骤：
1. 打开终端或命令提示符。
2. 导航到你的项目目录。 
3. 运行以下命令来创建虚拟环境：
   ```
   python -m venv venv
   ```
   这将在你的项目目录中创建一个名为 `venv` 的文件夹，其中包含虚拟环境的所有必要文件。

   或者新建".venv" 隐藏文件夹，美观一点

## 激活虚拟环境
在创建虚拟环境后，你需要激活它。激活方式取决于你的操作系统：

- **Windows:**
  ```
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```
  source venv/bin/activate
  ```
激活后，你会看到命令行提示符前面出现了 `(venv)`，表示你现在正在使用虚拟环境。

## 安装依赖包
在激活虚拟环境后，你可以使用 `pip` 来安装项目所需的依赖包。例如：
```pip install numpy pandas matplotlib
``` 


## 如果不激活虚拟环境

也可以直接使用 
```
.venv\Scripts\python.exe -m pip install package_name
```
linux
```
.venv/bin/python3 -m pip install package_name
```

来安装包，而不需要激活虚拟环境。

运行也是同样的道理。


## conda

某位我非常尊敬的续老师不推荐conda，认为他是商业软件，又慢。 只是在推广上花了很多功夫，很多人在写各种文档。

如果你使用的是 Anaconda 或 Miniconda，可以使用 `conda` 来创建和管理虚拟环境。以下是使用 `conda` 创建虚拟环境的步骤：
1. 打开终端或命令提示符。
2. 运行以下命令来创建虚拟环境：
   ```
   conda create --name myenv
   ```
   这将创建一个名为 `myenv` 的虚拟环境。

3. 激活虚拟环境：
   ```
   conda activate myenv
   ```  
4. 安装依赖包：
   ```
   conda install numpy pandas matplotlib
   ```
5. 退出虚拟环境：
   ```
   conda deactivate
   ```