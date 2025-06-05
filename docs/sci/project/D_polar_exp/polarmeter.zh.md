---
title: 已有的各种探测器
---

## dpol

### 探测器参数

- HOD1：9个水平分段塑料闪烁体，尺寸：1300 mm (宽) × 80 mm (高) × 10 mm (厚)
- HOD2：12个垂直分段塑料闪烁体，尺寸：900 mm (宽) × 100 mm (高) × 50 mm (厚)

### 光电探测器

- 主要型号：Hamamatsu H1161 PMT
    - 类型：绿光拓展型（green-extended type），H1161GS为变种型号，标准H1161 (R329) 也属此系列
    - 参考参数（CLAS EMC）：最小增益 1×10⁷

---

## bigdpol

### 探测器参数

| 探测器类型           | 宽度 (mm) | 高度 (mm) | 厚度 (mm) | 实验室角度 (°)                                 |
|----------------------|-----------|-----------|-----------|-----------------------------------------------|
| 质子探测器           | 20        | 40/60     | 20        | 21.3, 26.1, 30.9, 35.8, 40.8, 45.0, 50.8, 55.9 |
| 氘核探测器           | 24        | 40        | 10        | 20.1, 22.7, 25.6                              |
| 氘核探测器           | 50        | 40        | 10        | 29.3                                          |
| 准自由p–p探测器      | 50        | 60        | 10        | 44                                            |

---

## KuJyaku

### 探测器参数

- 束流能量：100 MeV/n, 135 MeV/n
- Pl_p探测器：塑料闪烁体（BC-408），尺寸 70×70×25 mm³，距离靶1000 mm
- Pl_d探测器：塑料闪烁体（BC-408），尺寸 250×70×10 mm³，距离靶950 mm

| 探测器         | 闪烁体尺寸 (mm³)         | PMT型号           | 距靶距离 (mm) |
|----------------|-------------------------|-------------------|---------------|
| Pl_p           | 70×70×25                | Hamamatsu H7195   | 1000          |
| Pl_d           | 250×70×10               | Hamamatsu H7195   | 950           |

- 束流计数率：10⁷–10⁹ cps
- 相关参考：[原文PDF（tohoku.repo.nii.ac.jp）](https://tohoku.repo.nii.ac.jp/record/2003966/files/250325-Saito-3575-1.pdf)

### 光电探测器

- Hamamatsu H7195 PMT

---

## JINR DSS

### 探测器参数

- 质子探测器：宽20 mm，高40/60 mm，厚20 mm，距靶630 mm，实验室角度覆盖2°（约质心系4°）
- 氘核探测器：宽24 mm或50 mm，高40 mm，厚10 mm
- 准弹性p–p探测器（束流强度监测）：宽50 mm，高60 mm，厚10 mm

- 相关参考：[arxiv:1005.0525（arxiv.org）](https://arxiv.org/pdf/1005.0525)

### 光电探测器

- 主要型号：Hamamatsu H7416MOD PMT
    - 多份文献指出塑料闪烁计数器与H7416MOD PMT耦合
    - [会议论文PDF（epj-conferences.org）](https://www.epj-conferences.org/articles/epjconf/pdf/2019/06/epjconf_ayss18_04005.pdf)
    - H7416MOD数据手册未直接公开，可参考同系列H7415（直径33mm，内置R6427 PMT，双碱光阴极，硼硅酸盐玻璃窗，光谱范围300-650nm，峰值波长420nm，上升时间1.7ns，在-1500V下增益5.0×10⁶）[产品页（hamamatsu.com）](https://www.hamamatsu.com/eu/en/product/optical-sensors/pmt/pmt-assembly/head-on-type/H7415.html)
- SiPM升级尝试：[Springer论文（springer.com）](https://link.springer.com/article/10.1134/S1547477123050710)

---

## 德国 Forschungszentrum Jülich

### EDDA极化计

EDDA探测器被用于COSY加速过程中束流极化的在线测量，最初设计用于pp弹性散射的激发函数和自旋相关系数，后也用于氘核极化测量。EDDA为全覆盖型hodoscope，适合加速器内部靶实验中监测极化度变化。

- [会议论文PDF（accelconf.web.cern.ch）](https://accelconf.web.cern.ch/p01/papers/rpph054.pdf)
- [KEK会议论文（epaper.kek.jp）](https://epaper.kek.jp/e00/PAPERS/MOP4B19.pdf)
- [BNL报告PDF（bnl.gov）](https://www.bnl.gov/edm/review/files/pdf/estephenson_cosy_writeup.pdf)

### 基于LYSO的量能器型极化计 (用于EDM搜索)

COSY开发的新型量能器型极化计，采用LYSO晶体和SiPM，专为EDM实验设计，要求高效率和长期稳定性。

- 特性: 光输出高 (NaI(Tl)的75%)，衰减时间快 (40 ns)，密度高 (7.1g/cm³)
- 排列: 52个LYSO模块，4个对称块（上、下、左、右）
- 尺寸: 主体30×30×100 mm³，前端小角度15×30 mm²
- 前置薄塑料闪烁体用于dE/dx粒子鉴别，组合成ΔE-E望远镜结构
- 采用SiPM

- [ResearchGate论文（researchgate.net）](https://www.researchgate.net/publication/344894223_A_New_Beam_Polarimeter_at_COSY_to_Search_for_Electric_Dipole_Moments_of_Charged_Particles)
- [arxiv:2010.13536（arxiv.org）](https://arxiv.org/abs/2010.13536)

---

## Jefferson Lab (JLab)

JLab多个实验大厅采用塑料闪烁体和PMT，广泛用于极化靶和束流实验。

### Møller极化计 Hall A

- 采用磁饱和铁箔靶，散射电子对由铅/闪烁光纤量能器探测，光纤捆绑后连接到PMT
- 主要用于电子束极化测量

- [arxiv:2207.02150（arxiv.org）](https://arxiv.org/pdf/2207.02150)

### BigHAND

- Hall A超核研究相关，但无氘核极化计具体细节
- [JLab PAC34报告（jlab.org）](https://www.jlab.org/exp_prog/PACpage/PAC34/talks/PAC34_hallc.pdf)

---

## SiPM/PMT常见参数范围

### SiPM 关键参数

- **探测光子产额范围 (Dynamic Range)：** 由微单元总数决定，单光子到数千光子，高密度像素可达数十万微单元。
- **增益 (Gain)：** 典型范围 10⁵ 到 10⁷，依赖于过电压和温度。
- **光子探测效率 (PDE)：** 峰值PDE 40%-60%（可见光），VUV波段约15%，受波长、过电压、温度等影响。
- **暗计数率 (DCR)：** 室温下几十kHz/mm²到几MHz/mm²，低温下显著降低。
- **时间分辨率 (Time Resolution)：** 单光子几十到几百皮秒，多光子更优。
- **工作电压 (Operating Voltage)：** 20V-100V，实际工作时在击穿电压之上加几伏过电压。
- **其他参数：**
    - 恢复时间：几十到几百纳秒
    - 串扰、后脉冲、尺寸和封装、辐射硬度等

总结：SiPM具有高增益（10⁵−10⁷）、宽动态范围、良好PDE，具体型号选择需结合实验需求。常用厂商有滨松、安森美等。

