# **ANAROOT 综合分析框架：

该文可能有诸多错误，请看[[anaroot2version.zh]]

## **前言**

ANAROOT 是一个基于 ROOT 开发的综合性数据分析框架，主要服务于日本理化学研究所仁科加速器科学研究中心 (RIKEN Nishina Center) 的放射性同位素束工厂 (Radioactive Isotope Beam Factory, RIBF) 的各项核物理实验。本报告旨在为 ANAROOT 用户提供一份详尽的中文文档，从软件的基本概念、安装配置，到核心功能的使用，最终帮助用户达到能够熟练运用 ANAROOT 进行实验数据分析的水平。报告将特别详细地介绍如何使用 ANAROOT 分析 BigRIPS 中的平行板雪崩计数器 (Parallel Plate Avalanche Counter, PPAC)（通常称为 PDC）以及 SAMURAI 谱仪中的 NEBULA (NEutron Detectors for Breakup of Unstable Nuclei with Large Acceptance) 中子探测器阵列的数据。  
**第一章：ANAROOT 简介**  
本章将对 ANAROOT 软件进行概述，包括其定义、设计目的、核心功能、软件架构及其与 ROOT 框架的关系，同时探讨其开发背景和主要应用场景。  
**1.1 ANAROOT 是什么**  
ANAROOT 是一个专为核物理实验数据分析设计的软件包，由 RIBF 数据采集组 (RIBFDAQ group) 开发和维护 1。它的底层完全构建于 CERN 开发的 ROOT 数据分析框架之上，旨在为 RIBF 的实验数据处理提供一套标准化、高效率的工具集 。ANAROOT 的设计目标是处理由 RIBF 数据采集系统 (Babirl)产生的 RIDF (RIKEN Data Format) 原始数据，并提供从数据解码、刻度、重建到最终物理结果分析的全套解决方案。  
**1.2 核心功能**  
ANAROOT 提供了一系列强大的功能以满足复杂核物理实验的需求 1：

* **数据解码 (Data Decoding):** 集成了多种硬件模块的解码器，例如 MDPP16、A3400、VME-Easyroc、MQDC32/MTDC32 等，能够直接处理 RIDF 格式的原始数据。  
* **数据重建 (Reconstruction):** 包含了针对不同探测器的重建算法，如 NeuLAND、BigRIPS 的塑料闪烁体 (Plastic) 和 PPAC、SAMURAI 径迹探测器以及 BigRIPS-Ge 分析等。  
* **数据刻度 (Calibration):** 提供了针对特定探测器（如 TKE、SAMURAI-TED、SAMURAI-ICF）的刻度程序。  
* **数据处理 (Data Handling):** 支持从 RIDF 数据头中获取运行信息 (RunInfo)，使用 Plastic 类处理 RF 信号，管理 FADC 的原始数据容器等。  
* **在线监控 (Online Monitoring):** 实现了 AnaLoop 例程，主要用于实验过程中的在线数据监控。  
* **事件处理 (Event Processing):** 在 push() 函数中具备事件跳过功能。

**1.3 软件架构与 ROOT 框架的关系**  
ANAROOT 的软件架构深度依赖于 ROOT 框架 。ROOT 不仅仅是一个依赖库，更是 ANAROOT 功能实现的基础。

* **基础库依赖:** ANAROOT 的编译和运行都离不开 ROOT 的核心库和类。  
* **环境集成:** ANAROOT 会生成 ROOT 登录宏 (rootlogon.C) 和配置文件 (.rootrc)，以便在 ROOT 环境中正确加载和使用其自身的库和类。  
* **版本兼容性:** ANAROOT 的开发版本通常与特定的 ROOT 版本相对应（例如，某些版本基于 ROOT 6.28.04 或 ROOT 5.34.21 开发）。因此，用户在安装和使用 ANAROOT 时，必须确保 ROOT 环境的兼容性。

这种紧密的集成关系意味着用户不仅需要掌握 ANAROOT 本身，还需要对 ROOT 的基本操作和编程有一定了解。  
**1.4 开发背景与主要应用场景**  
ANAROOT 由 RIBFDAQ 小组开发，这直接表明其主要服务于 RIKEN 的 RIBF 设施 。其更新日志频繁提及在 RIBF 的各种实验和运行中的开发与应用，例如：

* SAMURAI 2024 年 4 月实验  
* 2017 年春季 S009 实验  
* 2016 年秋季实验  
* SAMURAI s021 实验  
* 2015 年嬗变实验  
* 2012 年 EURICA 实验  
* SAMURAI 和 EURICA 调试运行

这些应用实例凸显了 ANAROOT 在 RIBF 核物理实验数据采集与分析流程中的核心地位，特别是在涉及 BigRIPS 次级束流分离器、SAMURAI 大型强子谱仪、NeuLAND 中子墙、DALI2 gamma 射线阵列等大型探测装置的实验中 。ANAROOT 不仅仅是一个通用的分析工具，更是针对 RIBF 特定实验需求（尤其是其独特的 RIDF 数据格式和复杂的探测器系统）深度定制和优化的专业软件。这种深度集成使得 ANAROOT 成为 RIBF 用户进行数据分析的首选框架，保证了数据处理的一致性和高效性。  
**第二章：ANAROOT 的安装与环境配置**  
本章详细介绍 ANAROOT 的安装过程和环境配置，包括系统需求、依赖项、不同版本的安装步骤以及常见问题的解决。  
**2.1 系统需求与依赖**  
成功安装和运行 ANAROOT 需要满足特定的软硬件环境：

* **操作系统:** 主要在 Linux 环境下开发和测试。虽然在 macOS 上也有成功案例，但 Linux 是首选平台 。  
* **ROOT:** ANAROOT 的核心依赖，必须预先安装并正确配置。不同 ANAROOT 版本可能需要特定范围的 ROOT 版本 。  
* **编译工具:** 标准的 C++ 编译器 (如 GCC)、make 工具。  
* **特定版本依赖 (v4.5 及更早版本) :**  
  * libxml2-devel: XML 解析库，用于处理参数文件。  
  * automake, autoconf, libtool: GNU 构建系统工具。  
  * libedit: 命令行编辑库。  
* **可选依赖:**  
  * minos-fem library: 若需要使用 MINOS 相关部分，则需安装此库 (minos-1.1.1-minimal.tar.gz) 。  
  * Qt: 若计划将 ANAROOT 与 Go4 图形化分析框架集成，则需要安装 Qt 库 4。

**2.2 安装 ROOT**  
在安装 ANAROOT 之前，必须首先安装 ROOT。

