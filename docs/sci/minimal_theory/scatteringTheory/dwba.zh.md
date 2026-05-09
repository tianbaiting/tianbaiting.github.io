# 畸变波 Born 近似

`coulomb_scattering.zh.md:305` 在 Coulomb 加短程势的具体场景下已经做了一次完整的"分块 Born"——把 $V_C$ 当成精确求解的零阶背景，把 $V_{SR}$ 当成微扰，得到 $f_{SR}^{\rm CB}$。本篇把这一具体化抽出来，写成两体散射框架下普适的 Distorted-Wave Born Approximation：把 $V$ 拆成 $V_0 + V_1$，对 $V_0$ 算精确散射态（畸变波 $\chi^{(\pm)}$），对 $V_1$ 在畸变波基底上做一阶 Born。它同时是 Born 级数的"分块求和"、`T_and_U_operators.zh.md:296` 那条 LS 方程的两势重写、Coulomb-distorted Born 的一般化、以及核物理里光学势加转移势的标准微扰起点。

定位：研究轨第 3 篇主线笔记。与 `polarization_formalism.zh.md` 联动给出含自旋的 DWBA；与 `appendix_EST_seperable_HVH_Esym.md` 联动给出复光学势 $V_0$ 下的微扰处理；与 `T_and_U_operators.zh.md` 联动指出 DWBA 是两体 $T$ 算符的两势重写、是三体 AGS $U_{\beta\alpha}$ 的弱耦合极限。

约定：薛定谔表象、$\hbar=1$、约化质量 $\mu$、单中心两体（多通道时再具体化）。势 $V$ 不显含时；分波公式中按主线惯例 $V$ 取局域中心；推广到非局域、含自旋、多通道的写法在对应小节给出。

## 目标

DWBA 想解决一个具体的失败：当 $V$ 不弱、但能自然分块为强 $V_0$ 加弱 $V_1$ 时，纯 Born 级数 $T = V + V G_0 V + \cdots$ 收敛慢甚至发散，但物理上 $V_1$ 仍然是"小"扰动。需要的是把 $V_0$ 完整解掉，再对 $V_1$ 做单次微扰。

