---
title: smsimultor
---

## 

read_me

readme.txt
2019年10月16日 — 版本 5.0（使用 Geant4.10.05.p01 编译）
2017年12月28日 — 版本 4.0（使用 Geant4.9.6.p04 编译）
2014年7月18日 — 版本 3.2（使用 Geant4.9.6.p02 编译）

--------
摘要
--------
“smsimulator”由 R. Tanaka、Y. Kondo 和 M. Yasuda 开发，用于模拟 SAMURAI 实验。从 5.0 版本起，兼容 Geant4.10.X。4.X 及更早版本兼容 Geant4.9.X。从 3.0 版本起，实现了从 Geant4 步骤到可观测量（如 TArtNEBULAPla）的转换。需要 ANAROOT 库。本版本还包含了 simtrace，可用于模拟带电粒子在 SAMURAI 磁铁中的轨迹。

目前 smsimulator 包含：
 - README：本文件
 - setup.sh：安装脚本
 - smg4lib：用于创建 SAMURAI 仿真库的主要文件
 - crosssection：创建截面数据集，并用 gnuplot 绘图
 - get_pdgmass：显示重离子 PDG 质量的简单程序
 - simtrace：检查 SAMURAI 磁铁中轨迹的简单示例
 - simdayone：重离子+中子的仿真示例
 - sim_samurai21：包含 NeuLAND 的 28O 实验仿真示例
 - sim_tm1510：TM1510，SAMURAI 配合 DALI、NeuLAND、NEBULA
 - sim_dali：DALI
 - sim_s21dali：SAMURAI21 实验中带 MINOS（作为对象）的 DALI
 - sim_catana：CATANA

----------
使用方法
----------
(1) 安装 Geant4
smsimulator 5.x 兼容 Geant4.10.x。smsimulator 4.x 兼容 Geant4.9.x。（建议中子模拟使用 4.9.6.p02 或更高版本。）如用旧版本，除 (1.a) 外还需其他修改。详情见 http://be.nucl.ap.titech.ac.jp/~ryuki/iroiro/geant4/（日文）。

(1.a) 修改 G4INCLCascade.cc 以避免致命中止，如下所示。（smsimulator 5.x 不需要此操作）

