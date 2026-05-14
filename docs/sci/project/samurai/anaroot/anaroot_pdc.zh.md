---
title: anaroot pdcS
tag: 
    - anaroot
---

# 重建与校准相关的C++类库

## TArtCalibPDCHit
- 位置：anaroot/sources/Reconstruction/SAMURAI/include/TArtCalibPDCHit.hh、TArtCalibPDCHit.cc  
- 作用：对PDC原始数据（如TDC、QDC等）进行hit级别的校准和重建，生成每根丝的打点（TArtDCHit）。
- 典型用法：
```cpp
TArtCalibPDCHit *pdchitcalib = new TArtCalibPDCHit();
pdchitcalib->ReconstructData();
TClonesArray *pdc_hit_array = (TClonesArray *)sman->FindDataContainer("SAMURAIPDCHit");
```
## TArtCalibPDCTrack
- 位置：anaroot/sources/Reconstruction/SAMURAI/include/TArtCalibPDCTrack.hh、TArtCalibPDCTrack.cc  
- 作用：基于TArtCalibPDCHit的输出，对所有hit进行径迹（track）重建，输出为TArtDCTrack对象。
- 典型用法：
```cpp
TArtCalibPDCTrack *pdctrackcalib = new TArtCalibPDCTrack();
pdctrackcalib->ReconstructData();
TClonesArray *pdc_trk_array = (TClonesArray *)sman->FindDataContainer("SAMURAIPDCTrack");
```

## TArtDCHit 和 TArtDCTrack
- TArtDCHit：保存单个PDC丝的打点信息（位置、TDC、QDC等）。
- TArtDCTrack：保存一条重建出来的PDC径迹（位置、角度、chi2等）。

# PDC参数库

## SAMURAIPDC.xml
- 位置：SAMURAIPDC.xml  
- 作用：保存PDC每根丝的参数（如geo、ch、wireid、位置等），供重建时查找和校准。


- ID：该丝的唯一编号（通常与 wireid 一致）。
- NAME：该丝的名称，格式如 `PDC_0_0`，表示第 0 层第 0 根丝。
- FPL：焦面编号（Focal Plane），如 13 表示 F13。
- layer：所在的层号（如 0、1、2 等）。
- id_plane：平面编号（plane id），如 81、82、83 等。
- anodedir：阳极丝方向（U/X/V），表示该层的测量方向。
- wireid：该层内的丝编号。
- wirepos：该丝在本层的物理位置（单位通常为 mm）。
- wirez：该丝在 Z 方向的位置（单位通常为 mm）。
- tzero_offset：时间零点修正（一般为 0）。
- det：探测器编号（如 37）。
- geo：电子学几何编号（如 0、1、2 等）。
- ch：电子学通道号（channel），用于数据解码。
  
  
# 宏与脚本

<!-- ## recoPDCTrack.C
- 位置：users/tbt/tbt_try/recoPDCTrack.C  
- 作用：典型的PDC重建宏。流程为：加载参数→打开RIDF→PDC hit重建→PDC track重建→输出track参数。
- 功能：用于批量处理数据文件，输出每个事件的PDC径迹参数。 -->

## RIDF2Tree.C
- 位置：users/tbt/tbt_try/RIDF2Tree.C  
- 作用：将RIDF原始数据解码并保存为ROOT TTree格式，便于后续分析。可包含PDC数据分支。

## RecoSAMURAI.C、RecoTrack_wSks.C
- 位置：Macros/SAMURAI/Analysis/RecoSAMURAI.C、Macros/SAMURAI/RKtrace/RecoTrack_wSks.C  
- 作用：主要用于SAMURAI谱仪碎片动量和轨迹的重建，默认用FDC/BDC，但可根据需要修改为用PDC track进行外推和动量重建。

## OnlineMonitor.cc
- 位置：OnlineMonitor.cc  
- 作用：在线监视宏，支持PDC数据的在线重建和可视化（只要fUsePDC为true）。

# 其它相关

## SAMURAIPDC.xml参数文件
- 注意：你必须保证所有实际用到的PDC通道（geo/ch）都在此文件中有定义，否则重建时会报错。

# 总结与建议

