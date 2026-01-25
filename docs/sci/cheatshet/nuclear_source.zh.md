# ☢ 精选核科学资源 ☢


https://sites.google.com/view/opticalpotentials/reaction-codes 这个页面主要是一个“核反应数值代码工具箱”的索引，收录了一批做光学势、转移反应、三体/多体反应等的程序

# 核科学与核工程开源项目列表
精选的开源项目列表，适用于核科学与核工程领域。

## 粒子输运

### 代码：蒙特卡洛

- [ERGnrc](https://nrc-cnrc.github.io/EGSnrc/) — 光子/电子/正电子的蒙特卡洛输运代码
- [FRENSIE](https://github.com/FRENSIE/FRENSIE) — 中子/光子蒙特卡洛输运代码
- [Geant4](https://geant4.web.cern.ch/) — 高能粒子蒙特卡洛输运工具
- [OpenMC](https://github.com/openmc-dev/openmc) — 中子/光子蒙特卡洛输运代码
- [SCONE](https://github.com/CambridgeNuclear/SCONE) — 中子蒙特卡洛输运代码
- [Warp](https://github.com/weft/warp) — 面向 GPU 的中子蒙特卡洛输运代码

### 代码：确定性方法

- [BART](https://github.com/SlaybaughLab/BART) — 加州大学伯克利分校开发的有限元、离散方向代码
- [DRAGON](https://www.polymtl.ca/merlin/) — 蒙特利尔理工学院开发的格点代码
- [FeenoX](https://www.seamplex.com/feenox) — 非结构化有限元（类）工具，包含扩散和离散方向求解
- [Gnat](https://github.com/OTU-Centre-for-SMRs/gnat) — 基于 MOOSE 的离散方向与流体活化求解器，由安大略理工开发
- [OpenMOC](https://github.com/mit-crpg/openmoc) — 特征线法（MOC）代码
- [OpenSN](https://github.com/open-sn/opensn) — [Chi-Tech](https://github.com/chi-tech/chi-tech) 的继任者，德州农工开发的大规模并行离散方向代码
- [Scarabée](https://github.com/scarabee-dev/scarabee) — 格点物理与确定性输运工具箱
- [THOR](https://github.com/NCSU-NCSG/THOR) — 在非结构化网格上使用 AHOT-C 方法的离散方向代码

### 代码：事件生成器

- [CGMF](https://github.com/lanl/CGMF) — 裂变事件生成器
- [FREYA](https://nuclear.llnl.gov/simulation/main.html) — 裂变事件生成器

### 相关工具

- [ACE Format](https://github.com/NuclearData/ACEFormat) — ACE 格式文档
- [csg2csg](https://github.com/makeclean/csg2csg) — 不同 CSG 类型间转换工具
- [DAGMC](https://github.com/svalinn/DAGMC) — 直接加速几何蒙特卡洛工具包
- [GeoUNED](https://github.com/GEOUNED-org/GEOUNED) — 基于 FreeCAD 的 CAD 与 CSG 相互转换工具
- [KDSource](https://github.com/KDSource/KDSource) — 从蒙特卡洛模拟生成 KDE 表面源的工具
- [McCAD](https://github.com/inr-kit/McCAD-Library) — 将 CAD (BRep) 转换为蒙特卡洛 (CSG) 的 C++ 库
- [MCNPTools](https://github.com/lanl/mcnptools) — MCNP 的 C++/Python 接口与工具
- [MCPL](https://github.com/mctools/mcpl) — 存储粒子状态的二进制文件格式
- [MontePy](https://github.com/idaholab/montepy) — 读取、编辑、写入 MCNP 文件的 Python 库
- [serpentTools](https://github.com/CORE-GATECH-GROUP/serpent-tools) — 基于 Python 的 Serpent 工具集
- [t4_geom_convert](https://www.cea.fr/energies/tripoli-4/tripoli-4/pre_post_tools/t4_geom_convert) — 将 MCNP 几何转换为 TRIPOLI-4

## 核数据

- [ACEMAKER](https://github.com/iaea-nds/acemaker) — 生成 ACE 文件的软件包
- [EMPIRE](https://www-nds.iaea.org/empire/index.html) — 核反应模型代码
- [endf-python](https://github.com/paulromano/endf-python) — ENDF 的 Python 解析器
- [FRENDY](https://rpg.jaea.go.jp/main/en/program_frendy) — 核数据处理工具
- [FUDGE](https://github.com/LLNL/fudge) — 基于 Python 的核数据处理库
- [JADE](https://github.com/dodu94/JADE) — 核数据库验证与确认工具
- [mendeleev](https://github.com/lmmentel/mendeleev) — 获取元素、离子与同位素属性的 Python 包
- [NJOY21](https://github.com/njoy/NJOY21) — 核数据处理代码
- [Nuclear Data Reader](https://github.com/php1ic/nuclear-data-reader) — 解析 NUBASE 和 AME 数据文件的 C++ 库
- [NucML](https://github.com/pedrojrv/nucml) — 面向核数据评估的机器学习流水线
- [PapillonNDL](https://github.com/HunterBelanger/papillon-ndl) — 读取与采样 ACE 文件的 C++ / Python 库
- [PREPRO](https://www-nds.iaea.org/public/endf/prepro/) — 核数据预处理工具
- [PyNjoy 2012](https://www.polymtl.ca/merlin/pynjoy2012.htm) — 核数据处理工具
- [SANDY](https://github.com/luca-fiorito-11/sandy) — 核数据抽样工具
- [SCALE](https://code.ornl.gov/scale/code/scale-public) — SCALE 的公开组件（如 AMPX、SAMMY）
- [TALYS](https://nds.iaea.org/talys) — 核反应模拟器

## 燃耗 / 转化 / 衰变

- [ADDER](https://github.com/anl-rtr/adder) — 基于 Python 的燃料管理与燃耗工具
- [ALARA](https://github.com/svalinn/ALARA) — 广泛用于聚变的活化计算代码
- [ONIX](https://github.com/jlanversin/ONIX) — 基于 Python 的燃耗代码
- [OpenMC](https://github.com/openmc-dev/openmc) — 在 OpenMC 中集成的燃耗求解器
- [radioactivedecay](https://github.com/radioactivedecay/radioactivedecay) — 放射性衰变求解器

## 动力学

- [KOMODO](https://github.com/imronuke/KOMODO) — 使用节点法求解三维扩散的核反应堆仿真器
- [PyRK](https://github.com/pyrk/pyrk) — 0 维中子学与热水力瞬态分析
- [Research Reactor Simulator](https://github.com/ijs-f8/Research-Reactor-Simulator) — 基于点动力学的实时 GUI 研究堆仿真器

## 燃料循环

- [Cyclus](https://github.com/cyclus/cyclus) — 核燃料循环仿真器
- [OpenMCyclus](https://github.com/arfc/openmcyclus) — 使用 OpenMC 的 `IndependentOperator` 实现的可燃耗反应堆原型，用于 Cyclus 燃料循环模拟

## 热液力学

- [DASSH](https://github.com/dassh-dev/dassh) — 适用于六角形组件的通道级热流体代码
- [Nek5000](https://github.com/Nek5000/Nek5000) — 谱元 CFD 代码
- [nekRS](https://github.com/Nek5000/nekRS) — 面向现代处理器与加速器的谱元 CFD 代码
- [OpenFOAM](https://www.openfoam.com/) — 有限体积 CFD 代码
- [TrioCFD](https://github.com/cea-trust-platform/TrioCFD-code) — 基于 TRUST 平台的计算流体力学代码

## 多物理场

- [Aurora](https://github.com/aurora-multiphysics/aurora) — 将 OpenMC 封装为 MOOSE 应用
- [Cardinal](https://github.com/neams-th-coe/cardinal) — 将 OpenMC 和 nekRS 封装为 MOOSE 应用
- [ENRICO](https://github.com/enrico-dev/enrico) — 蒙特卡洛与 CFD 耦合应用
- [GeN-Foam](https://gitlab.com/foam-for-nuclear/GeN-Foam) — 基于 OpenFOAM 的反应堆多物理求解器
- [MOOSE](https://github.com/idaholab/moose) — 有限元多物理框架
- [SALOME](https://www.salome-platform.org) — CAD 与多物理软件之间的互操作平台
- [TRUST](https://github.com/cea-trust-platform/trust-code) — 可用于构建 CFD 代码的软件平台

## 熔盐反应堆

- [Moltres](https://github.com/arfc/moltres) — 熔盐反应堆仿真代码
- [MSRE](https://github.com/openmsr/msre) — MSRE 的详细 CAD 模型
- [SaltProc](https://github.com/arfc/saltproc) — 燃料再处理仿真工具

## 其他

- [ARMI](https://github.com/terrapower/armi) — 反应堆分析自动化框架
- [NRIC Virtual Test Bed](https://github.com/idaholab/virtual_test_bed) — 示例问题仓库
- [PyNE](https://github.com/pyne/pyne) — Python/C++ 的核工程工具箱
- [RAVEN](https://github.com/idaholab/raven) — 不确定性量化、回归、概率风险分析、数据分析与模型优化框架
- [WATTS](https://github.com/watts-dev/watts) — 基于 Python 的模板化仿真工具
- [LaTeX classes and BibTeX style for ANS publications](https://github.com/paulromano/ans-latex-class) — ANS 出版物的 LaTeX 类与 BibTeX 样式

## 投入开源核科学与工程工具的研究团队

- [ARFC](https://arfc.github.io) (UIUC) — 先进反应堆与燃料循环
- [CNERG](https://cnerg.github.io) (UW-Madison) — 计算核工程研究组
- [CRPG](https://crpg.mit.edu) (MIT) — 计算堆物理小组
- [ONCORE](https://nucleus.iaea.org/sites/oncore/) (IAEA) — 由 IAEA 促成的一个面向开发与应用开源多物理仿真工具的国际合作框架，支持先进核电站的研究、教育与培训。
