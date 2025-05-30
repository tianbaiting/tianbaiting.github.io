---
title: pdc相关的anaroot库
tag: 
    - anaroot
---

# 重建与校准相关的C++类库

## TArtCalibPDCHit
- **位置**：anaroot/sources/Reconstruction/SAMURAI/include/TArtCalibPDCHit.hh、TArtCalibPDCHit.cc  
- **作用**：对PDC原始数据（如TDC、QDC等）进行hit级别的校准和重建，生成每根丝的打点（TArtDCHit）。
- **典型用法**：
```cpp
TArtCalibPDCHit *pdchitcalib = new TArtCalibPDCHit();
pdchitcalib->ReconstructData();
TClonesArray *pdc_hit_array = (TClonesArray *)sman->FindDataContainer("SAMURAIPDCHit");
```
## TArtCalibPDCTrack
- **位置**：anaroot/sources/Reconstruction/SAMURAI/include/TArtCalibPDCTrack.hh、TArtCalibPDCTrack.cc  
- **作用**：基于TArtCalibPDCHit的输出，对所有hit进行径迹（track）重建，输出为TArtDCTrack对象。
- **典型用法**：
```cpp
TArtCalibPDCTrack *pdctrackcalib = new TArtCalibPDCTrack();
pdctrackcalib->ReconstructData();
TClonesArray *pdc_trk_array = (TClonesArray *)sman->FindDataContainer("SAMURAIPDCTrack");
```

## TArtDCHit 和 TArtDCTrack
- **TArtDCHit**：保存单个PDC丝的打点信息（位置、TDC、QDC等）。
- **TArtDCTrack**：保存一条重建出来的PDC径迹（位置、角度、chi2等）。

# PDC参数库

## SAMURAIPDC.xml
- **位置**：SAMURAIPDC.xml  
- **作用**：保存PDC每根丝的参数（如geo、ch、wireid、位置等），供重建时查找和校准。

# 宏与脚本

<!-- ## recoPDCTrack.C
- **位置**：users/tbt/tbt_try/recoPDCTrack.C  
- **作用**：典型的PDC重建宏。流程为：加载参数→打开RIDF→PDC hit重建→PDC track重建→输出track参数。
- **功能**：用于批量处理数据文件，输出每个事件的PDC径迹参数。 -->

## RIDF2Tree.C
- **位置**：users/tbt/tbt_try/RIDF2Tree.C  
- **作用**：将RIDF原始数据解码并保存为ROOT TTree格式，便于后续分析。可包含PDC数据分支。

## RecoSAMURAI.C、RecoTrack_wSks.C
- **位置**：Macros/SAMURAI/Analysis/RecoSAMURAI.C、Macros/SAMURAI/RKtrace/RecoTrack_wSks.C  
- **作用**：主要用于SAMURAI谱仪碎片动量和轨迹的重建，默认用FDC/BDC，但可根据需要修改为用PDC track进行外推和动量重建。

## OnlineMonitor.cc
- **位置**：OnlineMonitor.cc  
- **作用**：在线监视宏，支持PDC数据的在线重建和可视化（只要fUsePDC为true）。

# 其它相关

## SAMURAIPDC.xml参数文件
- **注意**：你必须保证所有实际用到的PDC通道（geo/ch）都在此文件中有定义，否则重建时会报错。

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

- **只做PDC重建**：TArtCalibPDCHit、TArtCalibPDCTrack。
- **做全链路物理分析**：可在RecoSAMURAI.C、RecoTrack_wSks.C等宏中，将FDC/BDC部分替换为PDC track，实现用PDC track外推到靶点并重建动量。
- **在线监视**：用OnlineMonitor.s024，设置fUsePDC=true即可。

---

## PDC径迹重建的数据流与算法实现流程

### 数据流简述
- **输入**：PDC的所有 hit（TArtDCHit），每个 hit 有空间位置（x/y/z）、漂移时间等。
- **处理**：在 `TArtCalibPDCTrack::ReconstructData()` 中，先将 hit 分类（按层、方向），然后用几何方法（如加权重心、直线拟合等）重建出径迹的空间参数。
- **输出**：重建出的径迹参数（位置、角度、chi2等）通过 `SetAngle`、`SetPosition` 等接口写入 TArtDCTrack 对象。

### 典型实现流程（以加权重心法为例）

1. **hit 分类**  
   按照丝的方向（u/x/v/y）将所有 hit 分类，分别存入不同的缓冲区。

2. **计算每个方向的加权重心**  
   对每一层的 hit，计算加权平均位置（权重通常为漂移时间差或信号强度）。

3. **拟合直线，得到角度**  
   用加权重心点进行直线拟合，得到斜率（即角度）：  
   - X方向：a = (x2 - x1)/(z2 - z1)
   - Y方向：b = (y2 - y1)/(z2 - z1)  
   或者用多点最小二乘法拟合。

4. **写入 TArtDCTrack**  
   用 `SetAngle(a, 0)` 和 `SetAngle(b, 1)` 把拟合得到的角度存入 TArtDCTrack 的 ca[0] 和 ca[1]。

5. **后续访问**  
   通过 `GetAngle(0)` 和 `GetAngle(1)` 读取 X、Y 方向的角度。


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




