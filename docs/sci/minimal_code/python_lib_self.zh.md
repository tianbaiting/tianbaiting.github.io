# python 包的创建与使用

作为码农，经常需要编写可重用的代码来处理数据、进行模拟或实现复杂的算法。将这些代码打包成一个可以自己调用的 Python 包，是提高代码复用性、可维护性和协作效率的最佳实践。



-----

### 方式一：最简单的方式（本地目录导入）

这种方式适用于个人项目或快速测试，不需要安装，仅依赖 Python 的导入路径机制。

#### 1\. 创建项目结构

假设你的项目叫 `particle_analysis`，目录结构如下：

```
/path/to/your/project/
├── my_particle_lib/
│   ├── __init__.py
│   ├── kinematics.py
│   └── plotting.py
└── main_analysis.py
```

  * **`my_particle_lib/`**: 这就是你的 "包"。一个包含 `__init__.py` 文件的目录在 Python 中就会被视为一个包。
  * **`__init__.py`**: 这个文件可以是空的。它的存在告诉 Python，`my_particle_lib` 是一个包，而不是一个普通的文件夹。你也可以在这个文件里写代码，比如提前导入子模块中的常用函数。
  * **`kinematics.py`**: 你的一个功能模块，用于运动学计算。
  * **`plotting.py`**: 另一个功能模块，用于绘图。
  * **`main_analysis.py`**: 你的主程序脚本，将在这里调用你的包。

#### 2\. 编写包内代码

**`my_particle_lib/kinematics.py`**:

```python
# my_particle_lib/kinematics.py

import numpy as np

def calculate_momentum(mass, velocity):
    """Calculates momentum."""
    if mass < 0 or velocity < 0:
        return 0
    return mass * velocity

def calculate_energy(mass, velocity):
    """Calculates kinetic energy using a simple formula."""
    return 0.5 * mass * velocity**2
```

**`my_particle_lib/plotting.py`**:

```python
# my_particle_lib/plotting.py

import matplotlib.pyplot as plt

def plot_energy_vs_velocity(mass, velocities):
    """Plots energy as a function of velocity."""
    energies = [0.5 * mass * v**2 for v in velocities]
    plt.figure()
    plt.plot(velocities, energies)
    plt.xlabel("Velocity (m/s)")
    plt.ylabel("Kinetic Energy (J)")
    plt.title(f"Energy vs. Velocity for mass={mass}kg")
    plt.grid(True)
    plt.show()
```

**`my_particle_lib/__init__.py`** (可选，但推荐):
为了方便调用，你可以在 `__init__.py` 文件中将常用函数导入到包的顶层命名空间。

```python
# my_particle_lib/__init__.py

# 从子模块中导入函数，这样用户可以直接 from my_particle_lib import ...
from .kinematics import calculate_momentum, calculate_energy
from .plotting import plot_energy_vs_velocity

print("Particle analysis library loaded!")
```

#### 3\. 在主程序中调用

现在，在与 `my_particle_lib` 目录同级的 `main_analysis.py` 文件中，你可以这样调用你的包：

**`main_analysis.py`**:

```python
# main_analysis.py

import numpy as np
import my_particle_lib as ppl # 使用别名是一种好习惯

# --- 调用方式 1: 如果 __init__.py 中导入了函数 ---
# 这是最方便的调用方式
momentum = ppl.calculate_momentum(mass=10, velocity=5)
print(f"Momentum: {momentum}")

# --- 调用方式 2: 通过访问具体模块 ---
# 即使 __init__.py 是空的，这种方式也永远有效
energy = ppl.kinematics.calculate_energy(mass=10, velocity=5)
print(f"Kinetic Energy: {energy}")

# 调用绘图函数
velocities = np.linspace(0, 100, 50)
ppl.plotting.plot_energy_vs_velocity(mass=10, velocities=velocities)

# 如果 __init__.py 中导入了绘图函数，也可以这样：
# ppl.plot_energy_vs_velocity(mass=10, velocities=velocities)
```

**如何运行？**
直接在终端中运行主程序即可：

```bash
python main_analysis.py
```

Python 会自动将脚本所在的目录添加到 `sys.path`（模块搜索路径）中，因此它可以找到 `my_particle_lib` 这个包。

-----

### 方式二：标准化的方式（创建可安装的包）

当你的代码库越来越大，或者希望在其他项目中也能轻松使用，甚至分享给别人时，就应该创建一个标准的可安装包。这样你可以像安装 `numpy` 或 `matplotlib` 一样，通过 `pip` 来安装和管理你的包。

这是现代 Python 项目推荐的做法。

#### 1\. 改进项目结构

