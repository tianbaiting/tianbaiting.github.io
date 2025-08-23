## FDC2 相关库与文件

FDC2 相关的所有库和主要文件分布如下。

源码来源于 konda 在 gitlab upload  
[https://ribfrepo.riken.jp/kondo/smsimulator](https://ribfrepo.riken.jp/kondo/smsimulator)

### 目录结构

```bash
smsimulator
├── sources
│   ├── projects
│   │   └── sim_samurai21
│   │       ├── include
│   │       └── src
│   └── smg4lib
│       ├── action
│       ├── data
│       ├── detectors
│       │   └── FDC2
│       ├── devices
│       └── physics
└── work
    ├── field_map
    ├── g4mac
    ├── geometry
    ├── macros
    │   └── examples
    └── rootfiles
```

### 1. 探测器几何与构建 (Detector Geometry & Construction)

- **路径**: `sources/smg4lib/detectors/FDC2/`
- **文件**: `FDC2Construction.hh` / `.cc`
- **功能**: 负责 FDC2 的几何结构、材料、位置、角度等定义。

### 2. 敏感探测器与数据采集 (Sensitive Detector & Data Acquisition)

- **路径**: `sources/smg4lib/data/`
- **文件**:
    - `FragmentSD.hh` / `.cc`：挂载到 FDC2 的活跃体积上，负责采集粒子穿越时的物理信息。
    - `TSimData.hh` / `.cc`：存储每个事件的物理数据，包括 `detectorName` 字段用于区分 FDC2。
    - `TFragSimParameter.hh` / `.cc`：FDC2 的参数配置相关。
    - `SimDataManager.hh` / `.cc`：管理数据数组和数据流。

#### 数据采集流程与内容

- FDC2 的活跃体积会挂载敏感探测器（`FragmentSD`）。当粒子穿越 FDC2 时，`FragmentSD::ProcessHits` 方法会被自动调用，采集并存储物理信息。
- **存储的数据内容**（在 `TSimData` 或 `TFragSimData` 对象中）:
    - **探测器名称**：`fDetectorName`（如 "FDC2"），用于区分数据来源。
    - **粒子信息**:
        - `fPDGCode`：PDG 编码
        - `fParticleName`：粒子名称
        - `fZ`, `fA`：原子序数和质量数
        - `fCharge`：电荷
        - `fMass`：质量
    - **轨迹信息**:
        - `fParentID`：父粒子编号
        - `fTrackID`：轨迹编号
    - **位置与动量**:
        - `fPrePosition`, `fPostPosition`：步进前后的位置（x, y, z，单位 mm）
        - `fPreMomentum`, `fPostMomentum`：步进前后动量（单位 MeV）
    - **时间信息**:
        - `fPreTime`, `fPostTime`：步进前后全局时间（单位 ns）
    - **飞行长度**：`fFlightLength`（粒子到达该点的总路径长度，单位 mm）
    - **是否被接受**：`fIsAccepted`（用于筛选有效物理事件）
- **数据输出方式**:
    - 所有上述数据会被存入 ROOT 文件的 TTree 分支（如 "fragment"）。
    - 每个事件包含一个数据数组，数组中的每个元素对应一次有效的 step（通常是主粒子击中 FDC2 的 step）。
    - 后续分析脚本（如 `work/macros/examples/analysis_example.cc`）会读取这些分支，筛选 `fDetectorName == "FDC2"` 的数据进行物理分析。

### 3. 主探测器构建与集成 (Main Detector Construction & Integration)

- **路径**: `sources/projects/sim_samurai21/`
- **文件**:
    - `sim_samurai21.cc`：主程序入口。
    - `src/SAMURAI21DetectorConstruction.cc`：主探测器构建类，负责实例化 FDC2 并挂载敏感探测器。

### 4. 数据分析 (Data Analysis)

- **路径**: `work/macros/examples/`
- **文件**: `analysis_example.cc`, `analysis_crosstalk_example.cc`
- **功能**: 读取和分析 FDC2 采集的数据。

### 5. 其他辅助库 (Other Helper Libraries)

- **路径**: `sources/smg4lib/action/`
- **功能**: 包含事件、运行、跟踪等动作类，这些类间接影响 FDC2 的数据采集流程。
当粒子穿越 FDC2 时，FragmentSD::ProcessHits 方法会被自动调用，采集并存储物理信息。
2. 具体存储的数据内容
在 FragmentSD::ProcessHits 里，主要存储到 TSimData 或 TFragSimData 对象的数据包括：

探测器名称：fDetectorName（如 "FDC2"），用于区分数据来源。
粒子信息：
fPDGCode：PDG 编码
fParticleName：粒子名称
fZ、fA：原子序数和质量数
fCharge：电荷
fMass：质量
轨迹信息：
fParentID：父粒子编号
fTrackID：轨迹编号
位置与动量：
fPrePosition、fPostPosition：步进前后的位置（x, y, z，单位 mm）
fPreMomentum、fPostMomentum：步进前后动量（单位 MeV）
时间信息：
fPreTime、fPostTime：步进前后全局时间（单位 ns）
飞行长度：
fFlightLength：粒子到达该点的总路径长度（单位 mm）
是否被接受：
fIsAccepted：用于筛选有效物理事件
3. 数据输出方式
所有上述数据会被存入 ROOT 文件的 TTree 分支（如 "fragment"）。
每个事件包含一个数据数组，数组中的每个元素对应一次有效的 step（通常是主粒子击中 FDC2 的 step）。
后续分析脚本（如 work/macros/examples/analysis_example.cc）会读取这些分支，筛选 fDetectorName == "FDC2" 的数据进行物理分析。


构建 FDC2 并挂载敏感探测器
代码通过 fFDC2Construction->ConstructSub() 构建 FDC2 的几何体，并通过 fFDC2Construction->GetActiveVolume()->SetSensitiveDetector(fFDC2SD) 将敏感探测器 FragmentSD("/FDC2") 挂载到 FDC2 的活跃体积上。

事件模拟时自动采集数据
当粒子穿越 FDC2 的活跃体积时，Geant4 会自动调用 FragmentSD::ProcessHits 方法。该方法会采集粒子的能量沉积、位置、动量、时间、粒子类型等物理信息。

数据归属与存储
在 ProcessHits 方法中，采集到的数据会被封装到 TSimData 或 TFragSimData 对象，并设置 fDetectorName = "FDC2"，用于标识这些数据属于 FDC2。所有数据会被存入一个 ROOT 文件的 TTree 分支（如 "fragment"），每个事件对应一个数据数组。

后续分析
分析脚本（如 analysis_example.cc）会读取这些分支，通过 fDetectorName 字段筛选出 FDC2 的数据，进行物理分析。

总结：
FDC2 的输出数据由敏感探测器自动采集，封装为数据对象并存入 ROOT 文件，后续可通过分析脚本按探测器名称筛选和处理。

