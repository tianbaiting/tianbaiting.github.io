重建nebula需要这些文件：

参数 XML 文件（如 NEBULA.20250625.xml）

TArtCalibNEBULAHPC.hh/.cc

TArtCalibNEBULA.hh/.cc

TArtRecoNeutron.hh/.cc

TArtSAMURAIParameters.hh/.cc

相关数据对象类TArtNEBULAHPC、TArtNEBULAPla、TArtNeutron 


 TArtCalibNEBULAHPC

TArtCalibNEBULAHPC *nebulahpc_calib = new TArtCalibNEBULAHPC();

作用：负责校准 NEBULA 高压正比计数管（HPC - High Pressure Chamber）的数据。HPC 主要作为中子探测的否决探测器（veto detector），用于区分中子和带电粒子（如伽马射线转换产生的电子或质子）。

- 输入：从 TArtEventStore 读取 HPC 探测器的原始数据（如 TDC 时间信息）。
- 处理：
  - 应用时间校准参数（由 TArtSAMURAIParameters 管理）。
  - 将原始 TDC 值转换为物理时间。
  - 进行基本的 hit 判断。
- 输出：重建后的 TArtNEBULAHPC 对象，包含每个 HPC hit 的校准后信息（如时间、探测器 ID 等），存储于 TArtStoreManager 的 "NEBULAHPC" TClonesArray。




---

 TArtCalibNEBULA 

TArtCalibNEBULA *nebulapla_calib = new TArtCalibNEBULA();

作用：负责校准 NEBULA 塑料闪烁体（Pla - Plastic Scintillator）的数据，是 NEBULA 中子探测器的主要组成部分。

- 输入：从 TArtEventStore 读取塑料闪烁体两端 PMT 的原始数据（TDC 时间和 QDC 电荷）。
- 处理：
  - 应用时间和电荷校准参数。
  - 计算每个 hit 的平均时间、时间差（用于位置重建）、平均电荷。
  - 计算击中位置（position）。
  - 将校准后的时间和电荷转换为物理单位（ns, MeVee）。
- 输出：重建后的 TArtNEBULAPla 对象，包含每个 hit 的详细校准信息（ID, Layer, SubLayer, QUAveCal, TAveCal, PosCal 等），存储于 TArtStoreManager 的 "NEBULAPla" TClonesArray。

```
    Double_t pos[3];
    if(para->GetSubLayer() != 0){ // NEUT
      //      pos[0] = para->GetDetPos(0) + posxoff + gRandom->Uniform(-6,6);
      pos[0] = para->GetDetPos(0) + posxoff;
    }else{ // VETO
      //      pos[0] = para->GetDetPos(0) + posxoff + gRandom->Uniform(-16,16);
      pos[0] = para->GetDetPos(0) + posxoff;
    }
    pos[1] = posslw + para->GetDetPos(1) + posyoff; 
    pos[2] = para->GetDetPos(2) + poszoff;
```


代码通过判断 para->GetSubLayer() 是否为 0，区分 NEUT（中子探测层）和 VETO（反符合层）两种情况。无论是哪种情况，pos[0]（x 坐标）都设置为 para->GetDetPos(0) + posxoff，即参数表中该单元的 x 位置加上全局偏移量。

pos[1]（y 坐标）通过 posslw（基于信号时间差重建的 y 位置）加上参数表中的 y 位置和全局偏移量 posyoff 得到。pos[2]（z 坐标）则直接取参数表中的 z 位置加上 poszoff。这样，最终 pos 数组就包含了该探测单元在实验坐标系下的三维空间位置，便于后续的物理分析和可视化。


---

TArtRecoNeutron *reco_neutron = new TArtRecoNeutron();

作用：负责从中子探测器的校准数据中重建中子事件，是更高级别的重建步骤。

- 输入：
  - 主要依赖 TArtCalibNEBULA 校准后产生的 TArtNEBULAPla 对象集合（塑料闪烁体 hit 信息）。
  - 可使用 TArtCalibNEBULAHPC 的输出（TArtNEBULAHPC 对象）作为带电粒子否决信号，提高中子识别纯度。
  - 可能还需其他探测器信息（如束流探测器的时间作为 TOF 参考）。