| 名称                  | 类型     | 主要功能/用途                                   |
|-----------------------|----------|------------------------------------------------|
| TArtCalibPDCHit       | 类       | PDC hit级别重建（原始信号→打点）               |
| TArtCalibPDCTrack     | 类       | PDC track重建（打点→径迹）                     |
| TArtDCHit/TArtDCTrack | 类       | 存储单个打点/径迹信息                           |
| SAMURAIPDC.xml        | 参数文件 | PDC每根丝的参数库                               |
| transPDCData.C        | 宏       | PDC原始数据转可读文本                           |
| RIDF2Tree.C           | 宏       | RIDF转ROOT TTree，含PDC分支                     |
| RecoSAMURAI.C         | 宏       | SAMURAI碎片动量/轨迹重建（可用PDC track）       |
| RecoTrack_wSks.C      | 宏       | Runge-Kutta追踪重建（可用PDC track）            |
| OnlineMonitor.s024    | 宏       | 在线监视，支持PDC数据的重建和可视化             |

## 如何选择和使用？

- 只做PDC重建：TArtCalibPDCHit、TArtCalibPDCTrack。
- 做全链路物理分析：可在RecoSAMURAI.C、RecoTrack_wSks.C等宏中，将FDC/BDC部分替换为PDC track，实现用PDC track外推到靶点并重建动量。
- 在线监视：用OnlineMonitor.s024，设置fUsePDC=true即可。

---

## PDC径迹重建的数据流与算法实现流程

### 数据流简述
- 输入：PDC的所有 hit（TArtDCHit），每个 hit 有空间位置（x/y/z）、漂移时间等。
- 处理：在 `TArtCalibPDCTrack::ReconstructData()` 中，先将 hit 按层/方向分类，然后用 **TMinuit/MIGRAD 4-参数最小二乘** 拟合直线径迹（详见下方"真实算法"小节，并非加权重心法）。
- 输出：重建出的径迹参数（位置、角度、chi2等）通过 `SetAngle`、`SetPosition` 等接口写入 TArtDCTrack 对象。

### TArtCalibPDCHit 真实实现 (`TArtCalibPDCHit.cc:24-76`)

- 读取 RIDF 中 detector tag = `PDC` 的所有段。
- 对每条 TDC 数据 (`ch ≤ 63`, 仅 `edge ∈ {0, 1}`) 通过 `TArtRIDFMap(fpl, detector, geo, ch)` 反查参数 `TArtDCHitPara`，填出每根丝一条 `TArtDCHit`：
  - `edge == 0` → leading edge → `fTDC`
  - `edge == 1` → trailing edge → `fTrailTDC`
- `TArtDCHit` 字段 (`TArtDCHit.hh:5-86`)：`fTDC, fTrailTDC, fLayer, fWireID, fAnodeDir, fWirePos, fWireZ, fPosition` 等。

### TArtCalibPDCTrack 真实算法（4-参数 MIGRAD 拟合）

源码位置：`TArtCalibPDCTrack.cc:9-336`。

**1. 层几何硬编码** (`TArtCalibPDCTrack.cc:36-43`)：

```
PDC1 = U, X, V
PDC2 = U, X, V
nlayer_y = 0     // 没有独立的 Y 层
```

**2. 拟合参数与边界** (`TArtCalibPDCTrack.cc:122-133`)：

| 参数 | 含义 | 边界 |
|---|---|---|
| `x0` | 径迹在 z=0 处的 x 截距 | ±1000 mm |
| `y0` | 径迹在 z=0 处的 y 截距 | ± 800 mm |
| `k_xz` | dx/dz | ±100 |
| `k_yz` | dy/dz | ±100 |

调用 `TMinuit::mnexcm("MIGRAD", ...)` 做 χ² 极小化。

**3. χ² 计算** (`Chi2Calculation`, `TArtCalibPDCTrack.cc:224-336`)：

- 每层把所有有效 hit (`TDC>0 && TrailTDC>0`) 按 **TOT 加权丝心** 聚合：

$$
w_i = |\,\text{TDC}_i - \text{TrailTDC}_i\,|,\qquad
\bar{x}_\text{layer} = \frac{\sum_i w_i\,x_i}{\sum_i w_i}
$$

- 对 U 层：先把模型预测点 (x_pred, y_pred, z) 投影到 U 方向：$U_\text{pred} = (x + y)/\sqrt{2}$；
- 对 V 层：$V_\text{pred} = (x - y)/\sqrt{2}$；
- 对 X 层：直接用 x；
- 残差平方累加给出 χ²。

