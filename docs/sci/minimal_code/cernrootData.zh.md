# CERN ROOT 数据结构

.root 文件本质上是一个自描述的二进制文件系统。C++ 是静态语言，通常编译后会丢失类的信息（成员名、类型）。ROOT 通过生成字典（Dictionary）为 C++ 提供反射能力。TTree 使用列式存储（Columnar Storage）：读取特定列只需访问该列数据，不必读整个事件。

## 概念要点
- .root 文件格式：底层是序列化（Serialization）机制。
- TTree：上层是列式存储逻辑，便于高效分析。
- 字典（Dictionary）：由 rootcling/LinkDef.h 生成，描述类结构，支持 Streamer/Unstreamer 和 Schema Evolution。
- Basket（缓冲区）：TBranch 使用 TBasket 缓冲并压缩（ZLIB/LZMA/ZSTD），提高 I/O 与压缩效率。

## C++ 反射（字典）
字典告诉 ROOT 类的成员结构，例如：MyParticle 有 double energy、int id、vector<double> hits。写入时 ROOT 调用对象的 Streamer，把对象序列化到 Buffer；读取时调用 Unstreamer 按字典重建对象。

- 基本类型（int, double）：直接拷贝字节（注意大小端）。
- 指针：处理引用、避免重复写入。
- STL 容器：有专门算法把容器内数据连续写入。

## .root 的目录与对象
.root 文件包含目录（类似文件夹）和对象（类似文件）。每个目录可以包含子目录和数据对象，文件自描述便于跨平台读取。

## 列式存储与 TTree 结构
TTree 将同一变量的数据连续存储（列式），而不是每个事件打包存储（行式）。这样在只关心少数 Branch 时能大幅减少 I/O。

## Basket（篮子）与 Fill 流程
- Filling：调用 tree->Fill() 时，数据先写入内存 TBasket。
- Compressing：当 Basket 达到阈值（例如 32 KB）会压缩后写盘。相似数据容易被高效压缩。
- Flushing：压缩后的 Basket 写入 .root 文件，并更新分支索引。
- 读取优化：如果只给部分 Branch 设置 SetBranchAddress，ROOT 只读取对应 Branch 的 Baskets。

## 生成字典的核心步骤
1. 准备：编写一个特殊的头文件 `LinkDef.h`（告诉 ROOT 哪些类需要字典）。
2. 生成：使用工具 `rootcling` 生成 C++ 代码。

根据使用场景（脚本宏 vs 编译型程序），操作流程有明显区别，下面分开说明。

---

# 实践：link、split level、存储与读取
目标：生成既能被 ROOT 直接读取，又可被 C++ 高效访问，并且在 TBrowser 中能够展开嵌套（如直接画出 hits 的直方图）的 .root 文件。

要点：
1. 在 LinkDef.h 中生成对应类与容器的字典（例如 `std::vector<double>`）。
2. 通过 `ROOT_GENERATE_DICTIONARY` 或 `rootcling` 生成字典并编译成共享库。
3. 建立 Branch 时使用合适的 split level（通常用默认的 99，而不是 0），这样 TBrowser 能把对象拆开显示成员。

## LinkDef 示例
通常命名为 `LinkDef.h`，内容示例：

```cpp
#ifdef __CINT__
// 清除默认设置，防止把不该包的东西包进去
#pragma link off all globals;
#pragma link off all classes;
#pragma link off all functions;

// 显式列出你要生成字典的类
// 格式：#pragma link C++ class 类名+;
// 注意 "+" 表示让 ROOT 自动处理 I/O 格式演变（Schema Evolution）
#pragma link C++ class MyParticle+;
#pragma link C++ class EventHeader+;

// 如果用了 std::vector 等容器，也建议加上
#pragma link C++ class std::vector<MyParticle>+;

#endif
```

---

## 场景一：ROOT 宏脚本 (Macro)
场景：写一个 `.C` 文件，用 `root -l myScript.C` 快速运行，或用 `.L myScript.C` 加载。

### 要点（ACLiC，简便）
1. 在类定义中加入 `ClassDef` 宏（建议做法，虽然不加也可运行，但存文件会受限）。

```cpp
// MyScript.C
#include "TObject.h"

class MyData : public TObject {
public:
    double energy;
    MyData() : energy(0) {}
    ClassDef(MyData, 1);
};
```

2. 运行方式：使用“加号”编译

```cpp
root [0] .L MyScript.C+
# 或
root -l 'MyScript.C+'
```

原理：`+` 告诉 ROOT 调用编译器（g++）把脚本编译成动态库，ROOT 会自动在内存中生成字典，通常不需手写 LinkDef.h。

---

## 场景二：C++ 编译模式（Makefile / 手工 g++）
场景：写独立程序（如 `main.cc`）或构建大型库。标准做法如下。

### Header 示例（MyParticle.h）
```cpp
#ifndef MYPARTICLE_H
#define MYPARTICLE_H
#include "TObject.h"
#include <vector>

class MyParticle : public TObject {
public:
    int pid;
    double energy;
    std::vector<double> hits;

    MyParticle();
    virtual ~MyParticle();
    ClassDef(MyParticle, 1);
};
#endif
```

### 使用 rootcling 生成字典
```
rootcling -f Dict.cxx -c MyParticle.h LinkDef.h
```
执行后会得到 `Dict.cxx` 和 `Dict_rdict.pcm`。

### cpp 中设置 split level（写入时）
示例 `main.cxx`：