- 处理：
  - 聚类（Clustering）：将空间和时间上接近的 TArtNEBULAPla hits 组合成潜在的中子簇。
  - 粒子鉴别（PID）：利用电荷信息（dE/dx）和飞行时间（TOF）区分中子和其他粒子。
  - 飞行时间计算：计算中子从靶点（或参考探测器）到 NEBULA 的飞行时间。
  - 能量重建：根据飞行时间和路径长度计算中子动能。
  - 位置重建：确定中子相互作用的位置。
- 输出：重建后的 TArtNeutron 对象（或类似类），包含每个中子的物理属性（能量、时间、位置、角度等），存储于 TArtStoreManager 的 "Neutron" TClonesArray。

## NEBULA 重建流程（示例代码流程）

- 初始化与参数加载
  - 加载必要的库和头文件，设置 include 路径。
  - 获取并加载 `TArtSAMURAIParameters` 参数文件。
  - 打开 RIDF 数据文件。

- 初始化重建类
  - 创建 `TArtCalibNEBULAHPC`、`TArtCalibNEBULA`、`TArtRecoNeutron` 等对象。

- 事件循环处理
  - 对每个事件（如前 10 个事件）进行如下操作：
    - 清空上一次事件的数据（`ClearData()`）。
    - 调用 `ReconstructData()` 进行 hit 和中子重建。
    - 获取并输出 HPC hits、Pla hits 及中子重建结果。
    - 清理原始事件数据，为下一个事件做准备。

- 输出内容
  - 输出每个事件的 HPC hit 数及详细信息（如 ID、Layer、SubLayer、TRaw、TCal）。
  - 输出 Pla hit 数及详细信息（如 ID、Layer、SubLayer、QAveCal、TAveCal、PosCal）。
  - 输出重建出的中子数及其物理量（如 Time、MeVee、PosX、PosY、PosZ）。

- 收尾与资源释放
  - 事件循环结束后，释放所有分配的对象和资源。

> 具体代码实现详见下方示例（已集成于本文件后半部分）。

