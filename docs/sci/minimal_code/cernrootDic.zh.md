# root 字典

生成字典的核心只有两步：

1. **准备**：编写一个特殊的头文件 `LinkDef.h`（告诉 ROOT 哪些类需要字典）。
2. **生成**：使用工具 `rootcling` 生成 C++ 代码。

根据你的使用场景（是写简单的宏脚本，还是写正经的编译型程序），操作流程有很大区别。我们分开讲。

-----

### 核心准备：`LinkDef.h` 怎么写？

无论哪种模式，你都需要这个文件。它相当于给编译器的一份“愿望清单”。

通常命名为 `LinkDef.h`（或 `MyClassLinkDef.h`），内容如下：

```cpp
#if defined(__CINT__) || defined(__CLING__)
// 1. 先清除默认设置，防止把不该包的东西包进去
#pragma link off all globals;
#pragma link off all classes;
#pragma link off all functions;

// 2. 显式列出你要生成字典的类
// 格式：#pragma link C++ class 类名+;
// 注意那个 "+" 号！它表示让 ROOT 自动处理 I/O 格式演变（Schema Evolution）
#pragma link C++ class MyParticle+;
#pragma link C++ class EventHeader+;

// 3. 如果用了 std::vector 这种容器，通常也建议加上
#pragma link C++ class std::vector<MyParticle>+;

#endif // __CINT__ || __CLING__
```

-----

### 场景一：ROOT 宏脚本 (Macro)

场景：你写了一个 `.C` 文件，想用 `root -l myScript.C` 快速运行，或者用 `.L myScript.C` 加载。

这种情况下，ACLiC 是最简单的方案。你不需要手动敲 `rootcling` 命令，ROOT 会自动帮你做。

#### 步骤：

1. 在你的类定义中加入 `ClassDef` 宏（建议做法，虽然不加也能跑，但存文件会受限）。

```cpp
// MyScript.C
#include "TObject.h"

class MyData : public TObject { // 最好继承自 TObject
public:
    double energy;
    MyData() : energy(0) {}
    
    // 这里的 1 是版本号。如果你以后修改了类结构，要把 1 改成 2
    ClassDef(MyData, 1);
};
```

2. 运行方式：使用“加号”编译  
在 ROOT 命令行里，不要只用 `.L MyScript.C`，而是用：

```cpp
root [0] .L MyScript.C+
```

或者在终端直接运行：

```bash
root -l 'MyScript.C+'
```

原理：那个 `+` 号告诉 ROOT：“请调用编译器（g++）把这个脚本编译成动态库”。在这个过程中，ROOT 会自动检测类，自动在内存中生成字典，无需你手写 `LinkDef.h`（除非极其复杂的情况）。编译完后，它会生成一个 `MyScript_C.so`，下次运行会非常快。

-----

### 场景二：C++ 编译模式 (Makefile / CMake)

场景：你在写一个独立的程序（比如 `main.cc`），或者在构建一个大型库。这是物理实验中最标准的做法。

#### 步骤 1：准备源代码

Header.h（类定义）：

```cpp
#ifndef HEADER_H
#define HEADER_H
#include "TObject.h"

class MyParticle : public TObject {
public:
    double x, y, z;
    MyParticle();
    virtual ~MyParticle();

    // 这一行必须加！必须放在 public 区域
    ClassDef(MyParticle, 1);
};
#endif
```

LinkDef.h 请参考上文。

#### 步骤 2：使用 rootcling 生成字典

运行命令行工具：

- `-f` : 指定输出的字典文件名（一般叫 `Dict.cxx` 或 `G__MyClass.cxx`）。
- `-c` : 指定输入的头文件。
- 最后是 `LinkDef.h`。

```bash
rootcling -f Dict.cxx -c Header.h LinkDef.h
```

执行后，目录下会多出两个文件：`Dict.cxx`（C++ 源码）和 `Dict_rdict.pcm`（预编译模块）。

#### 步骤 3：编译所有文件

把你的源代码和生成的字典代码一起编译：

```bash
# 1. 编译你的类
g++ -c MyParticle.cxx `root-config --cflags`

# 2. 编译生成的字典（这一步至关重要）
g++ -c Dict.cxx `root-config --cflags`

# 3. 链接成可执行文件（main.cxx 是你的主程序）
g++ -o myAnalysis main.cxx MyParticle.o Dict.o `root-config --glibs`
```

-----

### 场景三：CMake (现代工程做法)

如果你的项目用 CMake，你不需要手写上面的 `g++` 命令。ROOT 提供了专门的 CMake 宏。

示例 CMakeLists.txt：

```cmake
# ... 前面的 find_package(ROOT ...) 省略 ...

# 1. 定义头文件列表
set(HEADERS MyParticle.h OtherClass.h)

# 2. 调用 ROOT 宏生成字典
# 这会自动运行 rootcling 并把输出文件放到变量 G__Dict 中
ROOT_GENERATE_DICTIONARY(G__Dict 
    ${HEADERS} 
    LINKDEF LinkDef.h
)

# 3. 编译库或可执行文件时，把生成的 G__Dict.cxx 带上
add_executable(myAnalysis main.cxx MyParticle.cxx ${G__Dict})
target_link_libraries(myAnalysis ${ROOT_LIBRARIES})
```

### 总结

1. 想省事/测试代码：在 ROOT 里用 `.L xxx.C+`，全自动。
2. 写正经项目/库：
   - 在头文件里加 `ClassDef(ClassName, 1)`。
   - 写 `LinkDef.h`。
   - 用 `rootcling` 生成 `Dict.cxx`。
   - 把 `Dict.cxx` 和你的代码一起编译。