```cpp
#include "TFile.h"
#include "TTree.h"
#include "TRandom3.h"
#include "MyParticle.h"
#include <iostream>

int main() {
    TFile *f = new TFile("output.root", "RECREATE");
    TTree *tree = new TTree("tree", "Event Tree");

    MyParticle *p = new MyParticle();

    // 参数: ("BranchName", "ClassName", &Pointer, BufferSize, SplitLevel)
    tree->Branch("particle", "MyParticle", &p, 32000, 99);

    TRandom3 r;
    for (int i = 0; i < 1000; ++i) {
        p->hits.clear(); // 清空容器

        p->pid = i;
        p->energy = r.Gaus(100, 10);

        int n_hits = (int)r.Uniform(5, 20);
        for (int j = 0; j < n_hits; ++j) {
            p->hits.push_back(r.Gaus(0, 1));
        }

        tree->Fill();
    }

    tree->Write();
    f->Close();
    delete f;
    std::cout << "Write done. Split Level 99 used." << std::endl;
    return 0;
}
```

### 编译（手工 g++）
```bash
# 1. 编译类实现
g++ -c MyParticle.cxx `root-config --cflags`

# 2. 编译生成的字典
g++ -c Dict.cxx `root-config --cflags`

# 3. 链接可执行文件
g++ -o myAnalysis main.cxx MyParticle.o Dict.o `root-config --glibs`
```

---

## CMake（现代工程做法）
使用 CMake 时可让 ROOT 自动处理字典生成。

示例 CMakeLists.txt 片段：

```cmake
find_package(ROOT REQUIRED COMPONENTS RIO Tree)

set(HEADERS MyParticle.h OtherClass.h)

ROOT_GENERATE_DICTIONARY(G__Dict
    ${HEADERS}
    LINKDEF LinkDef.h
)

add_executable(myAnalysis main.cxx MyParticle.cxx ${G__Dict})
target_link_libraries(myAnalysis ${ROOT_LIBRARIES})
```

---

# 读取数据（三种方式）
假设文件 `output.root`，Tree 名称 `"tree"`，分支名 `"particle"`，类型为自定义类 `MyParticle`。

在不清楚数据结构时，可用 TBrowser 浏览文件内容。 或者使用 TTree::Print() 查看结构 ; 或者 TTree::Show(0) 查看第一条记录; 或者 TTree::Scan("particle") 查看所有记录 ; 或者 TTree::GetListOfBranches() 列出所有分支 或者 TTree::GetBranch("particle")->Print() 查看分支详情。或者使用 TTree::GetBranch("particle")->GetSplitLevel() 查看 split level;或者 tfile->Map() 查看文件映射。

## 1. 传统方式：SetBranchAddress（不推荐新代码）
特点：手动管理指针，容易出错但可微调 I/O。

```cpp
#include "TFile.h"
#include "TTree.h"
#include "MyParticle.h"
#include <iostream>

void read_legacy() {
    TFile *f = new TFile("output.root", "READ");
    TTree *tree = (TTree*)f->Get("tree");

    MyParticle *p = nullptr; // 必须初始化为 nullptr
    tree->SetBranchAddress("particle", &p);

    Long64_t nentries = tree->GetEntries();
    for (Long64_t i = 0; i < nentries; ++i) {
        tree->GetEntry(i);
        if (p->energy > 50.0) {
            std::cout << "Event " << i << ": High Energy = " << p->energy
                      << " (Hits: " << p->hits.size() << ")" << std::endl;
        }
    }

    f->Close();
    delete f;
}
```

## 2. 现代推荐：TTreeReader

类型安全，自动按需加载，异常安全。

```cpp
#include "TFile.h"
#include "TTreeReader.h"
#include "TTreeReaderValue.h"
#include "MyParticle.h"
#include <iostream>

void read_modern() {
    TFile *f = TFile::Open("output.root", "READ");
    TTreeReader myReader("tree", f);
    TTreeReaderValue<MyParticle> p(myReader, "particle");

    while (myReader.Next()) {
        if (p->energy > 50.0) {
            std::cout << "High Energy: " << p->energy
                      << " | First Hit: " << (p->hits.empty() ? 0 : p->hits[0])
                      << std::endl;
        }
    }
    delete f;
}
```

## 3. 高级分析：RDataFrame
声明式、支持并行，适合统计分析与画图。

```cpp
#include <ROOT/RDataFrame.hxx>
#include "MyParticle.h"

void read_rdf() {
    ROOT::EnableImplicitMT();

    ROOT::RDataFrame df("tree", "output.root");

    auto h_hits = df.Filter([](const MyParticle &p){ return p.hits.size() > 0; }, {"particle"})
                    .Define("total_hits", [](const MyParticle &p){ return (int)p.hits.size(); }, {"particle"})
                    .Histo1D({"h_hits", "Hits Distribution", 20, 0, 20}, "total_hits");

    auto c = new TCanvas();
    h_hits->DrawClone();
}
```

---

# 总结
- 想省事/测试：在 ROOT 里用 `.L xxx.C+`，全自动生成字典。
- 写正式项目/库：在头文件加 `ClassDef`，写 `LinkDef.h`，用 `rootcling` 生成字典并与代码一起编译。
- split level：写入时使用 99，让 TBrowser 能展开成员变量。
- 读取推荐使用 TTreeReader 或 RDataFrame，尽量避免直接用 SetBranchAddress 在新代码中管理裸指针。
