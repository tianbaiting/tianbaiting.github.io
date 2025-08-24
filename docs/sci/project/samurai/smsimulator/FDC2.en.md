## FDC2 Related Libraries and Files

All libraries and main files related to FDC2 are listed below.

Source code by konda, uploaded to GitLab  
[https://ribfrepo.riken.jp/kondo/smsimulator](https://ribfrepo.riken.jp/kondo/smsimulator)

### Directory Structure

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

### 1. Detector Geometry & Construction

- **Path**: `sources/smg4lib/detectors/FDC2/`
- **Files**: `FDC2Construction.hh` / `.cc`
- **Function**: Defines the geometry, materials, position, and orientation of FDC2.

### 2. Sensitive Detector & Data Acquisition

- **Path**: `sources/smg4lib/data/`
- **Files**:
    - `FragmentSD.hh` / `.cc`: Mounted to the active volume of FDC2, responsible for collecting physical information when particles pass through.
    - `TSimData.hh` / `.cc`: Stores physical data for each event, including the `detectorName` field to distinguish FDC2.
    - `TFragSimParameter.hh` / `.cc`: Configuration parameters for FDC2.
    - `SimDataManager.hh` / `.cc`: Manages data arrays and data streams.

#### Data Acquisition Process and Content

- The active volume of FDC2 mounts the sensitive detector (`FragmentSD`). When a particle passes through FDC2, the `FragmentSD::ProcessHits` method is automatically called to collect and store physical information.
- **Stored Data Content** (in `TSimData` or `TFragSimData` objects):
    - **Detector Name**: `fDetectorName` (e.g., "FDC2"), used to identify the data source.
    - **Particle Information**:
        - `fPDGCode`: PDG code
        - `fParticleName`: Particle name
        - `fZ`, `fA`: Atomic number and mass number
        - `fCharge`: Charge
        - `fMass`: Mass
    - **Track Information**:
        - `fParentID`: Parent particle ID
        - `fTrackID`: Track ID
    - **Position and Momentum**:
        - `fPrePosition`, `fPostPosition`: Position before and after the step (x, y, z, in mm)
        - `fPreMomentum`, `fPostMomentum`: Momentum before and after the step (in MeV)
    - **Time Information**:
        - `fPreTime`, `fPostTime`: Global time before and after the step (in ns)
    - **Flight Length**: `fFlightLength` (total path length to this point, in mm)
    - **Accepted**: `fIsAccepted` (used to filter valid physical events)
- **Data Output**:
    - All the above data are stored in a ROOT file TTree branch (e.g., "fragment").
    - Each event contains a data array, with each element corresponding to a valid step (usually when the primary particle hits FDC2).
    - Analysis scripts (e.g., `work/macros/examples/analysis_example.cc`) read these branches and filter data with `fDetectorName == "FDC2"` for physics analysis.

### 3. Main Detector Construction & Integration

- **Path**: `sources/projects/sim_samurai21/`
- **Files**:
    - `sim_samurai21.cc`: Main program entry.
    - `src/SAMURAI21DetectorConstruction.cc`: Main detector construction class, responsible for instantiating FDC2 and mounting the sensitive detector.

### 4. Data Analysis

- **Path**: `work/macros/examples/`
- **Files**: `analysis_example.cc`, `analysis_crosstalk_example.cc`
- **Function**: Reads and analyzes data collected by FDC2.

### 5. Other Helper Libraries

- **Path**: `sources/smg4lib/action/`
- **Function**: Includes event, run, and tracking action classes, which indirectly affect the data acquisition process of FDC2.

### Summary

- The output data of FDC2 is automatically collected by the sensitive detector, encapsulated into data objects, and stored in ROOT files. Subsequent analysis scripts can filter and process data by detector name.
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

