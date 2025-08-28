## NEBULA 相关库

### 1. 参数管理 (Parameter Management)

#### TNEBULASimParameter
-   **文件**: `TNEBULASimParameter.hh / .cc`
-   **功能**: 存储 NEBULA 的所有参数，包括探测器数量、类型、几何参数等，供仿真和数据转换模块调用。

#### NEBULASimParameterReader
-   **文件**: `NEBULASimParameterReader.hh / .cc`
-   **功能**: 负责读取 NEBULA 的参数文件（如 `NEBULA_Dayone.csv`、`NEBULA_Detectors_Dayone.csv`），并将参数加载到仿真环境中。包括探测器数量、位置、尺寸等信息。

#### 相关数据文件
-   **文件**: `NEBULA_Dayone.csv` / `NEBULA_Detectors_Dayone.csv`
-   **功能**: 这些文件包含 NEBULA 阵列的具体参数，如每个探测器的位置、尺寸、编号等，仿真时会被 `NEBULASimParameterReader` 读取。

### 2. 几何构建 (Geometry Construction)

#### NEBULAConstruction & NEBULAConstructionMessenger
-   **文件**: `NEBULAConstruction.hh / .cc`
-   **功能**: 定义 NEBULA 中子探测器的几何结构，包括探测器阵列的尺寸、位置、材料等。负责在 Geant4 仿真中构建 NEBULA 的物理模型。
-   **文件**: `NEBULAConstructionMessenger.hh / .cc`
-   **功能**: 提供命令接口，允许用户通过宏文件或命令行动态设置 NEBULA 的参数（如阵列参数文件、探测器参数文件等）。

### 3. 仿真核心 (Simulation Core)

#### NEBULASD
-   **文件**: `NEBULASD.hh / .cc`
-   **功能**: 定义 NEBULA 探测器的敏感体（Sensitive Detector），用于在仿真过程中记录粒子在 NEBULA 探测器中的能量沉积、位置、时间等信息。

### 4. 数据处理 (Data Handling)

#### NEBULASimDataInitializer
-   **文件**: `NEBULASimDataInitializer.hh / .cc`
-   **功能**: 初始化 NEBULA 仿真数据结构，为每个探测器分配数据存储空间，准备后续的数据采集和分析。

#### NEBULASimDataConverter_TArtNEBULAPla
-   **文件**: `NEBULASimDataConverter_TArtNEBULAPla.hh / .cc`
-   **功能**: 将仿真过程中产生的原始数据（如能量沉积、探测器响应等）转换为实验分析所需的数据格式（如 TArtNEBULAPla），并写入 ROOT 文件。实现了能量转换、分辨率处理等物理模型。

## Geant4 中的 NEBULA 输出

### 1. 仿真输出信息
-   **能量沉积 (Energy Deposit)**：每个中子探测器模块（NEBULA单元）记录粒子（主要是中子）在探测器中的能量沉积。
-   **探测器响应 (Detector Response)**：根据能量沉积、探测器分辨率等物理模型，模拟实际实验中探测器的信号输出（如光电倍增管响应）。
-   **位置与时间信息 (Position and Time Information)**：记录粒子在探测器中的击中位置、入射时间等，用于后续飞行时间（TOF）、空间分布等分析。
-   **粒子类型与编号 (Particle Type and ID)**：区分不同粒子（如中子、伪中子、伪γ等）及其对应的探测器编号，便于事件筛选和物理分析。

### 2. 生成的 ROOT 文件
-   **数据结构**：NEBULA 的仿真数据会被转换为 ROOT 文件，通常包含一个或多个 TTree（如 `NEBULAPla`），每个条目对应一次事件或一次探测器响应。
-   **内容举例**：
    -   每个事件下，`NEBULAPla` 分支存储所有被击中的 NEBULA 探测器单元的响应数据（如能量、位置、时间等）。
    -   其他分支可能包含全局事件信息、粒子初始参数等。
-   **用途**：
    -   **实验数据对比**：仿真输出的 ROOT 文件结构和实验数据一致，可直接用于与真实实验数据进行对比分析。
    -   **物理分析**：可用 ROOT 脚本或分析框架对仿真数据进行统计、绘图、效率计算、能谱分析等。
    -   **探测器性能评估**：分析探测器的响应分布、分辨率、探测效率等，为实验设计和数据解释提供依据。
    -   **事件筛选**：可根据粒子类型、能量、位置等条件筛选感兴趣的物理事件。