```

#include <iostream>
void recoNebulaTrack(const char* ridffile = "/home/s057/exp/exp2505_s057/anaroot/users/tbt/ridf/data0073.ridf") {
    gSystem->Load("libXMLParser.so");
    gSystem->Load("libanacore.so");

    // It's good practice to set the include path if your custom classes are not in standard ROOT include paths
    // Adjust this path if your anaroot/users/tbt/src/include is different or if headers are elsewhere
    gSystem->AddIncludePath("-I/home/s057/exp/exp2505_s057/anaroot/users/tbt/src/include");
    gSystem->AddIncludePath("-I/home/s057/exp/exp2505_s057/anaroot/users/tbt/src/sources/Reconstruction/SAMURAI/include");


    TArtSAMURAIParameters *param = TArtSAMURAIParameters::Instance();
    if (!param) {
        std::cerr << "Error: Failed to get TArtSAMURAIParameters instance." << std::endl;
        return;
    }


    param->LoadParameter((char*)"/home/s057/exp/exp2505_s057/anaroot/users/tbt/db/NEBULA.2023_7_6.xml"); 

    TArtEventStore *estore = new TArtEventStore();
    if (!estore->Open(ridffile)) {
        std::cerr << "Error: Cannot open RIDF file: " << ridffile << std::endl;
        delete estore;
        return;
    }

    // Initialize reconstruction classes
    TArtCalibNEBULAHPC *nebulahpc_calib = new TArtCalibNEBULAHPC();
    TArtCalibNEBULA    *nebulapla_calib = new TArtCalibNEBULA(); // Corrected type
    TArtRecoNeutron    *reco_neutron    = new TArtRecoNeutron();

    TArtStoreManager *sman = TArtStoreManager::Instance();

    std::cout << "Starting event loop for NEBULA reconstruction..." << std::endl;
    int neve = 0;
    while (estore->GetNextEvent() && neve < 10) { // Process first 10 events
        std::cout << "========== Event " << neve + 1 << " ==========" << std::endl;

        // 1. Clear data from previous event
        nebulahpc_calib->ClearData();
        nebulapla_calib->ClearData(); 
        reco_neutron->ClearData();

        // 2. Reconstruct current event's data
        // LoadRawData is typically called internally by ReconstructData if fDataLoaded is false.
        // If your framework requires explicit LoadRawData, uncomment the lines below.
        // nebulahpc_calib->LoadRawData(); 
        // nebulapla_calib->LoadData(); // TArtCalibNEBULA uses LoadData()

        nebulahpc_calib->ReconstructData();
        nebulapla_calib->ReconstructData(); 
        reco_neutron->ReconstructData();

        // 3. Output reconstructed results

        // Output HPC hits
        int n_hpc_hits = nebulahpc_calib->GetNumNEBULAHPC();
        std::cout << "  NEBULA HPC Hits: " << n_hpc_hits << std::endl;
        for (int i = 0; i < n_hpc_hits; ++i) {
            TArtNEBULAHPC* hit = nebulahpc_calib->GetNEBULAHPC(i);
            if (hit) {
                std::cout << "    HPC Hit " << i
                          << ": ID=" << hit->GetID()
                          << ", Layer=" << hit->GetLayer()
                          << ", SubLayer=" << hit->GetSubLayer()
                          << ", TRaw=" << hit->GetTRaw()
                          << ", TCal=" << hit->GetTCal()
                          << std::endl;
            }
        }

        // Output Pla hits
        int n_pla_hits = nebulapla_calib->GetNumNEBULAPla();
        std::cout << "  NEBULA Pla Hits: " << n_pla_hits << std::endl;
        for (int i = 0; i < n_pla_hits; ++i) {
            TArtNEBULAPla* pla_hit = nebulapla_calib->GetNEBULAPla(i);
            if (pla_hit) {
                std::cout << "    Pla Hit " << i
                          << ": ID=" << pla_hit->GetID()
                          << ", Layer=" << pla_hit->GetLayer()
                          << ", SubLayer=" << pla_hit->GetSubLayer()
                          << ", QUAveCal=" << pla_hit->GetQAveCal()
                          << ", TAveCal=" << pla_hit->GetTAveCal()
                          << ", PosCal=" << pla_hit->GetPosCal()
                          << std::endl;
            }
        }

        // Output Neutron reconstruction results
        TClonesArray* neutron_array = reco_neutron->GetNeutronArray();
        int n_neutron = neutron_array ? neutron_array->GetEntriesFast() : 0;
        std::cout << "  Reconstructed Neutrons: " << n_neutron << std::endl;
        for (int i = 0; i < n_neutron; ++i) {
            TArtNeutron* neutron = (TArtNeutron*)neutron_array->At(i);
            if (neutron) {
                std::cout << "    Neutron " << i
                          << ": Time=" << neutron->GetTime()
                          << ", MeVee=" << neutron->GetMeVee()
                          << ", PosX=" << neutron->GetPos(0)
                          << ", PosY=" << neutron->GetPos(1)
                          << ", PosZ=" << neutron->GetPos(2)
                          << std::endl;
            }
        }

        estore->ClearData(); // Clear raw event data for the next event
        neve++;
    }

    std::cout << "Finished event loop. Processed " << neve << " events." << std::endl;

    // Clean up
    delete nebulahpc_calib;
    delete nebulapla_calib;
    delete reco_neutron;
    delete estore;
    // TArtStoreManager::Delete(); // If it's a singleton managed this way
    // TArtSAMURAIParameters::Delete(); // If it's a singleton managed this way
}
```

---

## TArtCalibNEBULA 真实校准链 (源码精确流程)

### 1. 原始解码 (`LoadData`, `TArtCalibNEBULA.cc:64-204`)

- 保留 `device == SAMURAI` 且 detector ∈ `{NEBULA1Q, NEBULA1T, NEBULA2Q, NEBULA2T, NEBULA3Q, NEBULA3T, NEBULA4Q, NEBULA4T}` 的数据段。
- 跳过 HPC 通道（`TArtCalibNEBULA.cc:121`）。
- TDC leading (edge==0) → `fTURaw / fTDRaw` + `TUMulti / TDMulti` 自增；trailing (edge==1) → `fTURaw_Trailing / fTDRaw_Trailing`（行 159-173）。
- QDC：U/D 端各 → `fQURaw / fQDRaw`（行 187-202）。

### 2. 校准 (`ReconstructData`, `TArtCalibNEBULA.cc:207-400`)

#### a. TRef 减除

