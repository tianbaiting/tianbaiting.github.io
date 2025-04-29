---
title: jupyter notebook
tag:
    - ipynb
    - jupyter
---

## jupyter notebook 可运行的编程语言

Jupyter Notebook 的前身是 IPython Notebook。后来，它扩展为支持多种编程语言，包括但不限于：

- Python
- R
- Julia
- Scala
- Ruby
- JavaScript
- Bash
- C++
- Go
- Kotlin

这种多语言支持使得 Jupyter Notebook 成为数据科学、机器学习和教育领域的强大工具。

## 安装 jupyter notebook

推荐使用 pip 安装。
在终端执行：
```bash
pip install jupyter metakernel
```

安装完毕后，测试是否正常运行。
在终端输入：
```
jupyter-notebook
```

安装 root 之后，在个人 home 目录.bashrc 文件中添加
```
source (pathof)thisroot.sh
```
进入自己的项目目录，在终端执行
```
root --notebook
```

## 添加 Kernel 的步骤

在 Jupyter Notebook 中添加新的 Kernel，可以按照以下步骤操作：

1. **安装所需的编程语言环境**  
    确保已安装目标编程语言的运行时环境。例如，安装 Python、R 或 Julia 等。

2. **安装 Jupyter Kernel**  
    根据目标语言安装相应的 Jupyter Kernel。例如：  
    - 对于 Python，可以使用 `ipykernel`：  
        ```bash
        pip install ipykernel
        ```  
    - 对于 R，可以使用 `IRkernel`：  
        ```R
        install.packages("IRkernel")
        IRkernel::installspec()
        ```  
    - 对于 Julia，可以使用 `IJulia`：  
        ```julia
        using Pkg
        Pkg.add("IJulia")
        ```  
    - 对于 C#，可以使用 `dotnet-interactive`：  
        ```bash
        dotnet tool install -g Microsoft.dotnet-interactive
        dotnet interactive jupyter install
        ```  
        或者`clingkernel`:
        ```
        pip install clingkernel
        clingkernel install --sys-prefix
        ```

3. **注册 Kernel**  
    安装完成后，Kernel 会自动注册到 Jupyter Notebook。如果未自动注册，可以手动执行相关命令。例如：
    ```bash
    python -m ipykernel install --user --name=my_kernel_name
    ```

4. **启动 Jupyter Notebook**  
    启动 Jupyter Notebook 并在新建文件时选择刚刚添加的 Kernel。

通过以上步骤，您可以在 Jupyter Notebook 中添加并使用新的 Kernel，从而支持更多的编程语言。



## 在 Jupyter Notebook 中运行 Bash 脚本

在 Jupyter Notebook 中，可以通过以下几种方式运行 Bash 脚本：

1. **使用 `!` 命令**  
    在代码单元中直接使用 `!` 来运行 Bash 命令或脚本。例如：
    ```bash
    !sh script.sh
    ```

2. **使用 `subprocess` 模块**  
    在 Python 代码中使用 `subprocess` 模块运行 Bash 脚本。例如：
    ```python
    import subprocess
    subprocess.run(['sh', 'script.sh'])
    ```

3. **使用 `%%bash` 魔法命令**  
    在代码单元中使用 `%%bash` 魔法命令运行 Bash 脚本。例如：
    ```bash
    %%bash
    # Bash 脚本内容
    sh script.sh
    ```

通过以上方法，可以在 Jupyter Notebook 中方便地运行 Bash 脚本，从而实现与系统命令的交互。

## ipyplot


```python
video_paths = ["my_video.mp4"]
video_labels = ["My Video"]
ipyplot.plot_videos(video_paths, video_labels, width=320)
```



```python
import matplotlib.pyplot as plt
import numpy as np
import ipyplot
import tempfile
import os

# 1. 使用 matplotlib 绘制图形
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.title("Matplotlib 图形")

# 2. 创建一个临时文件来保存 matplotlib 图形
with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_file:
    temp_filename = tmp_file.name
    plt.savefig(temp_filename)

# 3. 使用 ipyplot 显示临时图像文件
ipyplot.plot_images([temp_filename], ["Matplotlib Plot"], img_width=400)

# 4. 清理临时文件
os.remove(temp_filename)
```