使用 `src` 布局是当前推荐的最佳实践，它能清晰地将源码与项目配置文件分开。

```
/path/to/your/package-project/
├── src/
│   └── my_particle_lib/
│       ├── __init__.py
│       ├── kinematics.py
│       └── plotting.py
├── pyproject.toml
├── README.md
└── LICENSE
```

  * **`src/`**: 存放你的源代码。
  * **`src/my_particle_lib/`**: 你的包的实际代码。
  * **`pyproject.toml`**: **核心文件**。这是现代 Python 包的配置文件，用于告诉 `pip` 和其他构建工具如何构建和安装你的包。
  * **`README.md`**: 项目说明文件。
  * **`LICENSE`**: 开源许可证文件。

#### 2\. 编写 `pyproject.toml`

这是定义你的包的元数据和构建依赖的地方。

**`pyproject.toml`**:

```toml
# 使用 setuptools 作为构建后端
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

# 项目元数据
[project]
name = "my-particle-lib" # 包在 PyPI 上的名称，通常用连字符
version = "0.0.1"
authors = [
  { name="Your Name", email="your.email@example.com" },
]
description = "A simple library for basic particle physics calculations."
readme = "README.md"
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
# 项目依赖，安装此包时会自动安装这些依赖
dependencies = [
    "numpy",
    "matplotlib",
]
```

#### 3\. 在本地以“可编辑模式”安装包

现在，最关键的一步来了。在项目的根目录（即 `pyproject.toml` 所在的目录）下，运行以下命令：

```bash
pip install -e .
```

  * `pip install`: `pip` 安装命令。
  * `-e` 或 `--editable`: **可编辑模式**。这是一个非常强大的功能。它不会把你的代码复制到 Python 的 `site-packages` 目录，而是在那里创建一个指向你当前项目源码的链接。
  * `.`: 代表当前目录。

**这样做的好处是什么？**
你在 `src/my_particle_lib/` 目录下的任何代码修改，都会**立即生效**，无需重新安装。这对于开发和调试极其方便。

#### 4\. 在任何地方调用你的包

安装完成后，你可以在系统的**任何地方**启动 Python 解释器或运行 Python 脚本来调用你的包，就像调用其他第三方库一样。

例如，在你电脑的任何其他位置创建一个 `test_script.py`：

```python
# /some/other/location/test_script.py

import numpy as np
import my_particle_lib as ppl

# 现在你可以像使用 numpy 一样使用自己的包了
momentum = ppl.calculate_momentum(2, 10)
print(f"Momentum: {momentum}")

velocities = np.linspace(0, 50, 20)
ppl.plot_energy_vs_velocity(mass=2, velocities=velocities)
```

**运行脚本**:

```bash
python /some/other/location/test_script.py
```

代码会完美运行，因为 `my_particle_lib` 已经被 `pip` "注册"到了你的 Python 环境中。

### 总结与对比

| 特性 | 方式一 (本地目录导入) | 方式二 (可安装包) |
| :--- | :--- | :--- |
| **适用场景** | 简单、单个项目、快速原型 | 复杂项目、多项目复用、代码分发 |
| **结构要求** | 仅需 `__init__.py` | 标准化的项目结构，`src` 布局，`pyproject.toml` |
| **安装** | 无需安装 | `pip install -e .` (开发) 或 `pip install .` (部署) |
| **调用范围** | 只能在项目根目录或通过修改 `sys.path` 调用 | 安装后，可在当前 Python 环境的任何地方调用 |
| **依赖管理** | 手动管理 | 在 `pyproject.toml` 中声明，`pip` 自动处理 |
| **推荐度** | 适合初学者理解包的概念 | **专业开发和长期项目的最佳实践** |

强烈推荐使用**方式二**。它能让分析代码库更加模块化、可移植和易于管理。可以为不同的研究课题（如探测器模拟、数据拟合、统计分析）创建不同的包，然后在主分析脚本中组合使用它们。

### 信息来源

  * **Python Packaging User Guide (官方指南)**: 这是关于打包最权威的资源。
      * [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
  * **setuptools 文档**: `setuptools` 是最常用的 Python 构建工具之一。
      * [Why you shouldn't use `setup.py` directly](https://www.google.com/search?q=%5Bhttps://setuptools.pypa.io/en/latest/userguide/quickstart.html%23setuptools-quickstart%5D\(https://setuptools.pypa.io/en/latest/userguide/quickstart.html%23setuptools-quickstart\)) (解释了为何 `pyproject.toml` 是现代标准)
  * **PEP 621 – Storing project metadata in pyproject.toml**: 详细说明 `pyproject.toml` 中 `[project]` 表的技术规范。
      * [PEP 621](https://peps.python.org/pep-0621/)