每个 geo 反查参考时间 `tref`（行 500-513）：

```
turaw_subtref = turaw - turaw_ref
tdraw_subtref = tdraw - tdraw_ref
```

#### b. QDC 校准 + 平均

```
quped = quraw - QUPed
qdped = qdraw - QDPed
qucal = quped * QUCal
qdcal = qdped * QDCal
qaveped = sqrt(quped * qdped)
qavecal = QAveCal * sqrt(qucal * qdcal)
```

#### c. TDC 线性校准

```
tucal = turaw_subtref * TUCal + TUOff
tdcal = tdraw_subtref * TDCal + TDOff
```

#### d. Slewing 修正（关键非线性）

如果参数 `TUSlwLog[0] != 0`，使用 **5 项对数多项式**（`TArtCalibNEBULA.cc:291-307`）：

$$
t_u^\text{slw} = t_u^\text{cal} - \sum_{k=0}^{4} c_k\, \big[\log(q_u^\text{ped})\big]^{k+1}
$$

其中 $k=2$ 项被双重加权（实现细节）。否则回退到经典 1/√q 公式（行 309-310）：

$$
t_u^\text{slw} = t_u^\text{cal} - \frac{\text{TUSlw}}{\sqrt{q_u^\text{ped}}}
$$

下端同理。

#### e. 位置重建

```
dtcal = tdcal - tucal
dtslw = tdslw - tuslw

PosCal = dtcal * DTCal + DTOff
PosSlw = dtslw * DTCal + DTOff
```

最终 `pos[]`（`TArtCalibNEBULA.cc:329-340`）：

```cpp
pos[0] = DetPos[0] + posxoff;           // X 由 bar id 直接给出（无每事件随机化）
pos[1] = PosSlw + DetPos[1] + posyoff;  // Y 由 ΔT 重建
pos[2] = DetPos[2] + poszoff;           // Z 由 bar id 给出
```

#### f. QAveCal 光衰减修正 (`TArtCalibNEBULA.cc:339`)

$$
q_\text{ave}^\text{cal} \leftarrow \frac{q_\text{ave}^\text{cal}}{1 + y^2\cdot \text{QAveCalAtt}}
$$

#### g. TOF（飞行时间）

```cpp
TTOFGamma   = taveslw - L / 29.979;   // c, cm/ns → 即 γ 假设
TTOFNeutron = taveslw - L / 20.;      // β = 20/29.979 ≈ 2/3 假设
```

---

## TArtNEBULAFilter 5 种切除算法 (`TArtNEBULAFilter.cc`)

| 切除 | 行号 | 算法 |
|---|---|---|
| `IHitMin(ihitmin_n, ihitmin_v)` | 34-58 | 要求 `{TURaw, TDRaw, QURaw, QDRaw}` 中处在 `(0, 4096]` 的数 ≥ ihitmin（NEUT/VETO 各自阈值） |
| `Threshold(thr_n, thr_v)` | 85-112 | `QAveCal` 阈值，NEUT 与 VETO 分别切 |
| `TOF(tmin, tmax)` | 115-137 | 仅 NEUT，按 `TAveSlw` 时间窗 |
| `Veto(VetoNum)` | 140-196 | 扫所有 `SubLayer==0` veto bar，找最小 layer 的 veto 击中 `VetoHitMin`；若 `VetoHitMin == 1` 全部丢弃；否则丢弃所有 `Layer > VetoHitMin` 的 NEUT |
| `HitMinPos / HitMinTime / HitMinPos2` | 200-406 | 每 layer-group 保留最早位置或最早时间的 1 个 NEUT |

> SubLayer 区分：`SubLayer == 0` → VETO；`SubLayer ∈ {1, 2}` → NEUT 双副层。

---

## TArtRecoNeutron 实际逻辑 (`TArtRecoNeutron.cc:57-125`)

⚠️ **无聚类（no clustering）**。每个通过 Filter 的 `TArtNEBULAPla` 直接产生一个 `TArtNeutron`。聚类逻辑需要用户自己加。

每个 neutron 计算：

