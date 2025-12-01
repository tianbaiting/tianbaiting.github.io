# 获取环境变量

绝对路径在不同设备使用程序时候不好使

相对路径在不同路径使用宏的时候不好使

于是最好的方法是获取环境变量
c++
```c++
#include <cstdlib>
// 获取环境变量
#include <iostream>
const char* val = std::getenv("MY_ENV_VAR");
if (val) std::cout << val << std::endl;
//get env
```
python
```python
import os
# 获取环境变量
val = os.getenv("MY_ENV_VAR")
if val:
    print(val)
# get env
```
latex
```latex
% 获取环境变量
\documentclass{article}
\usepackage{ifthen}
\begin{document}
\newcommand{\getenv}[1]{%
  \ifthenelse{\isundefined{#1}}%
    {Environment variable #1 is not set.}%
    {The value of #1 is \csname #1\endcsname.}
}
\getenv{MY_ENV_VAR}
\end{document}
```
md
```md
# 获取环境变量
可以使用以下语法获取环境变量的值：  
`$ENV{MY_ENV_VAR}`
``` 

bash
```bash
# 获取环境变量
val=$MY_ENV_VAR
if [ -n "$val" ]; then
    echo "$val"
fi
# get env
```

geant4 macro
```g4macro
# 获取环境变量
/controls/execute /path/to/your/script.sh $ENV{MY_ENV_VAR}
# get env
```

cmake
```cmake
# 获取环境变量
set(ENV{MY_ENV_VAR} "default_value")
message(STATUS "MY_ENV_VAR: $ENV{MY_ENV_VAR}")
# get env
```
 