**4. 写入 `TArtDCTrack`** (`TArtCalibPDCTrack.cc:151-158`)：

```cpp
trk->SetPosition(x0, 0);
trk->SetPosition(y0, 1);
trk->SetAngle(atan(k_xz), 0);
trk->SetAngle(atan(k_yz), 1);
trk->SetNDF(2);
trk->SetNumHitLayer(nhit_total);
trk->SetChi2(chi2_sum);
```

**5. 注意：当前版本无 χ²/ndf 切除**  
源码中 `if (chi2 < 10000)` 行被注释掉（`TArtCalibPDCTrack.cc:148, 162-168`），意味着重建产物里会包含质量很差的径迹，下游分析需自行加 `Chi2/NDF` 切。

### 后续访问

```cpp
TArtDCTrack* trk = (TArtDCTrack*)pdc_trk_array->At(i);
double x  = trk->GetPosition(0);   // x0 at z=0
double y  = trk->GetPosition(1);   // y0 at z=0
double ax = trk->GetAngle(0);      // atan(dx/dz)
double ay = trk->GetAngle(1);      // atan(dy/dz)
double chi2 = trk->GetChi2();
int    nhit = trk->GetNumHitLayer();
```

---

## SAMURAIPDC.xml / SAMURAIPDC_fit.csv 参数库详解

CSV 列头 (`SAMURAIPDC_fit.csv:1`)：

```
ID, NAME, FPL, layer, id_plane, anodedir, wireid, wirepos, wirez, tzero_offset, det, geo, ch
```

总 ≈ 816 条丝记录，全部 `FPL=13`（F13 焦面），`det=37`。

层结构表：

| layer | anodedir | id_plane | wirez (mm) | wire 起始位置 | geo 起始 | 备注 |
|---|---|---|---|---|---|---|
| 0 | U | 81 | 40 | -822 mm | 0 | PDC1 第 1 层 |
| 1 | X | 82 | 24 | -822 mm | 2 | PDC1 第 2 层 |
| 2 | V | 83 | 8 | +822 mm (倒序) | 4 | PDC1 第 3 层 |
| 3 | U | 84 | -576 | -822 mm | 8 | PDC2 第 1 层 |
| 4 | X | 85 | -592 | -822 mm | 10 | PDC2 第 2 层 |
| 5 | V | 86 | -608 | +822 mm (倒序) | 13 | PDC2 第 3 层 |

- 每层 **136 根丝**，**间距 12 mm**；wirepos 范围 `-822..+822 mm`。
- **PDC1 中心 z ≈ 24 mm，PDC2 中心 z ≈ -592 mm，间距约 616 mm**（这是焦面本地坐标，不是实验室坐标；实验室坐标由谱仪几何参数另行加上 PDC 中心位置与旋转）。
- V 层把 `wireid` 从 0 → 135 对应到 `wirepos` 从 `+822` → `-798`，即倒序排列。

示例行：

```
1,PDC_0_0,13,0,81,U,0,-822,40,0,37,0,0
2,PDC_0_1,13,0,81,U,1,-810,40,0,37,0,1
...
137,PDC_1_0,13,1,82,X,0,-822,24,0,37,2,9
```

> 重要：`SAMURAIPDC.xml` 文件必须把所有实际用到的 (geo, ch) 都列全，否则 `TArtRIDFMap` 反查为空，hit 重建报错。

---

## PDC track 到靶点动量重建

⚠️ **anaroot 主线不直接用 PDC 做靶点重建**。`Macros/SAMURAI/RKtrace/RecoTrack_wSks.C` 中 `TArtRecoFragment::ReconstructData()` 使用 **FDC1 + FDC2**（不是 PDC）的径迹喂入 SKS-derived Runge-Kutta tracer，反推 `PrimaryPosition()` 作为靶顶点。

PDC 的 target 外推在两条独立路线：

1. **用户脚本**：`anaroot/tbt_try/recoPDCdataTosamurai.C` 等
2. **simulator 端 RK + NN**：`smsimulator5.5/libs/analysis_pdc_reco/`（详见 [smsimulator PDC reco](../smsimulator/PDC.md) 与 `bin/reconstruct_target_momentum`）

两条路线都需读取同一份 `SAMURAIPDC.xml` 以保持丝几何一致。