1. 访问 ROOT 官方网站 ([http://root.cern.ch](http://root.cern.ch)) 下载合适的 ROOT 版本源代码或预编译包 。  
2. 按照官方文档指引完成 ROOT 的编译和安装。  
3. 设置 ROOT 环境变量。通常，这通过在 shell 中执行 ROOT 安装目录下 bin/thisroot.sh (或 .csh, .fish 等，取决于所用 shell) 脚本来完成 。例如：  
   Bash  
   source $HOME/root/bin/thisroot.sh  
   其中 $HOME/root 是 ROOT 的安装路径。建议将此命令添加到 shell 的配置文件 (如 .bashrc, .zshrc) 中，以便自动加载。

**2.3 安装 ANAROOT**  
ANAROOT 的安装方法因版本而异。  
2.3.1 获取源代码  
ANAROOT 的源代码通常以 .tgz 压缩包的形式发布。可以从 RIBFDAQ 相关网站或通过内部渠道获取，例如 anaroot\_v4.6.1.tgz 。  
2.3.2 CMake 安装方法 (v4.6.1 及以后版本)  
较新版本的 ANAROOT（如 v4.6.1 起）采用 CMake 作为构建系统 。

1. 解压源代码包：  
   Bash  
   tar zxvf anaroot\_vX.Y.Z.tgz  
   cd anaroot

2. 创建构建和安装目录：  
   Bash  
   mkdir build install  
   cd build

3. 使用 CMake 配置编译选项。-DCMAKE\_INSTALL\_PREFIX 指定安装路径：  
   Bash  
   cmake \-DCMAKE\_INSTALL\_PREFIX=$PWD/../install..

4. 编译源代码：  
   Bash  
   make \-jN  \# N 为并行编译的线程数，例如 make \-j8

5. 安装到指定目录：  
   Bash  
   make install  
   ANAROOT 的库文件和头文件等将被安装到 anaroot/install 目录下。

2.3.3 Autotools 安装方法 (v4.5 及更早版本)  
早期版本的 ANAROOT（直至 v4.5.x）使用 Autotools (automake, autoconf, libtool) 构建系统 。

1. **安装第三方依赖软件:** 确保已安装 libxml2-devel, automake, autoconf, libtool, libedit。在基于 RPM 的系统 (如 CentOS, Fedora) 中，可以使用 yum 或 dnf 安装：  
   Bash  
   sudo yum install libxml2-devel automake autoconf libtool libedit-devel  
   在基于 Debian 的系统 (如 Ubuntu) 中，可以使用 apt-get：  
   Bash  
   sudo apt-get install libxml2-dev automake autoconf libtool libedit-dev

2. **(可选) 安装 MINOS 库:** 如果需要 MINOS 功能，下载 minos-1.1.1-minimal.tar.gz 并编译安装：  
   Bash  
   tar zxvf minos-1.1.1-minimal.tar.gz  
   cd minos-1.1.1-minimal  
   make all  
   \# 假设安装到某个自定义路径 \[minos\_install\_path\]  
   \# 需要设置 PKG\_CONFIG\_PATH 以便 ANAROOT 配置时能找到它  
   export PKG\_CONFIG\_PATH=\[minos\_install\_path\]/install/lib/pkgconfig:$PKG\_CONFIG\_PATH  
   cd..

3. **安装 ANAROOT:** 解压源代码包：  
   Bash  
   tar zxvf anaroot\_v4.5.X.tgz  
   cd anaroot  
   运行配置脚本。--prefix 指定安装路径。如果启用了 MINOS，添加 \--enable-minos=yes：

./autogen.sh \--prefix=$PWD \[--enable-minos=yes\]  
编译并安装：bash  
make \-jN install \# N 为并行编译的线程数  
\`\`\`  
**2.4 环境变量设置**  
正确设置环境变量是成功使用 ANAROOT 的关键。

* **ROOTSYS**: ROOT 的安装路径，由 thisroot.sh 设置。  
* **LD\_LIBRARY\_PATH (或 DYLD\_LIBRARY\_PATH for macOS)**: 需要包含 ANAROOT 库文件所在的目录。  
  * 对于 CMake 安装 (v4.6.1+): anaroot/install/lib  
  * 对于 Autotools 安装 (v4.5-): anaroot/lib (如果 \--prefix 指向 anaroot 目录本身) 或 \--prefix 指定的安装路径下的 lib 目录。 例如 (Autotools, 安装到 anaroot 目录内)：

Bash  
export LD\_LIBRARY\_PATH=$LD\_LIBRARY\_PATH:$PWD/lib

* **PKG\_CONFIG\_PATH**: 如果安装了可选的 minos-fem 库到非标准位置，需要包含其 pkgconfig 目录的路径，以便 ANAROOT 的 ./autogen.sh 能够找到它 。  
* **anaroot/setup.sh 脚本**: 成功安装 ANAROOT 后，通常会在其顶层目录生成一个 setup.sh (或类似名称的) 脚本 。在新的终端会话中，通过 source 命令执行此脚本，可以便捷地设置好所有必要的 ANAROOT 相关环境变量：  
  Bash  
  source /path/to/anaroot/setup.sh  
  建议将此行也添加到 shell 配置文件中。  
* **ROOT 登录宏**: ANAROOT 通常会提供 rootlogon.C 和 .rootrc 文件，位于 ANAROOT 的根目录或安装目录的 etc (或类似) 目录下。将它们复制或链接到用户的主目录或工作目录，可以在启动 ROOT 时自动加载 ANAROOT 库和设置 。

**2.5 常见安装问题与故障排除**  
以下是一些安装过程中可能遇到的问题及其解决方案 ：

* **从其他PC复制文件后启动ROOT时出错:**  
  * 在运行 ./autogen.sh \--prefix=$PWD (针对 Autotools 版本) 之前，尝试执行 make distclean 清理旧的构建文件。  
* **macOS 特定问题:**  
  * libtoolize 未安装: macOS 通常使用 glibtoolize。需要相应修改 autogen.sh 脚本。  
  * 共享库扩展名: macOS 上的共享库名为 \*.dylib 而非 \*.so。若要在 ROOT 中使用 gSystem-\>Load("...") 加载，可能需要将 .dylib 扩展名更改为 .so，或者确保 ROOT 能够识别 .dylib。  
  * Genie Jhang 编写了一份详细的 ANAROOT Mac 安装指南，可供参考: ANAROOTonMAC.html (通常位于 ANAROOT 文档或源码包中)。  
* **独立加载 analoop 库:**  
  * 如果单独加载 analoop 库，可能需要修改 rootlogon.C 以加载 libanaloop.so, libanaloopexample.so, 和 libanaloopencexample.so，而不是 libanaanaloop.so (注意库名称的细微差别)。  
* **依赖库缺失:**  
  * 编译时提示找不到头文件或库文件，通常是由于相关的 devel 包未安装 (如 libxml2-devel, gsl-devel 等)。根据错误信息安装相应的开发包。  
* **ROOT 版本不兼容:**  
  * 编译错误可能源于 ANAROOT 版本与当前 ROOT 版本不兼容。检查 ANAROOT 文档推荐的 ROOT 版本，并考虑升级或降级 ROOT。

**2.6 ANAROOT 目录结构分析**  
ANAROOT 安装完成后，其目录结构通常包含以下关键部分，这有助于用户理解和定位所需文件 1：

* **顶层目录 (anaroot/)**:  
  * setup.sh: 用于设置 ANAROOT 环境变量的脚本 1。  
  * rootlogon.C, .rootrc: ROOT 登录宏和配置文件，用于在 ROOT 启动时自动加载 ANAROOT 库和设置 1。  
  * source/: 包含 ANAROOT 核心源代码和各模块源代码。  
    * Core/: 包含 ANAROOT 的核心库，如 RIDF 数据解码、事件构建、以及基础类 TArtStoreManager 等 5。  
    * Reconstruction/: 包含各探测器数据重建相关的库 5。  
      * BigRIPS/: BigRIPS 探测器（PPAC, Plastic, IC, Ge）的刻度与重建代码 5。  
      * SAMURAI/: SAMURAI 探测器（BDC, FDC, HODF, ICF, NEBULA）的刻度与重建代码 5。  
      * DALI/: DALI2 NaI 探测器的刻度与重建代码 5。  
      * EURICA/: EURICA gamma 射线阵列的刻度与重建代码 5。  
    * AnaLoop/: 包含 TArtAnaLoop 基类及其派生类的实现 6。  
      * include/: 头文件。  
      * src/: 源文件。  
  * lib/ (通常在 Autotools 安装或 CMake 安装后的 install/lib/): 存放编译生成的共享库文件 (.so 或 .dylib) 1。  
  * include/ (通常在 CMake 安装后的 install/include/anaroot/): 存放 ANAROOT 的头文件 1。  
  * build/ (CMake 安装): 编译过程中产生的中间文件 1。  
  * install/ (CMake 安装): CMake 安装的目标路径，包含 lib/, include/, bin/ 等子目录 1。  
  * example/ 或 macros/: 包含示例分析宏和脚本 10。  
    * Macros/BigRIPS/: 针对 BigRIPS 分析的示例宏，如 RecoPID.C 10。  
    * Macros/Online/: 在线分析相关的示例宏，如 ShowModule.C 10。  
    * Macros/RIDF2Tree.C: 将 RIDF 数据转换为 ROOT TTree 的示例宏 10。  
  * run/ 或 db/: 通常用于存放用户分析时所需的参数文件（如 XML 文件）和用户自定义的分析宏 3。  
  * doc/ 或类似目录: 可能包含 ANAROOT 的文档、教程或特定安装说明 (如 ANAROOTonMAC.html) 1。

了解这些目录结构有助于用户查找库文件、头文件、示例代码和参数文件，从而更有效地进行 ANAROOT 的配置和使用。  
**第三章：ANAROOT 核心概念与组件**  
本章将深入探讨 ANAROOT 的内部结构、关键类、数据流以及参数管理机制，为后续的实际应用打下坚实基础。  
**3.1 ANAROOT 库结构**  
ANAROOT 的源代码和库文件组织有序，反映了其模块化的设计思想。其主要目录结构通常如下 5：

* source/Core: 包含 ANAROOT 的核心库。这些库负责基础功能，如 RIDF 数据的解码、事件的构建，以及一些基础类，例如 TArtStoreManager（用于管理数据对象和参数）。  
* source/Reconstruction: 包含用于从各个探测器原始数据中重建物理信息的库。这是一个顶层目录，其下通常按探测器系统或实验装置划分子目录：  
  * source/Reconstruction/BigRIPS: 包含了用于刻度和重建 BigRIPS 探测器（如 PPAC、Plastic、IC、Ge 探测器）数据的库，以及用于重建束流粒子 A/Q (质荷比) 和 Z (电荷数) 的库。  
  * source/Reconstruction/DALI: 包含了用于刻度 DALI2 NaI 探测器原始数据的库。  
  * source/Reconstruction/SAMURAI: 包含了用于刻度 SAMURAI 探测器（如 BDC1/2、FDC1/2、HODF/P、ICF、NEBULA）原始数据的库。  
  * source/Reconstruction/EURICA: 包含了用于刻度 EURICA gamma 射线探测器阵列原始数据的库。

这种模块化的结构使得针对特定探测器的分析代码可以独立开发和维护，同时也便于用户根据自己的实验需求选择性地加载和使用相关模块。  
**3.2 关键类概览**  
ANAROOT 中有许多核心类，它们协同工作以实现复杂的数据分析流程。

* **TArtStoreManager**: 这是一个至关重要的单例类，扮演着数据和参数的中央管家角色 5。它负责管理分析过程中产生的所有数据容器（通常是 TClonesArray 对象）的输入/输出，以及分析参数的输入/输出。各种分析模块通过 TArtStoreManager 注册和获取它们需要的对象。这种设计促进了不同分析模块间的解耦和数据共享，使得复杂的分析流程得以清晰地组织。例如，一个刻度模块可以将刻度后的数据对象注册到 TArtStoreManager，后续的重建模块则可以从中按名称检索这些对象。  
* **TArtEventStore**: 该类负责处理 RIDF 数据的输入和初步解码 3。它可以从 RIDF 文件（离线模式）或在线共享内存/数据流（在线模式）中读取事件数据。TArtEventStore 将原始的二进制数据流转换为结构化的 TArtRawEventObject。  
* **原始数据容器类**:  
  * TArtRawEventObject: 代表一个解码后的事件，包含运行号、事件号、时间戳以及一个 TArtRawSegmentObject 的数组 5。  
  * TArtRawSegmentObject: 代表 RIDF 数据格式中的一个数据段 (segment)，包含设备ID信息和 TArtRawDataObject 的数组 5。  
  * TArtRawDataObject: 存储了最原始的探测器通道数据 (如 ADC, TDC 值) 5。 这些原始数据对象直接映射了 RIDF 的数据结构，为用户提供了访问最底层数据的接口。  
* 刻度类 (TArtCalibXXX):  
  这类类（如 TArtCalibPPAC, TArtCalibPlastic, TArtCalibNEBULA）封装了特定探测器的原始数据刻度逻辑 3。它们从 TArtRawDataObject 中获取原始数据，结合从参数文件（通常是XML）加载的刻度常数，将其转换为有物理意义的量（如时间、能量、位置），并填充到相应的刻度后数据容器中。  
* 重建类 (TArtRecoXXX):  
  这类类（如 TArtRecoTOF, TArtRecoRIPS）则在刻度数据的基础上进行更高级的物理量重建 3。例如，TArtRecoTOF 可能利用多个 Plastic 探测器的刻度时间信息来计算飞行时间。  
* 探测器专用数据容器:  
  ANAROOT 为每种主要探测器定义了特定的数据容器类，用于存储刻度或重建后的数据。这些容器通常继承自 TObject，并以 TClonesArray 的形式进行管理和存储，以便高效处理每个事件中可能存在的多个同类探测器击中。常见的例子有 5：  
  * BigRIPS 相关: TArtPPAC, TArtIC, TArtPlastic, TArtFocalPlane, TArtTOF, TArtRIPS, TArtBeam。  
  * DALI 相关: TArtDALINaI。  
  * SAMURAI 相关: TArtDCHit, TArtDCTrack, TArtHODPla, TArtICF, TArtNEBULAPla, TArtNEBULAHPC。  
  * EURICA 相关: TArtNaI, TArtGeCluster, TArtSiStopper。 这种从原始的、通用的 TArtRawDataObject 到具体的、物理意义明确的探测器对象的转换，体现了 ANAROOT 数据处理的层次化抽象。用户在分析的后期阶段，可以更方便地操作这些高层数据对象。  
* **TArtAnaLoop**: 这是一个抽象基类，用户通过继承它来编写自己的事件循环分析逻辑 6。TArtAnaLoop 的派生类定义了在每个事件中执行的具体操作，如调用刻度/重建例程、填充直方图等。

**表1：ANAROOT 核心类及其功能**

| 类名 (Class Name) | 主要功能 | 关键方法/特性 | 来源 |
| :---- | :---- | :---- | :---- |
| TArtStoreManager | 数据和参数的中央管理器 | Instance(), AddParameters(), AddDataContainer(), FindObject(), FindDataContainer() | 5 |
| TArtEventStore | RIDF 数据输入 (文件/在线) 和解码 | Open(), GetNextEvent(), LoadMapConfig() | 3 |
| TArtRawEventObject | 存储解码后的整个事件信息 | 包含事件号、时间戳、TArtRawSegmentObject 数组 | 5 |
| TArtRawSegmentObject | 存储 RIDF 数据段信息 | 包含设备ID、TArtRawDataObject 数组 | 5 |
| TArtRawDataObject | 存储单个探测器通道的原始数据 | GetValue(), GetCategoryID(), GetDetectorID(), GetDatatypeID() | 5 |
| TArtCalibXXX (通用) | 特定探测器的原始数据刻度 | ReconstructData(), ClearData(), 通常加载XML参数 | 3 |
| TArtRecoXXX (通用) | 基于刻度数据进行物理量重建 | ReconstructData(), ClearData() | 3 |
| TArtPPAC, TArtNEBULAPla 等 | 存储特定探测器刻度/重建后的数据 | 通常作为 TClonesArray 的元素，提供访问具体物理量的方法 (如 GetX(), GetTOF()) | 5 |
| TArtAnaLoop | 用户自定义事件循环分析的基类 | 需用户实现 Construct(), Calculate(), Destruct(), ClassName() | 6 |

**3.3 数据流与处理流程**  
ANAROOT 中的数据处理遵循一个清晰的、分层次的流程，从原始数据输入到最终物理量提取，可以概括为 3：

1. **数据输入与解码 (Extract/Decode):**  
   * TArtEventStore 对象负责打开 RIDF 数据源（文件或在线流）。  
   * 在 GetNextEvent() 调用时，TArtEventStore 读取原始二进制数据，并将其解码填充到 TArtRawEventObject 中。TArtRawEventObject 内部包含一系列 TArtRawSegmentObject，每个 TArtRawSegmentObject 又包含若干 TArtRawDataObject，分别对应探测器各通道的原始测量值（如 TDC、ADC 值）。  
2. **数据刻度 (Transform/Calibrate):**  
   * 用户在分析代码中（通常是 TArtAnaLoop 的派生类中）创建并配置相应的 TArtCalibXXX 对象（例如 TArtCalibPPAC 用于 PPAC 探测器，TArtCalibNEBULA 用于 NEBULA 探测器）。  
   * 这些刻度对象从 TArtStoreManager 获取原始数据（间接通过 TArtEventStore 解码的 TArtRawDataObject），并利用从 XML 参数文件中加载的刻度常数（如 TDC 的时间转换系数、ADC 的能量转换系数、几何位置参数等），将原始道数转换为具有物理意义的量（如时间 ns、能量 MeV、位置 mm）。  
   * 刻度后的数据被填充到特定探测器的数据容器中（如 TArtPPAC 对象、TArtNEBULAPla 对象），这些容器通常以 TClonesArray 的形式存储，并通过 TArtStoreManager 进行管理。  
3. **数据重建 (Transform/Reconstruct):**  
   * 在刻度数据的基础上，TArtRecoXXX 类或更高级的 TArtCalibXXX 类（如 TArtCalibPID）执行更复杂的物理量重建。  
   * 例如，TArtRecoTOF 可能结合多个塑料闪烁体的时间信息和它们之间的距离来计算粒子的飞行时间 (TOF)。TArtCalibPID 则可能综合运用 PPAC 的位置信息、塑料闪烁体的 TOF 信息和电离室的能量损失信息来重建粒子的轨迹、磁刚度 (Bρ)、原子序数 (Z) 和质荷比 (A/Q)。  
   * 重建得到的物理量同样被存储在特定的数据容器中（如 TArtTOF, TArtRIPS, TArtBeam），并由 TArtStoreManager 管理。  
4. **用户分析与输出 (Load/Analyze):**  
   * 用户在 TArtAnaLoop 的 Calculate() 方法中，通过 TArtStoreManager 获取所需的刻度或重建后的数据容器。  
   * 利用这些数据进行进一步的物理分析，如填充直方图、应用物理判选条件 (cuts)、计算不变质量等。  
   * 最终的分析结果（如直方图、N元组）可以通过 ROOT 的标准机制保存到文件中。

这个流程体现了典型的 ETL (Extract, Transform, Load) 数据处理模式 8。ANAROOT 的分层抽象设计使得用户可以在数据处理的不同阶段介入，既可以访问最底层的原始数据，也可以方便地使用经过刻度和重建的高级物理对象。每个 TArtCalibXXX 和 TArtRecoXXX 对象都专注于特定的任务，这增强了代码的模块化和可维护性。  
**3.4 参数管理：XML 文件与 TArtEventStore::LoadMapConfig**  
ANAROOT 广泛使用 XML 文件来管理实验参数，这为用户提供了极大的灵活性，可以在不重新编译代码的情况下修改探测器设置、刻度常数等 3。

* **XML 参数文件:**  
  * 用户定义的参数，如探测器几何位置、电子学模块的通道映射、TDC/ADC 转换系数、时间偏移、能量刻度曲线参数等，都存储在 XML 格式的文件中 5。  
  * 这些 XML 文件可以通过多种软件生成和编辑，例如 Microsoft Access、Excel、Open Office、Google Spreadsheets，甚至纯文本编辑器 5。  
  * 在分析程序中，通常由 TArtBigRIPSParameters (针对 BigRIPS) 或各个 TArtCalibXXX 类负责加载和解析这些 XML 文件，并将参数应用到后续的计算中。  
  * 这种方式使得参数管理与分析逻辑分离，便于参数的调整、版本控制和共享。  
* **TArtEventStore::LoadMapConfig(char \*mapfilename):**  
  * ANAROOT 也支持加载 ANAPAW（一种较早的分析软件）风格的 Map 文件，用于用户分析中的数据映射 5。  
  * 通过调用 TArtEventStore::LoadMapConfig() 函数加载 Map 文件后，在扫描数据文件时，可以通过 TArtRawDataObject 的成员函数获取探测器类别号 (Category ID)、探测器号 (Detector ID) 和数据类型号 (Datatype ID)，例如：  
    * TArtRawDataObject::GetCategoryID()  
    * TArtRawDataObject::GetDetectorID()  
    * TArtRawDataObject::GetDatatypeID()  
  * 这些 ID 可以帮助用户识别和筛选特定探测器的特定类型数据（如 PPAC 的 Tx1 信号、Plastic 的 TA 信号等）。  
  * ANAROOT 示例中可能包含如 CheckBLDet.C 这样的宏，用于检查 BigRIPS 束流线探测器的数据类别号并告知用户保存了哪些类型的数据 5。

**3.5 坐标系定义**  
为了确保数据分析的一致性和结果的可比性，ANAROOT 推荐在实验和分析中使用统一的坐标系定义 5。虽然具体的定义细节（如原点位置、各轴指向）需要参考相应实验的约定或 ANAROOT 提供的示例图示，但遵循共同的坐标系对于正确解释粒子轨迹、角度等物理量至关重要。用户应查阅其合作组或 ANAROOT 的相关文档以获取推荐的坐标系标准。  
**第四章：ANAROOT 基本使用方法**  
本章介绍 ANAROOT 的基本操作方式，包括命令行界面、用户分析宏 TArtAnaLoop 的编写和使用，以及如何调用数据解码、刻度和重建例程。  
**4.1 ANAROOT 命令行界面与基本操作**  
ANAROOT 提供了一个基于命令行的用户界面 (CUI)，其部分命令风格类似于早期的 ANAPAW 分析软件，这是通过集成的 Nadeko 库实现的 。这个界面允许用户以交互方式控制分析流程、管理数据文件和直方图。  
**分析管理命令** 7:

* book(TArtAnaLoop\* analoop, const char\* anafilename \= 0): 注册用户定义的 TArtAnaLoop 派生类对象 (analoop) 和可选的 Anafile (anafilename) 到 TArtAnaLoopManager。这是启动分析前的重要初始化步骤。  
* push(const char\* filename, int eventnumber \= \-1): 将指定的 RIDF 数据文件 (filename) 添加到待处理的文件栈中。eventnumber 参数可以限制处理的事件数。对于在线分析，可以使用 push(int sid \= 0, int eventnumber \= \-1)，其中 sid 是共享内存 ID。  
* spush(const char\* filename\_start, const char\* filename\_end, int start, int end, int width \= 4, char fill \= '0'): 一次性添加多个具有相似命名规律的 RIDF 文件到栈中。例如，spush("ridf/run", ".ridf", 1, 11\) 会添加 ridf/run0001.ridf 到 ridf/run0011.ridf。  
* pop(int i): 从文件栈中移除指定索引的文件。  
* start(): 启动分析流程。首次调用时，会执行已 book 的 TArtAnaLoop 对象的 Construct() 方法。  
* stop(): 暂停正在进行的分析。可以使用 start() 命令恢复。  
* next(): 跳过当前 RIDF 文件中剩余的事件，开始处理文件栈中的下一个文件。  
* join(): 在宏模式下使用时，此命令会使主线程等待后台运行的分析任务完成。这表明分析过程可能在独立的线程中执行，特别是对于在线分析和 GUI 更新。  
* end(): 结束当前分析。会调用 TArtAnaLoop 对象的 Destruct() 方法。  
* clear(): 清除所有已创建的直方图，并销毁 TArtAnaLoopManager 对象，重置分析环境。  
* status(): 打印当前分析的状态信息，如文件栈内容、已处理事件数等。

直方图管理命令 7:  
这些命令主要用于管理和显示已经由用户在 TArtAnaLoop 逻辑中创建和填充的 ROOT TH1 对象。

* fetch(char\* filename): 从指定的 ROOT 文件 (filename) 中读取所有 TH1 对象到当前的 ROOT 内存目录。  
* hstore(char\* filename): 将当前 ROOT 内存目录中的所有 TH1 对象写入到指定的 ROOT 文件 (filename)。  
* hdel(): 删除当前目录下的所有直方图。也可以按 ID (hdel(int id)) 或 ID 范围 (hdel(int idstart, int idend)) 删除。  
* erase(): 重置 (Reset) 当前目录下的所有直方图内容，但不删除对象本身。  
* ls(): 显示当前 ROOT 目录中直方图的列表（类似于 shell 的 ls 命令）。  
* ht(int id, Option\_t\* option \= ""): 按 ID 绘制指定的直方图。option 参数可以传递给 ROOT 的 Draw() 方法，如 "SAME", "COLZ" 等。也可以用 ht(int idstart, int idend) 绘制一定范围内的直方图。  
* htp(): 绘制当前活动的直方图。  
* hn(): 绘制下一个直方图（按某种内部顺序）。  
* hb(): 绘制上一个直方图。  
* hht, hhtp, hhn, hhb: 这些是对应 ht, htp, hn, hb 的 "非移动画布" 版本，即在当前 TPad 中绘图而不切换 TPad。  
* sh(): 提供一个交互式的直方图浏览模式，可以通过键盘按键（如 'n' 代表下一个，'p' 代表上一个）切换显示的直方图。

这些命令构成了 ANAROOT 交互式分析的基础。用户通过 book 注册分析逻辑，通过 push 添加数据，通过 start 运行分析，并通过 hstore 保存结果。直方图的创建和填充逻辑则封装在用户自定义的 TArtAnaLoop 类中。对于在线分析，AnaLoop 的设计允许在一个独立的线程中填充直方图和树，这样用户可以在数据获取过程中实时查看和更新显示，这对于监控实验状态至关重要 10。  
**4.2 编写用户分析宏：TArtAnaLoop**  
TArtAnaLoop 是 ANAROOT 中用户实现自定义事件处理逻辑的核心机制 6。它是一个抽象基类，用户需要通过继承它并重写其定义的虚函数来构建自己的分析例程。  
TArtAnaLoop 的主要虚函数及其作用 6：

* Construct(): 此函数在分析开始时（即首次调用 start() 命令后）被调用一次。主要用于执行分析前的初始化工作，例如：  
  * 创建和配置探测器刻度对象 (如 new TArtCalibNEBULA(), new TArtCalibPPAC())。  
  * 将需要从参数文件加载参数的对象注册到 TArtStoreManager (例如，通过 TArtStoreManager::Instance()-\>AddParameters(myCalibObject))。  
  * 创建和预订 (book) ROOT 直方图 (TH1, TH2 等) 和 N元组 (TTree)。虽然也可以在全局的 book 函数 (如果重写的话) 中创建直方图，但在 Construct() 中创建也是常见的做法，如 TArtAnaLoopUser.C 所示例。  
* Calculate(): 这是事件循环的核心，每个事件都会被调用一次。用户在此函数中编写逐事件的处理逻辑，例如：  
  * 调用刻度对象的 ClearData() 和 ReconstructData() 方法。  
  * 从 TArtStoreManager 获取解码、刻度或重建后的数据容器。  
  * 根据获取的数据填充在 Construct() 中创建的直方图和 N元组。  
  * 执行用户特定的物理分析和判选。 由于此函数会被频繁调用，其代码效率至关重要。  
* Destruct(): 此函数在分析结束时（即调用 end() 命令后）被调用一次。主要用于执行清理工作，例如：  
  * 释放（delete）在 Construct() 中动态创建的对象（如刻度对象）。这对于在同一个 ROOT 会话中多次运行分析（多次 book）非常重要，以避免内存泄漏。  
  * ROOT 直方图通常由 gDirectory 管理，如果它们被正确添加到目录中，则不需要手动删除。但如果用户使用 new 创建且未交由 ROOT 管理，则需在此处 delete。  
* ClassName() const: 这个函数仅用于在 status() 命令的输出中显示当前 AnaLoop 类的名称，方便用户识别。

以下是一个自定义 AnaLoop 类的基本骨架：

C++

\#include "TArtAnaLoop.hh"  
\#include "TArtStoreManager.hh"  
// 根据需要包含其他 ANAROOT 头文件 (如 TArtCalibNEBULA.hh, TArtNEBULAPla.hh)  
// 以及 ROOT 头文件 (如 TH1F.h, TFile.h)

class MyCustomAnaLoop : public TArtAnaLoop {  
public:  
    MyCustomAnaLoop() : TArtAnaLoop() { /\* 可选：初始化简单成员 \*/ }  
    \~MyCustomAnaLoop() override { Destruct(); } // 确保调用 Destruct

    void Construct() override {  
        // std::cout \<\< "Constructing MyCustomAnaLoop" \<\< std::endl;  
        TArtStoreManager\* sm \= TArtStoreManager::Instance();

        // 示例：创建刻度对象  
        // calibNEBULA \= new TArtCalibNEBULA();  
        // sm-\>AddParameters(calibNEBULA); // 如果 calibNEBULA 需要从XML加载参数

        // 示例：预订直方图  
        // h\_neutron\_tof \= new TH1F("h\_neutron\_tof", "Neutron TOF;TOF (ns);Counts", 1000, 0, 1000);  
        // h\_ppac\_x \= new TH1F("h\_ppac\_x", "PPAC X Position;X (mm);Counts", 500, \-250, 250);  
    }

    void Calculate() override {  
        TArtStoreManager\* sm \= TArtStoreManager::Instance();  
        // TArtEventStore\* estore \= (TArtEventStore\*)sm-\>FindObject("EventStore"); // 通常由框架管理事件获取

        // 示例：调用刻度/重建 (假设 calibNEBULA 是成员变量)  
        // if (calibNEBULA) {  
        //     calibNEBULA-\>ClearData();  
        //     calibNEBULA-\>ReconstructData();  
        // }

        // 示例：从 StoreManager 获取数据容器  
        // TClonesArray\* nebulaplas \= (TClonesArray\*)sm-\>FindDataContainer("NEBULAPla");  
        // if (nebulaplas) {  
        //     for (int i \= 0; i \< nebulaplas-\>GetEntriesFast(); \++i) {  
        //         TArtNEBULAPla\* pla \= (TArtNEBULAPla\*)nebulaplas-\>At(i);  
        //         if (pla && pla-\>GetHit()) { // 检查是否是有效击中  
        //             // h\_neutron\_tof-\>Fill(pla-\>GetTOF()); // 假设 GetTOF() 返回刻度后的 TOF  
        //         }  
        //     }  
        // }

        // 示例：获取 PPAC 数据 (假设已通过 TArtCalibPID 或类似过程处理)  
        // TClonesArray\* ppacs \= (TClonesArray\*)sm-\>FindDataContainer("BigRIPSPPAC"); // 名称取决于注册方式  
        // if (ppacs) {  
        //     for (int i \= 0; i \< ppacs-\>GetEntriesFast(); \++i) {  
        //         TArtPPAC\* ppac \= (TArtPPAC\*)ppacs-\>At(i);  
        //         // if (ppac && strcmp(ppac-\>GetDetectorName()-\>Data(), "F3PPAC1A") \== 0\) {  
        //         //     h\_ppac\_x-\>Fill(ppac-\>GetX());  
        //         // }  
        //     }  
        // }  
    }

    void Destruct() override {  
        // std::cout \<\< "Destructing MyCustomAnaLoop" \<\< std::endl;  
        // delete calibNEBULA; calibNEBULA \= nullptr;  
        // 直方图通常由 ROOT 的 gDirectory 管理，除非特殊情况，否则不需要手动 delete  
    }

    const char\* ClassName() const override { return "MyCustomAnaLoop"; }

private:  
    // 在此声明成员变量指针，用于存储刻度对象、直方图等  
    // TArtCalibNEBULA\* calibNEBULA \= nullptr;  
    // TH1F\* h\_neutron\_tof \= nullptr;  
    // TH1F\* h\_ppac\_x \= nullptr;  
};

**4.3 编写自定义 TArtAnaLoop**  
用户可以通过以下两种主要方式使用自定义的 TArtAnaLoop 派生类 6：

1. **内置到库中 (Built-in to library):**  
   * 将自定义 AnaLoop 类的头文件 (.hh) 和源文件 (.cc 或 .C) 放置在 ANAROOT 源代码树的相应目录下（通常是 $ANAROOT\_SYS/source/AnaLoop/include 和 $ANAROOT\_SYS/source/AnaLoop/src）。  
   * 修改 ANAROOT 的构建系统（如 Makefile 或 CMakeLists.txt）以包含这些新文件，并重新编译整个 ANAROOT 库。  
   * 这种方式适合于开发稳定、通用的分析模块，或者当希望将分析逻辑作为黑盒提供给其他用户时。  
2. **在分析目录中创建宏并动态加载 (Create macro in analysis directory and load dynamically):**  
   * 这是更常用和灵活的方式，特别适合于用户频繁修改和调试分析代码的场景。  
   * 用户将自定义 AnaLoop 类的代码（例如 MyCustomAnaLoop.C）放在其实验分析的工作目录下。  
   * 在 ROOT 会话中，使用 .L 命令动态加载并编译这个宏：  
     C++  
     root.L MyCustomAnaLoop.C+  
     注意命令末尾的 \+ 号。它指示 ROOT 使用 ACLiC (Automatic Compiler of Libraries for CINT) 来编译该 C++ 文件并生成一个共享库，然后加载这个库。这允许用户在宏中使用完整的 C++ 语法，包括模板、类等，而不仅仅是 CINT 解释器支持的子集。相比之下，.x MyCustomAnaLoop.C 命令是直接由 CINT 解释执行，功能受限，不适合加载类定义。  
   * 动态加载后，就可以在 book 命令中使用这个自定义类了：  
     C++  
     root book(new MyCustomAnaLoop(), "myanalysis.ana"); // 可选的 anafile  
     root push("data/run0001.ridf");  
     root start();

   * ANAROOT 提供了一些示例 AnaLoop 类，如 TArtAnaLoopUser.C 6 和 TAlRawDataExample.C 10，它们是学习和修改的良好起点。用户甚至可以通过 ANAROOT 提供的脚本（如 getAnaLoop.sh TAlRawDataExample 10）获取这些示例代码的副本，然后在副本基础上进行开发。

**4.4 数据解码、刻度与重建的调用**  
在用户自定义的 TArtAnaLoop::Calculate() 方法中，通常需要按顺序调用数据处理的各个阶段 3。ANAROOT 的设计期望用户遵循一个三步分析流程来访问刻度和重建后的数据 5：

1. **数据解码 (Decoding):**  
   * 这一步通常由 TArtEventStore 在其内部的 GetNextEvent() 方法中隐式完成。当 GetNextEvent() 被调用时，原始的 RIDF 数据被读取并解码成 TArtRawEventObject，其中包含了各个探测器通道的原始数据 (TArtRawDataObject)。这些原始数据对象会被注册到 TArtStoreManager，或者可以直接从 TArtEventStore 获取（尽管后者不常见于用户代码）。  
2. **数据刻度 (Calibration):**  
   * 用户需要在 TArtAnaLoop::Construct() 方法中创建其实验设置所需的各种 TArtCalibXXX 对象（例如 TArtCalibPPAC, TArtCalibPlastic, TArtCalibIC for BigRIPS; TArtCalibNEBULA for NEBULA）。  
   * 如果这些刻度类需要从 XML 文件加载参数，它们应该被添加到 TArtStoreManager 的参数列表中（例如 sm-\>AddParameters(calibPPAC);）。  
   * 在 TArtAnaLoop::Calculate() 的每个事件循环开始时，用户需要为每个相关的刻度对象调用其 ClearData() 方法，以清除前一个事件的残留数据。  
   * 然后，调用刻度对象的 ReconstructData() 方法（注意：尽管名为 "ReconstructData"，对于 TArtCalibXXX 类，这通常指的是执行刻度过程）。此方法会从 TArtStoreManager 或其他来源获取原始数据，应用刻度参数，并将刻度后的数据（如 TArtPPAC 对象）填充到相应的 TClonesArray 中，这些数组也会被注册到 TArtStoreManager。  
3. **数据重建 (Reconstruction):**  
   * 某些更高级的物理量（如粒子的飞行时间 TOF、径迹参数、A/Q、Z 等）的重建，可能由专门的 TArtRecoXXX 类（如 TArtRecoTOF, TArtRecoRIPS）或功能更全面的校准/重建类（如 TArtCalibPID，它内部可能协调多个 TArtCalibXXX 和 TArtRecoXXX 子模块）来完成。  
   * 这些重建类的对象同样在 TArtAnaLoop::Construct() 中创建和配置。  
   * 在 TArtAnaLoop::Calculate() 中，在相应的刻度步骤完成之后，调用这些重建类的 ClearData() 和 ReconstructData() 方法。  
   * 重建后的数据对象（如 TArtTOF, TArtRIPS, TArtBeam）也会被注册到 TArtStoreManager，供用户在分析的最后阶段使用。

用户通过在 AnaLoop 中按正确的顺序和依赖关系组织这些调用，来构建从原始数据到最终物理结果的完整处理链。TArtStoreManager 在这个过程中充当了不同模块间数据交换的桥梁。  
**4.5 ANAROOT 工作流分析**  
ANAROOT 的分析工作流通常围绕着用户定义的 TArtAnaLoop 派生类展开，并通过命令行界面 (CUI) 或 ROOT 宏进行控制。其核心思想是将数据处理流程模块化，并通过 TArtStoreManager 实现数据共享 3。  
**4.5.1 典型分析流程**  
一个典型的 ANAROOT 分析会话（无论是在线还是离线）通常遵循以下步骤 3：

1. **环境准备与库加载:**  
   * 启动 ROOT 环境。  
   * 加载 ANAROOT 核心库和特定探测器的分析库（例如 libanacore.so, libanabrips.so, libanasamurai.so 等）。这可以通过 gSystem-\>Load("library\_name.so") 在 ROOT 宏中完成，或者通过 rootlogon.C 自动加载。  
2. **初始化分析逻辑 (book 命令):**  
   * 用户使用 book(new MyCustomAnaLoop(), "optional\_anafile.ana") 命令注册一个自定义的 TArtAnaLoop 派生类实例（例如 MyCustomAnaLoop）和一个可选的 Anafile 文件到 TArtAnaLoopManager 7。  
   * MyCustomAnaLoop 类封装了用户定义的分析逻辑，包括探测器对象的创建、参数加载、直方图预订等（在 Construct() 方法中），以及逐事件的数据处理和直方图填充（在 Calculate() 方法中）。  
   * Anafile 是一个文本文件，可以用来定义直方图、切割条件 (cuts) 和树 (trees)，主要用于在线分析场景 10。  
3. **指定输入数据 (push 或 spush 命令):**  
   * 使用 push("datafile.ridf", nEvents) 命令将一个 RIDF 格式的数据文件添加到处理队列中，可以指定处理的事件数 nEvents 7。  
   * 对于在线分析，可以使用 push(shared\_memory\_id, nEvents) 从共享内存读取数据 7。  
   * spush("prefix", "suffix", start\_run, end\_run) 命令可以方便地一次性添加多个具有序列号的 RIDF 文件 7。  
4. **启动分析 (start 命令):**  
   * 执行 start() 命令开始事件循环处理 7。  
   * 首次调用 start() 时，会执行已 book 的 TArtAnaLoop 对象的 Construct() 方法，进行初始化设置。  
   * 随后，对 push 进队列的每个数据文件中的每个事件，都会调用 TArtAnaLoop 对象的 Calculate() 方法。  
5. **分析过程控制:**  
   * stop(): 暂停分析，可以使用 start() 恢复 7。  
   * next(): 跳过当前数据文件中剩余的事件，处理队列中的下一个文件 7。  
   * status(): 显示当前分析状态，如文件队列、已处理事件数等 7。  
6. **等待分析完成 (在宏模式下使用 join 命令):**  
   * 如果在 ROOT 宏中执行分析，通常在 start() 之后调用 join() 命令，使主线程等待后台分析任务完成 7。  
7. **结束分析 (end 命令):**  
   * 执行 end() 命令结束分析过程。此时会调用 TArtAnaLoop 对象的 Destruct() 方法，进行资源清理 7。  
8. **结果处理与保存:**  
   * 在分析过程中或分析结束后，可以使用 ht() 系列命令绘制直方图 7。  
   * 使用 hstore("output.root") 命令将当前 ROOT 目录中的所有直方图保存到指定的 ROOT 文件中 7。  
   * 如果用户在 TArtAnaLoop 中创建了 TTree，它们也会在关闭输出文件时被保存。  
9. **清理环境 (clear 命令):**  
   * clear() 命令会删除所有直方图并销毁 TArtAnaLoopManager，重置分析环境，以便开始新的分析会话 7。

**4.5.2 数据处理的 ETL 模式**  
ANAROOT 的内部数据处理流程遵循典型的提取-转换-加载 (Extract-Transform-Load, ETL) 模式 3：

* **提取 (Extract):** TArtEventStore 从 RIDF 文件或在线数据流中读取原始二进制数据 3。  
* **转换 (Transform):**  
  * **解码 (Decode):** TArtEventStore 将原始数据解码为 TArtRawEventObject，其中包含 TArtRawDataObject 形式的原始探测器信号 3。  
  * **刻度 (Calibrate):** TArtCalibXXX 类（如 TArtCalibPPAC, TArtCalibNEBULA）利用 XML 参数文件中的刻度常数，将原始数据（如 TDC 道数、ADC 道数）转换为具有物理意义的量（如时间、能量、位置），并填充到特定的数据容器中（如 TArtPPAC, TArtNEBULAPla）3。  
  * **重建 (Reconstruct):** TArtRecoXXX 类（如 TArtRecoTOF, TArtRecoRIPS）或更高级的校准类（如 TArtCalibPID）在刻度数据的基础上，进行更复杂的物理量重建，如计算飞行时间、磁刚度、粒子鉴别参数 (A/Q, Z) 等，并将结果存入相应的数据容器（如 TArtTOF, TArtRIPS, TArtBeam）3。  
* **加载 (Load):**  
  * 所有中间和最终的数据容器都通过 TArtStoreManager 进行管理和共享 5。  
  * 用户在 TArtAnaLoop::Calculate() 方法中，通过 TArtStoreManager 获取这些处理过的数据容器，进行最终的物理分析、填充直方图和 N元组。  
  * 最终的分析结果（直方图、树等）被加载（保存）到 ROOT 文件中。

**4.5.3 不同分析策略**  
ANAROOT 支持多种分析策略以适应不同用户的需求和偏好 10：

1. **纯 ROOT 宏分析:** 用户可以编写自己的 ROOT 宏，直接使用 ANAROOT 提供的解码和重建库（如 TArtEventStore, TArtCalibPID 等）。这种方式下，用户对分析流程有完全的控制，但不直接使用 TArtAnaLoop 框架和 CUI 命令。示例宏如 RecoPID.C 和 RIDF2Tree.C 体现了这种方式 3。  
2. **使用 TArtAnaLoop 和 Anafile:** 用户创建一个 TArtAnaLoop 派生类，并在 book 命令中关联一个 Anafile。Anafile 用于定义直方图、切割和树的结构。这种方式特别适合在线监控，因为直方图填充可以在独立线程中进行，允许在数据获取过程中实时绘图 3。  
3. **使用 TArtAnaLoop（不使用 Anafile）:** 用户在 TArtAnaLoop 派生类的 Construct() 方法中直接创建和预订 ROOT 直方图和树，并在 Calculate() 方法中填充它们。这种方式结合了 TArtAnaLoop 框架的便利性和用户对结果对象的完全控制 6。

这种灵活的工作流设计使得 ANAROOT 既能满足需要快速进行标准化在线监控的用户，也能支持需要进行复杂离线分析和算法开发的用户。  
**第五章：使用 ANAROOT 分析 PDC 探测器数据**  
平行板雪崩计数器 (PDC)，在 RIBF 的语境下通常指 BigRIPS 次级束流分离器中的 PPAC 探测器，是进行束流粒子鉴别 (PID) 和轨迹追踪的关键组成部分。本章将扩展讨论范围至 BigRIPS 中用于 PID 的主要探测器组合，包括 PPACs、塑料闪烁体 (Plastic Scintillators) 和电离室 (Ionization Chambers, IC)，并详细介绍如何使用 ANAROOT 分析它们的数据。  
**5.1 PDC 及相关 BigRIPS 探测器概述**  
BigRIPS 的粒子鉴别依赖于对通过分离器的每个次级束流粒子进行精确测量，以确定其原子序数 Z、质量数 A 和电荷 q。这通常通过所谓的 Bρ−TOF−ΔE 方法实现，其中涉及到以下关键探测器 3：

* **PPAC (Parallel Plate Avalanche Counter):**  
  * 功能：精确测量带电粒子通过探测器的时间以及二维位置 (X, Y)。  
  * 原理：当带电粒子通过充满低压气体的平行电极板之间时，会引起气体雪崩放大，产生可测量的电信号。通过分析阳极条或延迟在线不同位置感应到的信号的时间差或电荷量，可以重建粒子的击中位置。  
  * 布局：多个 PPAC 探测器沿 BigRIPS 的不同焦点（如 F3, F5, F7, F8, F11 等）分布，用于精确重建粒子在各个焦平面的位置和角度，进而确定粒子轨迹和飞行路径长度。  
* **塑料闪烁体 (Plastic Scintillators):**  
  * 功能：主要用于测量粒子飞越两个闪烁体之间所需的时间 (Time-Of-Flight, TOF)，也可用于测量粒子在闪烁体中损失的能量 (ΔE)。  
  * 原理：带电粒子穿过塑料闪烁体时，会激发闪烁体材料发光。这些光信号通过光导或直接由闪烁体两端耦合的光电倍增管 (PMT) 收集并转换为电信号。  
  * 布局：通常成对放置在 BigRIPS 的不同焦点处（如 F3, F7, F8, F11），作为 TOF 测量的起点和终点。  
* **电离室 (Ionization Chambers, IC):**  
  * 功能：主要用于测量带电粒子在气体中损失的能量 (ΔE)。由于能量损失与粒子电荷的平方 (Z2) 近似成正比，IC 是确定粒子原子序数 Z 的关键探测器。  
  * 原理：带电粒子通过填充特定气体的电离室时，会使气体分子电离，产生电子-离子对。在电场作用下，这些电荷被收集起来形成电流或脉冲信号，其幅度与粒子损失的能量成正比。  
  * 布局：通常放置在 BigRIPS 的下游部分（如 F7 之后），在粒子速度已经通过 TOF 测量大致确定之后。

这些探测器协同工作，为 ANAROOT 提供了进行精确粒子鉴别所需的原始信息。  
**5.2 相关 ANAROOT 类**  
ANAROOT 为 BigRIPS 的这些探测器提供了一系列专门的类，用于参数管理、数据刻度、重建和数据存储 3。  
**表2：用于 PDC/BigRIPS 分析的核心 ANAROOT 类**

| 类名 (Class Name) | 探测器/用途 (Detector/Purpose) | 主要功能/存储数据 (Main Function/Stored Data) | 来源 |
| :---- | :---- | :---- | :---- |
| TArtBigRIPSParameters | BigRIPS整体参数 | 加载和管理 BigRIPS 各探测器 (PPAC, Plastic, IC, FocalPlane 等) 的 XML 参数文件 |  |
| TArtCalibPPAC | PPAC | PPAC 原始数据刻度 (时间、位置 TDC/ADC 到 ns/mm) |  |
| TArtPPAC | PPAC | 存储单个 PPAC 刻度后的数据 (如 X, Y, TX, TY, TSum, QSum, A, B 等) | 5 |
| TArtCalibPlastic | Plastic Scintillator | Plastic 原始数据刻度 (时间 TDC 到 ns，电荷 QDC 到任意单位或 MeVee) | 5 (推断) |
| TArtPlastic | Plastic Scintillator | 存储单个 Plastic 刻度后的数据 (如 TOF\_UL, TOF\_UR, TOF\_DL, TOF\_DR, QDC\_L, QDC\_R 等) | 5 |
| TArtCalibIC | Ionization Chamber | IC 原始数据刻度 (ADC 到能量损失 dE，可能包含温度气压修正) | 5 (推断) |
| TArtIC | Ionization Chamber | 存储单个 IC 刻度后的数据 (如 dE, dEX, SumRaw 等) | 5 |
| TArtCalibFocalPlane | BigRIPS 焦平面 | (可能存在或功能集成于 TArtCalibPID) 重建焦平面参数 (X, A, Y, B) | 5 (推断) |
| TArtFocalPlane | BigRIPS 焦平面 | 存储焦平面重建参数 (如 X, A, Y, B，对应 F3, F5, F7 等焦点) | 3 |
| TArtCalibPID | BigRIPS PID | 综合性的 PID 刻度与重建类，协调各探测器数据，计算 TOF, Bρ, Z, A/Q |  |
| TArtTOF | BigRIPS TOF | 存储计算得到的 TOF 值 (如 F3Plastic-F7Plastic TOF, F8Plastic-F11Plastic TOF) | 5 |
| TArtRIPS | BigRIPS A/Q, Z | 存储通过 Bρ−TOF−ΔE 方法重建的 RIPS 参数 (如 AoQ, Z) | 5 |
| TArtBeam | BigRIPS 束流粒子 | 存储最终鉴别出的束流粒子信息 (通常是 TArtRIPS 对象的集合，代表不同 PID 门的选择) | 5 |

理解这些类的作用和它们之间的关系，对于有效地使用 ANAROOT 进行 BigRIPS 数据分析至关重要。例如，TArtBigRIPSParameters 首先加载所有配置，然后各个 TArtCalibXXX 类利用这些参数进行刻度，生成如 TArtPPAC, TArtPlastic, TArtIC 等数据容器，最后 TArtCalibPID 综合这些信息，产生 TArtTOF, TArtRIPS, TArtBeam 等最终的物理结果。  
**5.3 参数设置与加载**  
BigRIPS 的分析高度依赖于准确的参数设置，这些参数通常存储在 XML 文件中，并通过 TArtBigRIPSParameters 类加载 。  
一个典型的参数加载过程可能如下所示（通常在 TArtAnaLoop::Construct() 中执行）：

C++

// 创建 TArtBigRIPSParameters 对象  
TArtBigRIPSParameters \*brparams \= new TArtBigRIPSParameters("BigRIPSParameters", "BigRIPSParameters");  
// 加载各个探测器和焦平面的参数文件  
brparams-\>LoadParameter("db/BigRIPSPPAC.xml");      // PPAC 参数  
brparams-\>LoadParameter("db/BigRIPSPlastic.xml");   // Plastic 参数  
brparams-\>LoadParameter("db/BigRIPSIC.xml");        // IC 参数  
brparams-\>LoadParameter("db/FocalPlane.xml");     // 焦平面参数 (如磁场、漂移长度)  
// 可能还需要加载其他参数文件，如 TOF 偏移、离子光学矩阵等

// 将参数对象注册到 TArtStoreManager，以便其他类可以访问  
TArtStoreManager\* sm \= TArtStoreManager::Instance();  
sm-\>AddParameters(brparams);

// 创建并注册 TArtCalibPID 对象，它会使用上面加载的参数  
TArtCalibPID \*calibPID \= new TArtCalibPID();  
sm-\>AddParameters(calibPID); // TArtCalibPID 也可能是一个参数提供者  
// 或者 calibPID 在其构造函数或特定方法中从 sm 获取 brparams

XML 文件结构简介:  
虽然具体的 XML 文件结构可能因实验和 ANAROOT 版本而略有不同，但它们通常包含以下类型的信息：

* **探测器标识 (Detector ID):** 每个探测器或其子单元（如 PPAC 的特定层面，Plastic 的特定 PMT）都有唯一的名称或 ID。  
* **通道映射 (Channel Mapping):** 将物理探测器通道（如 PPAC 的阳极条、PMT）映射到数据采集系统中的电子学模块（如 TDC、ADC）的通道号。  
* **刻度系数 (Calibration Coefficients):**  
  * 对于 PPAC：TDC 的时间转换系数 (ns/channel)、时间偏移 (ns)、位置转换系数 (mm/ns 或 mm/channel)、电荷敏感性等。  
  * 对于 Plastic：TDC 的时间转换系数、时间偏移、QDC 的电荷转换系数、渡越时间修正参数等。  
  * 对于 IC：ADC 的能量转换系数 (MeV/channel 或任意单位)、气体参数、温度气压修正系数等。  
* **几何参数 (Geometric Parameters):** 探测器的物理位置 (X, Y, Z 坐标)、旋转角度、有效尺寸、漂移长度等。  
* **其他参数:** 如磁场设定值、离子光学矩阵元素、TOF 路径长度、全局时间偏移等。

用户需要根据具体的实验设置和刻度结果来准备或修改这些 XML 文件。这些文件是 ANAROOT 进行正确数据处理的基础。  
表3：BigRIPS PPAC 分析的 XML 参数示例 (概念性)  
下表为一个概念性的 PPAC 参数示例，展示了 XML 文件中可能包含的参数类型。实际的 XML 标签和结构可能有所不同。

| 参数路径 (示例 XML Path) | 参数名 (Parameter Name) | 示例值/范围 | 描述 (Description) |
| :---- | :---- | :---- | :---- |
| BigRIPSPPAC/PPAC\[@id="F3PPAC1A"\]/anode\_x1/tdc\_channel | tdc\_channel\_x1 | 32 | X1 阳极条对应的 TDC 通道号 |
| BigRIPSPPAC/PPAC\[@id="F3PPAC1A"\]/anode\_x1/tdc\_slope | tdc\_slope\_ns\_per\_ch\_x1 | 0.025 | X1 TDC 斜率 (ns/channel) |
| BigRIPSPPAC/PPAC\[@id="F3PPAC1A"\]/anode\_x1/tdc\_offset | tdc\_offset\_ns\_x1 | 100.0 | X1 TDC 时间偏移 (ns) |
| BigRIPSPPAC/PPAC\[@id="F3PPAC1A"\]/position/x\_factor | pos\_x\_factor\_mm\_per\_ns | 5.8 | X 方向时间差到位置的转换系数 (mm/ns) |
| BigRIPSPPAC/PPAC\[@id="F3PPAC1A"\]/position/x\_offset | pos\_x\_offset\_mm | \-2.5 | X 方向位置整体偏移 (mm) |
| BigRIPSPPAC/PPAC\[@id="F3PPAC1A"\]/geometry/z\_position | z\_position\_mm | 15000.0 | PPAC 在束流方向的 Z 位置 (mm) |
| BigRIPSPPAC/PPAC\[@id="F3PPAC1A"\]/timing/tsum\_low | tsum\_window\_low\_ns | 50.0 | 时间和 (TX1+TX2)/2 信号的有效窗口下限 (ns) |
| BigRIPSPPAC/PPAC\[@id="F3PPAC1A"\]/timing/tsum\_high | tsum\_window\_high\_ns | 150.0 | 时间和信号的有效窗口上限 (ns) |

这个表格帮助用户理解 XML 文件中参数的类型和含义，指导他们如何查找和修改这些参数以适应特定的实验条件和刻度结果。  
**5.4 数据刻度步骤与实例**  
精确的数据刻度是获得可靠物理结果的前提。以下是 BigRIPS 主要探测器的典型刻度流程：

* **PPAC 刻度:**  
  * **时间刻度 (Timing Calibration):**  
    * 目标：将每个阳极条/延迟线输出的 TDC 原始道数转换为精确的时间 (ns)。  
    * 方法：通常使用已知时间间隔的电子学脉冲（来自脉冲发生器）注入到 TDC 通道，测量不同延迟下的 TDC 值，拟合得到每个通道的斜率 (ns/channel) 和偏移 (offset)。这些参数写入 PPAC 的 XML 配置文件。  
  * **位置刻度 (Position Calibration):**  
    * 目标：根据 TDC 测量到的时间信息（或 QAC/ADC 测量到的电荷信息）重建粒子在 PPAC 平面上的击中位置 (X, Y)。  
    * 方法 (基于时间差)：对于延迟线型 PPAC，X 位置通常由两端 (Left, Right) 信号的时间差 (TL​−TR​) 得到，Y 位置由另外两端 (Up, Down) 信号的时间差 (TU​−TD​) 得到。需要确定时间差到物理位置的转换系数 (mm/ns) 和中心偏移 (mm)。这可以通过使用已知开口形状的准直板 (collimator mask) 配合均匀束流照射 PPAC，分析时间差谱与准直板几何形状的对应关系来获得。  
    * 校正：可能需要进行非线性校正、旋转校正（如果探测器安装有微小旋转角度）以及效率图谱校正。  
  * **TArtCalibPPAC 类** 负责执行这些刻度计算。  
* **塑料闪烁体刻度:**  
  * **时间刻度 (Timing Calibration):**  
    * 目标：将闪烁体两端 PMT 输出的 TDC 信号转换为精确的粒子通过时间。  
    * 方法：  
      1. **渡越时间修正 (Walk Correction / Slewing Correction):** PMT 输出信号的上升时间可能与信号幅度有关，导致幅度大的信号看起来比幅度小的信号“早”到达甄别阈值。需要根据信号幅度 (通常用 QDC/ADC 值) 对 TDC 时间进行修正。  
      2. **两端时间对齐 (Mean Timing):** 粒子的平均通过时间通常取为两端 PMT 修正后时间的平均值：Tplastic​=(Tleft​+Tright​)/2−Toffset​。其中 Toffset​ 是一个全局偏移，用于将此探测器的时间与其他探测器或参考时间对齐。  
      3. **位置相关时间校正 (Position-dependent Timing Correction):** 闪烁光在棒内传播到两端 PMT 的时间与击中位置有关。如果需要极高的时间分辨率，可能需要根据沿棒的击中位置（可由 Tleft​−Tright​ 或 Qleft​/Qright​ 得到）进行进一步校正。  
  * **能量损失刻度 (QDC/ADC Calibration):**  
    * 目标：将 PMT 输出的电荷信号 (QDC 或 ADC 积分值) 刻度为粒子在闪烁体中损失的能量 (ΔE) 或相对光产额。  
    * 方法：可以使用已知能量沉积的粒子（如宇宙射线 muon 的最小电离峰）或 γ 源（如 60Co 的康普顿边）进行刻度。对于重离子，通常关注的是相对能量损失，用于粒子鉴别。  
  * **TArtCalibPlastic 类** 负责执行这些刻度。  
* **电离室 (IC) 刻度:**  
  * **能量损失刻度 (ADC Calibration):**  
    * 目标：将 IC 各阳极板输出的 ADC 原始道数转换为粒子损失的能量 (ΔE)，单位通常是 MeV 或任意单位（用于相对比较）。  
    * 方法：需要进行基线扣除。刻度常数（如 MeV/channel）可以通过已知能量损失的束流（例如，通过磁谱仪精确选择的已知粒子和能量）或通过与其他探测器（如硅探测器）的能量损失进行比对来确定。  
    * 校正：  
      1. **气体增益稳定性:** IC 的响应可能随气体温度和压强的变化而变化，需要进行相应的监测和修正。  
      2. **复合效应 (Recombination Effect):** 对于电离密度非常高的重离子，电子和离子在被收集前可能发生复合，导致信号损失。需要根据粒子的 Z 值和能量进行修正。  
      3. **通道间增益匹配:** 确保 IC 内多个阳极板之间的响应一致。  
  * **TArtCalibIC 类** 负责执行这些刻度。

所有这些刻度参数最终都会保存在相应的 XML 文件中，供 ANAROOT 在后续分析中使用。  
**5.5 径迹重建与粒子鉴别 (PID)**  
在 BigRIPS 中，精确的粒子鉴别 (Particle Identification, PID) 是实验的核心目标之一。这通常通过综合利用多个探测器的信息，采用 Bρ−TOF−ΔE 方法来实现 3。

* **飞行时间 (TOF) 计算:**  
  * TOF 是指粒子飞越已知距离所需的时间。在 BigRIPS 中，通常使用放置在不同焦平面（如 F3 和 F7，或 F8 和 F11）的两个塑料闪烁体来测量。  
  * TOF=Tdownstream\_plastic​−Tupstream\_plastic​−TOFoffset​  
  * 其中 Tdownstream\_plastic​ 和 Tupstream\_plastic​ 分别是粒子通过下游和上游塑料闪烁体的精确时间（经过刻度校正），TOFoffset​ 是一个全局的时间偏移常数，需要通过已知粒子（如初级束流或已知 A/Q 的次级束流）进行标定。  
  * 准确的飞行路径长度 L 也至关重要，它通常由离子光学计算或通过径迹重建得到。  
  * TArtTOF 对象存储计算得到的 TOF 值。  
* **能量损失 (ΔE) 测量:**  
  * ΔE 是指粒子穿过特定材料（通常是电离室气体或薄塑料闪烁体）时损失的能量。  
  * 根据 Bethe-Bloch 公式，$\\Delta E \\propto (Z^2 / \\beta^2) \\times \\text{material\_properties}$，其中 Z 是粒子的原子序数，β=v/c 是粒子的相对速度。  
  * 在 BigRIPS 中，ΔE 主要由电离室 (IC) 测量得到，其刻度后的输出信号直接反映了能量损失。  
  * TArtIC 对象存储刻度后的 ΔE 值。  
* **磁刚度 (Bρ) 确定:**  
  * 磁刚度 Bρ 是粒子动量 p 和其电荷 q 的比值，即 Bρ=p/q。它是带电粒子在磁场中运动的一个重要特征量。  
  * 在 BigRIPS 中，次级束流粒子会通过一系列偶极磁铁。通过精确测量粒子在磁铁前后焦平面上的位置和角度（主要由 PPAC 探测器提供），并结合已知的磁场强度和离子光学传输矩阵，可以重建出每个粒子的 Bρ 值。  
  * 12 (幻灯片 7\) 清晰地概述了 TOF−Bρ−ΔE 方法：PPAC 提供位置和方向信息，用于计算 Bρ；塑料闪烁体提供通过时间，用于计算 TOF (进而得到 β)。  
  * TArtFocalPlane 对象存储了焦平面上的位置和角度信息，这些是计算 Bρ 的输入。  
* **粒子鉴别图谱 (PID Plots):**  
  * **ΔE vs TOF 图谱:** 这是进行粒子鉴别的第一步。对于速度相近的粒子，ΔE 主要依赖于 Z2，而 TOF 与 A/q 和 β 有关。在此二维图谱上，不同 Z 的粒子会形成清晰的带状分布。  
  * **A/Q vs Z 图谱:** 这是最终的、最常用的 PID 图谱。  
    * 原子序数 Z 可以从 ΔE 和 TOF (用于得到 β) 近似得到：Z∝βΔE​。  
    * 质荷比 A/Q 可以通过以下公式计算： A/Q=(mu​c)−1×(Bρ/(βγ)) 其中 mu​ 是原子质量单位，c 是光速，L 是 TOF 的飞行路径长度，β=(L/TOF)/c，γ=1/1−β2​。  
    * 在 A/Q vs Z 图谱上，不同的同位素会聚集在离散的点或区域，从而实现对每个粒子的唯一识别。  
  * TArtRIPS 对象存储重建得到的 A/Q 和 Z 值，而 TArtBeam 对象则可能存储根据不同 PID 门选择出的特定束流粒子集合。

实现高质量的 PID 并非依赖单一探测器，而是 BigRIPS 中 PPACs、塑料闪烁体和电离室协同工作的结果。PPAC 提供精确的轨迹信息用于 Bρ 重建和路径长度校正；塑料闪烁体提供核心的 TOF 信息；电离室则提供关键的 ΔE 信息用于 Z 的确定。分析软件（如 ANAROOT 中的 TArtCalibPID 类）必须能够有效地整合这些来自不同探测器的、经过各自复杂刻度的数据流，才能最终实现可靠的粒子鉴别。任何一个环节的刻度不准确，都会直接影响最终 PID 的分辨率和准确性。  
**5.6 示例分析脚本：RecoPID.C 剖析**  
ANAROOT 在其 example/Macros/BigRIPS/ 目录下提供了一个名为 RecoPID.C 的示例宏 10。这个宏展示了如何使用 ANAROOT 对 BigRIPS 数据进行粒子鉴别分析。以下是对其主要步骤的剖析：

1. **加载必要的 ANAROOT 共享库:**  
   C++  
   gSystem-\>Load("libanacore.so");      // ANAROOT 核心库  
   gSystem-\>Load("libanabrips.so");     // BigRIPS 相关分析库  
   // 可能还需要加载其他特定探测器的库

   这些库包含了进行后续分析所需的类定义和函数实现。  
2. **创建参数管理器并加载 XML 参数文件:**  
   C++  
   TArtStoreManager\* sm \= TArtStoreManager::Instance();  
   TArtBigRIPSParameters \*brparams \= new TArtBigRIPSParameters("BigRIPSParameters", "BigRIPSParameters");  
   brparams-\>LoadParameter("db/BigRIPSPPAC.xml");  
   brparams-\>LoadParameter("db/BigRIPSPlastic.xml");  
   brparams-\>LoadParameter("db/BigRIPSIC.xml");  
   brparams-\>LoadParameter("db/FocalPlane.xml");  
   // 根据需要加载其他参数文件，如 TOFCalib.xml, Matrix.xml 等  
   sm-\>AddParameters(brparams);

   这一步与 5.3 节描述的类似，为后续的刻度和重建准备好所有必要的参数。  
3. **创建事件存储对象并打开 RIDF 数据文件:**  
   C++  
   TArtEventStore \*estore \= new TArtEventStore();  
   estore-\>Open("path/to/your/datafile.ridf"); // 或者 estore-\>Open(shared\_memory\_key) 用于在线分析

4. **创建核心 PID 校准/重建对象:**  
   C++  
   TArtCalibPID \*calibPID \= new TArtCalibPID();  
   // TArtCalibPID 对象会自动从 TArtStoreManager 中查找 TArtBigRIPSParameters 等所需参数  
   // 它内部会创建和管理 TArtCalibPPAC, TArtCalibPlastic, TArtCalibIC,  
   // TArtRecoTOF, TArtRecoRIPS 等子对象。

   TArtCalibPID 是执行 BigRIPS 粒子鉴别的核心引擎。  
5. **定义直方图和 N元组 (可选，但通常需要):**  
   C++  
   // 例如: ΔE vs TOF, A/Q vs Z, 各探测器的原始/刻度谱等  
   TH2F \*hDeltaE\_TOF \= new TH2F("hDeltaE\_TOF", "DeltaE vs TOF;TOF (arb. units);DeltaE (arb. units)", 400, 200, 300, 400, 500, 1500);  
   TH2F \*hAoQ\_Z \= new TH2F("hAoQ\_Z", "A/Q vs Z;Z;A/Q", 200, 20, 70, 200, 2.0, 3.0);  
   // TTree \*pid\_tree \= new TTree("pid\_tree", "PID Ntuple");  
   // pid\_tree-\>Branch(...);

6. **进入事件循环:**  
   C++  
   while(estore-\>GetNextEvent()){  
       // 清除上一个事件的数据  
       calibPID-\>ClearData(); // 这会递归调用其管理的子对象的 ClearData()

       // 执行本事件的刻度和重建  
       calibPID-\>ReconstructData(); // 这会递归调用其管理的子对象的 ReconstructData()

       // 从 TArtStoreManager 或 TArtCalibPID 对象获取刻度/重建后的数据容器  
       // 示例：获取最终的 RIPS 对象 (包含 A/Q 和 Z)  
       TClonesArray \*rips\_array \= (TClonesArray\*)sm-\>FindDataContainer("BigRIPSRIPS"); // 名称可能为 "BigRIPSRIPS" 或由 TArtCalibPID 定义  
       if(rips\_array){  
           for(int i=0; i\<rips\_array-\>GetEntriesFast(); \++i){  
               TArtRIPS \*rips \= (TArtRIPS\*)rips\_array-\>At(i);  
               if(rips){  
                   // hAoQ\_Z-\>Fill(rips-\>GetZet(), rips-\>GetAoQ());  
               }  
           }  
       }

       // 示例：获取 TOF 对象 (如 F3PL-F7PL TOF)  
       TArtTOF \*tof\_f3f7 \= (TArtTOF\*)calibPID-\>FindTOF("F3F7TOF"); // 假设 FindTOF 存在或通过 sm 获取  
       // 示例：获取 IC 能量损失对象  
       TArtIC \*ic\_sum \= (TArtIC\*)calibPID-\>FindIC("F7ICSUM"); // 假设 FindIC 存在或通过 sm 获取

       // if (tof\_f3f7 && ic\_sum) {  
       //     hDeltaE\_TOF-\>Fill(tof\_f3f7-\>GetTOF(), ic\_sum-\>GetEnergy());  
       // }

       // 示例：获取特定 PPAC 的数据，如  所示  
       TArtCalibPPAC \*calibPPAC \= calibPID-\>GetCalibPPAC(); // 获取 PPAC 校准对象的指针  
       if (calibPPAC) {  
           TArtPPAC \*f3ppac1a \= calibPPAC-\>FindPPAC("F3PPAC-1A"); // 按名称查找特定的 PPAC 对象  
           if (f3ppac1a) {  
               // Double\_t x\_pos \= f3ppac1a-\>GetX();  
               // Double\_t y\_pos \= f3ppac1a-\>GetY();  
               // Fill PPAC related histograms...  
           }  
       }  
       // 填充 N元组 (pid\_tree-\>Fill())  
   }

7. **事件循环结束后，保存结果:**  
   C++  
   TFile \*outFile \= new TFile("RecoPID\_output.root", "RECREATE");  
   hDeltaE\_TOF-\>Write();  
   hAoQ\_Z-\>Write();  
   // pid\_tree-\>Write();  
   outFile-\>Close();

RecoPID.C 的核心在于正确配置 TArtBigRIPSParameters，实例化 TArtCalibPID，然后在事件循环中调用其 ClearData() 和 ReconstructData() 方法。之后，用户就可以通过 TArtStoreManager 或 TArtCalibPID 提供的接口函数（如 FindRIPS(), FindTOF(), GetCalibPPAC()-\>FindPPAC() 等）来访问所需的各种刻度和重建后的数据对象，并用于填充直方图或 N元组，从而完成粒子鉴别分析。这个宏是理解 BigRIPS 数据分析流程的一个非常重要的实际案例。  
**第六章：使用 ANAROOT 分析 NEBULA 探测器数据**  
NEBULA (NEutron Detectors for Breakup of Unstable Nuclei with Large Acceptance) 是一个大型塑料闪烁体阵列，设计用于探测核反应（尤其是在 SAMURAI 谱仪实验中）中出射的高能中子。本章将详细介绍如何使用 ANAROOT 分析 NEBULA 探测器的数据，包括其探测原理、相关 ANAROOT 类、刻度流程和中子事件重建。  
**6.1 NEBULA 探测器概述**  
NEBULA 探测器系统主要由多层塑料闪烁体棒组成，排列成墙状结构，以覆盖较大的立体角，从而高效探测来自靶反应区的中子 5。

* **主要构成:**  
  * **塑料闪烁体棒 (Plastic Scintillator Bars):** 每根棒的两端通常都连接有光电倍增管 (PMT)，用于探测中子与闪烁体材料（主要是氢核和碳核）相互作用后产生的闪烁光。  
  * **VETO 探测器 (可选):** NEBULA 前方可能还配备有带电粒子否决探测器（如薄塑料闪烁体或多丝正比室，如 NEBULA-HPC 5），用于区分入射的是中子还是带电粒子，以减少带电粒子引起的本底。  
* **测量目标:**  
  * 中子的飞行时间 (Time-Of-Flight, TOF)：通过测量中子从反应靶到达 NEBULA 棒的时间。  
  * 中子在闪烁体中的能量沉积 (Light Output)：与中子能量有关，但关系复杂，主要用于设置阈值和进行中子/γ甄别。  
  * 中子击中位置：沿闪烁体棒方向的位置可以通过两端 PMT 信号的时间差或幅度比确定；击中哪一根棒则给出了中子在垂直于棒方向的二维位置。  
  * 综合这些信息，可以重建中子的出射角度和动量/能量。

NEBULA 通常与 SAMURAI 磁谱仪联用，用于研究不稳定原子核的破裂反应、共振态衰变等物理过程，其中中子是重要的出射粒子。  
**6.2 相关 ANAROOT 类**  
ANAROOT 为 NEBULA 探测器提供了专门的类，用于数据处理 5。  
**表4：用于 NEBULA 分析的核心 ANAROOT 类**

| 类名 (Class Name) | 探测器/用途 (Detector/Purpose) | 主要功能/存储数据 (Main Function/Stored Data) | 来源 |
| :---- | :---- | :---- | :---- |
| TArtCalibNEBULA | NEBULA | NEBULA 探测器阵列的整体刻度与重建协调类。它会管理和调用对单个闪烁体棒进行刻度的逻辑，并可能包含中子/γ甄别、串扰处理等高级功能。 | 6 |
| TArtNEBULAPla | NEBULA Plastic Bar | 存储单个 NEBULA 塑料闪烁体棒刻度后的数据。通常包含：TOF\_L, TOF\_R, QDC\_L, QDC\_R (两端 PMT 的时间和电荷), 平均时间 (MeanTime), 沿棒的击中位置 (PosY), 总光输出 (QTotal), 脉冲形状甄别参数 (如 QTail/QTotal) 等。 | 5 |
| TArtNEBULAHPC | NEBULA HPC (VETO) | (如果实验中使用了 NEBULA 的高压正比计数管作为 VETO) 存储 HPC 的数据，用于识别和否决穿过 NEBULA 的带电粒子。 | 5 |

TArtCalibNEBULA 是进行 NEBULA 数据分析的入口点，它负责驱动整个刻度和初步重建流程。分析结果，即每个被击中的 NEBULA 闪烁体棒的信息，则存储在 TArtNEBULAPla 对象中，这些对象通常以 TClonesArray 的形式由 TArtStoreManager 管理。  
**6.3 中子探测原理与数据特点**  
理解中子在塑料闪烁体中的探测原理对于正确分析 NEBULA 数据至关重要。

* **探测原理:**  
  * 中子是电中性的，不能直接引起电离或激发。它们主要通过与闪烁体材料中的原子核（主要是氢核 H 和碳核 C）发生强相互作用（弹性或非弹性散射）来被探测。  
  * 在弹性散射中，中子将其部分能量转移给反冲的质子或碳核。这些带电的反冲粒子随后在闪烁体中损失能量，引起材料的激发并发射闪烁光。  
  * 这些闪烁光被 PMT 收集并转换为电信号。  
* **数据特点:**  
  * **TOF 是关键:** 中子的能量主要通过测量其飞行时间 (TOF) 来确定。TOF 越短，能量越高。  
  * **光输出 (QDC/ADC):** PMT 信号的幅度（通常由 QDC 或 ADC 测量得到的光输出量）与中子在闪烁体中沉积的能量有关。然而，对于给定的中子能量，由于散射过程的随机性（散射角度、反冲核类型等），光输出的响应并非唯一确定，而是一个较宽的分布。因此，光输出主要用于设置探测阈值（以排除低能噪声）和进行中子/γ甄别。  
  * **击中位置:** 沿闪烁体棒的长度方向（通常定义为 Y 方向）的击中位置可以通过比较两端 PMT 信号到达的时间差 (Tleft​−Tright​) 或信号幅度（光衰减效应导致 Qleft​ vs Qright​）来确定。这对于精确计算中子的飞行路径长度和出射角度非常重要。  
  * **γ 射线本底:** γ 射线是 NEBULA 实验中的主要本底来源。它们通过康普顿散射或光电效应与闪烁体中的电子相互作用，产生与中子类似的闪烁信号。必须通过脉冲形状甄别 (PSD) 技术来区分中子和 γ 事件。  
  * **串扰 (Cross-talk):**  
    * **散射串扰:** 一个中子可能在一个闪烁体棒中发生散射，损失部分能量后，以较低能量进入相邻的棒再次发生相互作用，导致在多个棒中产生信号。这可能被误判为多个独立的中子击中。  
    * **光学串扰:** 一个棒中产生的闪烁光可能直接传播到相邻棒的 PMT，或者通过反射被探测到，造成虚假信号。 串扰处理是中子阵列数据分析中的一个重要挑战。

**6.4 NEBULA 刻度流程详解**  
对 NEBULA 探测器进行精确刻度是获得可靠中子物理信息的基础。13 强调了刻度程序在类似实验中的重要性。一个典型的 NEBULA 刻度流程包括以下几个方面：

* **时间刻度 (Timing Calibration):**  
  * **PMT 信号的渡越时间校正 (Walk Correction / Slewing Correction):** PMT 输出信号的实际触发时间可能依赖于信号的幅度。幅度较大的信号通常会比较早地达到甄别器的阈值。这种效应（称为 time walk 或 slewing）需要被校正，以确保时间测量的准确性，不受信号大小的影响。校正通常基于 TDC 值和相应的 QDC/ADC 值（信号幅度）之间的关系进行。  
  * **棒内时间对齐 (Intra-bar Time Alignment / Time Offset Correction):** 确保闪烁体棒两端 PMT 的相对时间基准一致。即，当粒子击中棒的几何中心时，两端 PMT 记录的时间（经过 walk 校正后）应该相同，或者其差值应该对应于光在棒内传播半长所需的时间。这通常通过调整其中一个 PMT 的时间偏移来实现。可以使用宇宙射线 muon 或中心放置的 γ 源进行标定。  
  * **绝对时间参考 (Absolute Time Reference / T0​ Calibration):** 将 NEBULA 探测器记录的时间与实验的全局起始时间 (T0​) 对齐，以便计算真实的飞行时间 (TOF)。T0​ 通常由反应靶区的快信号提供，例如：  
    * 束流粒子到达靶的时刻（由上游束流探测器如塑料闪烁体给出）。  
    * 反应产生的瞬发 γ 射线闪光（由放置在靶区附近的小型、快速 γ 探测器，如 BaF$\_2$ 或 LaBr$\_3$ 闪烁体，探测到）。 通过测量已知 TOF 的粒子（如直接从靶区飞向 NEBULA 的 γ 射线，其 TOF \= 距离/c）或通过分析特定反应道的时间结构，可以确定每个 NEBULA 棒的 T0​ 偏移。  
* **能量刻度 (Light Output Calibration):**  
  * 目标：建立 PMT 输出的电荷信号 (QDC/ADC 值) 与粒子在闪烁体中沉积的能量之间的关系。对于中子探测，通常将光输出刻度为电子等效能量 (MeVee)，即产生相同光输出的电子的能量。  
  * 方法：  
    * 使用标准 γ 射线源 (如 60Co, $^{137}$Cs, 22Na, 241Am 等)。这些源发射已知能量的 γ 射线，它们在塑料闪烁体中主要通过康普顿散射损失能量。通过测量康普顿散射电子能谱的末端（康普顿边）对应的 QDC/ADC 值，可以建立光输出与 MeVee 之间的关系。  
    * 使用宇宙射线 muon。Muon 在塑料闪烁体中通常表现为最小电离粒子 (MIP)，其能量损失谱有一个可识别的峰（朗道分布）。这个峰位可以作为一个刻度点。  
  * 此能量刻度主要用于：  
    1. 设置探测器的能量阈值，以排除电子学噪声和极低能的背景。  
    2. 为中子/γ甄别 (PSD) 提供

#### **引用的著作**

1. Tools/Analysis/ANAROOT/Installation \- RIBFDAQ, 访问时间为 五月 23, 2025， [https://ribf.riken.jp/RIBFDAQ/index.php?Tools%2FAnalysis%2FANAROOT%2FInstallation](https://ribf.riken.jp/RIBFDAQ/index.php?Tools/Analysis/ANAROOT/Installation)  
2. Tools/Analysis/ANAROOT \- RIBFDAQ, 访问时间为 五月 23, 2025， [https://ribf.riken.jp/RIBFDAQ/index.php?Tools%2FAnalysis%2FANAROOT](https://ribf.riken.jp/RIBFDAQ/index.php?Tools/Analysis/ANAROOT)  
3. ANAROOT: new online/offline framework for RIBF data analysis based on ROOT, 访问时间为 五月 23, 2025， [https://ribf.riken.jp/RIBFDAQ/index.php?plugin=attach\&refer=Tools%2FAnalysis%2FANAROOT\&openfile=anaroot\_ribfusermeeting2013.pdf](https://ribf.riken.jp/RIBFDAQ/index.php?plugin=attach&refer=Tools/Analysis/ANAROOT&openfile=anaroot_ribfusermeeting2013.pdf)  
4. Tools/Analysis/ANAROOT/Go4 \- RIBFDAQ, 访问时间为 五月 23, 2025， [https://ribf.riken.jp/RIBFDAQ/index.php?Tools%2FAnalysis%2FANAROOT%2FGo4](https://ribf.riken.jp/RIBFDAQ/index.php?Tools/Analysis/ANAROOT/Go4)  
5. Tools/Analysis/ANAROOT/Abstract \- RIBFDAQ, 访问时间为 五月 23, 2025， [https://ribf.riken.jp/RIBFDAQ/index.php?Tools%2FAnalysis%2FANAROOT%2FAbstract](https://ribf.riken.jp/RIBFDAQ/index.php?Tools/Analysis/ANAROOT/Abstract)  
6. ANAROOT/Manual/analoop \- Kondo Moin Wiki, 访问时间为 五月 23, 2025， [http://be.nucl.ap.titech.ac.jp/\~kondo/moin/moin.cgi/ANAROOT/Manual/analoop](http://be.nucl.ap.titech.ac.jp/~kondo/moin/moin.cgi/ANAROOT/Manual/analoop)  
7. ANAROOT/Manual/reference \- Kondo Moin Wiki, 访问时间为 五月 23, 2025， [http://be.nucl.ap.titech.ac.jp/\~kondo/moin/moin.cgi/ANAROOT/Manual/reference](http://be.nucl.ap.titech.ac.jp/~kondo/moin/moin.cgi/ANAROOT/Manual/reference)  
8. Different Types of Workflows in Data Pipelines \- Peliqan, 访问时间为 五月 23, 2025， [https://peliqan.io/blog/different-types-of-workflows-in-data-pipelines/](https://peliqan.io/blog/different-types-of-workflows-in-data-pipelines/)  
9. Graceful Logic Evolution in Web Data Processing Workflows, 访问时间为 五月 23, 2025， [http://i.stanford.edu/\~olston/publications/workflowEvolutionTR.pdf](http://i.stanford.edu/~olston/publications/workflowEvolutionTR.pdf)  
10. Tools/Analysis/ANAROOT/Tutorial \- RIBFDAQ, 访问时间为 五月 23, 2025， [https://ribf.riken.jp/RIBFDAQ/index.php?Tools%2FAnalysis%2FANAROOT%2FTutorial](https://ribf.riken.jp/RIBFDAQ/index.php?Tools/Analysis/ANAROOT/Tutorial)  
11. 访问时间为 一月 1, 1970， [https\_ribf\_riken\_jp\_RIBFDAQ\_index\_php\_plugin\_attach\_refer\_Tools%2FAnalysis%2FANAROOT\_openfile\_anaroot\_ribfusermeeting2013\_pdf](http://docs.google.com/https_ribf_riken_jp_RIBFDAQ_index_php_plugin_attach_refer_Tools%2FAnalysis%2FANAROOT_openfile_anaroot_ribfusermeeting2013_pdf)  
12. Yuto Ichinohe (RIKEN Nishina Center) \- Indico Global, 访问时间为 五月 23, 2025， [https://indico.global/event/6805/contributions/58357/attachments/29459/52337/OS\_day2\_id48\_ichinohe.pdf](https://indico.global/event/6805/contributions/58357/attachments/29459/52337/OS_day2_id48_ichinohe.pdf)  
13. Low-energy dipole response of the halo nuclei \- INIS-IAEA, 访问时间为 五月 23, 2025， [https://inis.iaea.org/records/w1kc8-5ep03/files/53109350.pdf?download=1](https://inis.iaea.org/records/w1kc8-5ep03/files/53109350.pdf?download=1)  
14. Low-energy dipole response of the halo nuclei 6,8He \- TUprints \- TU Darmstadt, 访问时间为 五月 23, 2025， [https://tuprints.ulb.tu-darmstadt.de/20267/1/Dissertation\_LehrChristopher\_2022-01-04.pdf](https://tuprints.ulb.tu-darmstadt.de/20267/1/Dissertation_LehrChristopher_2022-01-04.pdf)