### 3. 相关代码模块
-   **`NEBULASimDataConverter_TArtNEBULAPla`**：负责将仿真数据转换为 `TArtNEBULAPla` 格式，并写入 ROOT 文件。
-   **`NEBULASD`**：实现敏感体，负责在仿真过程中采集粒子击中信息。
-   **`NEBULASimParameterReader`**：读取探测器参数，决定输出数据结构和内容。

## TArtNEBULAPla 数据结构

`TArtNEBULAPla` 是 ANAROOT 框架中用于描述 NEBULA 单个探测器模块（Plastic Scintillator）的数据结构类。它的主要作用是存储和管理每个 NEBULA 塑料条的实验或仿真响应信息，便于后续物理分析和实验数据处理。

### 1. 主要成员变量（常见字段）
-   **探测器编号（ID）**: 唯一标识每个 NEBULA 塑料条的编号，便于定位和区分。
-   **能量（Energy）**: 记录粒子在该塑料条中的能量沉积（单位通常为 MeV），用于能谱分析和事件筛选。
-   **时间（Time）**: 记录粒子击中该塑料条的时间信息（如飞行时间 TOF），用于时间分辨和事件重建。
-   **位置（Position）**: 塑料条在阵列中的空间坐标，便于空间分布分析和几何重建。
-   **粒子类型（ParticleID）**: 记录击中该塑料条的粒子类型（如中子、γ、重离子等），用于物理过程区分。
-   **分辨率/信号处理相关变量**: 可能包含模拟或实验中的分辨率、信号幅度、光电倍增管响应等信息。