PDC 只是一个多丝漂移室，只能测量粒子的空间轨迹（x、y、a、b），不能单独测出动量。
动量的获得需要结合磁场信息和谱仪的传输矩阵（或磁场追踪算法），通常要用到碎片在多个位置的径迹（如FDC1、FDC2、BDC、PDC等）和磁场参数。

代码示例：
```
#include <sys/stat.h>
#include <string>
#include <set>
#include <vector>
#include <iostream>
void recoPDCTrack(const char* ridffile = "/home/s057/exp/exp2505_s057/anaroot/users/tbt/ridf/data0074.ridf") {

  gSystem->Load("libXMLParser.so"); // 先加载XML解析库
    gSystem->Load("libanacore.so");
    // 加载PDC参数
    TArtSAMURAIParameters *samuraiparameters = TArtSAMURAIParameters::Instance();
    samuraiparameters->LoadParameter("../db/SAMURAIPDC.xml");

    // 打开RIDF文件
    TArtEventStore *estore = new TArtEventStore();
    estore->Open(ridffile);

    // 初始化PDC hit和track重建
    TArtCalibPDCHit *pdchitcalib = new TArtCalibPDCHit();
    TArtCalibPDCTrack *pdctrackcalib = new TArtCalibPDCTrack();

    TArtStoreManager *sman = TArtStoreManager::Instance();
    TClonesArray *pdc_hit_array = (TClonesArray *)sman->FindDataContainer("SAMURAIPDCHit");
    TClonesArray *pdc_trk_array = (TClonesArray *)sman->FindDataContainer("SAMURAIPDCTrack");

    // 获取输入文件名
    std::string inputFileName = std::string(ridffile);
    size_t pos = inputFileName.find_last_of('/');
    std::string fileName = (pos != std::string::npos) ? inputFileName.substr(pos + 1) : inputFileName;

    // 创建输出ROOT文件和TTree
    const char* outputDir = "./output";
    std::string outroot = std::string(outputDir) + "/" + fileName + "_pdc.root";
    std::string outpng = std::string(outputDir) + "/" + fileName + "_pdc_track_xy.png";

    TFile *fout = new TFile(outroot.c_str(), "RECREATE");
    TTree *tree = new TTree("pdctree", "PDC Track Tree");
    int event, trackid, ndf, nhit;
    double x, y, ax, ay, chi2;
    tree->Branch("event", &event, "event/I");
    tree->Branch("trackid", &trackid, "trackid/I");
    tree->Branch("x", &x, "x/D");
    tree->Branch("y", &y, "y/D");
    tree->Branch("ax", &ax, "ax/D");
    tree->Branch("ay", &ay, "ay/D");
    tree->Branch("chi2", &chi2, "chi2/D");
    tree->Branch("ndf", &ndf, "ndf/I");
    tree->Branch("nhit", &nhit, "nhit/I");

    int neve = 0;
    while (estore->GetNextEvent() && neve < 1000) {
        pdchitcalib->ClearData();
        pdctrackcalib->ClearData();
        pdchitcalib->ReconstructData();
        pdctrackcalib->ReconstructData();

        int ntrk = pdc_trk_array->GetEntries();
        for (int i = 0; i < ntrk; ++i) {
            TArtDCTrack *trk = (TArtDCTrack*)pdc_trk_array->At(i);
            x = trk->GetPosition(0);
            y = trk->GetPosition(1);
            ax = trk->GetAngle(0);
            ay = trk->GetAngle(1);
            chi2 = trk->GetChi2();
            ndf = trk->GetNDF();
            nhit = trk->GetNumHitLayer();
            event = neve;
            trackid = i;
            tree->Fill();
            std::cout << "Event: " << neve << ", Track ID: " << i 
                      << ", X: " << x << ", Y: " << y 
                      << ", Ax: " << ax << ", Ay: " << ay 
                      << ", Chi2: " << chi2 
                      << ", NDF: " << ndf 
                      << ", NHits: " << nhit 
                      << std::endl;
        }
        neve++;
    }
    tree->Write();

    TCanvas *c1 = new TCanvas("c1", "PDC Track X-Y", 800, 600);
    tree->Draw("y:x>>hxy", "", "COLZ");
    c1->SaveAs(outpng.c_str());
    delete c1;
    std::cout << "Output ROOT file: " << outroot << std::endl;
    std::cout << "Output PNG file: " << outpng << std::endl;
    
    fout->Close();
    delete pdchitcalib;
    delete pdctrackcalib;
    delete estore;
}

```




