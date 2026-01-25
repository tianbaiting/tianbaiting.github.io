# ROOT 库管理与单元测试

https://root.cern/manual/integrate_root_into_my_cmake_project/



本文档旨在为粒子物理学家提供关于 ROOT (CERN) 第三方库管理、制作以及单元测试的综合教程。

## 第一部分：ROOT 库的制作与查找

在 ROOT 中，“库”通常指共享目标文件（`.so`（Linux）、`.dylib`（macOS）、`.dll`（Windows））。为了让 ROOT 的解释器（Cling）理解你的 C++ 类，必须生成字典（dictionary）。

### 1. 制作一个 ROOT 库（工作流程）

假设有一个简单的物理类 `MyParticle`。

步骤 A: 编写源码

文件：`MyParticle.h`
```cpp
#ifndef MYPARTICLE_H
#define MYPARTICLE_H

#include "TObject.h"

class MyParticle : public TObject {
private:
    double fE; // Energy
    double fPx; // Momentum X

public:
    MyParticle();
    MyParticle(double e, double px);
    virtual ~MyParticle();

    double GetMass() const;
    
    // 必须包含这个宏，用于 ROOT RTTI (Run Time Type Information)
    ClassDef(MyParticle, 1); 
};

#endif
```

文件：`MyParticle.cxx`
```cpp
#include "MyParticle.h"
#include <cmath>

ClassImp(MyParticle); // 对应 ClassDef

MyParticle::MyParticle() : fE(0), fPx(0) {}
MyParticle::MyParticle(double e, double px) : fE(e), fPx(px) {}
MyParticle::~MyParticle() {}

double MyParticle::GetMass() const {
    return std::sqrt(fE*fE - fPx*fPx);
}
```

步骤 B: 编写 `LinkDef.h`（关键）

告诉 ROOT 哪些类需要生成字典的配置文件：

文件：`LinkDef.h`
```cpp
#ifdef __CINT__
#pragma link off all globals;
#pragma link off all classes;
#pragma link off all functions;

// 开启我们要制作库的类
#pragma link C++ class MyParticle+;
#endif
```

步骤 C: 编译与生成字典（不使用 CMake 的手动方式）

为了演示原理，直接使用编译器命令。在实际工程中推荐使用 CMake。

1. 生成字典源代码（`G__MyParticle.cxx`）：
```bash
rootcling -f G__MyParticle.cxx -c MyParticle.h LinkDef.h
```

2. 编译物理类和字典，生成共享库（`.so`）：
```bash
g++ -shared -fPIC -o libMyParticle.so MyParticle.cxx G__MyParticle.cxx `root-config --cflags --libs`
```

现在会得到 `libMyParticle.so` 和 `G__MyParticle_rdict.pcm`（ROOT 6+ 需要 pcm 文件）。

### 2. 寻找与加载第三方库

分两类：解释型（ROOT 宏 / Cling）与编译型（可执行程序）。

场景：不想 `make install`（本地调试）

如果不将库安装到系统路径，需要告诉系统和 ROOT 库的位置。假设库在当前目录 `/path/to/workdir`。

方式一：ROOT 解释器 / 宏（Cling）

- 动态加载（常用）：
```cpp
// 在宏的开头
gSystem->Load("/path/to/workdir/libMyParticle.so");
```

- R__LOAD_LIBRARY（推荐，在解析脚本前处理依赖）：
```cpp
// myScript.C
R__LOAD_LIBRARY("/path/to/workdir/libMyParticle.so")

void myScript() {
    MyParticle p(10, 2);
    cout << p.GetMass() << endl;
}
```

- 修改动态路径并以短名加载：
```cpp
gSystem->AddDynamicPath("/path/to/workdir");
gSystem->Load("libMyParticle"); // 或 gSystem->Load("MyParticle")，ROOT 会尝试补全
```

方式二：编译型 C++ 程序（Compiled Executable）

编译示例：
```bash
g++ main.cpp -o runAnalysis -I. -L. -lMyParticle `root-config --cflags --libs`
```

运行时若未安装库，需设置环境变量：

Linux:
```bash
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/workdir
```

macOS:
```bash
export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:/path/to/workdir
```

## 第二部分：使用 Google Test (gtest) 测试 ROOT 代码

ROOT 代码本质是 C++，可以用 Google Test 编写单元测试。

### 1. 环境准备

Ubuntu:
```bash
sudo apt-get install libgtest-dev googletest
# 可能需要手动编译 gtest 或使用 CMake FetchContent
```

