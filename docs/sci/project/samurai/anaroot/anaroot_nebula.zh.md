重建nebula需要这些文件：

参数 XML 文件（如 NEBULA.20250625.xml）

TArtCalibNEBULAHPC.hh/.cc

TArtCalibNEBULA.hh/.cc

TArtRecoNeutron.hh/.cc

TArtSAMURAIParameters.hh/.cc

相关数据对象类TArtNEBULAHPC、TArtNEBULAPla、TArtNeutron 


** TArtCalibNEBULAHPC

TArtCalibNEBULAHPC *nebulahpc_calib = new TArtCalibNEBULAHPC();

**作用**：负责校准 NEBULA 高压正比计数管（HPC - High Pressure Chamber）的数据。HPC 主要作为中子探测的否决探测器（veto detector），用于区分中子和带电粒子（如伽马射线转换产生的电子或质子）。

- **输入**：从 TArtEventStore 读取 HPC 探测器的原始数据（如 TDC 时间信息）。
- **处理**：
  - 应用时间校准参数（由 TArtSAMURAIParameters 管理）。
  - 将原始 TDC 值转换为物理时间。
  - 进行基本的 hit 判断。
- **输出**：重建后的 TArtNEBULAHPC 对象，包含每个 HPC hit 的校准后信息（如时间、探测器 ID 等），存储于 TArtStoreManager 的 "NEBULAHPC" TClonesArray。




---

** TArtCalibNEBULA 

TArtCalibNEBULA *nebulapla_calib = new TArtCalibNEBULA();

**作用**：负责校准 NEBULA 塑料闪烁体（Pla - Plastic Scintillator）的数据，是 NEBULA 中子探测器的主要组成部分。

- **输入**：从 TArtEventStore 读取塑料闪烁体两端 PMT 的原始数据（TDC 时间和 QDC 电荷）。
- **处理**：
  - 应用时间和电荷校准参数。
  - 计算每个 hit 的平均时间、时间差（用于位置重建）、平均电荷。
  - 计算击中位置（position）。
  - 将校准后的时间和电荷转换为物理单位（ns, MeVee）。
- **输出**：重建后的 TArtNEBULAPla 对象，包含每个 hit 的详细校准信息（ID, Layer, SubLayer, QUAveCal, TAveCal, PosCal 等），存储于 TArtStoreManager 的 "NEBULAPla" TClonesArray。

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

**作用**：负责从中子探测器的校准数据中重建中子事件，是更高级别的重建步骤。

- **输入**：
  - 主要依赖 TArtCalibNEBULA 校准后产生的 TArtNEBULAPla 对象集合（塑料闪烁体 hit 信息）。
  - 可使用 TArtCalibNEBULAHPC 的输出（TArtNEBULAHPC 对象）作为带电粒子否决信号，提高中子识别纯度。
  - 可能还需其他探测器信息（如束流探测器的时间作为 TOF 参考）。
- **处理**：
  - 聚类（Clustering）：将空间和时间上接近的 TArtNEBULAPla hits 组合成潜在的中子簇。
  - 粒子鉴别（PID）：利用电荷信息（dE/dx）和飞行时间（TOF）区分中子和其他粒子。
  - 飞行时间计算：计算中子从靶点（或参考探测器）到 NEBULA 的飞行时间。
  - 能量重建：根据飞行时间和路径长度计算中子动能。
  - 位置重建：确定中子相互作用的位置。
- **输出**：重建后的 TArtNeutron 对象（或类似类），包含每个中子的物理属性（能量、时间、位置、角度等），存储于 TArtStoreManager 的 "Neutron" TClonesArray。

## NEBULA 重建流程（示例代码流程）

- **初始化与参数加载**
  - 加载必要的库和头文件，设置 include 路径。
  - 获取并加载 `TArtSAMURAIParameters` 参数文件。
  - 打开 RIDF 数据文件。

- **初始化重建类**
  - 创建 `TArtCalibNEBULAHPC`、`TArtCalibNEBULA`、`TArtRecoNeutron` 等对象。

- **事件循环处理**
  - 对每个事件（如前 10 个事件）进行如下操作：
    - 清空上一次事件的数据（`ClearData()`）。
    - 调用 `ReconstructData()` 进行 hit 和中子重建。
    - 获取并输出 HPC hits、Pla hits 及中子重建结果。
    - 清理原始事件数据，为下一个事件做准备。

- **输出内容**
  - 输出每个事件的 HPC hit 数及详细信息（如 ID、Layer、SubLayer、TRaw、TCal）。
  - 输出 Pla hit 数及详细信息（如 ID、Layer、SubLayer、QAveCal、TAveCal、PosCal）。
  - 输出重建出的中子数及其物理量（如 Time、MeVee、PosX、PosY、PosZ）。

- **收尾与资源释放**
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
```