```cpp
m = 939.565 MeV          // 中子质量
time = pla->GetTAveSlwT0()
mevee = pla->GetQAveCal()
pos = pla->GetPos()      // (x, y, z) 在 lab
β_i = pos[i] / (time * 29.979 cm/ns)
γ   = 1 / sqrt(1 - β·β)
p_i = m * γ * β_i
E   = sqrt(m^2 + p·p) - m
θ   = atan( sqrt(p_x^2 + p_y·p_z) / p_z )
```

> 注：上式中 `sqrt(p_x^2 + p_y*p_z)` 是源码实际写法（`TArtRecoNeutron.cc:105`），看起来像是 `p_y^2` 的笔误，使用时建议核对版本。

---

## NEBULA 参数库 (db/NEBULA.csv) 列头与配置

`NEBULA.csv` 完整列头（`db/NEBULA.csv:1`）：

```
ID, NAME, FPl, Layer, SubLayer, PosX, PosY, PosZ,
TUCal, TUOff, TUSlw, QUCal, QUPed,
TDCal, TDOff, TDSlw, QDCal, QDPed,
DTCal, DTOff, TAveOff,
tu_det, tu_geo, tu_ch,
td_det, td_geo, td_ch,
qu_geo, qu_ch, qd_geo, qd_ch,
is_tref, is_hpc, id_hpc, Ignore
```

184 模块行。模块分布：

| Layer | SubLayer | 类型 | 数量 | PosZ (mm) |
|---|---|---|---|---|
| 1 | 0 | VETO/参考 | 13 | — |
| 2 | 0 | VETO/参考 | 18 | — |
| 3 | 0 | VETO 前墙 | 14 | 11493.72 / 11508.72 (staggered) |
| 3 | 1 | **NEUT 前墙 SL1** | **30** | **13895.2** |
| 3 | 2 | **NEUT 前墙 SL2** | **30** | **14025.2** (+130) |
| 4 | 0 | VETO 后墙 | 16 | 12339.72 / 12354.72 |
| 4 | 1 | **NEUT 后墙 SL1** | **30** | **14741.2** |
| 4 | 2 | **NEUT 后墙 SL2** | **30** | **14871.2** (+130) |
| 5 | 0 | 簿记 | 3 | — |

**部署计：120 NEUT + ~61 VETO 模块**（与 Geant4 Dayone 模型 120+24 略有差异；真实实验有更多结构性 VETO/参考 bar）。

X 方向跨度 `-1901.8..+1647.8 mm`，pitch 122.4 mm → 30 bar × 122.4 ≈ 3672 mm 宽。

### 典型标定数值范围

- `TUCal, TDCal ≈ 0.0976` ns/ch (TDC LSB)
- `QUCal, QDCal ≈ 0.035–0.048` MeVee/ch
- `QUPed, QDPed ≈ 100–145` ch
- `DTCal = 1`，`DTOff ≈ -20..+30 mm`（光在 bar 中的等效速度编码在 DTCal 里）
- `TUSlw, TDSlw = 0`（当前 CSV 关闭经典 slewing；XML 通过 `<TUSlwLog>` 提供对数多项式系数）

### 磁中心坐标系

`db/NEBULA_Pos_FromMagCenter.csv` 提供相同模块 ID 但 `PosZ ≈ 9784..10374 mm`（磁中心相对 lab 偏移 ≈ 4111 mm 上游）。RK 追踪与 TOF 计算用这套坐标更方便。

### HPC (反符合)

`db/NEBULAHPC.csv` 列头：`NAME, FPl, Layer, SubLayer, PosX, PosY, PosZ, TCal, TOff, tdc_geo, tdc_ch`，共 **16 个 HPC paddle**，置于 `Layer 1 SubLayer 1, Z = 9442.3 mm`，单 TDC 通道（无 Q、无 TU/TD 区分）。在 NEBULA 前面挡带电粒子。

---

## 参考资料

- `../refs/Kondo_NIMA_967_163826_NEBULA_calibration.pdf` — NEBULA 完整标定方法论（Kondo et al., NIM A 967 (2020) 163826）
- `../refs/NEBULA_workshop_Kondo.pdf` — 含光衰减、时间分辨、效率测量
- `../refs/Detector-NEBULA.pdf` — RIKEN SAMURAI 官方 NEBULA 介绍页
- `../refs/Kondo_arXiv_2412.17887_QFS_review.pdf` — 多中子重建综述（含 NEBULA-Plus）
