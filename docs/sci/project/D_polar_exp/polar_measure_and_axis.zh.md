---
title: 氘核极化测量与极化轴确定
tag:
    - 极化
    - polarimeter
    - isovector
    - 磁场进动
---

本页整理 isovector reorientation 文章 (*Simulation studies of the isovector reorientation effect of deuteron scattering on heavy target*) 中关于氘核极化测量、极化散射的推导和监测方案，并在此基础上补充两部分：(1) 束流经过磁场元件时自旋的进动；(2) 在束流不同位置放置极化探测器以确定极化轴的方法。

## 1. 实验背景

文章的目标是在 RIKEN Nishina Center 的 SAMURAI 谱仪上，测量 190 MeV/u 极化氘核束流与重靶（$^{112}$Sn, $^{124}$Sn, $^{208}$Pb）散射后发生破裂时，同向性势 (isovector potential) 所导致的 reorientation 效应。该效应要求氘核束流的张量极化必须已知且稳定，因此在靶前放置一个专用 polarimeter 用 $p(\vec{d},d)p$ 弹性散射来在线监测张量极化。

使用极化束流的意义在于：如果束流不极化，破裂后中子–质子角分布的各向异性会在统计平均下抵消，无法观察到 IVR 效应。

## 2. 张量极化的定义

氘核是自旋 1 的原子核。它的极化态由自旋密度算符 $\hat{\rho}$ 表征。对自旋 1 体系，$\hat{\rho}$ 是 $3\times 3$ 的 Hermitian 矩阵，同时携带矢量极化和张量极化信息。

在 Cartesian 基下 (参见 Ohlsen 1972) 密度矩阵可以展开成

$$
\hat{\rho} = \frac{1}{3}\left\{ I + \frac{3}{2}\sum_i p_i \mathscr{P}_i + \frac{2}{3}\sum_{i\neq j} p_{ij}\mathscr{P}_{ij} + \frac{1}{3}\sum_i p_{ii}\mathscr{P}_{ii} \right\}
$$

其中 $\mathscr{P}_i = S_i$ 是矢量极化算符，$\mathscr{P}_{ij} = 3 S_i S_j - 2I$ 是张量极化算符，$p_i$ 与 $p_{ij}$ 是相应的极化分量。由于

$$
\mathscr{P}_{xx} + \mathscr{P}_{yy} + \mathscr{P}_{zz} = 0,
$$

张量的三个对角分量并非独立，实验中常取 $p_{z'z'}$ 或 $p_{y'y'}$ 作为监测量。

实验中通常使用束流系 $S'$：$z'$ 轴沿入射方向 $\vec{k}_\text{in}$，$y'$ 轴指向上方。理想的张量极化态是 $p_{z'z'}=1$（纵向极化）或 $p_{y'y'}=1$（垂直极化）。

## 3. 极化微分散射截面

末态密度矩阵与初态的关系为 $\hat{\rho}_f = M\hat{\rho}_i M^\dagger$。定义分析本领

$$
A_i = \frac{\operatorname{Tr}(M\mathscr{P}_i M^\dagger)}{\operatorname{Tr}(MM^\dagger)}, \qquad A_{ij} = \frac{\operatorname{Tr}(M\mathscr{P}_{ij} M^\dagger)}{\operatorname{Tr}(MM^\dagger)}.
$$

从而极化束流的微分截面为

$$
\sigma = \sigma_0(\theta)\left\{ 1 + \frac{3}{2}\sum_i p_i A_i + \frac{1}{3}\sum_{ij} p_{ij} A_{ij} \right\}
$$

其中 $\sigma_0(\theta) = \tfrac{1}{3}\operatorname{Tr}(MM^\dagger)$ 是非极化差分截面。

利用宇称守恒（要求 $N_x + N_z$ 为偶数）以及束流系 $S'$ 与散射体系 $S$ 之间的坐标变换，上式可写成 Ohlsen 形式：