### 2. TArtNEBULAPla.h
```cpp
#ifndef _TARTNEBULAPLA_H_
#define _TARTNEBULAPLA_H_

#include "TString.h"

#include <iostream>

#include "TArtDataObject.hh"

class TArtNEBULAPla : public TArtDataObject
{
public:
  TArtNEBULAPla()
    : TArtDataObject(),
      fLayer(-1), fSubLayer(-1), fHit(0),
      fQURaw(-1), fQDRaw(-1), fQUCal(-1), fQDCal(-1),
      fQAvePed(-1), fQAveCal(-1), fLogQPed(0), fLogQCal(0),
      fIvSqrtQUPed(-1), fIvSqrtQDPed(-1), fIvSqrtQAvePed(-1), 
      fTURaw(-1), fTDRaw(-1), fTURaw_Trailing(-1), fTDRaw_Trailing(-1), fTURaw_Width(-1), fTDRaw_Width(-1), 
      fTURawRef(-1), fTDRawRef(-1), fTURaw_SubTRef(-99999), fTDRaw_SubTRef(-99999), 
      fTUMulti(0), fTDMulti(0), 
      fTUCal(-1), fTDCal(-1), fTUCal_Width(-1), fTDCal_Width(-1), fTUSlw(-1), fTDSlw(-1),
      fDTRaw(-1), fDTCal(-1), fDTSlw(-1), fTAveRaw(-1), fTAveCal(-1), fTAveSlw(-1),
      fTUCalT0(-1), fTDCalT0(-1), fTUSlwT0(-1), fTDSlwT0(-1), fTAveCalT0(-1), fTAveSlwT0(-1),
      fTTOFGamma(-90000), fTTOFNeutron(-90000),
      fPosCal(0), fPosSlw(0), fFlightLength(-1), fFlightAngle(-1)
  {
    for(Int_t i=0; i<3; ++i) fDetPos[i] = -90000;
    for(Int_t i=0; i<3; ++i) fPos[i] = -90000;
  }
  virtual ~TArtNEBULAPla(){;}

  virtual void SetLayer(Int_t val){fLayer = val;}
  virtual void SetSubLayer(Int_t val){fSubLayer = val;}
  virtual void SetDetPos(const Double_t* val){for(Int_t i=0; i<3; ++i){fDetPos[i] = val[i];}}
  virtual void SetDetPos(Double_t val, Int_t i){fDetPos[i] = val;}
  virtual void SetHit(Int_t val){fHit = val;}

  virtual void SetQURaw(Int_t    val){fQURaw = val;}
  virtual void SetQDRaw(Int_t    val){fQDRaw = val;}
  virtual void SetQUPed(Double_t val){fQUPed = val;}
  virtual void SetQDPed(Double_t val){fQDPed = val;}
  virtual void SetQUCal(Double_t val){fQUCal = val;}
  virtual void SetQDCal(Double_t val){fQDCal = val;}
  virtual void SetQAvePed(Double_t val){fQAvePed = val;}
  virtual void SetQAveCal(Double_t val){fQAveCal = val;}
  virtual void SetLogQPed(Double_t val){fLogQPed = val;}
  virtual void SetLogQCal(Double_t val){fLogQCal = val;}
  virtual void SetIvSqrtQUPed(Double_t val){fIvSqrtQUPed = val;}
  virtual void SetIvSqrtQDPed(Double_t val){fIvSqrtQDPed = val;}
  virtual void SetIvSqrtQAvePed(Double_t val){fIvSqrtQAvePed = val;}

  virtual void SetTURaw(Int_t    val){fTURaw = val;}
  virtual void SetTDRaw(Int_t    val){fTDRaw = val;}
  virtual void SetTURaw_Trailing(Int_t    val){fTURaw_Trailing = val;}
  virtual void SetTDRaw_Trailing(Int_t    val){fTDRaw_Trailing = val;}
  virtual void SetTURaw_Width(Int_t    val){fTURaw_Width = val;}
  virtual void SetTDRaw_Width(Int_t    val){fTDRaw_Width = val;}
  virtual void SetTURawRef(Int_t val){fTURawRef = val;}
  virtual void SetTDRawRef(Int_t val){fTDRawRef = val;}
  virtual void SetTURaw_SubTRef(Int_t val){fTURaw_SubTRef = val;}
  virtual void SetTDRaw_SubTRef(Int_t val){fTDRaw_SubTRef = val;}
  virtual void SetTUMulti(Int_t val){fTUMulti = val;}  
  virtual void SetTDMulti(Int_t val){fTDMulti = val;}  
  virtual void SetTUCal(Double_t val){fTUCal = val;}
  virtual void SetTDCal(Double_t val){fTDCal = val;}
  virtual void SetTUCal_Width(Double_t val){fTUCal_Width = val;}
  virtual void SetTDCal_Width(Double_t val){fTDCal_Width = val;}
  virtual void SetTUSlw(Double_t val){fTUSlw = val;}
  virtual void SetTDSlw(Double_t val){fTDSlw = val;}
  virtual void SetDTRaw(Double_t val){fDTRaw = val;}
  virtual void SetDTCal(Double_t val){fDTCal = val;}
  virtual void SetDTSlw(Double_t val){fDTSlw = val;}
  virtual void SetTAveRaw(Double_t val){fTAveRaw = val;}
  virtual void SetTAveCal(Double_t val){fTAveCal = val;}
  virtual void SetTAveSlw(Double_t val){fTAveSlw = val;}
  virtual void SetTUCalT0(Double_t val){fTUCalT0 = val;}
  virtual void SetTDCalT0(Double_t val){fTDCalT0 = val;}
  virtual void SetTUSlwT0(Double_t val){fTUSlwT0 = val;}
  virtual void SetTDSlwT0(Double_t val){fTDSlwT0 = val;}
  virtual void SetTAveCalT0(Double_t val){fTAveCalT0 = val;}
  virtual void SetTAveSlwT0(Double_t val){fTAveSlwT0 = val;}
  virtual void SetTTOFGamma(Double_t val){fTTOFGamma = val;}
  virtual void SetTTOFNeutron(Double_t val){fTTOFNeutron = val;}

  virtual void SetPosCal(Double_t val){fPosCal = val;}
  virtual void SetPosSlw(Double_t val){fPosSlw = val;}
  virtual void SetPos(const Double_t* val){for(Int_t i=0; i<3; ++i) fPos[i] = val[i];}
  virtual void SetPos(Double_t val, Int_t i){fPos[i] = val;}
  virtual void SetFlightLength(Double_t val){fFlightLength = val;}
  virtual void SetFlightAngle(Double_t val){fFlightAngle = val;}

  virtual Int_t GetLayer() const {return fLayer;}
  virtual Int_t GetSubLayer() const {return fSubLayer;}
  virtual const Double_t* GetDetPos() const {return fDetPos;}
  virtual Double_t GetDetPos(Int_t i) const {return fDetPos[i];}
  virtual Int_t GetHit() const {return fHit;}

  virtual Int_t    GetQURaw() const {return fQURaw;}
  virtual Int_t    GetQDRaw() const {return fQDRaw;}
  virtual Double_t GetQUPed() const {return fQUPed;}
  virtual Double_t GetQDPed() const {return fQDPed;}
  virtual Double_t GetQUCal() const {return fQUCal;}
  virtual Double_t GetQDCal() const {return fQDCal;}
  virtual Double_t GetQAvePed() const {return fQAvePed;}
  virtual Double_t GetQAveCal() const {return fQAveCal;}
  virtual Double_t GetLogQPed() const {return fLogQPed;}
  virtual Double_t GetLogQCal() const {return fLogQCal;}
  virtual Double_t GetIvSqrtQUPed() const {return fIvSqrtQUPed;}
  virtual Double_t GetIvSqrtQDPed() const {return fIvSqrtQDPed;}
  virtual Double_t GetIvSqrtQAvePed() const {return fIvSqrtQAvePed;}

  virtual Int_t    GetTURaw() const {return fTURaw;}
  virtual Int_t    GetTDRaw() const {return fTDRaw;}
  virtual Int_t    GetTURaw_Trailing() const {return fTURaw_Trailing;}
  virtual Int_t    GetTDRaw_Trailing() const {return fTDRaw_Trailing;}
  virtual Int_t    GetTURaw_Width() const {return fTURaw_Width;}
  virtual Int_t    GetTDRaw_Width() const {return fTDRaw_Width;}
  virtual Int_t    GetTURawRef() const {return fTURawRef;}
  virtual Int_t    GetTDRawRef() const {return fTDRawRef;}
  virtual Int_t    GetTURaw_SubTRef() const {return fTURaw_SubTRef;}
  virtual Int_t    GetTDRaw_SubTRef() const {return fTDRaw_SubTRef;}
  virtual Int_t    GetTUMulti() const {return fTUMulti;}
  virtual Int_t    GetTDMulti() const {return fTDMulti;}
  virtual Double_t GetTUCal() const {return fTUCal;}
  virtual Double_t GetTDCal() const {return fTDCal;}
  virtual Double_t GetTUCal_Width() const {return fTUCal_Width;}
  virtual Double_t GetTDCal_Width() const {return fTDCal_Width;}
  virtual Double_t GetTUSlw() const {return fTUSlw;}
  virtual Double_t GetTDSlw() const {return fTDSlw;}
  virtual Double_t GetDTRaw() const {return fDTRaw;}
  virtual Double_t GetDTCal() const {return fDTCal;}
  virtual Double_t GetDTSlw() const {return fDTSlw;}
  virtual Double_t GetTAveRaw() const {return fTAveRaw;}
  virtual Double_t GetTAveCal() const {return fTAveCal;}
  virtual Double_t GetTAveSlw() const {return fTAveSlw;}
  virtual Double_t GetTUCalT0() const {return fTUCalT0;}
  virtual Double_t GetTDCalT0() const {return fTDCalT0;}
  virtual Double_t GetTUSlwT0() const {return fTUSlwT0;}
  virtual Double_t GetTDSlwT0() const {return fTDSlwT0;}
  virtual Double_t GetTAveCalT0() const {return fTAveCalT0;}
  virtual Double_t GetTAveSlwT0() const {return fTAveSlwT0;}
  virtual Double_t GetTTOFGamma() const {return fTTOFGamma;}
  virtual Double_t GetTTOFNeutron() const {return fTTOFNeutron;}

  virtual Double_t GetPosCal() const {return fPosCal;}
  virtual Double_t GetPosSlw() const {return fPosSlw;}
  virtual const Double_t* GetPos() const {return fPos;}
  virtual Double_t GetPos(Int_t i) const {return fPos[i];}
  virtual Double_t GetFlightLength() const {return fFlightLength;}
  virtual Double_t GetFlightAngle() const {return fFlightAngle;}

private:
  Int_t    fLayer;  
  Int_t    fSubLayer;  
  Double_t fDetPos[3];
  Int_t    fHit;

  Int_t    fQURaw;
  Int_t    fQDRaw;
  Double_t fQUPed;
  Double_t fQDPed;
  Double_t fQUCal;
  Double_t fQDCal;
  Double_t fQAvePed;
  Double_t fQAveCal;
  Double_t fLogQPed;
  Double_t fLogQCal;
  Double_t fIvSqrtQUPed;
  Double_t fIvSqrtQDPed;
  Double_t fIvSqrtQAvePed;

  Int_t    fTURaw;
  Int_t    fTDRaw;
  Int_t    fTURaw_Trailing;
  Int_t    fTDRaw_Trailing;
  Int_t    fTURaw_Width;
  Int_t    fTDRaw_Width;
  Int_t    fTURawRef;
  Int_t    fTDRawRef;
  Int_t    fTURaw_SubTRef;
  Int_t    fTDRaw_SubTRef;
  Int_t    fTUMulti;
  Int_t    fTDMulti;
  Double_t fTUCal;
  Double_t fTDCal;
  Double_t fTUCal_Width;
  Double_t fTDCal_Width;
  Double_t fTUSlw;
  Double_t fTDSlw;
  Double_t fDTRaw;
  Double_t fDTCal;
  Double_t fDTSlw;
  Double_t fTAveRaw;
  Double_t fTAveCal;
  Double_t fTAveSlw;
  Double_t fTUCalT0;
  Double_t fTDCalT0;
  Double_t fTUSlwT0;
  Double_t fTDSlwT0;
  Double_t fTAveCalT0;
  Double_t fTAveSlwT0;
  Double_t fTTOFGamma;
  Double_t fTTOFNeutron;

  Double_t fPosCal;
  Double_t fPosSlw;
  Double_t fPos[3];
  Double_t fFlightLength;
  Double_t fFlightAngle;

  ClassDef(TArtNEBULAPla,1);
};
#endif
```

