# cmake项目

## gcc g++

GCC 是编译器。 gcc是c语言，g++是其中的c++.

编译流程

        - 预处理（expand macros、处理#include）
        - 编译（.c/.cpp -> 汇编）
        - 汇编（汇编 -> 目标文件 .o）
        - 链接（把若干 .o / 库组合成可执行文件或库）

常用选项
  - -Wall 开启常见警告
  - -g 生成调试信息
  - -O2 或 -O3 优化
  - -I \<dir\> 添加头文件搜索路径
  - -L \<dir\> 和 -l \<name\> 添加库搜索路径与链接库

### 单个文件
```bash
g++ -c main.cpp -o main.o
```
```bash
g++ main.cpp 
```
这会直接编译汇编链接成可执行文件，不利于理解


常用命令
- 只编译生成目标文件（不链接）：
```bash
g++ -c main.cpp -o main.o
```
这会生成 main.o（可重定位目标文件），适合把多个源文件分别编译再链接。

- 链接生成可执行文件（把 .o 链接成可执行文件）：
```bash
g++ main.o -o main
```




### 多个文件无库

多个文件，
可以不用头文件，
g++ -c mian.cc b.cc

```cpp
// main.cpp
#include <stdio.h>

extern const char *msg;

int main() {
    printf("%s\n", msg);
    return 0;
}
```

```cpp
//b.cc
const char *msg = "您好";
```


注意
- .o 文件是目标文件，不可直接运行，需要链接生成可执行文件。
- 当有多个源文件时，推荐分别 -c 生成 .o，再统一链接，方便增量构建与并行编译。
- 对 C++ 项目用 g++ 来链接，避免缺少标准库链接的问题。




按需编译与未定义符号示例

 main.cpp 中引用了一个外部变量  `extern const char *msg;`。当编译器编译 main.cpp 时，它并不知道 `msg` 在哪儿定义，所以在生成的目标文件 main.o 中会留下对 `msg` 的未定义符号引用。之后编译 b.cpp 时，如果在 b.cpp 中定义了 `const char *msg = ...;`，编译器会把该定义编译到 b.o。最终链接器把 main.o 与 b.o 链接在一起，从而解析并完成对 `msg` 的解析。

这个流程说明按需编译的要点：先把每个源文件分别编译成目标文件（.o），再由链接器把它们合并解析未定义符号。这样当某个源文件修改时，只需重新编译被修改的源文件生成新的 .o，然后重新链接，避免不必要的全量编译，提升构建效率。


“无头文件”的写法是一种为了教学、为了展示extern关键字和链接器底层工作原理的极限简化示例。在任何真实的、稍具规模的项目中，这都是绝对不推荐的做法。

我们来对比一下：

无头文件的做法 (不推荐)
工作原理: 在 main.cpp 中使用 extern const char *msg; 告诉编译器：“别担心，msg 这个变量确实存在，只不过在别的文件里。你先编译，链接器到时候会找到它的。”

为什么这是坏习惯:

没有“契约”: main.cpp 的作者只能靠口头约定或者记忆来知道 b.cpp 里有 msg，并且知道它的类型是 const char *。如果 b.cpp 的作者把 msg 的类型改成了 std::string，main.cpp 在编译时完全不会报错，直到链接阶段才会因为找不到匹配的符号而失败，这种错误非常难以排查。

可读性极差: 任何人想使用 b.cpp 里的功能，都必须去阅读 b.cpp 的源代码，而不是查阅一个清晰的 .h 头文件。

无法提供函数声明: 如果 b.cpp 提供的是一个函数 int get_value()，main.cpp 同样需要 extern int get_value(); 这样的“外部声明”。随着函数增多，在每个使用它的 .cpp 文件里都手写一遍声明，是一场维护灾难。


有头文件的做法
```
#include <iostream>
#include "b.h" // 包含接口说明书，编译器就知道 msg 是什么了

int main() {
    std::cout << msg << std::endl;
    return 0;
}

```


```
#pragma once // 防止头文件被重复包含

// 在头文件中“声明”接口，告诉所有人：
// “我这里对外提供一个名为 msg 的变量”
extern const char* msg;
```