$$
\begin{aligned}
\frac{\sigma(\theta,\phi)}{\sigma_0(\theta)} = 1 &+ \frac{3}{2}(p_{x'}\sin\phi + p_{y'}\cos\phi) A_y(\theta) \\
&+ \frac{2}{3}(p_{x'z'}\cos\phi - p_{y'z'}\sin\phi) A_{xz}(\theta) \\
&+ \frac{1}{6}\big[(p_{x'x'}-p_{y'y'})\cos 2\phi - 2 p_{x'y'}\sin 2\phi\big]\big[A_{xx}(\theta)-A_{yy}(\theta)\big] \\
&+ \frac{1}{2}p_{z'z'} A_{zz}(\theta).
\end{aligned}
$$

## 4. LRUD 四探测器方案

在同一极角 $\theta$、方位角 $\phi = 0^\circ,90^\circ,180^\circ,270^\circ$ 放置四个探测器，分别记为 L, U, R, D。代入上式得

$$
\begin{aligned}
\sigma_L &= \sigma_0\Big\{1 + \tfrac{3}{2}p_{y'}A_y + \tfrac{2}{3}p_{x'z'}A_{xz} + \tfrac{1}{6}(p_{x'x'}-p_{y'y'})(A_{xx}-A_{yy}) + \tfrac{1}{2}p_{z'z'}A_{zz}\Big\}, \\
\sigma_R &= \sigma_0\Big\{1 - \tfrac{3}{2}p_{y'}A_y - \tfrac{2}{3}p_{x'z'}A_{xz} + \tfrac{1}{6}(p_{x'x'}-p_{y'y'})(A_{xx}-A_{yy}) + \tfrac{1}{2}p_{z'z'}A_{zz}\Big\}, \\
\sigma_U &= \sigma_0\Big\{1 - \tfrac{3}{2}p_{x'}A_y + \tfrac{2}{3}p_{y'z'}A_{xz} - \tfrac{1}{6}(p_{x'x'}-p_{y'y'})(A_{xx}-A_{yy}) + \tfrac{1}{2}p_{z'z'}A_{zz}\Big\}, \\
\sigma_D &= \sigma_0\Big\{1 + \tfrac{3}{2}p_{x'}A_y - \tfrac{2}{3}p_{y'z'}A_{xz} - \tfrac{1}{6}(p_{x'x'}-p_{y'y'})(A_{xx}-A_{yy}) + \tfrac{1}{2}p_{z'z'}A_{zz}\Big\}.
\end{aligned}
$$

### 4.1 监测 $p_{y'y'}$（既有方法）

按 Bieber 2001 定义左右上下的计数不对称

$$
R_{LRUD} = \frac{N_L + N_R - N_U - N_D}{N_L + N_R + N_U + N_D} = \frac{p_{y'y'}(A_{xx}-A_{yy})}{2 p_{y'y'} A_{zz} - 4},
$$

反解出

$$
p_{y'y'} = \frac{R_{LRUD}}{\tfrac{1}{2}A_{zz} R_{LRUD} - \tfrac{1}{4}(A_{xx}-A_{yy})}.
$$

### 4.2 监测 $p_{z'z'}$（本工作提出）

四路平均截面

$$
\bar{\sigma} = \frac{\sigma_L + \sigma_R + \sigma_U + \sigma_D}{4} = \sigma_0\left(1 + \tfrac{1}{2}p_{z'z'} A_{zz}\right),
$$

若已知 $A_{zz}$ 可直接由 $\bar{\sigma}$ 得到 $p_{z'z'}$。为消去束流强度与靶厚带来的系统误差，取两个不同极角 $\theta_1$ 与 $\theta_2$ 处的 $\bar{\sigma}$ 作比值，即可抵消公共因子，仅保留两个角度的 $\sigma_0$ 与 $A_{zz}$ 组合。

## 5. Polarimeter 设计与模拟结果

探测器方案：$p(\vec{d},d)p$ 弹性散射，CH$_2$ 靶厚 $1000\,\text{mg/cm}^2$，束流 $1.6\times 10^{-3}$ pnA（即 $10^7$ pps）。双角度反冲质子探测点：$\theta_1 = 55.9^\circ$ 与 $\theta_2 = 11.3^\circ$，靶距 600 mm，探测器接收角各向约 $20\times 20\,\text{mm}^2$；并在 $\theta = 20.87^\circ$ 处放置一个 $50\times 40\,\text{mm}^2$ 的 deuteron 探测器（距靶 500 mm）。

分析本领取自 Sekiguchi 等人的公开 $d$–$p$ 弹性散射测量数据。

GEANT4 模拟结果：

- 在 $\theta_1$ 处四个方位 30 min 内可累积 $\sim 10^5$ 事例；
- 两角度计数比对 $p_{zz}$ 的灵敏度（Fig. Ratio_vs_pzz）和 $R_{LRUD}$ 对 $p_{y'y'}$ 的灵敏度（Fig. R\_LRUD\_vs\_pyy）都显示，统计误差远小于 $\sim 10\%$ 的张量极化分辨率要求；
- 因此本 polarimeter 可以稳定地把 $p_{z'z'}$ 与 $p_{y'y'}$ 监测到 $\sim 10\%$ 的相对精度。

## 6. 磁场中的自旋进动

polarimeter 的读数只给出"在该位置"的极化分量。要把它与束流产生端（polarized ion source 与 Wien filter）以及靶处的极化态联系起来，必须追踪束流在加速与传输系统中的自旋进动。

### 6.1 氘核的 g-factor

氘核 g 因子 $g_d \approx 0.8574$。定义异常磁矩因子

$$
G = \frac{g - 2}{2}.
$$

对氘核 $G_d \approx -0.1430$。

### 6.2 Thomas–BMT 进动

在纯磁场中，相对论 Thomas–BMT 方程给出自旋绕磁场的进动。对于在竖直弯曲磁场中运动的粒子，自旋相对于动量方向的额外旋转角为

$$
\theta_\text{spin} - \theta_\text{bend} = G\gamma\, \theta_\text{bend},
$$

即自旋 tune（每绕一圈相对动量多转的圈数）为 $G\gamma$。

对 190 MeV/u 的氘核，$\gamma = 1 + T/(m_u c^2) = 1.204$，

$$
G\gamma \approx -0.172.
$$

每经过一段弯铁（几何弯角 $\theta_B$），水平面内的极化方向相对动量方向多转过 $G\gamma\,\theta_B$。对纵向 $p_{z'z'}$ 与垂直 $p_{y'y'}$ 的区别在于：

- 垂直极化 ($y'$) 与磁场方向平行，Thomas–BMT 不会使其在一级效应下发生方向变化，只会保持；
- 纵向极化 ($z'$) 位于水平面内，会随 $G\gamma\,\theta_B$ 相对动量方向发生旋转，因此从离子源到靶前，polarimeter 前段的任何水平弯铁都会改变"在 polarimeter 处看到的极化轴方向"。

### 6.3 Wien filter

RIKEN 方案在加速器前端放置 Wien filter（正交电、磁场）。在 Wien filter 中粒子轨迹不偏转，但自旋可以任意旋转到所需方向。这使得在源端可以把极化轴调到任一目标方向（沿 $x$, $y$, $z$ 中任一轴，或它们的合成方向）。Wien filter 的设定值需要由后续 polarimeter 的实测反馈，以保证到达靶位时的极化轴与设计一致。

### 6.4 单次通过 cyclotron 提取的自旋守恒

三台 cyclotron (AVF, RRC, SRC) 的单圈提取（single-turn extraction）保证了束流在加速过程中没有因多圈叠加相消导致的极化幅度降低，最终提取极化仍保持理论值的 $\sim 80\%$。

## 7. 用多位置 polarimeter 确定极化轴

如果只把 polarimeter 放在束线的一个点上，L/R/U/D 四路计数能够给出该点处几个 $p_{i'j'}$ 的组合（参见 §4），但无法把极化轴 $\hat{S}$ 在三维空间中的方向完全确定出来。原因是：在单点处，自由度有限——例如只靠 $R_{LRUD}$ 本身无法同时解出 ($\beta,\phi$)。

### 7.1 任意极化轴下的截面

把极化轴方向写成球面角 $(\beta,\phi)$，仅存纵向极化 $P_{zz}$ 的情况下（Ohlsen 旋转规则，参见本站 `spherical_operator.md`），束流系中

$$
\begin{aligned}
p_{xx} &= \tfrac{1}{2}(3\sin^2\beta\sin^2\phi - 1)P_{zz}, \\
p_{yy} &= \tfrac{1}{2}(3\sin^2\beta\cos^2\phi - 1)P_{zz}, \\
p_{zz} &= \tfrac{1}{2}(3\cos^2\beta - 1)P_{zz}, \\
p_{xy} &= -\tfrac{3}{2}\sin^2\beta\sin\phi\cos\phi\, P_{zz}, \\
p_{yz} &= \sin\beta\cos\beta\cos\phi\, P_{zz}, \\
p_{xz} &= -\sin\beta\cos\beta\sin\phi\, P_{zz}.
\end{aligned}
$$

相应 LRUD 非对称性变为

$$
\begin{aligned}
\frac{2(L-R)}{L+R+U+D} &= \frac{\tfrac{3}{2}P_z\sin\beta A_y}{1 + \tfrac{1}{2}P_{zz}(3\cos^2\beta - 1)A_{zz}}, \\
\frac{2(U-D)}{L+R+U+D} &= \frac{P_{zz}\sin\beta\cos\beta A_{xz}}{1 + \tfrac{1}{2}P_{zz}(3\cos^2\beta - 1)A_{zz}}, \\
\frac{(L+R) - (U+D)}{L+R+U+D} &= \frac{-\tfrac{1}{4}P_{zz}\sin^2\beta(A_{xx}-A_{yy})}{1 + \tfrac{1}{2}P_{zz}(3\cos^2\beta - 1)A_{zz}}.
\end{aligned}
$$

这三个观测量一起是 ($P_z$, $P_{zz}$, $\beta$, $\phi$) 的函数，但实际上 $\sin\beta$ 与 $\cos\beta$ 存在分支、$\phi$ 有 $\phi \leftrightarrow \phi + \pi$ 的对称性等等。单点 LRUD 对 $\hat{S}$ 的空间方向并不具完全可逆性。

### 7.2 多位置 polarimeter 的方案

沿束线在磁场元件前后各设一台 polarimeter（记为 $P_1$ 与 $P_2$），它们之间的束流要经过已知的磁场 $B$ 及几何弯角 $\theta_B$。根据 §6.2，水平面内的极化轴在两点之间会相对动量方向多转 $\Delta\phi_s = G\gamma\,\theta_B$。

设极化轴在 $P_1$ 处的球面角为 $(\beta,\phi_1)$，则在 $P_2$ 处对应于 $P_2$ 的束流系的角为

$$
(\beta,\phi_2) = (\beta,\phi_1 + G\gamma\,\theta_B).
$$

（竖直极化分量 $\cos\beta$ 部分不受水平弯铁影响，因此 $\beta$ 在一级近似下不变。）

这样两台 polarimeter 给出的 6 个独立不对称量（每台 3 个）成为四个未知数 ($P_z$, $P_{zz}$, $\beta$, $\phi_1$) 的超定方程组。用最小二乘或 $\chi^2$ 拟合即可同时解出

1. 矢量极化大小 $P_z$；
2. 张量极化大小 $P_{zz}$；
3. 极化轴天顶角 $\beta$；
4. 方位角 $\phi_1$ (进而 $\phi_2$)。

### 7.3 为什么一定要用磁场做中介

两台 polarimeter 之间若没有磁场（即 drift space），自旋方向不变，两台读数完全等价，信息量没有增加。必须要有已知的磁场进动 $\Delta\phi_s$ 才能把原本简并的 ($\beta,\phi$) 分量拆开——这就是"利用磁场进动 + 多位置 polarimeter 来确定极化轴"的物理本质。

实际操作上常用的三种"中介磁铁"：

- 束线上原有的 dipole/弯铁：$\theta_B$ 几何已知，$G\gamma\,\theta_B$ 直接给出进动差；
- 专门的 spin rotator (如 Wien filter, solenoid)：$\Delta\phi_s$ 可以程序化扫描，作为校准手段；
- 前置的 solenoid：把极化轴从 $z'$ 转到 $y'$ 或其组合，与两端 polarimeter 配合做系统化校准。

### 7.4 实用布局建议

对 IVR 实验而言，可以采用的最小配置为：

1. 在 RRC→SRC bypass beam line 某个弯铁前后各放一台 polarimeter（或复用已有 dPol / BigDpol 设备）；
2. 目标 polarimeter 设置成本文提出的 LRUD + 双角度 ($\theta_1, \theta_2$) 组合，即可同时监测 $p_{y'y'}$ 与 $p_{z'z'}$；
3. 利用两台 polarimeter 的六个不对称量拟合 ($P_z,P_{zz},\beta,\phi$)，将结果反馈给源端 Wien filter 进行闭环调节；
4. 靶前 polarimeter 作最终值使用，IVR 分析以靶前实测 $p_{z'z'}$ / $p_{y'y'}$ 为准。

这样既继承了论文中已论证的"单点 LRUD + 双角度"方案的灵敏度，又把极化轴方向纳入可观测量，从而在实验过程中确认 Wien filter 工作在目标状态。

## 8. 同时存在矢量极化与张量极化的情况

§7 假设束流只带张量极化 ($P_{zz}$, $P_z = 0$)。真实的 RIKEN 极化离子源由不同 RF 跃迁态叠加产生，一般同时带有矢量极化 $P_z$ 和张量极化 $P_{zz}$。此时单一极化轴 $(\beta,\phi)$ 加两个幅度一共有 **4 个未知数** $(P_z, P_{zz}, \beta, \phi)$。

### 8.1 极化分量的完整表达

沿 $(\beta,\phi)$ 方向的矢量极化在束流系的分量

$$
\begin{aligned}
p_{x'} &= -P_z \sin\beta\sin\phi, \\
p_{y'} &= \phantom{-}P_z \sin\beta\cos\phi, \\
p_{z'} &= \phantom{-}P_z \cos\beta.
\end{aligned}
$$

张量极化分量（已在 §7.1 给出）重述为

$$
\begin{aligned}
p_{x'x'}-p_{y'y'} &= -\tfrac{3}{2}\sin^2\beta\cos 2\phi\, P_{zz}, \\
p_{z'z'} &= \tfrac{1}{2}(3\cos^2\beta - 1)P_{zz}, \\
p_{y'z'} &= \sin\beta\cos\beta\cos\phi\, P_{zz}, \\
p_{x'z'} &= -\sin\beta\cos\beta\sin\phi\, P_{zz}.
\end{aligned}
$$

### 8.2 四个独立观测量

把上述分量代入 §4 的 Ohlsen 截面公式，单台 polarimeter 在同一极角 $\theta$ 下给出三路不对称量

$$
\begin{aligned}
\mathcal{A}_{LR} &\equiv \frac{2(\sigma_L - \sigma_R)}{\sigma_L+\sigma_R+\sigma_U+\sigma_D}
= \frac{\tfrac{3}{2}P_z \sin\beta\cos\phi\, A_y - \tfrac{2}{3}P_{zz}\sin\beta\cos\beta\sin\phi\, A_{xz}}{1 + \tfrac{1}{4}(3\cos^2\beta - 1)P_{zz} A_{zz}}, \\[4pt]
\mathcal{A}_{UD} &\equiv \frac{2(\sigma_U - \sigma_D)}{\sigma_L+\sigma_R+\sigma_U+\sigma_D}
= \frac{\tfrac{3}{2}P_z \sin\beta\sin\phi\, A_y + \tfrac{2}{3}P_{zz}\sin\beta\cos\beta\cos\phi\, A_{xz}}{1 + \tfrac{1}{4}(3\cos^2\beta - 1)P_{zz} A_{zz}}, \\[4pt]
\mathcal{A}_{LR-UD} &\equiv \frac{(\sigma_L+\sigma_R)-(\sigma_U+\sigma_D)}{\sigma_L+\sigma_R+\sigma_U+\sigma_D}
= \frac{-\tfrac{1}{4}\sin^2\beta\cos 2\phi\, P_{zz}(A_{xx}-A_{yy})}{1 + \tfrac{1}{4}(3\cos^2\beta - 1)P_{zz} A_{zz}}.
\end{aligned}
$$

加上 §4.2 的双角度平均截面比

$$
\mathcal{R}_{12} \equiv \frac{\bar{\sigma}(\theta_1)}{\bar{\sigma}(\theta_2)} = \frac{\sigma_0(\theta_1)}{\sigma_0(\theta_2)}\cdot\frac{1 + \tfrac{1}{4}(3\cos^2\beta - 1)P_{zz} A_{zz}(\theta_1)}{1 + \tfrac{1}{4}(3\cos^2\beta - 1)P_{zz} A_{zz}(\theta_2)},
$$

则单台 polarimeter 共提供 **4 个独立观测量** $\{\mathcal{A}_{LR},\mathcal{A}_{UD},\mathcal{A}_{LR-UD},\mathcal{R}_{12}\}$，与 4 个未知数数目相同。但这些方程对 $(\beta,\phi)$ 存在多重简并：

- $\phi \leftrightarrow \phi + \pi$：$(\mathcal{A}_{LR},\mathcal{A}_{UD})$ 同时反号，$\mathcal{A}_{LR-UD}$ 与 $\mathcal{R}_{12}$ 不变；等价于同时翻转 $P_z \to -P_z$，无法区分。
- $\beta \leftrightarrow \pi - \beta$：$\cos\beta \to -\cos\beta$，$\mathcal{R}_{12}$ 与 $\mathcal{A}_{LR-UD}$ 不变。
- 当 $\beta$ 或 $\sin\beta$ 较小时某些项被压制，对应分量灵敏度骤降。

因此单点 polarimeter 虽然方程数够，但反解不稳定。

### 8.3 用两台 polarimeter 解除简并

在两台 polarimeter 之间设置已知水平弯铁（弯角 $\theta_B$）。由 §6.2，垂直 $p_{y'}$ 分量守恒，水平面内的极化分量多旋转 $\Delta\phi_s = G\gamma\,\theta_B$。对 $(\beta,\phi)$ 而言，$\beta$ 不变，而 $\phi$ 映射为

$$
\phi_2 = \phi_1 + \Delta\phi_s.
$$

（严格来说"方位角"指的是水平面内围绕 $y'$ 的方位，本节仍沿用 §7.1 的 Ohlsen 记号。对纯竖直极化 $\beta=\pi/2,\phi=0$，弯铁不改变可观测量，此时必须依赖下文的 spin-flip 方法。）

两台 polarimeter 共给出 **8 个观测量**：

$$
\big\{\mathcal{A}_{LR}^{(1)},\mathcal{A}_{UD}^{(1)},\mathcal{A}_{LR-UD}^{(1)},\mathcal{R}_{12}^{(1)};\ \mathcal{A}_{LR}^{(2)},\mathcal{A}_{UD}^{(2)},\mathcal{A}_{LR-UD}^{(2)},\mathcal{R}_{12}^{(2)}\big\}.
$$

其中 $(2)$ 号 polarimeter 的公式结构与 $(1)$ 号完全相同，只是把 $\phi_1$ 换成 $\phi_1 + \Delta\phi_s$。把这 8 个非线性方程用 $\chi^2$ 最小化

$$
\chi^2(P_z, P_{zz}, \beta, \phi_1) = \sum_{k=1}^{2}\sum_{X\in\{LR,UD,LR-UD,12\}}\frac{\big[\mathcal{A}_X^{(k),\text{meas}} - \mathcal{A}_X^{(k),\text{model}}(P_z,P_{zz},\beta,\phi_k)\big]^2}{\delta_X^{(k)\,2}}
$$

同时对 $(P_z, P_{zz}, \beta, \phi_1)$ 进行拟合，即可唯一解出 4 个未知数，且留下 4 个自由度可用于自洽检验（goodness-of-fit 与系统偏差诊断）。

### 8.4 与 spin-flip 技术的互补

在离子源端切换 RF 跃迁态可以得到几组不同的源态，例如

| 源态 | $P_z$ | $P_{zz}$ |
|---|---|---|
| 纯 $m=+1$ | $+1$ | $+1$ |
| 纯 $m=0$ | $\phantom{+}0$ | $-2$ |
| 纯 $m=-1$ | $-1$ | $+1$ |

态 $m=\pm 1$ 互换可翻转 $P_z$ 而保持 $P_{zz}$；因此

- $(N^{(+)}-N^{(-)})$ 只留下线性 $P_z$ 的项 → 直接给出 **矢量不对称**；
- $(N^{(+)}+N^{(-)})/2 - N^{\text{unpol}}$ 只留下线性 $P_{zz}$ 的项 → 直接给出 **张量不对称**。

这两类技术互补：

- **Spin-flip** 从源端纯化观测量，代价是需要可控且稳定的快速源态切换；
- **两台 polarimeter** 利用传输线自身的磁场进动同时确定极化幅度与极化轴方向，不要求源态切换，但要求至少一段已知几何的弯铁。

实践上推荐两者合用：以 spin-flip 把 $\{P_z, P_{zz}\}$ 的线性响应分开，再用两台 polarimeter 的 8 个观测量同时拟合 $\beta$ 与 $\phi$，把 Wien filter 的闭环调节精度推到极化轴角度 $\sim$ 几度的量级。

### 8.5 拟合流程小结

1. 离线标定：在已知源态（如 unpolarized 或纯 $m=0$）下测 $\sigma_0(\theta_1),\sigma_0(\theta_2)$，固定两台 polarimeter 的几何与效率因子；从 $d$–$p$ 数据库（Sekiguchi 等）取 $A_y(\theta),A_{xz}(\theta),A_{zz}(\theta),(A_{xx}-A_{yy})(\theta)$。
2. 在线数据：对每个源态取两台 polarimeter 的计数，计算 8 个观测量及其统计误差。
3. 全局 $\chi^2$ 拟合 $(P_z, P_{zz}, \beta, \phi_1)$；$\Delta\phi_s$ 作为固定量（或作为 nuisance 参数）。
4. 用 spin-flip 后的独立数据集交叉验证，确认拟合稳定性。
5. 把 $(\beta,\phi)$ 的实测值反馈到 Wien filter，实现极化轴闭环稳定。

## 9. 与相关参考页的交叉索引

- `spherical_operator.md`：Cartesian / spherical tensor 的算符矩阵、$U$ 变换下的张量分量、极化轴 $(\beta,\phi)$ 分解；
- `my_polarimeter.zh.md`：束团间隔 (bunch spacing) 与 polarimeter 时间分辨率要求；
- `other_polarmeter.zh.md`：RIKEN (dPol, BigDpol, KuJyaku)、JINR (DSS)、COSY (EDDA, JePo) 等组的 polarimeter 方案对比；
- `stastic.zh.md`：从多项式分布/误差传递角度评估 $R_{LRUD}$、$\bar{\sigma}_{\theta_1}/\bar{\sigma}_{\theta_2}$ 的统计不确定度。
