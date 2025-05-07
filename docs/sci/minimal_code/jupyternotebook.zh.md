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

[资料](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)

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

## jupyter使用root

[jupyroot](https://github.com/root-project/root/tree/master/bindings/jupyroot)
1. [Install ROOT6](https://root.cern.ch/building-root) (> 6.05)
2. Install dependencies: `pip install jupyter metakernel`
### 开始使用 ROOTbooks

设置 ROOT 环境（`. $ROOTSYS/bin/thisroot.[c]sh`），然后在终端中输入：
```shell
root --notebook
```
这将在您的计算机上启动一个带有 ROOT 功能的 notebook 服务器。

或者，如果您希望直接使用 Jupyter 命令，可以执行以下操作：
```shell
jupyter kernelspec install $ROOTSYS/etc/root/notebook/kernels/root --user
```

服务器启动后，您可以使用 ROOT 提供的两种 Kernel：

1. ROOT C++：由 ROOT 提供的新 Kernel
2. Python：Jupyter 已经提供的 Kernel

### C++ ROOTbook

ROOT 提供了一个 C++ Kernel，将 notebook 转变为一个 ROOT 提示符。该 Kernel 提供了嵌入式图形、语法高亮和自动补全等功能。

以下是如何在 C++ ROOTbook 中绘制直方图的示例：
```cpp
TCanvas c;
TH1F h("h","ROOT Histo;X;Y",64,-4,4);
h.FillRandom("gaus");
h.Draw();
c.Draw();
```

### Python ROOTbook

如果您更喜欢使用 Python，可以创建一个新的 Python Kernel 并导入 ROOT 库：
```python
import ROOT
```
然后您可以编写如下代码：
```python
c = ROOT.TCanvas("c")
h = ROOT.TH1F("h","ROOT Histo;X;Y",64,-4,4)
```


此外，您还可以通过使用 **%%cpp** 魔法命令在同一个 notebook 中混合使用 Python 和 C++：
```cpp
%%cpp
h->FillRandom("gaus");
h->Draw();
c->Draw();
```

假如要在Jupyter里调用其他地方的函数，得:
```cpp
%%cpp
#pragma cling add_include_path("include")

#include "/data4/tbt23/smsimulator5.5/anal_D_tbt/original_data_tbt/include/get_ratio.h"
#include "/data4/tbt23/smsimulator5.5/anal_D_tbt/original_data_tbt/src/get_ratio.cpp"
```
目前我搞不清楚相对路径是相对的什么东西。特别是get_ratio.cpp里面应该怎么写.h文件的路径。但写绝对路径肯定没错...


### jupyter 魔法命令

Jupyter Notebook 提供了许多魔法命令（Magic Commands），可以帮助用户更高效地完成任务。这些命令分为两类：行魔法命令（以 `%` 开头）和单元魔法命令（以 `%%` 开头）。

#### 常用行魔法命令

```bash
# 列出所有可用的魔法命令
%lsmagic
```

1. **`%time`**  
    用于测量单行代码的执行时间。例如：
    ```python
    %time sum(range(1000000))
    ```

2. **`%timeit`**  
    用于多次运行代码并测量平均执行时间。例如：
    ```python
    %timeit sum(range(1000000))
    ```

3. **`%who` 和 `%whos`**  
    显示当前命名空间中的变量。例如：
    ```python
    %who
    %whos
    ```

4. **`%run`**  
    运行外部 Python 脚本。例如：
    ```python
    %run script.py
    ```

5. **`%matplotlib`**  
    设置 matplotlib 的绘图模式。例如：
    ```python
    %matplotlib inline
    ```

#### 常用单元魔法命令
1. **`%%time`**  
    测量整个单元代码的执行时间。例如：
    ```python
    %%time
    total = 0
    for i in range(1000000):
         total += i
    ```

2. **`%%writefile`**  
    将单元内容写入文件。例如：
    ```python
    %%writefile script.py
    print("Hello, World!")
    ```

3. **`%%bash`**  
    在单元中运行 Bash 脚本。例如：
    ```bash
    %%bash
    echo "Hello from Bash"
    ```

4. **`%%capture`**  
    捕获单元输出并存储到变量中。例如：
    ```python
    %%capture captured_output
    print("This will be captured")
    ```

通过使用这些魔法命令，您可以更高效地完成数据分析、脚本运行和调试等任务。



## jupyter 快捷键

Jupyter Notebook 提供了许多快捷键，可以帮助用户更高效地操作和编辑 notebook。以下是一些常用的快捷键：

### 命令模式（按 `Esc` 进入）
- **Enter**：进入编辑模式
- **Shift + Enter**：运行当前单元并跳转到下一个单元
- **Ctrl + Enter**：运行当前单元
- **Alt + Enter**：运行当前单元并在其下方插入一个新单元
- **A**：在当前单元上方插入一个新单元
- **B**：在当前单元下方插入一个新单元
- **D + D**：删除当前单元
- **Z**：撤销删除单元
- **Y**：将当前单元设置为代码单元
- **M**：将当前单元设置为 Markdown 单元
- **H**：显示快捷键帮助
- **Shift + M**：合并选中的单元

### 编辑模式（按 `Enter` 进入）
- **Ctrl + A**：全选
- **Ctrl + Z**：撤销
- **Ctrl + Shift + Z**：重做
- **Ctrl + Home**：跳转到单元开头
- **Ctrl + End**：跳转到单元末尾
- **Tab**：代码补全或缩进
- **Shift + Tab**：显示工具提示
- **Ctrl + /**：注释或取消注释选中的代码

### 通用快捷键
- **Ctrl + S**：保存 notebook
- **Ctrl + Shift + P**：打开命令面板
- **Shift + L**：切换行号显示
- **O**：切换单元输出的显示/隐藏
- **Shift + O**：切换单元输出的滚动模式




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