```
#include "b.h" // 包含自己的接口声明，确保实现与声明一致
// 在源文件中“定义”实现
const char* msg = "Hello from b.cpp with header!";
```


include 相当于在预处理把 b.h 的内容直接插入到 main.cpp 和 b.cpp 里。这样 main.cpp 和 b.cpp 都能看到对 msg 的声明，编译器就知道 msg 是什么了。



### 动态库 静态库


#### 无头文件的不规范写法

打包成动态库
```bash
g++ -fPIC -c b.cpp -o b.o       # 生成位置无关代码
g++ -shared -o libb.so b.o      # 打包成动态库
g++ main.cpp -L. -lb -o main    # 使用动态库
export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH && ./main
```


打包成静态库
```bash
g++ -c b.cpp -o b.o             # 编译目标文件
ar rcs libb.a b.o               # 打包成静态库
g++ main.cpp -L. -lb -o main    # 使用静态库
```

#### 有头文件的规范写法

要点
- 头文件 (*.h / *.hpp) 只放公有接口：函数声明、外部变量声明、类型定义、宏、inline/模板实现等；实现放在 .cpp/.cc。
- 使用 include guard 或 `#pragma once` 防止重复包含。
- 模板、inline 函数、类定义需在头文件中可见，不能仅靠二进制库提供。
- 若需以 C 风格导出以避免 C++ name mangling，可在头文件使用 `extern "C"`（仅在需要与 C 互操作时）。
- 在 Windows 上常用宏控制导出/导入（如 __declspec(dllexport/__declspec(dllimport)）。

最小示例

```cpp
// b.h
#pragma once

extern const char *msg;
```

```cpp
// b.cc
#include "b.h"
const char *msg = "您好";
```

```cpp
// main.cpp
#include <stdio.h>
#include "b.h"

int main() {
    printf("%s\n", msg);
    return 0;
}
```

构建与链接（静态库）
```bash
g++ -c b.cc -o b.o
ar rcs libb.a b.o
g++ main.cpp libb.a -o main
./main
```

构建与链接（动态库）
```bash
g++ -fPIC -c b.cc -o b.o
g++ -shared -o libb.so b.o
g++ main.cpp -L. -lb -o main
export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
./main
```



简短注意事项
- 头文件保证声明与定义一致，减少调用方错误；不使用头文件易出现类型/签名不匹配难以排查的问题。
- 模板与 inline 必须放头文件；若需要跨语言或控制可见性，需在头文件中添加相应的修饰（extern "C"、导出宏等）。
- 保持头文件最小且稳定，避免在头文件中包含大量实现细节以减少不必要的重编译。

简短注意事项
- 头文件保证声明与定义一致，减少调用方错误；不使用头文件易出现类型/签名不匹配难以排查的问题。
- 模板与 inline 必须放头文件；若需要跨语言或控制可见性，需在头文件中添加相应的修饰（extern "C"、导出宏等）。


## make

一个较好的文档  https://seisman.github.io/how-to-write-makefile/index.html

make原理，主要通过文件的时间戳来判断哪些文件需要重新编译。每个目标文件都有一个依赖列表，make 会检查这些依赖文件的修改时间，如果发现某个依赖文件比目标文件新，就会重新编译该目标文件。

make命令用于检查更新，执行命令。（当make命令寻找makefile时，它按照以下顺序尝试查找文件名： GNUmakefile 、 makefile 和 Makefile。）


GNU Make是一个自动化构建工具，主要用于管理项目中的文件依赖关系和自动化编译过程。它通过读取Makefile文件中的规则和指令，来决定哪些文件需要重新编译，并执行相应的命令。在linux中认为make=gnu make。

make install 把可执行文件（target目标）复制到系统目录（如 /usr/local/bin），以便全局使用。


```makefile
# Makefile
CXX := g++ # CXX是makefile的内置变量，表示C++编译器
TARGET := hello 

# 内置变量有很多，常用的有：
# CXX      : C++ 编译器
# CC       : C 编译器
# CFLAGS   : C 编译器选项
# CXXFLAGS : C++ 编译器选项
# LDFLAGS  : 链接器选项
# LDLIBS   : 链接库选项
# TARGET   : 目标文件名
# SRCS    : 源文件 一般写很多个，就不用再编译链接都手动加了
# OBJS    : 目标文件

$(TARGET): main.o b.o
	$(CXX) -o $(TARGET) main.o b.o

main.o: main.cpp # main.o 目标文件， 检查main.cpp更新时间，若更新则执行下面的命令
	$(CXX) -c main.cpp

b.o: b.cpp
	$(CXX) -c b.cpp

clean:
	rm -f *.o $(TARGET)

.PHONY: clean  #声明伪目标，并不生成一个叫clean的文件
```



上诉makefile压根没写.h文件，makefile如何找到源文件所对应的头文件的：

实际上make 本身完全不关心 C++ 语法，它不认识 #include。make 的任务是执行写下的命令。所以，“找头文件”这个动作是由 make 调用的 g++ 命令来完成的。


- 通过依赖关系：在 makefile 中明确指定源文件对头文件的依赖，例如 `main.o: main.cpp b.h`。这样当 b.h 修改时，make 会重新编译 main.o。(简单但不推荐)
- 使用自动依赖生成工具：如 gcc 的 `-MMD -MP` 选项，可以在编译时生成依赖文件（.d），然后在 makefile 中包含这些依赖文件，自动处理头文件的变化。

在上个 Makefile 中，因为 b.h 和 main.cpp 都在同一个目录下，所以 g++ 默认就能找到它，一切看似正常。



g++ 查找头文件遵循以下顺序：

对于 #include "b.h"：首先在源文件所在的当前目录查找。

对于 #include <iostream>：在系统指定的标准库路径中查找。

在 -I 选项指定的路径中查找：我们可以通过 g++ 的 -I 选项来手动添加头文件的搜索目录。



如何改进 Makefile 来明确指定路径？
一个好的 Makefile 应该使用 CXXFLAGS 变量来统一管理编译选项，包括头文件路径。

```makefile
# Makefile - 版本 2 (明确指定头文件路径)
CXX := g++
# 使用 CXXFLAGS 统一管理编译选项
# -I. 表示将当前目录“.”也加入头文件搜索路径
CXXFLAGS := -Wall -I. 
TARGET := hello

$(TARGET): main.o b.o
	$(CXX) -o $(TARGET) main.o b.o

main.o: main.cpp
	$(CXX) $(CXXFLAGS) -c main.cpp # 使用 $(CXXFLAGS)

b.o: b.cpp
	$(CXX) $(CXXFLAGS) -c b.cpp # 使用 $(CXXFLAGS)

clean:
	rm -f *.o $(TARGET)

.PHONY: clean
```



```makefile
# Makefile - 最终版 (自动化依赖管理)
CXX := g++
CXXFLAGS := -Wall -I. -g # 添加了-g调试选项
TARGET := hello
SOURCES := main.cpp b.cpp
OBJECTS := $(SOURCES:.cpp=.o) # 通过源文件列表自动生成目标文件列表
DEPS := $(SOURCES:.cpp=.d)    # 通过源文件列表自动生成依赖文件列表

# 默认目标
all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CXX) $(OBJECTS) -o $(TARGET)

# 通用编译规则
# %.o: %.cpp 表示任何 .o 文件都依赖于同名的 .cpp 文件
%.o: %.cpp
	# -MMD -MP 会在编译时自动生成 .d 依赖文件
	$(CXX) $(CXXFLAGS) -c $< -o $@ -MMD -MP

clean:
	rm -f $(OBJECTS) $(TARGET) $(DEPS)

# 包含所有自动生成的 .d 依赖文件
# -include 会在文件不存在时不报错，这在第一次编译时是必需的
-include $(DEPS)

.PHONY: clean all
```


## CMAKE

用于生成makefile。


简单的 add_executable(hello main.cpp b.cpp) 写法在项目变大后难以维护。现代CMake的核心思想是**“万物皆目标 (Target)”**，我们将属性（如头文件路径、链接库、编译选项）精确地附加到具体的目标上。



一个较为优秀的例子，由上交的ipads提供。 提供了在项目中cmake的各种功能。

【IPADS新人培训第二讲：CMake】 https://www.bilibili.com/video/BV14h41187FZ/?share_source=copy_web&vd_source=727ffe1727e24c229169af42b43aa2e0

https://github.com/richardchien/modern-cmake-by-example


```cmake
# CMakeLists.txt
cmake_minimum_required(VERSION 3.10) 
project(HelloProject)

add_executable(hello main.cpp b.cpp)
```


构建流程:
```bash
mkdir build && cd build
cmake ..
make
./hello
```

cmake 怎么怎么查找第三方包？

cmake 查找包主要通过 `find_package` 命令实现。它会在系统预定义的路径以及用户指定的路径中查找包的配置文件（通常是 `<PackageName>Config.cmake` 或 `Find<PackageName>.cmake`）。这些配置文件定义了包的包含目录、库文件等信息，供 cmake 使用。

cmake 怎么加入自己写的动态库或者静态库？

可以使用 `add_library` 命令来添加自己写的动态库或静态库，然后使用 `target_link_libraries` 将其链接到可执行文件。

```cmake
# CMakeLists.txt
cmake_minimum_required(VERSION 3.10)
project(HelloProject)

# 添加静态库
add_library(mylib STATIC mylib.cpp)

# 添加可执行文件
add_executable(hello main.cpp)

# 链接库到可执行文件
target_link_libraries(hello mylib)
```




####  一个能测试的最小demo


源文件，库文件，main.cpp, lib.cpp, lib.h

```cpp
#include <iostream>
#include "lib.h"

int main() {
    std::cout << "Hello, World!" << std::endl;
    mylib_function();
    return 0;
}
```

```cpp
#include <iostream>

void mylib_function() {
    std::cout << "Hello from mylib!" << std::endl;
}
```




```cmake
# 1. 设置CMake最低版本和项目信息
cmake_minimum_required(VERSION 3.15)
project(RealWorldProject LANGUAGES CXX VERSION 1.0)

# 2. 设置C++标准
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 3. [核心] 将模块化代码构建成一个库(Target)
add_library(mylib STATIC src/b.cpp)

# 4. [核心] 为库(Target)附加属性
# target_include_directories: 为目标指定头文件搜索路径
# PUBLIC: 编译 mylib 自己需要此路径，任何链接 mylib 的目标也自动获得此路径。
target_include_directories(mylib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

# 5. 添加可执行文件(Target)
add_executable(hello src/main.cpp)

# 6. [核心] 将可执行文件(Target)链接到库(Target)
# PRIVATE: 只有 hello 这个目标需要链接 mylib，这个链接关系不会传递给其他目标。
target_link_libraries(hello PRIVATE mylib)

# 7. [进阶] 查找与链接外部库 (以ROOT为例)
# 在粒子物理领域，这非常常见
find_package(ROOT COMPONENTS RIO Hist REQUIRED)
if(ROOT_FOUND)
    # 如果找到了ROOT，将其库链接到我们的可执行文件
    target_link_libraries(hello PRIVATE ROOT::RIO ROOT::Hist)
endif()

# 8. [进阶] 精细控制编译选项
# 为所有目标添加基础警告选项
add_compile_options(-Wall -Wextra -Wpedantic)

# 使用“生成器表达式”为不同构建类型设置不同选项
# $<CONFIG:Debug> 表示仅在Debug模式下生效
target_compile_options(hello PRIVATE
    $<$<CONFIG:Debug>:-g>
    $<$<CONFIG:Release>:-O3>
)
target_compile_definitions(hello PRIVATE
    $<$<CONFIG:Debug>:MY_DEBUG_MACRO>
)

# 9. [进阶] 添加测试 (使用CTest)
enable_testing() # 开启测试功能
# 添加一个名为 "BasicTest" 的测试，它执行命令 ./hello
add_test(NAME BasicTest COMMAND hello)
# 运行测试: cd build && ctest
```


#### debug 和 测试