### 3. 成员变量详解
#### a. 探测器结构相关
-   `fLayer`: 所在层编号（如 NEBULA 阵列的第几层）。
-   `fSubLayer`: 子层编号（如同一层内的分组）。
-   `fDetPos[3]`: 探测器空间坐标（X, Y, Z），用于几何定位。

#### b. 信号与能量相关
-   `fQURaw` / `fQDRaw`: 上/下端原始信号（ADC），未经过校准。
-   `fQUCal` / `fQDCal`: 上/下端校准后的信号（能量），单位通常为 MeV。
-   `fQAveCal`: 上下端信号的平均值，常用于能量重建。
-   `fLogQCal`: 信号的对数变换，便于谱分析或分辨率处理。
-   `fIvSqrtQUPed` 等: 信号处理相关变量，用于分辨率、噪声分析。

#### c. 时间相关
-   `fTURaw` / `fTDRaw`: 上/下端原始时间信号（TDC）。
-   `fTUCal` / `fTDCal`: 校准后的时间信号（单位 ns）。
-   `fTAveCal`: 上下端时间的平均值，常用于飞行时间（TOF）计算。
-   `fTTOFGamma` / `fTTOFNeutron`: γ/中子的飞行时间，便于粒子鉴别。

#### d. 位置与飞行参数
-   `fPosCal` / `fPosSlw`: 击中位置的校准值和慢信号值。
-   `fPos[3]`: 击中点的空间坐标（X, Y, Z）。
-   `fFlightLength`: 粒子从反应点到探测器的飞行距离。
-   `fFlightAngle`: 粒子入射角度。

#### e. 多重击中与参考信号
-   `fTUMulti` / `fTDMulti`: 上/下端多重击中计数。
-   `fTURawRef` / `fTDRawRef`: 参考时间信号（如触发参考）。
-   `fTURaw_SubTRef` / `fTDRaw_SubTRef`: 与参考信号的差值。

#### f. 其他
-   `fHit`: 是否被击中（0/1），用于事件筛选。
-   还有大量信号处理相关变量（如 `trailing`、`width`、`slw`），用于详细分析探测器响应特性。

---




## 附录：在 MkDocs 中启用 Mermaid 图表

要在文档中正确显示 Mermaid 流程图，需要在 `mkdocs.yml` 配置文件中添加以下扩展。

```yaml
# mkdocs.yml

markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
```

