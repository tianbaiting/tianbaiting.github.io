# SAMURAI 光谱仪带电粒子探测器详细功能

SAMURAI（Superconducting Analyzer for Multi-particles from RAdioIsotope beams）光谱仪配备了多种带电粒子探测器，用于精确测量和分析放射性同位素束反应产生的粒子。以下是各个探测器的主要功能：

---

## 1. 束流粒子追踪与鉴定

这些探测器位于靶前，用于精确测量入射束流粒子的特性。

- **束流正比室 (Beam Proportional Chamber, BPC)**
  - 功能：主要用于在F5焦点处标记束流的磁刚度（rigidity tagging），对于确定入射束流的动量至关重要。
- **束流漂移室1和2 (Beam Drift Chamber 1, 2 - BDC1, BDC2)**
  - 功能：记录束流的相空间信息（beam phase space file），精确测量束流粒子的二维位置和方向，详细重建束流轨迹。
- **束流离子室 (Ion Chamber for Beam, ICB)**
  - 功能：测量入射束流的电荷（Z），有助于识别束流中的粒子种类。

---

## 2. 反应产物（碎片）分析

这些探测器位于靶后，用于分析反应产生的带电碎片。

- **前向漂移室1 (Forward Drift Chamber 1, FDC1)**
  - 功能：测量反应产生碎片的散射角，是理解反应机制的重要参数。
- **前向漂移室2 (Forward Drift Chamber 2, FDC2)**
  - 功能：对反应产物碎片进行刚度分析，结合磁场信息确定碎片的动量。
- **碎片离子室 (Ion Chamber for Fragments, ICF)**
  - 功能：测量碎片的电荷（Z），帮助识别碎片种类，通常结合其他测量（如能量损失）区分不同核素。
- **碎片闪烁体阵列 (Hodoscope for Fragment, HODF)**
  - 功能：测量碎片的飞行时间（ToF）和电荷（Z）。ToF与路径长度结合可得速度，进而推算质量（若能量或动量已知）。
- **全内反射切伦科夫探测器 (Total Internal Reflection Cherenkov, TIRC)**
  - 功能：专门用于测量碎片的飞行时间，精确确定其速度，尤其适用于高能碎片鉴别。
- **总能量探测器 (TED)**
  - 功能：测量带电粒子的总能量，常用于重离子，通过测量其在探测器中沉积的总能量帮助识别粒子和确定初始能量。

---

## 3. 轻带电粒子（如质子）分析

这些探测器专门用于测量反应中发射的轻带电粒子，例如从非束缚态衰变或敲出反应中产生的质子。

- **质子漂移室1和2 (Proton Drift Chamber 1,2 - PDC1,2)**
  - 功能：对质子等轻带电粒子进行动量分析。通常放置在分析磁铁之后，通过测量粒子在磁场中的弯曲轨迹确定其动量。
- **质子闪烁体阵列 (Hodoscope for Protons, HODP)**
  - 功能：测量质子的飞行时间和电荷。与HODF类似，有助于确定质子的速度和进行粒子鉴别。

---

Sources:

https://ribf.riken.jp/SAMURAI/index.php?ChargedParticleDetector

https://www.nishina.riken.jp/ribf/SAMURAI/tecinfo.html