Conda（推荐）:
```bash
conda install -c conda-forge gtest
```

### 2. 编写测试用例

文件：`test_MyParticle.cpp`
```cpp
#include <gtest/gtest.h>
#include "MyParticle.h"

// 测试构造函数
TEST(MyParticleTest, Constructor) {
    MyParticle p;
    EXPECT_DOUBLE_EQ(p.GetMass(), 0.0);
}

// 测试质量计算逻辑
TEST(MyParticleTest, MassCalculation) {
    // E=5, Px=3 -> Mass = sqrt(25-9) = 4
    MyParticle p(5.0, 3.0); 
    EXPECT_DOUBLE_EQ(p.GetMass(), 4.0);
}
```

> 如果测试需要 ROOT 的全局对象（如 `TFile`, `TCanvas`, `TH1`），可能需要在 `main` 中初始化 `TApplication`；纯数学/逻辑类通常不需要。

### 3. 编译测试程序

需要链接：gtest、ROOT、自定义库。例如：
```bash
g++ test_MyParticle.cpp -o runTests \
    -I. -L. -lMyParticle \
    -lgtest -lgtest_main -pthread \
    `root-config --cflags --libs`
```

运行前设置库路径：
```bash
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.
./runTests
```

预期输出示例：
```
[==========] Running 2 tests from 1 test suite.
[----------] 2 tests from MyParticleTest
[ RUN      ] MyParticleTest.Constructor
[       OK ] MyParticleTest.Constructor (0 ms)
[ RUN      ] MyParticleTest.MassCalculation
[       OK ] MyParticleTest.MassCalculation (0 ms)
[  PASSED  ] 2 tests.
```

## 第三部分：高级技巧 - 使用 CMake 自动化

手动敲 `g++` 容易出错。建议使用 CMake。

示例 `CMakeLists.txt`：
```cmake
cmake_minimum_required(VERSION 3.10)
project(MyAnalysis)

# 寻找 ROOT
find_package(ROOT REQUIRED COMPONENTS RIO Net)
include(${ROOT_USE_FILE})

# 寻找 GTest
find_package(GTest REQUIRED)

# 包含目录
include_directories(${CMAKE_CURRENT_SOURCE_DIR} ${ROOT_INCLUDE_DIRS})

# 生成字典并创建库
ROOT_GENERATE_DICTIONARY(G_MyParticle MyParticle.h LINKDEF LinkDef.h)
add_library(MyParticle SHARED MyParticle.cxx G_MyParticle.cxx)
target_link_libraries(MyParticle ${ROOT_LIBRARIES})

# 创建测试可执行文件
add_executable(unit_tests test_MyParticle.cpp)
target_link_libraries(unit_tests MyParticle GTest::gtest GTest::gtest_main ${ROOT_LIBRARIES})

# 测试支持
enable_testing()
add_test(NAME ParticlesTest COMMAND unit_tests)
```

构建与运行测试：
```bash
mkdir build && cd build
cmake ..
make
ctest --verbose
```

## 总结（关键命令 / 方法）

- 制作库：`rootcling` + `g++ -shared`，必须有 `LinkDef.h` 生成字典。  
- 编译时链接：`-L/path -lName`。  
- 运行时加载：未 install 时需设置 `LD_LIBRARY_PATH`（或 macOS 的 `DYLD_LIBRARY_PATH`）。  
- ROOT 解释器加载：`gSystem->Load("path/to/lib.so")` 或 `R__LOAD_LIBRARY("path/to/lib.so")`（脚本首选）。  
- 单元测试：使用 `gtest`，按普通 C++ 程序方式测试 ROOT 类。

## 附录：库名、文件名与标识符详解 (FAQ)

1. 好多名字


| 身份 | 示例 | 决定时刻 | 使用场景 | 规则 / 解释 |
|---|---|---|---|---|
| 链接名 (Linker Name) | libMyParticle.so | 制作软链时 | 编译链接 (g++ -lMyParticle) | 这是一个软链接。它不含版本号，直接指向 SONAME 或真实文件。它的存在是为了让 g++ 能找到库。 |
| SONAME (内部逻辑名) | libMyParticle.so.1 | 编译库源码时 | 程序运行时 (ld.so 加载器) | 最关键的名字。它被“烙印”在库文件头中，也被烙印在 executable 里。程序运行时只认这个名字！ |
| 真实名 (Real Name) | libMyParticle.so.1.2 | 编译生成文件时 (-o) | 物理存储、ls、cp | 包含完整版本信息（主版本.次版本）的真实物理文件。 |
| 加载名 (Load Name) | MyParticle | ROOT 脚本编写时 | gSystem->Load | ROOT 封装的查找逻辑，通常为了方便交互式使用。 |


