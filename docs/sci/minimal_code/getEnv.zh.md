# 获取环境变量

绝对路径在不同设备运行程序时不通用，且相对路径在不同上下文（比如宏或构建系统）中也可能失效。最佳做法是通过环境变量来传递可移植的路径或配置。

## 1. C++ (标准)
获取：
```cpp
#include <cstdlib>
#include <iostream>
#include <string>

// 获取环境变量
const char* val = std::getenv("MY_ENV_VAR");

// 检查是否获取成功
if (val) {
    std::cout << "MY_ENV_VAR 的值: " << val << std::endl;
} else {
    std::cerr << "环境变量 MY_ENV_VAR 未设置!" << std::endl;
    // 可以在这里设置默认值或退出
}
```
使用：
```cpp
// 假设 MY_ENV_VAR 是一个项目根目录的路径
if (val) {
    std::string base_dir(val);
    std::string config_path = base_dir + "/config/settings.ini";
    std::cout << "配置路径: " << config_path << std::endl;
}
```

## 2. Python
获取：
```python
import os

# 获取环境变量，如果未设置，则使用默认值 "/path/to/default"
my_env_var_value = os.getenv("MY_ENV_VAR", "/path/to/default")
print(f"MY_ENV_VAR 的值: {my_env_var_value}")
```
使用：
```python
# 假设 MY_ENV_VAR 是一个数据目录路径，使用 os.path.join 跨平台构造路径
import os
data_file_path = os.path.join(my_env_var_value, "simulation", "output.root")
print(f"数据文件路径: {data_file_path}")
```

## 3. Bash
获取：
```bash
# 获取环境变量的值
val="$MY_ENV_VAR"

# 检查是否非空
if [ -n "$val" ]; then
    echo "MY_ENV_VAR 的值: $val"
fi
```
使用：
```bash
# 假设 $MY_ENV_VAR 是一个软件安装路径，使用花括号更安全
echo "Running script from directory: ${val}/scripts"

# 在执行命令时使用
"${val}/bin/run_simulation" --input "${val}/data/input.dat"
```

## 4. CMake
获取（在 CMakeLists.txt 中）：
```cmake
# 读取环境变量并赋值给 CMake 变量（推荐）
set(MY_DIR_FROM_ENV $ENV{MY_ENV_VAR})

# 检查是否被设置
if(MY_DIR_FROM_ENV)
    message(STATUS "MY_ENV_VAR (Env): $ENV{MY_ENV_VAR}")
    message(STATUS "MY_DIR_FROM_ENV (CMake Var): ${MY_DIR_FROM_ENV}")
else()
    # 如果未设置，使用默认值
    set(MY_DIR_FROM_ENV "/opt/myproject/default")
    message(STATUS "MY_ENV_VAR 未设置，使用默认值: ${MY_DIR_FROM_ENV}")
endif()
```
使用：
```cmake
# 使用 CMake 变量指定包含目录或源文件路径
include_directories(${MY_DIR_FROM_ENV}/include)
add_library(MyLib STATIC ${MY_DIR_FROM_ENV}/src/MySource.cpp)
```

## 5. Geant4 宏
获取：
```text
# 将操作系统环境变量 SMSIMDIR 的值赋给 Geant4 宏变量 SMSIMDIR
/control/getEnv SMSIMDIR
```
使用：
```text
# 假设 SMSIMDIR 是模拟输出的根目录
/action/file/SaveDirectory {SMSIMDIR}/data/g4output
/run/initialize

# 或使用 $ 符号（常用于路径）
/file/open $SMSIMDIR/results.root
```

## 6. LaTeX（使用 LuaLaTeX）
标准 LaTeX 不易安全跨平台地读取系统环境变量。推荐使用 LuaLaTeX，通过 Lua 的 `os.getenv` 访问环境变量。

```latex
% 必须使用 LuaLaTeX 编译: lualatex your_file.tex
\documentclass{article}
\usepackage{luacode}

\begin{document}

% 定义命令获取环境变量
\newcommand{\GetEnvVar}[1]{%
    \directlua{tex.print(os.getenv("#1") or "")}%
}

\textbf{MY\_ENV\_VAR 的值:}\par
\GetEnvVar{MY_ENV_VAR}

\end{document}
```
使用示例：
```latex
\section{Simulation Details}
The data was processed using the configuration located in: \GetEnvVar{MY_ENV_VAR}/config.yaml.
```

以上示例展示了常见语言/工具中读取和使用环境变量的规范写法，注意在生产环境中对未设置变量的情况做容错处理（默认值或报错提示）。