形式上：把 LS 方程 $|\psi^{(+)}\rangle = |\alpha\rangle + G_0^{(+)} V |\psi^{(+)}\rangle$ 重写为以 $H' = H_0 + V_0$ 的 Green 函数 $G_0' = (E - H' + i0)^{-1}$ 为参考的等价形式，定义畸变波 $|\chi_\alpha^{(+)}\rangle = |\alpha\rangle + G_0^{(+)} V_0 |\chi_\alpha^{(+)}\rangle$，再对 $V_1$ 一阶截断。结果是 Gell-Mann–Goldberger 两势公式与 DWBA 跃迁矩阵元

$$
T_{fi}^{\rm DWBA} = T_{fi}^{(0)} + \langle \chi_\beta^{(-)} | V_1 | \chi_\alpha^{(+)}\rangle \tag{DWBA-master}
$$

后项结构上像"用畸变波代替平面波的 Born"，但畸变波带相位累积，与纯 Born 的物理内容相距甚远。

适用范围列三类典型情形：

- 反应散射 $a + A \to b + B$：入射、出射通道各取光学势作畸变源，$V_1$ 是把核状态从 $|A\rangle$ 改到 $|B\rangle$ 的转移算符。这是核反应理论的"DWBA 工业"（核子转移、电磁、电弱跃迁）。
- 弹性散射的 Coulomb 加短程势：$V_0 = V_C$，$V_1 = V_{SR}$，畸变波是 Coulomb 波。这就是 `coulomb_scattering.zh.md:305` 的 Coulomb-distorted Born，本篇把它一般化。
- 光学势加弱微扰：复光学势 $V_0 = U(r) + iW(r)$ 提供吸收的弹性背景，$V_1$ 是被忽略的细节（如非中心耦合、isovector 修正、非局域成分）。

与极化形式联动（A 篇）：$V_0$、$V_1$ 在自旋空间是矩阵，畸变波 $\chi^{(\pm)}$ 在自旋分量上是 $(2s_a+1)(2s_A+1)$ 维向量，DWBA 矩阵元就是自旋空间的双线性形式。这给出 polarized 反应的 M 矩阵。

## Born 级数回顾与失效图像

`T_and_U_operators.zh.md:296` 的两体 $T$ 方程

$$
T(E) = V + V G_0^{(+)}(E)\, T(E) \tag{LS-T}
$$

迭代得到 Born 级数

$$
T = V + V G_0^{(+)} V + V G_0^{(+)} V G_0^{(+)} V + \cdots \tag{Born-series}
$$

收敛性的判据：算符范数 $\|V G_0^{(+)}(E)\| < 1$。物理直观：散射强度比单次散射的"自由再激发率" $G_0^{(+)} V$ 衰减得快，多次散射尾部可忽略。

一阶截断（纯 Born 近似）：

$$
T \approx V \quad\Longrightarrow\quad f^B(\mathbf k_f \leftarrow \mathbf k_i) = -\frac{\mu}{2\pi}\int d^3 r\, e^{-i\mathbf q\cdot\mathbf r}\, V(\mathbf r) \tag{f-B}
$$

$\mathbf q = \mathbf k_f - \mathbf k_i$；这正是 `S_matrix_and_cross_section.zh.md:506` 给出的标准 Born 公式。

何时 Born 级数发散

经典失效情景有四：

- $V$ 强到产生束缚态。$T(E)$ 在 $E = E_b < 0$ 处有极点，$\|VG_0^{(+)}\|$ 在阈值附近不再小于 1。
- $V$ 强到产生共振。$E$ 接近共振位置时 Born 级数缓慢收敛。
- $V$ 是长程势。`coulomb_scattering.zh.md:21` 已分析：Coulomb 让自由参考动力学失效，Cook 判据破坏，纯 Born 公式 $\text{(f-B)}$ 直接发散（$V_C$ 的 Fourier 在 $\mathbf q\to 0$ 处奇异）。
- $V$ 含吸收虚部 $iW$，$|W|$ 与 $|U|$ 同阶。光学势是这种情形，Born 完全捕捉不到吸收引起的 elastic 衰减。

DWBA 的存活条件：以上四种"强 $V$" 都可以通过分块 $V = V_0 + V_1$ 重新组织——把强、长程、共振制造、吸收的部分塞进 $V_0$，把仍然弱的部分留在 $V_1$。$V_0$ 的精确处理由数值积分径向方程或 EST/separable 展开（`appendix_EST_seperable_HVH_Esym.md:97`）完成；$V_1$ 的处理由本篇主公式 $\text{(DWBA-master)}$ 完成。

## 两势分解与畸变波

### 中间哈密顿量与畸变波 LS 方程

把势二分

$$
V = V_0 + V_1 \tag{V-split}
$$

定义中间哈密顿量

$$
H' = H_0 + V_0 \tag{H-prime}
$$

它有自己的精确散射态（畸变波）

$$
|\chi_\alpha^{(\pm)}\rangle = \Omega_\pm^{(0)} |\alpha\rangle,\qquad
\Omega_\pm^{(0)} = \operatorname*{s-lim}_{t\to\mp\infty} e^{iH't/\hbar}\, e^{-iH_0 t/\hbar} \tag{chi-Mol}
$$

只要 $V_0$ 是短程的（或 Coulomb 经过 Dollard 修正后等效短程），$\Omega_\pm^{(0)}$ 强极限存在，$|\chi_\alpha^{(\pm)}\rangle$ 是 $H'$ 的精确广义本征态，满足

$$
H' |\chi_\alpha^{(\pm)}\rangle = E_\alpha |\chi_\alpha^{(\pm)}\rangle \tag{chi-eig}
$$

它们也满足相对 $V_0$ 的 LS 方程

$$
|\chi_\alpha^{(\pm)}\rangle = |\alpha\rangle + G_0^{(\pm)}(E_\alpha)\, V_0\, |\chi_\alpha^{(\pm)}\rangle \tag{chi-LS}
$$

数值实现上 $\chi^{(\pm)}$ 由数值积分径向 Schrödinger 方程（仅 $V_0$ 项）得到——这是已知怎么做的部分。

完整精确态 $|\psi_\alpha^{(\pm)}\rangle$ 满足含全 $V$ 的 LS 方程（`T_and_U_operators.zh.md:204`）

$$
|\psi_\alpha^{(+)}\rangle = |\alpha\rangle + G_0^{(+)}(E_\alpha)\,(V_0 + V_1)\,|\psi_\alpha^{(+)}\rangle
$$

### Gell-Mann–Goldberger 重写

把上式重新围绕 $H'$ 整理。先把 $V_0$ 那一块吸收进新的 Green 函数

$$
G_0'^{(\pm)}(E) = \frac{1}{E - H' \pm i0} = \frac{1}{E - H_0 - V_0 \pm i0} \tag{G0p}
$$

由 resolvent 恒等式 $G_0'^{(\pm)} = G_0^{(\pm)} + G_0^{(\pm)} V_0\, G_0'^{(\pm)} = G_0^{(\pm)} + G_0'^{(\pm)} V_0\, G_0^{(\pm)}$。把这个等式代入 $\psi^{(+)} = |\alpha\rangle + G_0^{(+)} V \psi^{(+)}$，并用 $\text{(chi-LS)}$ 的左作用形式 $|\alpha\rangle = (1 - G_0^{(+)} V_0) |\chi_\alpha^{(+)}\rangle$，整理后得到

$$
|\psi_\alpha^{(+)}\rangle = |\chi_\alpha^{(+)}\rangle + G_0'^{(+)}(E_\alpha)\, V_1\, |\psi_\alpha^{(+)}\rangle \tag{psi-LS-prime}
$$

这就是 DWBA 的核心方程：把全 $V$ 下的 LS 方程换成以 $H'$ 为参考、$V_1$ 为相互作用的 LS 方程。畸变波 $\chi^{(+)}$ 取代了平面波 $|\alpha\rangle$，$G_0'^{(+)}$ 取代了 $G_0^{(+)}$。形式上完全平行 `T_and_U_operators.zh.md:204`。

### 两势 T 矩阵元的 Gell-Mann–Goldberger 公式

精确 T 矩阵元

$$
T_{fi} = \langle \beta | V | \psi_\alpha^{(+)}\rangle = \langle \beta | V_0 + V_1 | \psi_\alpha^{(+)}\rangle
$$

self-derive 第一种分裂（"prior form"）。把 $\langle\beta|V_0$ 用畸变波出态的对偶表达 $\langle\chi_\beta^{(-)}|(1 - V_0 G_0^{(-)\dagger}) = \langle\beta|$ 反推（这里用了 $\text{(chi-LS)}$ 的 $\beta, -$ 版本对厄米共轭）：

$$
\langle\beta|V_0 |\psi_\alpha^{(+)}\rangle = \langle\chi_\beta^{(-)}|V_0|\alpha\rangle + (\text{交叉项})
$$

把所有项重新分组，得到 Gell-Mann–Goldberger 两势公式（标准 prior form）：

$$
T_{fi} = \langle \beta | V_0 | \chi_\alpha^{(+)}\rangle + \langle \chi_\beta^{(-)} | V_1 | \psi_\alpha^{(+)}\rangle \tag{GMG-prior}
$$

也存在等价的 post form

$$
T_{fi} = \langle \chi_\beta^{(-)} | V_0 | \alpha \rangle + \langle \chi_\beta^{(-)} | V_1 | \psi_\alpha^{(+)}\rangle' \tag{GMG-post}
$$

其中 $|\psi_\alpha^{(+)}\rangle'$ 由 $\text{(psi-LS-prime)}$ 与 $|\chi^{(+)}\rangle$ 的关系定。

self-derive 简洁路径：从 $\text{(psi-LS-prime)}$ 左乘 $\langle\beta|V$，用 $|\beta\rangle = (1-G_0^{(-)}V_0)|\chi_\beta^{(-)}\rangle$ 改写左矢端：

$$
T_{fi} = \langle\beta|V|\psi_\alpha^{(+)}\rangle = \langle\beta|V_0|\chi_\alpha^{(+)}\rangle + \langle\beta|V_0 G_0'^{(+)} V_1|\psi_\alpha^{(+)}\rangle + \langle\beta|V_1|\psi_\alpha^{(+)}\rangle
$$

把后两项合并并利用 $\langle\beta|(1 + V_0 G_0'^{(+)}) = \langle\chi_\beta^{(-)}|$（这是 $\text{(chi-LS)}$ 的对偶版本对 $H'$ 演化得到的关系，类比 `T_and_U_operators.zh.md:248` 的 $\Omega_+|\alpha\rangle = (1 + G_0^{(+)} T)|\alpha\rangle$）：

$$
T_{fi} = \underbrace{\langle\beta|V_0|\chi_\alpha^{(+)}\rangle}_{\equiv T_{fi}^{(0)}} + \langle\chi_\beta^{(-)}|V_1|\psi_\alpha^{(+)}\rangle \tag{GMG-clean}
$$

第一项 $T^{(0)}$ 是 $V_0$ 单独的精确 T 矩阵——它由畸变波相移 $\delta_l^{(0)}$（通过 $V_0$ 的径向方程数值积分得到）完全决定。第二项含完整态 $|\psi^{(+)}\rangle$，仍然是精确的。

物理意义：$\text{(GMG-clean)}$ 把跃迁拆成两段——纯 $V_0$ 散射部分（不需要 $V_1$ 信息，已经精确解掉）+ 在 $V_0$ 提供的畸变波基底上由 $V_1$ 制造的额外跃迁。两段之间没有重复计算，因为 $V_1$ 项的右矢已经把 $V_0$ 的全部多次散射效应通过 $|\psi^{(+)}\rangle$ 吸收。

## DWBA 一阶截断

把 $\text{(GMG-clean)}$ 中的 $|\psi_\alpha^{(+)}\rangle$ 用畸变波近似

$$
|\psi_\alpha^{(+)}\rangle \approx |\chi_\alpha^{(+)}\rangle \tag{DWBA-approx}
$$

得到

$$
T_{fi}^{\rm DWBA} = \langle\beta|V_0|\chi_\alpha^{(+)}\rangle + \langle\chi_\beta^{(-)}|V_1|\chi_\alpha^{(+)}\rangle \tag{T-DWBA}
$$

第一项是 $V_0$ 单独的精确弹性 T 矩阵（"distorted elastic"），第二项是 DWBA 跃迁矩阵元。

弹性 vs 反应

- 弹性 ($\beta = \alpha$，无通道改变)：两项都贡献，第一项给 $V_0$ 的弹性散射振幅，第二项是 $V_1$ 引起的额外弹性修正。这一情形 $\text{(T-DWBA)}$ 退化为 Coulomb-distorted Born 类公式（下一节）。
- 反应 ($\beta \neq \alpha$，通道改变)：第一项消失（$V_0$ 不耦合通道，$\langle\beta|V_0|\chi_\alpha^{(+)}\rangle = 0$ 当 $\beta$ 与 $\alpha$ 是不同核状态时；这要求 $V_0$ 在通道空间是对角的），只剩 DWBA 跃迁矩阵元

$$
T_{fi}^{\rm DWBA, react} = \langle\chi_\beta^{(-)}|V_1|\chi_\alpha^{(+)}\rangle \tag{T-DWBA-react}
$$

这是核反应文献里默认的"DWBA 公式"，例如 (d, p) 转移、(p, p') 非弹性激发。

误差结构

把 $\text{(psi-LS-prime)}$ 完整迭代，

$$
|\psi_\alpha^{(+)}\rangle = |\chi_\alpha^{(+)}\rangle + G_0'^{(+)} V_1 |\chi_\alpha^{(+)}\rangle + G_0'^{(+)} V_1 G_0'^{(+)} V_1 |\chi_\alpha^{(+)}\rangle + \cdots
$$

代回 $\text{(GMG-clean)}$ 跃迁项给

$$
\langle\chi_\beta^{(-)}|V_1|\psi_\alpha^{(+)}\rangle = \langle\chi_\beta^{(-)}|V_1|\chi_\alpha^{(+)}\rangle + \langle\chi_\beta^{(-)}|V_1 G_0'^{(+)} V_1|\chi_\alpha^{(+)}\rangle + O(V_1^3)
$$

DWBA 一阶截断丢掉 $O(V_1^2)$ 项。准则：当

$$
\bigl|\langle\chi_\beta^{(-)}|V_1 G_0'^{(+)} V_1|\chi_\alpha^{(+)}\rangle\bigr| \ll \bigl|\langle\chi_\beta^{(-)}|V_1|\chi_\alpha^{(+)}\rangle\bigr| \tag{DWBA-criterion}
$$

时 DWBA 准。这是"在畸变波基底上 $V_1$ 是小扰动"的精确陈述——不是 $V_1$ 在自由波基底上小，而是在已经被 $V_0$ 畸变后的基底上小。

## Coulomb 退化与纯 Born 退化

### Coulomb 加短程势的特例

取 $V_0 = V_C$，$V_1 = V_{SR}$。畸变波就是 Coulomb 波（`coulomb_scattering.zh.md:177`-185 的 $\psi_C^{(\pm)}$）。$\text{(T-DWBA)}$ 化为

$$
T_{fi}^{\rm DWBA} = T_C(\beta\leftarrow\alpha) + \langle\psi_C^{(-)}(\mathbf k_f)|V_{SR}|\psi_C^{(+)}(\mathbf k_i)\rangle \tag{T-DWBA-Coul}
$$

第一项给 Rutherford 振幅 $f_C$（`coulomb_scattering.zh.md:190`），第二项给 $f_{SR}^{\rm CB}$（`coulomb_scattering.zh.md:311`）。总散射振幅 $f = f_C + f_{SR}^{\rm CB}$ 与 `coulomb_scattering.zh.md:264` 的 $\text{(f-decomp)}$ 完全一致。

这一致性是结构上必须的：B 篇是本篇的 $V_0 = V_C, V_1 = V_{SR}$ 特例，公式不可能不一致。但 B 篇先做了 Dollard 修正（因为 $V_C$ 长程），本篇把那一层抽象掉——只要承认 $\chi^{(\pm)}$ 存在（无论是经过 Dollard 还是直接 Cook 判据保证），DWBA 的代数结构对 $V_0$ 是否长程一视同仁。

### 纯 Born 退化

取 $V_0 = 0$，$V_1 = V$。则 $H' = H_0$，$|\chi^{(\pm)}\rangle = |\alpha\rangle$（自由平面波）。$\text{(T-DWBA)}$ 化为

$$
T_{fi}^{\rm DWBA}\bigl|_{V_0 = 0} = \langle\beta|V|\alpha\rangle = \int d^3 r\, e^{-i\mathbf q\cdot\mathbf r} V(\mathbf r)
$$

经振幅约定 $f = -(2\pi)^2 \mu t$ 立得 $f^B$ 的纯 Born 公式 $\text{(f-B)}$。所以 DWBA 是纯 Born 的严格推广：把 $V_0$ 从零开拓到任意可处理势，主公式形式不变，自由波换成畸变波。

### 中间情形：DWBA 在两个极限之间

| 情形 | $V_0$ | $V_1$ | $\chi^{(\pm)}$ | DWBA 公式 |
|:--|:--|:--|:--|:--|
| 纯 Born | $0$ | $V$ | 平面波 $e^{i\mathbf k\cdot\mathbf r}$ | $\text{(f-B)}$ |
| Coulomb-distorted Born | $V_C$ | $V_{SR}$ | Coulomb 波 $\psi_C^{(\pm)}$ | $\text{(T-DWBA-Coul)}$ |
| 光学势 + 转移 | $U_a, U_b$（含吸收） | $V_{aA\to bB}$ | 光学畸变波（数值） | $\text{(T-DWBA-react)}$ |
| 完全无近似（极限） | $V$ | $0$ | 精确入态 $\psi^{(\pm)}$ | 等价于精确 T |

在四个层级里 DWBA 都给出唯一的封闭主公式。

## 分波形式

### 局域中心势的分波展开

设 $V_0(r), V_1(r)$ 都是局域中心势。畸变波径向函数 $\chi_l^{(\pm)}(k, r)$ 是

$$
\Bigl[-\frac{d^2}{dr^2} + \frac{l(l+1)}{r^2} + 2\mu V_0(r) - k^2\Bigr] \chi_l(k, r) = 0 \tag{rad-chi}
$$

满足 $\chi_l(k, 0) = 0$、渐近 $\chi_l(k, r) \to \sin(kr - l\pi/2 + \delta_l^{(0)}(k))$（$V_0$ 短程时）或 $F_l, G_l$ 组合（$V_0 = V_C$ 时；`coulomb_scattering.zh.md:276`）。

self-derive DWBA 跃迁矩阵元的分波展开。三维 DWBA 矩阵元

$$
M_{\rm DWBA}(\mathbf k_f, \mathbf k_i) = \langle\chi^{(-)}(\mathbf k_f)|V_1|\chi^{(+)}(\mathbf k_i)\rangle = \int d^3 r\, [\chi^{(-)}(\mathbf k_f, \mathbf r)]^* V_1(r)\, \chi^{(+)}(\mathbf k_i, \mathbf r)
$$

把畸变波分波展开（局域中心势下，类比平面波展开）

$$
\chi^{(+)}(\mathbf k, \mathbf r) = \frac{4\pi}{kr}\sum_{l m} i^l\, e^{i\delta_l^{(0)}(k)}\, \chi_l(k, r)\, Y_{lm}(\hat{\mathbf r})\, Y_{lm}^*(\hat{\mathbf k}) \tag{chi-pw}
$$

$\chi^{(-)}(\mathbf k_f, \mathbf r) = [\chi^{(+)}(-\mathbf k_f, \mathbf r)]^*$（时间反演关系）。代入并对 $\hat{\mathbf r}$ 积分（$V_1$ 中心，球谐正交），用加法定理 $\sum_m Y_{lm}(\hat{\mathbf k}_f) Y_{lm}^*(\hat{\mathbf k}_i) = (2l+1)/(4\pi)\, P_l(\cos\theta)$：

$$
M_{\rm DWBA}(\theta) = \frac{(4\pi)^2}{k_f k_i} \sum_{l=0}^{\infty} (2l+1)\, e^{i[\delta_l^{(0)}(k_f) + \delta_l^{(0)}(k_i)]}\, I_l\, P_l(\cos\theta)
$$

其中径向积分

$$
I_l(k_f, k_i) = \frac{1}{4\pi} \int_0^\infty dr\, \chi_l(k_f, r)\, V_1(r)\, \chi_l(k_i, r) \tag{Il}
$$

弹性 ($k_f = k_i = k$)：

$$
M_{\rm DWBA}^{\rm el}(\theta) = \frac{(4\pi)^2}{k^2}\sum_l (2l+1)\, e^{2i\delta_l^{(0)}(k)}\, I_l(k, k)\, P_l(\cos\theta) \tag{M-DWBA-el}
$$

把振幅约定 $f = -(\mu/2\pi) M$ 代入并跟 `partial_wave_projection.zh.md:360` 的 $f(\theta) = \sum_l(2l+1) f_l P_l(\cos\theta)$ 对照：

$$
f_l^{\rm DWBA, el}(k) = -\frac{8\pi\mu}{k^2}\, e^{2i\delta_l^{(0)}}\, I_l(k, k) \tag{fl-DWBA}
$$

把这个跟精确分波振幅 $f_l = (e^{2i\delta_l^{\rm tot}} - 1)/(2ik)$ 用 $\delta_l^{\rm tot} = \delta_l^{(0)} + \delta_l^{(1)}$、$\delta_l^{(1)} \ll 1$ 比较，给出 DWBA 下的 $\delta_l^{(1)}$：

$$
\delta_l^{(1), \rm DWBA}(k) \approx -\frac{2\mu}{k}\int_0^\infty dr\, [\chi_l(k, r)]^2\, V_1(r) \tag{delta1-DWBA}
$$

### 退化检验

$V_0 = 0$：$\chi_l(k, r) = (kr) j_l(kr)$（精确，自由 Riccati-Bessel），$\delta_l^{(0)} = 0$，$\text{(delta1-DWBA)}$ 化为

$$
\delta_l^{(1), B}(k) \to -2\mu k \int_0^\infty dr\, r^2\, j_l(kr)^2\, V_1(r)
$$

这正是 `partial_wave_projection.zh.md:348` 的纯 Born 相移。

$V_0 = V_C$：$\chi_l(\eta, kr) = F_l(\eta, kr)$（`coulomb_scattering.zh.md:106`），$\delta_l^{(0)} = \sigma_l(\eta)$，$\text{(delta1-DWBA)}$ 化为 `coulomb_scattering.zh.md:352` 的 $\delta_l^{SR, \rm CB}$ 公式。

### 一般情形

非局域 $V_0$（如 separable 势 `appendix_EST_seperable_HVH_Esym.md:97`）：$\chi_l^{(\pm)}$ 仍由相应 LS 方程给出，DWBA 矩阵元改为算符形式 $\langle\chi_l^{(-)}|V_1|\chi_l^{(+)}\rangle$ 在动量空间的积分；分波关系式 $\text{(fl-DWBA)}$ 形式不变。

非中心 $V_1$（含自旋-轨道、张量）：分波耦合 $l \to l \pm 2$ 等，$I_l$ 推广为耦合矩阵 $I_{l'l}$；这是 `partial_wave_projection.zh.md:396` 类型的耦合通道扩展。

含自旋的 DWBA：见后面"极化 DWBA"节。

## 多通道反应：弹性 + 非弹性 + 重排

### 通道空间与多通道 LS 方程

反应 $a + A \to b + B$（含 $b = a, B = A^*$ 的非弹性激发，$b \neq a$ 的重排）。通道指标 $\alpha = (a, A)$, $\beta = (b, B)$。每个通道有自己的内部状态（弹性散射的核内部本征态 $|A\rangle, |B\rangle$）和相对运动。通道哈密顿量

$$
H_\alpha = h_a + h_A + K_\alpha + U_\alpha(r_\alpha),\qquad H_\beta = h_b + h_B + K_\beta + U_\beta(r_\beta) \tag{H-channel}
$$

其中 $K$ 是相对动能，$U$ 是该通道的光学势（实部 + 吸收）。$h_a, h_A$ 是核内部哈密顿量。这与 `T_and_U_operators.zh.md:407` 的三体通道哈密顿量结构一致。

DWBA 选 $V_0 = U_\alpha$（入射通道光学势）或 $V_0 = U_\beta$（出射通道光学势，对应 prior 还是 post form），$V_1 = V_{aA\to bB}$ 是把核状态从 $|A\rangle$ 改到 $|B\rangle$（含可能的核子转移）的算符。

入射通道畸变波 $\chi_\alpha^{(+)}$ 是 $H_0 + U_\alpha$ 的精确散射态（含 $|A\rangle$ 的内部态，相对运动由 $U_\alpha$ 畸变）；出射通道 $\chi_\beta^{(-)}$ 类似。

### DWBA 反应矩阵元

$$
T_{\beta\alpha}^{\rm DWBA} = \langle \chi_\beta^{(-)}\, b\, B | V_{aA\to bB} | \chi_\alpha^{(+)}\, a\, A\rangle \tag{T-react}
$$

显式写开内部坐标与相对坐标：

$$
T_{\beta\alpha}^{\rm DWBA} = \int d\mathbf r_\beta\, d\mathbf r_\alpha\, [\chi_\beta^{(-)}(\mathbf k_\beta, \mathbf r_\beta)]^* \langle b B | V_{aA\to bB} | a A\rangle_\text{core}\, \chi_\alpha^{(+)}(\mathbf k_\alpha, \mathbf r_\alpha)
$$

中间 $\langle bB|V|aA\rangle_\text{core}$ 是核形状因子（form factor），由内部波函数（壳模型/玻尔-莫泰尔松/集体模型）算出。这一部分在反应理论里独立处理。

### 应用例

(d, p) 单核子转移：$a = d$（氘核），$A$ = 靶核，$b = p$（质子），$B = (A+1)$核（俘获了一个中子）。$U_\alpha$ 是 $d + A$ 光学势，$U_\beta$ 是 $p + (A+1)$ 光学势，$V_{1}$ 含 deuteron 内部 $\langle p | V_{np} | d\rangle$ 矩阵元 + 中子在 $(A+1)$ 中的束缚态波函数。微分截面正比于 spectroscopic factor $S_{nlj}$（核结构信息，独立于反应机制）。

(p, p') 非弹性激发：$a = b = p$，靶从基态 $|A\rangle$ 跃迁到激发态 $|A^*\rangle$。$V_1$ 是核的多极矩跃迁算符，DWBA 振幅含核结构 form factor $\rho_{tr}^{(\lambda)}(r)$。

(p, n) 电荷交换：$a = p, b = n$，靶核同位旋投影改变。$V_1$ 含 isovector 部分 $V_\tau\, \boldsymbol\tau_a \cdot \boldsymbol\tau_A$。

每一类反应的核形状因子由该领域的核结构计算单独给出；DWBA 框架本身是结构无关的"外场+畸变"骨架。

### 与多通道 LS 方程的关系

`partial_wave_projection.zh.md:396` 的耦合通道 LS 方程 $T^J_{l'l}$ 是精确多通道处理。DWBA 是它的"一阶在 $V_1$ 上"截断：把通道间耦合矩阵元 $V^J_{l'l}$ 中的对角部分（自身光学势）放进 $V_0$，把非对角部分（通道转移）放进 $V_1$，对 $V_1$ 一阶 Born。当通道间耦合弱时（即 elastic dominates over reaction），DWBA 准；当通道间耦合强时（如重核破坏散射），需要耦合通道（CC）方法。

## 光学势加 DWBA 的核物理实践

### 复光学势作 $V_0$

`appendix_EST_seperable_HVH_Esym.md:13` 的 Woods-Saxon 光学势

$$
U(r) = -V_0\, f(r) - i\,W_0\, f_I(r) \tag{WS}
$$

把它当 DWBA 的 $V_0$。复光学势下 $\text{(rad-chi)}$ 改为

$$
\Bigl[-\frac{d^2}{dr^2} + \frac{l(l+1)}{r^2} + 2\mu U(r) - k^2\Bigr] \chi_l(k, r) = 0
$$

$\chi_l$ 是复值函数，模 $|\chi_l(k, r)|$ 在内部（$r < R$）随 $W_0$ 衰减——这是吸收的物理体现：粒子进入核内后部分 flux 被非弹性 / 吸收通道夺走。

分波相移 $\delta_l^{(0)}(k) = \delta_l^R(k) + i\delta_l^I(k)$ 复数，分波 S 矩阵 $|S_l| = |e^{2i\delta_l^{(0)}}| = e^{-2\delta_l^I} < 1$（吸收使幺正性破坏，转入未明示通道）。这与 `appendix_EST_seperable_HVH_Esym.md:33` 的描述一致。

### EST 与 DWBA 的分工

EST（`appendix_EST_seperable_HVH_Esym.md:121`-129）把光学势 $U$ 转写为有限秩 separable 形式 $U_{\rm sep} = \sum_n |g_n\rangle \lambda_n \langle g_n|$，使弹性 LS 方程退化为代数方程，$\chi^{(\pm)}$ 闭式可得。

DWBA 则把 $U$ 当作精确背景，对剩余微扰 $V_1$ 做一阶 Born。两者的分工：

- EST 解决 "$V_0$ 弹性散射怎么精确算"——既可以数值 Numerov 也可以 separable 化
- DWBA 解决 "在 $V_0$ 已经精确解掉的前提下，怎么处理小微扰 $V_1$"

合起来：用 EST 的 $\chi^{(\pm)}$ 作畸变波，代入 $\text{(T-DWBA-react)}$ 算反应矩阵元。这就是核反应理论里"光学势 + DWBA"的标准流程。

### 实例

$E_p = 30$ MeV 的 $(p, p')$ 在 ${}^{40}\text{Ca}$ 上激发到 $3^-$ 集体态：$U_\alpha = U_\beta$ 取 KD03 全局光学势，$V_1$ 是 $3^-$ 跃迁的 $\rho_{tr}^{(3)}(r)$（由壳模型算）；DWBA 微分截面与实验数据通常吻合到 20% 以内（共振区域更差，需要 CC）。

$E_d = 12$ MeV 的 $(d, p)$ 在 ${}^{16}\text{O}$ 上俘获中子至 ${}^{17}\text{O}$ 基态（$1d_{5/2}$ 单粒子）：$U_\alpha$ 取 deuteron 光学势，$U_\beta$ 取 proton 光学势，$V_1 = V_{np}$，$\langle B | V | A\rangle_\text{core}$ 含 ${}^{17}\text{O}$ 基态 $1d_{5/2}$ 中子束缚态波函数；DWBA 给出 spectroscopic factor $S = 1.0 \pm 0.1$。

## 极化 DWBA

### 含自旋的畸变波

把粒子自旋 $s_a, s_A$ 引入。畸变波在自旋空间是 $(2s_a+1)(2s_A+1)$ 维向量

$$
\chi^{(\pm)}_{m_a m_A}(\mathbf k, \mathbf r) \in V_{s_a} \otimes V_{s_A}
$$

光学势 $V_0$ 在自旋空间一般是矩阵（含中心 + 自旋-轨道项 $V_{LS}(r)\, \mathbf L\cdot\mathbf S$ + 张量等）：

$$
V_0 = V_C(r) + V_{LS}(r)\, \mathbf L\cdot\mathbf s_a + \cdots
$$

径向方程在耦合基 $|(l, s_a) j m_j; s_A m_A\rangle$ 中分块对角，每块给出 $\chi_{l, s_a, j}^{(0)}(k, r)$ 与对应的相移 $\delta_l^{j, (0)}$。

### DWBA 的 M 矩阵

`polarization_formalism.zh.md:41` 定义 M 矩阵 $M_{m'_b m'_B; m_a m_A}(\mathbf k', \mathbf k)$；DWBA 跃迁矩阵元 $\text{(T-DWBA-react)}$ 在自旋指标上展开得

$$
M_{m'_b m'_B; m_a m_A}^{\rm DWBA} = -\frac{\mu_\beta}{2\pi}\, \langle \chi_\beta^{(-), m'_b m'_B}(\mathbf k_\beta) | V_{aA\to bB} | \chi_\alpha^{(+), m_a m_A}(\mathbf k_\alpha)\rangle \tag{M-DWBA}
$$

带有完整的入射、出射自旋指标。$V_1$ 的自旋结构（中心、自旋-翻转、张量）决定 M 的算符分解（A 篇主公式 `polarization_formalism.zh.md:60` 的具体化）。

### dpol 应用

氘核 $d$ 加靶核 $A$ 的弹性 / 反应散射，$d$ 自旋 1：M 矩阵 $M_{m'_d m'_a; m_d m_a}$ 是 $3 \times 3$（$s_a = 0$ 简化情形）。光学势 $V_0 = U_C(r) + U(r) + U_{LS}(r) \mathbf L\cdot\mathbf s_d + U_T(r) S_{12}(\hat r)$ 含自旋-轨道 + 张量。

DWBA 给出张量分析力 $iT_{11}, T_{20}, T_{21}, T_{22}$ 的能量依赖：直接由 $\text{(M-DWBA)}$ 经 `polarization_formalism.zh.md:80`-200 的极化代数得到。这是 dpol polarimeter 的理论基底——光学势参数（特别是张量项 $U_T$）从 dpol 测量值反推得到。

注：含 Coulomb 时 $V_0$ 应取 $U_C + U_{\rm nuc}$，畸变波是 Coulomb-distorted nuclear waves。`polarization_formalism.zh.md:538` 提到的 "含 Coulomb 长程势的修正" 在本框架内自动包含。

## DWBA 何时准、何时不准

### 物理判据

形式判据 $\text{(DWBA-criterion)}$ 给出二阶项相对一阶项的相对大小。在分波形式下化为：

$$
|\delta_l^{(1)}|^2 \ll |\delta_l^{(1)}| \quad\Leftrightarrow\quad |\delta_l^{(1)}| \ll 1\ \text{(每分波)}
$$

即 $V_1$ 引起的额外分波相移每分波都小。当 $|\delta_l^{(1)}| \sim O(0.1)$ 时 DWBA 通常 5%-10% 准；$\sim O(1)$ 时失效。

实际判据：

- 弹性 + 短程修正：$V_1$ 比 $V_0$ 小一个量级时（如 isospin-breaking 修正、Pauli blocking 修正）DWBA 准。
- (p, p') 集体激发：$V_1$ 是核形状变形，集体性不太强时（$\beta_\lambda \lesssim 0.1$）DWBA 准；强变形核（actinides, ${}^{154}\text{Sm}$ 等）需要 CC。
- (d, p) 转移：DWBA 在 $E_d \gtrsim 10$ MeV 时通常准；低能时 deuteron 破坏（$d \to p + n$ 三体）效应强，需要 ADWA / CDCC（连续离散化耦合通道）。
- 重离子 transfer：质量大、库仑高，畸变强但 transfer 也强，DWBA 经常失效；需要 CC 或 CRC（耦合反应通道）。

### 失败与下一步

DWBA 失效的下一步：

- 二阶 DWBA：保留 $\text{(GMG-clean)}$ 中 $|\psi^{(+)}\rangle$ 的二阶迭代项，得 $\langle\chi^{(-)}|V_1 G_0' V_1|\chi^{(+)}\rangle$。这是中间态求和，对 (p, p') 高激发态、(p, t) 双核子转移等有效。
- 耦合通道 (CC)：把多通道 LS 方程精确求解，不做 $V_1$ 微扰。耦合通道方程组在分波耦合基下化为一阶常微分方程组（CHUCK, FRESCO, ECIS 等代码）。
- CDCC（连续离散化 CC）：把 $d$ 的连续 breakup 状态离散化为伪态，再做 CC。处理 $d, {}^{6}\text{Li}, {}^{6}\text{He}$ 等弱束缚弹核的反应。

### 与 EST 的对照

EST 是"弹性散射的精确 separable 化"（`appendix_EST_seperable_HVH_Esym.md:121`）；它在 elastic channel 内是精确的，但只处理弹性。DWBA 是"非弹性 / 反应的微扰"；它给出反应振幅但需要 elastic background 已知（来自 EST、Numerov 或其它精确弹性求解）。

两者互补：EST 提供 $\chi^{(\pm)}$ 的高效计算，DWBA 提供反应振幅的微扰公式。

## 与主线笔记的对账

| 主线知识点 | 对账位置 | 本篇对应位置 |
|:--|:--|:--|
| 两体 LS 方程 $T = V + VG_0 T$ | `T_and_U_operators.zh.md:296` | $\text{(LS-T)}$ + $\text{(psi-LS-prime)}$ |
| Born 级数与一阶 Born | `Green_operator.zh.md:116` + `S_matrix_and_cross_section.zh.md:506` | "Born 级数回顾" + 纯 Born 退化 |
| 波算符 $\Omega_\pm$ 与渐进态 | `T_and_U_operators.zh.md:80` | 畸变波 Møller 算符 $\text{(chi-Mol)}$ |
| 通道哈密顿量 $H_\alpha$ | `T_and_U_operators.zh.md:407` | 反应通道 $\text{(H-channel)}$ |
| Coulomb-distorted Born | `coulomb_scattering.zh.md:311` | DWBA 的 $V_0 = V_C, V_1 = V_{SR}$ 特例 $\text{(T-DWBA-Coul)}$ |
| Coulomb 波 $F_l$ 与 $\sigma_l$ | `coulomb_scattering.zh.md:106` | 分波 DWBA 退化检验 |
| 分波 LS 方程 | `partial_wave_projection.zh.md:340` | $\text{(rad-chi)}$ + $\text{(M-DWBA-el)}$ |
| 分波纯 Born 相移 | `partial_wave_projection.zh.md:348` | $V_0 = 0$ 退化 $\text{(delta1-DWBA)}$ |
| 耦合通道 $T^J_{l'l}$ | `partial_wave_projection.zh.md:396` | DWBA 是其 $V_1$ 一阶截断 |
| M 矩阵定义 | `polarization_formalism.zh.md:41` | DWBA 极化矩阵元 $\text{(M-DWBA)}$ |
| Wigner D 函数 | `partial_wave_projection.zh.md:226` | DWBA 旋转协变性 |
| Woods-Saxon 光学势 | `appendix_EST_seperable_HVH_Esym.md:13` | DWBA 复 $V_0$ 实例 |
| EST separable 形式 | `appendix_EST_seperable_HVH_Esym.md:121` | EST 与 DWBA 互补 |
| Coulomb 加短程势分解 | `coulomb_scattering.zh.md:264` | DWBA 一致性 |
| AGS 三体 $U_{\beta\alpha}$ | `T_and_U_operators.zh.md:519` | DWBA 是 AGS 弱耦合极限 |

每一条都可用 `grep -n` 在源文件中校验。

## next-step

- 数值 DWBA 演示（指向 `examples/12_dwba_demo`）：用 ${}^{40}\text{Ca}(p, p')$ 集体 $3^-$ 激发为标度模型，KD03 全局光学势 $U(r)$ 数值积分得复畸变波 $\chi_l(k, r)$，3- 跃迁形状因子 $\rho_{tr}^{(3)}(r)$ 取集体模型，按 $\text{(T-DWBA-react)}$ 数值求积。绘 $d\sigma/d\Omega(\theta)$ 曲线，与 PDG / EXFOR 数据对比。退化检验：$U \to 0$ 给出纯 Born，$E_p \to$ 高能极限给出 PWBA（plane-wave Born approximation）。
- 高阶 DWBA / Distorted-Wave Born Series：把 $\text{(psi-LS-prime)}$ 迭代到二阶、三阶，给出 $\langle\chi^{(-)}|V_1 G_0' V_1|\chi^{(+)}\rangle$ 等中间态求和；适用于双核子转移 (p, t)、二阶集体激发；与 sequential vs simultaneous 转移的物理区分。
- 耦合通道 (CC) 方法：把多通道 LS 方程 `partial_wave_projection.zh.md:396` 精确求解，不再对 $V_1$ 做 Born；FRESCO / ECIS / CHUCK 等代码的物理基底；与 DWBA 在弱耦合极限下重合的检验。
- DWBA 在转移反应 (d, p) 中的具体核形状因子：分离反应顶点 $\langle p | V_{np} | d\rangle$ 与束缚态波函数 $\phi_{nlj}^{(B)}(r)$；spectroscopic factor $S_{nlj}$ 的提取流程；ADWA（Johnson-Soper）对 zero-range vs finite-range 的处理；与 deuteron breakup 的 CDCC 方案对照。
- 与 Faddeev / AGS 三体散射的关系：DWBA 是 AGS（`T_and_U_operators.zh.md:595`）的弱耦合极限——把 AGS 方程组中通道间耦合 $T_\gamma G_0 U_{\gamma\alpha}$ 截断到一阶，且 $V_0$ 取相应通道光学势时退化为 DWBA。在三体破坏 $(d, p n)$、$(p, 2p)$ 等情形下三体精确处理与 DWBA 的差别可达数倍；这是核物理三体方法的判据。
- 屏蔽 Coulomb 与 DWBA 的相对论推广：电子-核电磁过程（电子散射 $(e, e')$）在 Born 近似下给出形状因子 $F(q^2)$，DWBA 给出 Coulomb-distorted 修正（"Mott 修正"），重核（$Z > 50$）下不可忽略；Dirac 方程下 $\chi^{(\pm)}$ 改为 Dirac 自旋子，结构上完全平行。
- DWBA 在弱相互作用过程中的应用：$(\nu, e^-)$ 反应、$(p, n)$ Gamow-Teller 跃迁、$\beta$ 衰变内的"过去式 DWBA"（弱矩阵元在核 distorted wave 基底上的修正）；与电弱标准模型的核结构耦合。