---------------------------------------------------------------------------
  G4bool INCL::prepareReaction(const ParticleSpecies &projectileSpecies, const G4double kineticEnergy, const G4int A, const G4int Z) {
    if(A < 0 || A > 300 || Z < 1 || Z > 200) {
      ERROR("Unsupported target: A = " << A << " Z = " << Z << std::endl);
      ERROR("Target configuration rejected." << std::endl);
      return false;
    }

    //--> 为避免中止添加
    if (projectileSpecies.theA==1 && A==1){
      return false;
    }
    //<--

    // 初始化最大宇宙半径
    initUniverseRadius(projectileSpecies, kineticEnergy, A, Z);
---------------------------------------------------------------------------

(1.b) 编译 Geant4

(2) 安装 ANAROOT
(2.a)
ANAROOT 可从 RIBFDAQ 网页下载。
http://ribf.riken.jp/RIBFDAQ/

(3) 编译 smsimulator
根据你的系统修改 smsimulator/setup.sh。

$ . setup.sh
$ cd smg4lib
$ make
$ cd ../simtrace
$ make
...（simdayone、get_pdgmass、crosssection 等同理）

(4) 运行 Geant4
将工作目录 "smsimulator/work" 复制到其他地方。（不建议直接在 "smsimulator/work" 下工作，以便将来更新。）SAMURAI 磁铁的场图可在 http://ribf.riken.jp/SAMURAI/ 下载。你可以在 work/xxxxx/g4mac/examples/ 下找到 Geant4 宏文件示例。

- vis.mac
  可视化示例

- example_Pencil.mac
  铅笔束流示例

- example_Gaus.mac
  单能束流，具有高斯分布的位置和角度扩展的示例

- example_Tree.mac
  用于三体系统相空间衰变的 Tree 输入示例

(4.a) NEBULA 的探测器几何由 smsimulator/simdayone/geometry/ 下的两个 csv 文件给出。
  - NEBULADetectors_xxx.csv ：每个探测器的位置
  - NEBULA_xxx.csv ：整个 NEBULA 系统的几何

还包含用于生成参数文件的 perl 脚本示例。用法如下：

$ ./CreatePara_NEBULAFull.pl > NEBULADetector_Full.csv

(4.b) 输出 root 文件
输出的 root 文件包含如下 Tree：
  - Geant4 步骤
  - 参数
  - 从 Geant4 步骤转换而来的可观测量
由于存储 Geant4 步骤会导致文件很大，你可以通过如下方式跳过存储：
  - 在 geant4 宏中加入 /action/data/NEBULA/StoreSteps false
  - NEBULASimDatainitializer::SetDataStore(false)

(5) 分析 Geant4 输出
可在 smsimulator/xxxx/macros/examples/ 下找到用于分析 Geant4 输出的 ROOT 宏示例。

  - GenerateInputTree_PhaseSpaceDecay.cc
    用于三体相空间衰变模拟的输入 tree 文件生成示例。

  - analysis_example.cc
    分析 Geant4 输出的简单示例。

(5.a) 串扰分析
如需使用串扰分析示例，请按如下操作：

(5.a.1) 修改 ANAROOT 数据类
在 TArtNEBULAPla.hh（ANAROOT 类）中添加如下代码以支持 TClonesArray::Sort。

---------------------------------------------------------------------------
  // 基于 TAveSlw 的排序重载函数
public:
  Bool_t IsEqual(TObject *obj) const {return fTAveSlw == ((TArtNEBULAPla*)obj)->fTAveSlw;}
  Bool_t IsSortable() const {return kTRUE;}
  Int_t Compare(const TObject *obj) const{
    if (fTAveSlw < ((TArtNEBULAPla*)obj)->fTAveSlw) return -1;
    else if (fTAveSlw > ((TArtNEBULAPla*)obj)->fTAveSlw) return 1;
    else return 0;
  }
---------------------------------------------------------------------------

(5.a.2) 为 ROOT 生成库文件
在 smsimulator/work/smanalib/ 下生成库文件。
$ cd smsimulator/work/smanalib/
$ ./auto.sh
$ make
$ make install

修改 rootlogon.C 以加载库并添加 include 路径。可在 smsimulator/work/sim_samurai21/macros/examples/analysis_crosstalk_example.cc 中找到 TArtCrosstalk_XXX 类的使用示例。

-----------
更新信息
-----------
- 版本 4.2
  - TFragSimData 中增加了 TargetThickness

- 版本 3.2
  - 实现了 NeuLAND
  - 实现了串扰分析示例

- 版本 3.0
  - 合并了 simtrace
  - 实现了从 Geant4 步骤数据到 TArtNEBULAPla 的转换
  - 修改了数据类定义
  - 支持实验室充气
  - 整理了 Messenger 的命令名称
  - 移除了 BeamTypeDemocraticDecay（可通过 BeamTypeTree 实现）
  - 为每个元素准备了 DetectorConstruction，便于将来使用

-----
提示
-----
- 大量事件模拟
  为避免中止，在 g4mac/xxx.mac 中加入如下行：
  /control/suppressAbortion 1
  在 Geant4.10.x 中已改进。

- 升级到 smsimulator 5.x + Geant4.10.x 时
  使用单位时需添加 "#include \"G4SystemOfUnits.hh\""。

- 通过 messenger 命令
  在 Geant4 交互模式下可用如下方式查看已实现命令：
  Idle> ls /action/
  Idle> ls /samurai/

- 事件生成器
  - 可通过 tree 向 smsimulator 输入任意分布。get_pdgmass 可用于获取重离子的质量值。

- NeuLAND 实验仿真
  - smsimulator3.2/sim_samurai21 是使用 NEBULA+NeuLAND 配置的 28O 实验示例。你可以复制该目录为 sim_samuraiXX，并根据你的实验设置进行修改。

- 自定义串扰算法
  - 你可以开发自己的串扰算法。TArtCrosstalkAnalysis 基类可用于此目的。复制 TArtCrosstalkAnalysis_XXX.cc 和 .hh 并修改。别忘了在 smanalib/sources/smana_linkdef.hh 中添加一行，以便在 ROOT 中使用。

- 自定义数据类
  如需自定义数据类，请创建如下类：
  - TXXXSimData ：用于存储 Geant4 步骤的数据类
  - XXXSimDataInitializer ：初始化器（继承自 SimDataInitializer）
  - XXXSimDataConverter ：从 Geant4 步骤到可观测量的转换器（继承自 SimDataConverter）
  - XXXSD ：灵敏探测器类（继承自 G4VSensitiveDetector）

  然后可通过 SimDataManager 控制它们。

-----
待办事项
-----
- 尚未包含的内容
  - 重离子的分辨率
  - 靶材中的能量损失差异（对 Erel 分辨率有重要影响）

- 有关模拟器有效性/评估的文档。