方法 A: 使用 CMake (推荐)

CMake 会自动帮你处理复杂的参数和软链接生成。
```
add_library(MyParticle SHARED MyParticle.cxx G_MyParticle.cxx)

# PROPERTIES 指令决定了 SONAME 和 Real Name
# VERSION 1.2  -> 决定真实名为 libMyParticle.so.1.2
# SOVERSION 1  -> 决定 SONAME 为 libMyParticle.so.1 (意味着 API 兼容性版本为 1)
set_target_properties(MyParticle PROPERTIES VERSION 1.2 SOVERSION 1)
```

结果：make 之后，CMake 会自动生成真实文件，并创建两个软链接 (.so 指向 .so.1，.so.1 指向 .so.1.2)。

方法 B: 使用 g++ 手动制作 (Hardcore Mode)

你需要手动传递链接器参数 (-Wl 选项)。

```
# 1. 编译库：同时指定输出文件名(-o) 和 内部SONAME (-Wl,-soname,...)
g++ -shared -fPIC \
    -Wl,-soname,libMyParticle.so.1 \
    -o libMyParticle.so.1.2 \
    MyParticle.cxx G__MyParticle.cxx `root-config --libs`

# 此时你得到了一个文件：libMyParticle.so.1.2
# 如果你用 readelf -d libMyParticle.so.1.2 查看，会发现它内心知道自己叫 libMyParticle.so.1

# 2. 手动建立软链接体系 (必须做，否则编译或运行会报错)

# 给运行时用 (满足 SONAME 查找)
ln -s libMyParticle.so.1.2 libMyParticle.so.1

# 给编译连接器用 (满足 -lMyParticle 查找)
ln -s libMyParticle.so.1 libMyParticle.so
```


2. 库的“身份证” (Symbols)

当加载 `.so` 时，库内部包含一张“符号表”。可以用 `nm` 查看：

```bash
# -C: demangle, -D: dynamic symbols
nm -C -D libMyParticle.so | grep MyParticle
```

示例输出：
```
0000000000001140 T MyParticle::MyParticle(double, double)  <-- 构造函数
0000000000001180 T MyParticle::GetMass() const             <-- 成员函数
0000000000004050 V typeinfo for MyParticle                 <-- RTTI (ROOT 需要)
```

如果遇到 `undefined reference to MyParticle::GetMass()`，通常原因：
- 链接时路径不对（`-L` 未指向正确目录）。
- 链接到的库中缺少实现（生成库时漏编译源文件）。

3. 我该用哪个名字？

- 在 `LinkDef.h` 中：使用 C++ 类名（`MyParticle`）。  
- 在 `g++` 编译命令中：使用链接名（`-lMyParticle`）。  
- 在 ROOT 脚本中：推荐使用物理文件名（`libMyParticle.so`）或确保 `LD_LIBRARY_PATH` 设置正确后使用加载名。

进阶：版本号危机与软链接 (Versioning & Symlinks)

现象: 编译时报错 cannot find -lMyParticle，或者运行时报错 error while loading shared libraries: libMyParticle.so.1: cannot open shared object file。

原因: 系统在寻找库时，遵循一套严格的 SONAME (Shared Object Name) 机制。

库文件通常有三个名字（以 libfoo 为例）：

真实名 (Real Name): libfoo.so.1.2.3 (实际包含代码的文件，带完整版本号)

SONAME (内部名): libfoo.so.1 (标志主版本兼容性。编译后的程序运行时只认这个名字！)

链接名 (Linker Name): libfoo.so (不带版本号。编译时 g++ 只认这个名字！)

典型故障与修复 (软链接)：

故障 A: 编译失败
你有一个 libMyParticle.so.1.0，但 g++ -l MyParticle 报错找不到库。

原因: g++ 找的是 libMyParticle.so，而你只有带版本号的文件。

修复: 创建软链接。

```
ln -s libMyParticle.so.1.0 libMyParticle.so
```

故障 B: 运行失败
你编译好的程序在另一台机器运行，报错 libMyParticle.so.1 not found，但目录下明明有 libMyParticle.so。

原因: 程序编译时记住了 SONAME 是 so.1，它运行时就死板地找 so.1，不认 so。

修复:

ln -s libMyParticle.so libMyParticle.so.1


总结: 在发布库时，标准做法是保留真实文件，并创建两个软链接指向它（一个给编译用，一个给运行用）。
