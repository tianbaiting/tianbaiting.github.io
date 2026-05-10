# Jost 函数与解析性

前面几篇已经把分波相移 $\delta_l(k)$、分波 $S$ 矩阵 $S_l(k) = e^{2i\delta_l}$ 和分波振幅 $f_l(k) = (e^{2i\delta_l}-1)/(2ik)$ 都写出来了，但这些对象只在物理实 $k > 0$ 上定义。物理上想问的问题——束缚态在哪、共振在哪、虚态在哪、为什么 ${}^1 S_0$ 通道里 NN 散射长度奇大——都不能在实轴上回答；它们都是 $f_l(k)$ 解析延拓到复 $k$ 平面后的奇性。这一篇把这件事正面写出来：把分波振幅看作复 $k$ 函数，引入 Jost 函数 $F_l^\pm(k)$，把 $f_l$ 的极点结构归结到 $F_l^+$ 的零点结构。

这条主线笔记同时把已经在教学轨上各自处理过的极点搜索算法——`examples/03_delta_shell.zh.md` 的 $S_0$ 极点 Newton 迭代、`examples/05_separable_rank1.zh.md` 的 $\tau(E)$ 闭式分母、`examples/08_centrifugal_barrier.zh.md` 的 d 波极点轨迹——归到同一个解析框架下。后面两篇主线（Levinson + 有效力程定理、$S$ 矩阵在复 $E$ 平面的色散关系）都建立在这个 Jost 框架上。

## 目标与对账

放在最前的几条断言，本篇要把每一条都兑现：

- 分波振幅 $f_l(k)$ 在 $k$ 上半平面（短程势下）解析延拓存在，奇性是孤立极点。
- 极点位置完全由 Jost 函数 $F_l^+(k)$ 的零点决定：$f_l(k)$ 极点 $\Leftrightarrow$ $F_l^+(k) = 0$。
- 物理实极点（正虚轴）= 束缚态；下半平面极点（解析延拓）= 共振；负虚轴零点 = 虚态。
- 分波 $S$ 矩阵的紧凑形式是 $S_l(k) = F_l^-(k)/F_l^+(k)$，幺正性 $|S_l| = 1$（实 $k$）等价于 $F_l^+(k)^* = F_l^-(k)$。
- Levinson 定理把 $\delta_l(0) - \delta_l(\infty)$ 与 $F_l^+$ 在上半平面的零点数联系起来，证明用论域原理。
- $E = k^2$ 是双叶映射，物理面 = $\mathrm{Im}\,k > 0$，第二张面 = $\mathrm{Im}\,k < 0$。

## 为什么需要 Jost 函数

主线笔记 `S_matrix_and_cross_section.zh.md` 与 `partial_wave_projection.zh.md` 把 $S$ 矩阵的物理意义与分波展开都讲清楚了，但有几件事在那个层次上没法回答：

第一，$f_l(k)$ 的极点在哪？$f_l(k) = e^{i\delta_l(k)}\sin\delta_l(k)/k$ 这个写法只对实 $k > 0$ 成立。$\delta_l(k)$ 是实数，分子在实轴上没有极点；$k$ 在分母上让 $f_l$ 在 $k = 0$ 行为反常，但这不是真正的"束缚态极点"。要看到束缚态极点，需要把 $f_l$ 解析延拓到复 $k$ 平面，并解释 $\delta_l$ 在复 $k$ 上的"复化"是怎么发生的。

第二，幺正性 $|S_l| = 1$ 怎么写成自然的解析约束？若只写 $S_l = e^{2i\delta_l}$，幺正性靠 $\delta_l$ 实数性手工保证，离开实轴这条性质就失去意义。需要一个把幺正性写成"两个解析函数取共轭值"的形式。

第三，$f_l(k)$ 在 $k$ 平面的整体解析结构能否一次写出来？分波振幅在物理上既包含束缚态信息（极点）、又包含连续散射（实轴）、又包含共振（解析延拓后）。这些信息都应该统一进同一个解析对象的奇性结构里。

Jost 函数 $F_l^\pm(k)$ 同时解决这三件事：

- $f_l(k)$ 写成 $F_l^-/F_l^+ - 1$ 除以 $2ik$，极点完全归到 $F_l^+(k) = 0$ 上；
- 实势的对称性 $F_l^+(k)^* = F_l^-(k^*)$ 把幺正性化作两个解析函数的共轭关系；
- $F_l^+(k)$ 在上半 $k$ 平面（短程势下）解析，所有奇性是孤立零点，按位置归到束缚态、虚态、共振、阈值零能态四类。

## 短程势的径向方程与两组特解

记号沿用 `partial_wave_projection.zh.md:340` 与 `partial_wave_projection.zh.md:378`。取 $\hbar = 2\mu = 1$，分波径向方程为

$$
\Bigl[\frac{d^2}{dr^2} + k^2 - V(r) - \frac{l(l+1)}{r^2}\Bigr] u_l(k, r) = 0 \tag{rad}
$$

势 $V(r)$ 假定短程，强意义下要求 $\int_0^\infty r |V(r)|\, dr < \infty$ 且 $\int_1^\infty e^{2|\mathrm{Im}\, k|\, r}\,|V(r)|\, dr < \infty$。后者即 Yukawa 类指数衰减，保证下面定义的 Jost 解对 $k$ 在某个上半平面带状区域上解析。Coulomb 不满足这条，留到后面单独处理。

方程 (rad) 是二阶线性常微分方程，对每个 $k$ 都有两维解空间。把它"由原点定边界"和"由远处定边界"分别钉死，得到两组在物理上意义互补的特解。

regular 解 $\phi_l(k, r)$。在 $r \to 0$ 钉住边界条件

$$
\phi_l(k, r) \xrightarrow{r \to 0}\frac{r^{l+1}}{(2l+1)!!} \tag{phi-0}
$$

这条规则化条件挑出"在原点不发散"的那一支；$r^{l+1}$ 是 $V = 0$ 时的 Riccati–Bessel $\hat j_l(kr) = kr\, j_l(kr)$ 的小 $r$ 行为去掉 $k$ 依赖后的结果。规则解的存在性、对 $k^2$ 的整函数依赖性，都是 (rad) 在原点处的标准结果（Newton 第 12.1 节）。

Jost 解 $f_l^\pm(k, r)$。在 $r \to \infty$ 钉住边界条件

$$
f_l^\pm(k, r) \xrightarrow{r \to \infty} e^{\pm i k r} \tag{f-inf}
$$

记号上把"出射波 $e^{+ikr}$"作为 $f_l^+$，"入射波 $e^{-ikr}$"作为 $f_l^-$。注意这里渐近条件没有 $\mp i l\pi/2$ 的相位，纯粹是纯指数；这是 Jost 约定与物理"入出态"约定的差别，归到 $F_l^\pm$ 的归一化常数里去消化。

短程势的关键解析性结论：在 $\mathrm{Im}\,k > 0$ 的上半平面 $k$ 上，$f_l^+(k, r)$ 关于 $k$ 解析；在 $\mathrm{Im}\,k < 0$ 上半平面 $f_l^-(k, r)$ 解析。证明思路是把 (rad) 写成 Volterra 积分方程

$$
f_l^+(k, r) = e^{ikr} - \int_r^\infty G_0^l(k; r, r')\,V(r')\,f_l^+(k, r')\,dr'
$$

其中 $G_0^l(k; r, r')$ 是自由径向 Green 函数。Volterra 核在 $\mathrm{Im}\,k > 0$ 时有 $|G_0^l(k; r, r')| \leq C\, e^{-\mathrm{Im}\,k\,(r' - r)}$ 的指数衰减（利用 $f_0^{\pm} \to e^{\pm ikr}$ 的远场行为可显式构造），结合 $V$ 的衰减条件，迭代级数 $\sum_n f_l^{(n)}$ 逐项有界且一致收敛。每一项是 $k$ 的解析函数（因为积分核 $G_0^l$ 与边界条件 $e^{ikr}$ 都解析依赖 $k$ 在上半平面），一致收敛限里也保持解析。这就是"$f_l^+$ 在上半 $k$ 平面解析"的标准 Newton 12.1 节论证骨架。

两组解的相互关系 $f_l^-(k, r) = f_l^+(-k, r)$（实势）把上半平面解析性自动延拓到下半平面，但要付出复共轭的代价。具体地，把 $k \to -k$ 代入 (rad)，方程不变（只含 $k^2$），但边界条件 $e^{+ikr} \to e^{-ikr}$ 互换，故 $f_l^+(-k, r) = f_l^-(k, r)$。$f_l^-$ 的自然解析域是下半 $k$ 平面。

## Jost 函数的两个等价定义

把 regular 解 $\phi_l(k, r)$ 在远处展开成两组 Jost 解的线性组合。$\phi_l$ 在远处既然满足 (rad) 的渐近自由方程，那它必然写成 $e^{+ikr}$ 与 $e^{-ikr}$ 的线性组合。把这两个组合系数取出来，就得到 Jost 函数。

定义一：远场展开。

$$
\phi_l(k, r) \xrightarrow{r \to \infty} \frac{1}{2 k^{l+1}}\bigl[F_l^-(k)\, e^{ikr} - (-1)^l\, F_l^+(k)\, e^{-ikr}\bigr] \tag{F-asy}
$$

这个归一化（来自 Newton (12.27)）的好处是让 $V \to 0$ 时退化到 $\phi_l \to k^{-(l+1)}\,\hat j_l(kr) \sim k^{-(l+1)}\sin(kr - l\pi/2)$，即 $F_l^\pm \to 1$。

定义二：Wronskian。两个 (rad) 的解 $u_1, u_2$ 的 Wronskian $W[u_1, u_2] = u_1 u_2' - u_1' u_2$ 与 $r$ 无关（因为 (rad) 没有一阶项）。$F_l^\pm$ 可以等价定义为

$$
F_l^\pm(k) = \frac{(\mp k)^{-l}}{(2l+1)!!}\, W\!\bigl[f_l^\pm(k, \cdot),\, \phi_l(k, \cdot)\bigr] \tag{F-W}
$$

证明 (F-asy) $\Leftrightarrow$ (F-W)：在 $r \to \infty$ 用 (F-asy) 与 (f-inf) 直接算 Wronskian。$f_l^+(k, r) \to e^{ikr}$，$f_l^{+ \prime}(k, r) \to ik\, e^{ikr}$；$\phi_l \to (2k^{l+1})^{-1}[F_l^- e^{ikr} - (-1)^l F_l^+ e^{-ikr}]$，$\phi_l' \to (2k^{l+1})^{-1}[ik F_l^- e^{ikr} + (-1)^l ik F_l^+ e^{-ikr}]$。代入

$$
W[f_l^+, \phi_l] = e^{ikr}\, \phi_l' - ik e^{ikr}\, \phi_l
= (2k^{l+1})^{-1}\bigl[2 ik\,(-1)^l\,F_l^+\bigr] = \frac{(-1)^l\, i\, F_l^+}{k^l}
$$

代入 (F-W) 的 $F_l^+$ 公式（取 $\mp = -$ 对应正号 Jost 解）确实复原，常数 $1/(2l+1)!!$ 来自 (phi-0) 的小 $r$ 行为，这里跳过严格的归一对账。

两个定义各有用处。(F-asy) 直观，把 $F_l^\pm$ 看作"散射波的入射与出射振幅"；(F-W) 简洁，因 Wronskian 与 $r$ 无关，只要 $\phi_l$、$f_l^\pm$ 各算出一次，在任意 $r$ 上做一次代数即得 $F_l^\pm$。数值上后者更稳定（实践上选 $r$ 在势支撑外，这时 $\phi_l$ 已积分到自由区，$f_l^+$ 就是纯 $e^{ikr}$，Wronskian 退化成代数）。

零势检验。$V \equiv 0$ 时，规则解就是 Riccati–Bessel $\phi_l(k, r) = k^{-(l+1)}\,\hat j_l(kr)/(2l+1)!! \cdot ((2l+1)!!) = \hat j_l(kr)/k^{l+1}$（用 $\hat j_l$ 在原点行为 $\hat j_l(x) \to x^{l+1}/(2l+1)!!$ 验证 (phi-0)）；Jost 解 $f_l^\pm(k, r)$ 退化为 Riccati–Hankel $\hat h_l^{(\pm)}(kr)$，远场行为 $\hat h_l^{(\pm)}(x) \to (\mp i)^{l+1}\, e^{\pm ix}$ 满足 (f-inf) 的归一化（差一个 $(\mp i)^{l+1}$ 因子，已并入 (F-W) 系数 $(\mp k)^{-l}$）。$\hat j_l$ 的远场展开 $\hat j_l(x) \to \sin(x - l\pi/2) = (e^{i(x - l\pi/2)} - e^{-i(x - l\pi/2)})/(2i)$ 代入 (F-asy)，比对系数得 $F_l^\pm \equiv 1$。这是归一化常数 $1/[(2l+1)!! \cdot 2 k^{l+1}]$ 的来源——选这个归一就是为了让自由极限 $F_l^\pm = 1$。

短程势加进来后，$F_l^\pm(k)$ 偏离 $1$ 的程度由 $V$ 的作用强度决定。Born 极限下

$$
F_l^+(k) \approx 1 - \int_0^\infty dr\, V(r)\,[\hat j_l(kr)]^2 \cdot \text{(归一化系数)}
$$

至 $V$ 的一阶；高阶贡献来自 Volterra 迭代。$F_l^+ = 0$ 的零点对应"势效应足够强，使得 1 减去某正定积分（吸引势下）变零"，几何上自然给出束缚态。

## 对称性与分波 $S$ 矩阵

对实势，$V(r) = V(r)^*$。复共轭整条 (rad)，把 $k \to k^*$，得到 $f_l^\pm(k^*, r)^* = f_l^\mp(k, r)$（用边界条件验证），$\phi_l(k^*, r)^* = \phi_l(k, r)$（因 (phi-0) 与 $k$ 无关，且 (rad) 系数对 $k^2$ 是 $k$ 的函数）。代入 Wronskian 定义

$$
F_l^+(k)^* = F_l^-(k^*) \tag{F-conj}
$$

实 $k > 0$ 时 $k^* = k$，所以 $F_l^-(k) = F_l^+(k)^*$，两者只差复共轭。

把 (F-conj) 与 (F-asy) 结合，看 $\phi_l(k, r)$ 在实 $k$ 上的远场。$F_l^- = (F_l^+)^*$，所以 $\phi_l \to (2k^{l+1})^{-1}[(F_l^+)^* e^{ikr} - (-1)^l F_l^+ e^{-ikr}]$，可以重写为

$$
\phi_l(k, r) \xrightarrow{r \to \infty} \frac{|F_l^+(k)|}{k^{l+1}}\,(-1)^l\, \sin\!\Bigl(kr - \frac{l\pi}{2} + \delta_l(k)\Bigr)
$$

只要把 $F_l^+(k) = |F_l^+(k)|\, e^{-i\delta_l(k)}$ 中的相位定义成相移。这给出实轴上的物理识别：

$$
F_l^+(k) = |F_l^+(k)|\, e^{-i\delta_l(k)},\quad k > 0 \tag{F-phase}
$$

由 (F-conj) 立即 $|F_l^-(k)| = |F_l^+(k)|$，于是

$$
S_l(k) = \frac{F_l^-(k)}{F_l^+(k)} = \frac{|F_l^+(k)|\, e^{+i\delta_l(k)}}{|F_l^+(k)|\, e^{-i\delta_l(k)}} = e^{2i\delta_l(k)} \tag{S-Jost}
$$

这与 `partial_wave_projection.zh.md:378` 的 $S_l = e^{2i\delta_l}$ 一致；幺正性 $|S_l| = 1$ 在 (S-Jost) 写法下是 (F-conj) 的一行推论。

## 分波振幅与 $F_l^+$ 零点

把 (S-Jost) 代入 $f_l(k) = (S_l(k) - 1)/(2ik)$：

$$
f_l(k) = \frac{1}{2ik}\bigl[\frac{F_l^-(k)}{F_l^+(k)} - 1\bigr] = \frac{F_l^-(k) - F_l^+(k)}{2ik\, F_l^+(k)} \tag{f-Jost}
$$

(f-Jost) 是这一篇的中心公式。它把分波振幅写成两个解析函数的比，分母是 $F_l^+(k)$。$F_l^+(k)$ 在上半 $k$ 平面解析（前一节结论），所以 $f_l(k)$ 在上半平面的奇性必然来自 $F_l^+(k)$ 的零点（分子在 $F_l^+ = 0$ 处一般非零；若同时为零，则是高阶奇性，是不一般情形）。这就是"$f_l$ 极点 $=$ $F_l^+$ 零点"这条断言的内容。

留数解读。在 $F_l^+(i\kappa) = 0$ 处对 $f_l(k)$ 做留数：

$$
\operatorname*{Res}_{k = i\kappa} f_l(k) = \frac{F_l^-(i\kappa) - F_l^+(i\kappa)}{2 i\kappa\, F_l^{+\prime}(i\kappa)} = \frac{F_l^-(i\kappa)}{2 i\kappa\, F_l^{+\prime}(i\kappa)}
$$

留数的模 $|\operatorname{Res}|$ 与束缚态波函数归一化常数（$\int|\phi_l|^2\,dr$）通过 $F_l^{+\prime}$ 因子相联系。这是 ANC（asymptotic normalization constant，渐近归一化常数）的解析根源——核物理低能反应（如 ${}^7\mathrm{Be}(p,\gamma){}^8\mathrm{B}$、$d(d, p)t$）观测量经常归到 ANC，$\mathrm{ANC}^2 \propto |\operatorname{Res} f_l|$ 数量级。$F_l^{+\prime}$ 是束缚态波函数斜率信息的 Jost 函数版本。

## 零点的物理分类

$F_l^+(k)$ 在复 $k$ 平面上的零点位置完整决定了散射的解析结构。按零点位置可以分四类。

正虚轴零点：束缚态。设 $F_l^+(i\kappa) = 0$，$\kappa > 0$。由 (F-W) 与 $f_l^+(i\kappa, r) \to e^{-\kappa r}$ 远场指数衰减，再由 Wronskian 为零意味着 $\phi_l(i\kappa, r)$ 与 $f_l^+(i\kappa, r)$ 线性相关，即 $\phi_l(i\kappa, r) \propto e^{-\kappa r}$ 在远处指数衰减，加上 (phi-0) 在原点 $r^{l+1}$ 规则，正好就是 $L^2$ 束缚态波函数。能量 $E_b = (i\kappa)^2 = -\kappa^2 < 0$。这与 `Green_operator.zh.md:412` 的谱分解一致：束缚态在 $G(z)$ 的 $z$ 实负轴上是真极点。

负虚轴零点：虚态（virtual / antibound state）。$F_l^+(-i\kappa) = 0$，$\kappa > 0$。这一点本身在物理面外面（下半 $k$ 平面），不是 $f_l$ 的物理面极点。但若把 $F_l^-(k)$ 的零点放进来看（由 (F-conj)，$F_l^-$ 的下半平面零点 = $F_l^+$ 的上半平面零点的共轭），$F_l^+(-i\kappa) = 0$ 等价于 $F_l^-(i\kappa) = 0$，对应的是 $f_l$ 在物理面外的零点而非极点。$\phi_l(-i\kappa, r) \propto e^{+\kappa r}$ 在远处指数发散，不是 $L^2$。物理上重要的不是这一点本身，而是它如果靠近实轴（小 $\kappa$），就把实 $k = 0$ 阈值附近的散射长度推到极大。s 波 NN 散射 ${}^1 S_0$ 通道的 $a_0 \approx -23.7$ fm 大散射长度就是这个机制——在那里 $\kappa \approx 0.04$ fm⁻¹，对应的虚态能量 $E_v \approx -0.066$ MeV，几乎贴在零阈值下方。

实轴 $k = 0$ 零点：阈值零能态。$F_l^+(0) = 0$ 是临界情形：束缚态能量 $E_b \to 0^-$ 时 $\kappa \to 0$，零点滑到原点。这种"在阈值上"的零点会让 $f_l(k)$ 在 $k = 0$ 行为反常（s 波下散射长度发散），它也修正 Levinson 定理常数（下面会说）。

上半平面非虚轴零点：禁止。短程实势下，$F_l^+(k) = 0$ 在上半 $k$ 平面只能落在正虚轴上。证明：若 $F_l^+(k_0) = 0$，$k_0 = a + ib$，$b > 0$，$a \neq 0$，则 $\phi_l(k_0, r) \propto e^{ik_0 r} = e^{i a r - b r}$ 远处指数衰减，是个 $L^2$ 本征态。但 $H = -d^2/dr^2 + V + l(l+1)/r^2$ 是自伴算符，本征值必为实数；而 $E_0 = k_0^2 = a^2 - b^2 + 2 i a b$ 在 $a \neq 0$ 时虚部 $2ab \neq 0$，矛盾。所以 $a = 0$，$k_0$ 在虚轴上。

第二张面（下半 $k$ 平面）零点：共振。$F_l^+(k_R - i k_I) = 0$，$k_R > 0$，$k_I > 0$。这一点不在 $F_l^+$ 的解析定义域内（前面强调 $F_l^+$ 短程势下在上半平面解析），但通过把 (F-W) 中的 $f_l^+(k, r)$ 显式解析延拓——对充分指数衰减的 $V$，$f_l^+(k, r)$ 可延拓到 $-\mathrm{Im}\,k < \alpha$ 的某个带状区域，其中 $\alpha$ 是势的衰减率——可以把 $F_l^+$ 延拓到下半平面有限带。在这个延拓后的函数里，下半平面零点对应共振。

能量映射（下面再细说）给

$$
E_R - i\Gamma/2 = (k_R - i k_I)^2 = k_R^2 - k_I^2 - 2 i k_R k_I,
\quad \Gamma = 4 k_R k_I \tag{ER-Gamma}
$$

(ER-Gamma) 与 `friedrichsModel.zh.md:551` 的 $z_* = E_R - i\Gamma_R/2$ 是同一对象。$\Gamma > 0$ 由 $k_R, k_I > 0$ 自动保证。

把上面四类零点画在一张概念图（口头描述：复 $k$ 平面，实轴水平、虚轴竖直）上：上半平面只有正虚轴上的束缚态零点；下半平面包含负虚轴的虚态、第三象限与第四象限的共振对（共振总成对出现，因 $F_l^+(k)^* = F_l^-(k^*) \neq F_l^+(-k^*)$ 在一般势下，但若进一步要求时间反演 $S(k)^* = S(-k)$，则下半平面零点关于虚轴对称分布；详见 `S_matrix_and_cross_section.zh.md` 与时间反演主线）。共振极点必然成对：$(k_R - i k_I, -k_R - i k_I)$，对应 $E_R - i\Gamma/2$ 与 $E_R^* - i\Gamma/2 = E_R - i\Gamma/2$（实部相同，因 $E$ 是 $k$ 偶函数）——但这是 $E$ 平面同一个共振，$k$ 平面两个根。

## 复 $k$ 平面与复 $E$ 平面

$E = k^2$ 是 $k \to E$ 的双叶映射，分支点在 $E = 0$。两张面的具体对应：

物理面 = 上半 $k$ 平面 $\mathrm{Im}\,k > 0$。这一面包含 $E$ 平面的"第一张"，即从正实轴取 $k = +\sqrt{E}$（$E > 0$），从负实轴取 $k = i\sqrt{|E|}$（$E < 0$）。负实轴对应 $\mathrm{Im}\,k > 0$ 正虚轴，正是束缚态 $E_b = -\kappa^2 < 0$ 在 $k = i\kappa$ 的位置。$E$ 平面正实轴是切割（连续谱），$G(z)$ 在那里有跳跃 (`Green_operator.zh.md:443`)，对应 $k$ 平面实正轴是 $F_l^+$ 与 $F_l^-$ 互换共轭的边界。

第二张面 = 下半 $k$ 平面 $\mathrm{Im}\,k < 0$。从 $E$ 平面正实轴上方穿过切割向下走，绕分支点回到原位时进入第二张；按 $E = k^2$ 反查，$E$ 第一张 $\mathrm{Im}\, E > 0$ 加切割上沿对应 $k$ 第一象限实部正、虚部正，穿切割后进入第四象限实部正、虚部负。所以共振极点 $k_R - i k_I$（$k_R, k_I > 0$）落在第四象限，对应 $E = E_R - i\Gamma/2$ 第二张面下半部。这正是 `Green_operator.zh.md:470` 与 `Green_operator.zh.md:480` 的图像。

把两张面拼起来看：

- 物理面正虚轴 $k = i\kappa$，对应 $E$ 第一张面负实轴 $E_b = -\kappa^2$（束缚态）；
- 物理面正实轴 $k > 0$，对应 $E$ 第一张面正实轴 $E > 0$（连续谱）；
- 第二张面（下半 $k$）负虚轴 $k = -i\kappa$，对应 $E$ 第二张面负实轴（虚态）；
- 第二张面下半第四象限 $k = k_R - i k_I$，对应 $E$ 第二张面下半 $E_R - i\Gamma/2$（共振）。

这条字典完整解释了为什么 `examples/03_delta_shell.zh.md` 第 79 行的衰变态极点会落在"下半 $k$ 平面"，为什么 `examples/08_centrifugal_barrier.zh.md` 的 d 波极点扫描出现的轨迹是"$V_0$ 增大时极点从下半第四象限爬到正虚轴"——共振变束缚态的过程在 $k$ 平面就是极点穿过实轴。

为什么要分两张面而不是直接在 $E$ 平面上看？$F_l^+(k)$ 在 $k$ 平面是单值解析（上半平面），而对应的 $F_l^+$ 看作 $E = k^2$ 的函数会变成多值——在 $E$ 平面上必须取分支割（标准选取沿 $E > 0$ 实轴），切割上下沿对应不同的 $k$ 值。$k$ 视角的好处是：单值、解析、零点位置直接读；$E$ 视角的好处是：跟物理量纲（能量）对齐，色散关系、Mandelstam 表象都自然写在 $E$ 上。两者互补，不偏废。

## Levinson 定理与论域原理

把上面的结论翻译成一条积分恒等式：在上半 $k$ 平面取大半圆围道 $C_R$，由实轴段 $[-R, R]$ 与上半平面半圆段 $\Gamma_R$ 组成，对 $\log F_l^+(k)$ 的导数沿 $C_R$ 积分。论域原理给出

$$
\frac{1}{2\pi i}\oint_{C_R} \frac{d}{dk}\log F_l^+(k)\, dk = N_l \tag{argP}
$$

其中 $N_l$ 是 $F_l^+$ 在 $C_R$ 包围区域内的零点数（计重数）。前一节论证了上半平面零点都在正虚轴上，对应束缚态，所以 $R \to \infty$ 时 $N_l = n_l$，即第 $l$ 分波束缚态数。

把围道积分拆开。实轴段：

$$
\int_{-R}^{R} \frac{F_l^{+\prime}(k)}{F_l^+(k)}\, dk
$$

用 (F-phase)：在 $k > 0$ 上 $\log F_l^+(k) = \log|F_l^+(k)| - i \delta_l(k)$。$\log|F_l^+|$ 是实数，沿实轴积分给出实部，对相位的论域贡献为零；$-i\delta_l$ 给纯虚贡献。将 $k < 0$ 一段用 $F_l^+(-k) = F_l^-(k) = F_l^+(k)^*$（实势对称）翻折，并约定相移在 $k = 0$ 起点，得到

$$
\int_{-R}^{R} \frac{F_l^{+\prime}(k)}{F_l^+(k)}\, dk = -2 i\,[\delta_l(R) - \delta_l(0)] + (\text{实部})
$$

（实部最终在虚部恒等式上不出现。）

半圆段。短程势下 $V(r)$ 衰减足够快，$F_l^+(k) \to 1$ 当 $|k| \to \infty$ 在上半平面（这是 Volterra 迭代展开零阶项），所以 $\log F_l^+ \to 0$，$\int_{\Gamma_R} d\log F_l^+ \to 0$。$\delta_l(R) \to \delta_l(\infty)$。

把两段加起来代入 (argP)，取虚部：

$$
\frac{1}{2\pi i}\cdot (-2i)\,[\delta_l(\infty) - \delta_l(0)] = n_l
$$

$$
\boxed{\;\delta_l(0) - \delta_l(\infty) = n_l \pi\;} \tag{Levinson}
$$

这就是 Levinson 定理的标准形式。物理含义：低能相移与高能相移之差等于 $\pi$ 乘束缚态数。约定 $\delta_l(\infty) = 0$（高能下势的影响消失），定理化为 $\delta_l(0) = n_l \pi$，意味着低能相移完全由束缚态计数决定。这也解释了为什么强吸引势会让 $\delta_l(k)$ 在低能"绕一圈"——每多一个束缚态，低能相移就多 $\pi$。

在数值上验证 Levinson 定理是检查相移代码是否正确的常用 sanity check：把 $\delta_l(k)$ 从 $k = 0$ 一直积分到 $k = \infty$（或截断到大 $k$），数 $\pi$ 的个数与独立计算的束缚态数比对。s 波 NN ${}^1 S_0$ 通道无束缚态但虚态把 $\delta_0(0) = 0^+$（按修正版 (Levinson-mod) 给出 $n_l^{1/2} = 1/2$ 的边缘行为），$\delta_0(\infty) \approx -\pi$（指实验拟合相移在大 $k$ 行为）；${}^3 S_1$ 通道有氘核束缚态，$n_0 = 1$，$\delta_0(0) = \pi$、$\delta_0(\infty) \to 0$，差正好是 $\pi$。

证明的微妙处。上面用了"半圆段贡献为零"和"实轴段虚部"两步，其中半圆贡献为零依赖 $F_l^+(k) \to 1$ 的速度。短程指数衰减势严格保证（Volterra 零阶项主导）；纯短程幂律衰减势 $V \sim 1/r^n$（$n > 2$）也成立但需要更细的渐近分析；Coulomb 势上半圆贡献不为零，Levinson 定理需修改成 Coulomb 版本（含 $\eta$ 依赖的常数项）。这就是为什么把 Levinson 和 Coulomb 分开讲是必要的。

另一个微妙处：$\delta_l(k)$ 是按 (F-phase) 从 $\arg F_l^+$ 定义的"绝对相移"，不是文献里常见的 mod $\pi$ 约定。两者差一个整数倍 $\pi$，但 Levinson 定理对的是绝对相移（连续积分得到的，零能起点 $\delta_l(0) = n_l\pi$，高能终点 $\delta_l(\infty) = 0$）。数值代码里用 $\arctan$ 给出的相移是 mod $\pi/2$ 的，需要 unwrap（连续追踪经过 $\pi/2$ 的次数）才能用于 Levinson 验证。这一点也是写相移代码时最常出错的地方。

零阈值修正。如果 $F_l^+(0) = 0$（阈值零能态），围道在 $k = 0$ 处必须做小半圆绕避，绕避方向贡献 $\pm\pi i$ 的额外项，对应公式右边加上 $\pi/2$（s 波下）或不变（高分波下，因角动量势垒压制零能行为）。规范的修正陈述：

$$
\delta_l(0) - \delta_l(\infty) = (n_l + n_l^{1/2})\, \pi,\quad n_l^{1/2} = \begin{cases}1/2 & l=0 \text{ 且 } F_0^+(0) = 0 \\ 0 & \text{其它}\end{cases} \tag{Levinson-mod}
$$

这条修正在 NN s 波 ${}^1 S_0$ 通道里看得最清楚——零阈值附近的虚态把这一项推到 $1/2$ 的边缘，给出反常大的散射长度。

## 极点 vs 零点：物理面 vs 第二张面再细化

主线笔记中"束缚态是物理面实极点、共振是第二张面复极点"（`Green_operator.zh.md:478` 与 `Green_operator.zh.md:480`）的图像，在 Jost 函数语言下要更精确表述："物理面极点对应 $F_l^+$ 在上半 $k$ 平面的零点（必在正虚轴）"，"第二张面极点对应 $F_l^+$ 解析延拓到下半 $k$ 平面后的零点"。下面列三条容易混淆的对应。

第一条：束缚态。$F_l^+(i\kappa) = 0$，$\kappa > 0$。$f_l(k)$ 在 $k = i\kappa$ 是真极点。$E_b = -\kappa^2$ 在 $E$ 第一张面（物理面）负实轴上。这与 `Green_operator.zh.md:412` 的 $G(z) = \sum_n |n\rangle\langle n|/(z - E_n)$ 离散和直接对应：束缚态在 resolvent 中是物理面真极点。

第二条：共振。$F_l^+$ 解析延拓到 $\mathrm{Im}\,k < 0$ 的零点 $k_R - i k_I$。$f_l$ 在原 $k$ 平面没有这个极点（因 $F_l^+$ 在原定义域里是上半平面），但若把 $f_l$ 也延拓到下半平面，则它在 $k_R - i k_I$ 上有极点。$E$ 平面上：$E = (k_R - i k_I)^2 \in $ 第二张面下半部，对应 $G(z)$ 解析延拓后的复极点 `Green_operator.zh.md:470`。

第三条：虚态。$F_l^+(-i\kappa) = 0$（解析延拓后）。$E_v = -\kappa^2$ 在 $E$ 第二张面负实轴上。这一点在物理上不是束缚态（波函数指数发散，非 $L^2$），但靠近实 $k = 0$ 阈值时显著影响低能散射长度。从 $S_l(k) = F_l^-(k)/F_l^+(k)$ 看，$F_l^+(-i\kappa) = 0$ 等价于 $F_l^-(-i\kappa)$ 的某种条件，但虚态本身不是 $f_l$ 在物理面上的极点——它是物理面外的零点对低能散射的"远场效应"。这条区分容易在文献里被简化掉，但在写 ${}^1 S_0$ 的 NN 散射时必须分清楚：${}^1 S_0$ 没有束缚态（$F_0^+$ 上半平面无零点），但有虚态（$F_0^+$ 下半平面接近原点处有零点），这两件事在 Jost 语言里完全不一样。

## 教学轨例子的 Jost 化对账

前面教学轨上各自在用 Newton 法或解析公式找极点，本节把它们都翻译成 $F_l^+$ 零点。

`examples/03_delta_shell.zh.md` 的 delta 壳。势 $V(r) = (\gamma/R)\,\delta(r - R)$。规则解 $\phi_0(k, r) = \sin(kr)/k$（$r < R$），跨过 $r = R$ 时 $u_0$ 连续、$u_0'$ 跳变 $\gamma\, u_0(R)/R$，于是 $r > R$ 区有

$$
\phi_0(k, r > R) = A(k)\, e^{ikr} + B(k)\, e^{-ikr}
$$

匹配条件给出 $A(k), B(k)$ 的代数表达，代入 (F-asy)（$l = 0$）：$F_0^+(k) = -2k\, B(k)$。用 `examples/03_delta_shell.zh.md:73` 给出的 $\tan\delta_0$ 表达式

$$
\tan\delta_0(k) = \frac{-\gamma\sin^2(kR)}{kR + (\gamma/2)\sin(2kR)}
$$

把它代回 $S_0(k) = e^{2i\delta_0} = (1 + i\tan\delta_0)/(1 - i\tan\delta_0)$，再用 (S-Jost) $S_0 = F_0^-/F_0^+$ 反解：$F_0^+(k) = 0$ 等价于 $\tan\delta_0(k) = -i$，等价于 `examples/03_delta_shell.zh.md:73` 的极点条件

$$
kR + \gamma\sin(kR)\, e^{ikR} = 0
$$

这正是脚本 `examples/03_delta_shell.py` 用 Newton 迭代搜索的复 $k$ 根。`examples/03_delta_shell.zh.md:88` 给出的三个共振极点 $\{k_n\}$ 就是 $F_0^+$ 在下半 $k$ 平面的三个零点（解析延拓后的）。$\gamma > 0$ 时全部在下半平面（共振），$\gamma < -1$ 时第一个跳到正虚轴（束缚态）——正是上一节"共振穿过实轴变束缚态"的图像。

`examples/05_separable_rank1.zh.md` 的 Yamaguchi 模型。秩 1 separable 势 $V = \lambda\,|g\rangle\langle g|$，$g(p) = 1/(p^2 + \beta^2)$，$T$ 矩阵闭式 `examples/05_separable_rank1.zh.md:42`：

$$
\tau(E) = \frac{\lambda}{1 - \lambda\, I(E)}
$$

separable 势的 Jost 函数有特别简单的形式：分波 $l = 0$ 下，$F_0^+(k) \propto 1 - \lambda\, I(k^2)$，归一化常数与 $g$ 的 form factor 相关。证明：把 $V = \lambda|g\rangle\langle g|$ 代入 (rad)，规则解满足 $\phi_0(k, r) = \phi_0^{(0)}(k, r) + \lambda\,(\langle g|\phi_0\rangle)\, G_0^+ g$，闭合后 $\langle g|\phi_0\rangle = (1 - \lambda I(k^2))^{-1}\langle g|\phi_0^{(0)}\rangle$，把这个因子代回 (F-W)，分母 $1 - \lambda I(k^2)$ 直接出现在 $F_0^+$ 里。所以

$$
F_0^+(k) = 0 \Leftrightarrow 1 - \lambda I(k^2) = 0 \Leftrightarrow \tau(k^2) \text{ 极点}
$$

`examples/05_separable_rank1.zh.md:154` 给出的束缚态极点 $\kappa \approx 0.0925$、$E_b \approx -0.0086$ 就是 $F_0^+$ 在正虚轴上的零点。Yamaguchi 例子是"$F_l^+$ 闭式可求"的最直接显化。

`examples/08_centrifugal_barrier.zh.md` 的 d 波方阱。$V_0$ 调节下扫描共振极点。`examples/08_centrifugal_barrier.zh.md:155` 把 $S_2(k)$ 写成 $(D + iN)/(D - iN)$，极点条件 $D - iN = 0$（等价 $N + iD = 0$）。从 (S-Jost) 看，$S_2 = F_2^-/F_2^+$ 的极点正是 $F_2^+ = 0$。比较 `examples/08_centrifugal_barrier.zh.md:155` 的 $D - iN$ 与 (F-asy) 给的 $F_2^+$ 表达式（$l = 2$ 下规则解的 $e^{-ikr}$ 系数），两者只差非零的归一化常数，零点集合相同。`examples/08_centrifugal_barrier.zh.md:161` 描述的"$V_0 \in [8, 19.5]$ 共振极点沿弧爬升，$V_{0,\rm crit} \approx 20$ 跳到正虚轴变束缚态"，在 Jost 语言里就是 $F_2^+$ 的零点轨迹随 $V_0$ 连续移动，临界 $V_0$ 时零点穿过实轴。

`examples/07_well_barrier_1d.zh.md` 的 1D 类似物。1D Schrödinger $u'' + (E - V)u = 0$ 没有原点边界（$r$ 整条实数轴），但有"左 Jost 解 / 右 Jost 解"的对称版本：$f^\pm(k, x) \to e^{\pm ikx}$（$x \to \pm\infty$），$F(k)$ 由两组 Jost 解的 Wronskian 定义。极点条件 $L(E) + ik = 0$（用 logarithmic derivative $L$）就是 1D 版本的 $F^+(k) = 0$，与 3D 完全平行。Friedrichs 模型的 $z - E_d - \Sigma(z) = 0$（`friedrichsModel.zh.md:512`）则是把 Jost 类似物推广到通道空间：$\Sigma(z)$ 起 self-energy 的角色，方程零点给出离散通道解析延拓后的极点。

## Coulomb 势与长程修补

Coulomb 势 $V_C = 2k\eta/r$ 不满足 $\int_0^\infty r |V|\,dr < \infty$，前面所有结论都要重写。`coulomb_scattering.zh.md:140` 已经写出 Coulomb 径向解 $F_l(\eta, \rho)$、$G_l(\eta, \rho)$ 的渐近形式：相比短程势的 $\sin(kr - l\pi/2 + \delta_l)$，Coulomb 远场多了 $-\eta\ln(2kr)$ 对数项与 $\sigma_l(\eta) = \arg\Gamma(l+1+i\eta)$ 的总相移。

Coulomb-Jost 函数定义需要修改：直接套 (f-inf) 的边界条件 $f_l^\pm \to e^{\pm i kr}$ 不再奏效，因为远场带对数发散相位。正确做法是把 $f_l^\pm$ 替换成"Coulomb 畸变 Jost 解"，远场边界条件改为

$$
f_l^{\pm, C}(k, r) \xrightarrow{r \to \infty} e^{\pm i[kr - \eta\ln(2kr)]}
$$

加 $V_{SR}$ 后总 Jost 函数 $F_l^{+, C+SR}(k)$ 用畸变波 $f_l^{\pm, C}$ 与 regular 解的 Wronskian 定义。物理可观测的 Coulomb-distorted 短程相移 $\delta_l^{SR}$（`coulomb_scattering.zh.md:279`）出现在 $F_l^{+, C+SR}$ 的实轴相位中，纯 Coulomb 部分 $\sigma_l$ 已经吸收进畸变波基底。`examples/11_coulomb_demo` 给数值实现。

这种"两次畸变"的结构和 DWBA 的 distorted wave 思路（`dwba.zh.md`）是同一回事：把已经解掉的部分作为参考，剩下的视为微扰。Jost 函数从短程到长程的推广就是把这条思路在边界条件层面操作化。

Coulomb 极点结构的特殊点：纯 Coulomb 势的束缚态（氢原子 Bohr 能级 $E_n = -1/(2 n^2)$，$n = 1, 2, 3, \ldots$）在 $k$ 平面对应正虚轴上无穷多个零点 $k_n = i/n$，且趋向 $k = 0$ 没有间隔——这与短程势束缚态有限个、分立的图像形成对比。原因是 Coulomb 势的长程吸引让所有 $n$ 都出现束缚态，无穷凝聚于阈值。短程势加 Coulomb 后，$F_l^{+, C+SR}$ 的束缚态零点结构是 Coulomb 谱的扰动：每个 $n$ 都微移，加入了短程修正。这是原子物理 Rydberg 修正、核物理 Coulomb-displacement 能量等物理量的解析框架。

## Jost 函数的数值实现轮廓

把上面所有内容落地到代码层面有两条路。

直接积分 (rad)。给定 $V(r)$，从 $r = 0$ 用 (phi-0) 边界条件出发，Numerov 或 RK4 向外积分到势支撑外的 $r = R$。在 $r > R$ 区域 (rad) 已是自由方程，解为 $\phi_l(k, r) = A(k)\, e^{ikr} + B(k)\, e^{-ikr}$ 的线性组合。比对 (F-asy)：

$$
A(k) = \frac{F_l^-(k)}{2 k^{l+1}},\quad B(k) = -\frac{(-1)^l\, F_l^+(k)}{2 k^{l+1}}
$$

数值上 $A, B$ 由匹配 $\phi_l(R)$ 与 $\phi_l'(R)$ 到自由远场组合给出（$2 \times 2$ 线性方程），然后反解 $F_l^\pm$。这种方法在复 $k$ 上自然推广：积分常微分方程对复 $k$ 仍稳定（只要远场指数衰减没把数值吹爆）。`examples/13_jost_demo` 计划用这条路径在 Yukawa、Hulthén 两个例子上把零点画出来。

Volterra 迭代。从 $f_l^+(k, r) = e^{ikr} - \int_r^\infty G_0^l(k; r, r')\, V(r')\, f_l^+(k, r')\, dr'$ 出发，离散化 $r$ 网格，迭代到收敛。每步是矩阵向量乘法。优点是直接给 $f_l^+$ 的整条 $r$ 依赖，缺点是大 $r$ 上 $G_0^l$ 的指数尾巴对截断敏感。两条路径互补，复杂势模型推荐第一条。

数值 sanity check：

- $V \equiv 0$ 应给 $F_l^\pm \equiv 1$（精度判定基准）；
- 实 $k$ 上 $|F_l^+(k)| = |F_l^-(k)|$（来自 (F-conj)）；
- 实 $k$ 上 $\arg F_l^+(k) = -\delta_l(k)$，$\delta_l$ 与 $\tan\delta_l$ 直接积分对比；
- 已知束缚态势（如方阱）在 $k = i\kappa$ 上 $F_l^+(i\kappa) = 0$，$\kappa$ 与束缚能 $E_b = -\kappa^2$ 比对独立计算的本征值；
- Levinson 定理：$\delta_l(0) - \delta_l(\infty) = n_l \pi$ 对积分相移做端点差。

四条 sanity check 通过则 Jost 函数的代码可信。

## 解析结构的统一图谱

把前面的零点物理含义归到一张概念表（不展开成图，按主线笔记的对账风格列）：

- 上半 $k$ 平面正虚轴 $k = i\kappa$，$F_l^+ = 0$：束缚态，$E_b = -\kappa^2 < 0$，对应 `Green_operator.zh.md:412` 的实极点；
- 下半 $k$ 平面负虚轴 $k = -i\kappa$，$F_l^+ = 0$（解析延拓后）：虚态，$E_v = -\kappa^2 < 0$，物理面外但贴近实轴可显著影响低能散射；
- $k = 0$ 实轴零点 $F_l^+(0) = 0$：阈值零能态，修正 Levinson 常数 $n_l^{1/2}$；
- 下半 $k$ 平面第四象限 $k = k_R - i k_I$，$F_l^+ = 0$（解析延拓后）：共振，$E = E_R - i\Gamma/2$，$\Gamma = 4 k_R k_I$，对应 `Green_operator.zh.md:470` 与 `friedrichsModel.zh.md:551` 的第二张面极点。

主线笔记的对账：

- resolvent 谱分解与极点结构：`Green_operator.zh.md:412` 的离散和 + 连续积分，`Green_operator.zh.md:470` 的第二张面共振极点；
- 分波 $f_l$ 与 $\delta_l$ 的关系：`partial_wave_projection.zh.md:366` 的 $f_l = e^{i\delta_l}\sin\delta_l/k$，`partial_wave_projection.zh.md:378` 的 $S_l = e^{2i\delta_l}$；
- Friedrichs 第二张面：`friedrichsModel.zh.md:512` 的极点方程 $z - E_d - \Sigma(z) = 0$，`friedrichsModel.zh.md:551` 的 $z_* = E_R - i\Gamma_R/2$；
- Coulomb 修正：`coulomb_scattering.zh.md:142` 的 $-\eta\ln(2kr)$ 对数相位，`coulomb_scattering.zh.md:152` 的 $\sigma_l(\eta) = \arg\Gamma(l+1+i\eta)$；
- 教学轨极点搜索：`examples/03_delta_shell.zh.md:73` 的 $S_0$ 极点条件、`examples/05_separable_rank1.zh.md:42` 的 $\tau(E)$ 闭式分母、`examples/08_centrifugal_barrier.zh.md:155` 的 $D - iN = 0$ 条件、`examples/07_well_barrier_1d.zh.md` 的 1D Jost 类似物；
- delta 壳极点轨迹：`examples/03_delta_shell.zh.md:88` 给出 $\gamma = 20$ 的三个共振极点；
- Yamaguchi 束缚态：`examples/05_separable_rank1.zh.md:154` 的 $\kappa \approx 0.0925$；
- d 波共振轨迹：`examples/08_centrifugal_barrier.zh.md:161` 的 $V_0 \to V_{0,\rm crit}$ 共振变束缚态。

## Regge 极点的简介

到此为止把 $f_l(k)$ 看作 $k$ 的函数，分波量子数 $l$ 当离散标签。把 $l$ 也复化是另一条解析延拓方向。把分波 LS 方程 (`partial_wave_projection.zh.md:340`) 中的 $l$ 推广到复数（径向方程把 $l(l+1) \to \alpha(\alpha+1)$，球 Bessel 函数变成一般的 $\alpha$ 阶 Bessel），得到 $f_\alpha(k)$ 在复 $\alpha$ 平面的解析延拓。

$f_\alpha(k)$ 在复 $\alpha$ 平面的极点称为 Regge 极点，记为 $\alpha = \alpha_n(k)$。能量变 $k$ 时，极点位置 $\alpha_n(k)$ 描出一条轨迹，称为 Regge 轨迹。物理上每条 Regge 轨迹对应一族不同 $l$ 的束缚态/共振：在某个能量下 $\alpha_n(k) = l_0$（整数）时，对应 $l = l_0$ 分波出现一个束缚态或共振；不同能量下不同 $l$ 整数对应同一条轨迹的不同截点。

Regge 极点在高能下 dominant：固定能量 $s = -E$ 在交叉道，$\theta$ 大角度的渐近行为由最右 Regge 极点 $\alpha(0)$ 控制，$f \sim s^{\alpha(0)}$（Regge 渐近）。这是强子物理 Regge 现象学的基础——把 $\rho$、$f_2$、$\omega$ 等介子轨迹拟合成 $\alpha(t) = \alpha(0) + \alpha'\, t$ 的直线，斜率 $\alpha' \approx 0.9$ GeV⁻²。完整的 Regge 理论（Watson-Sommerfeld 变换、Mandelstam 表象、Pomeron）超出本主线笔记的范围，留作后续专题。

势模型层面的 Regge 极点：Yukawa 势 $V(r) = -g\, e^{-\mu r}/r$ 的 Regge 轨迹可数值计算。固定 $k$，把分波径向方程在复 $\alpha$ 平面寻找解使 (rad) 在 $r \to 0$ 与 $r \to \infty$ 同时正则——这正是把 (phi-0) 与 (f-inf) 边界条件在复 $\alpha$ 上联立，等价于 $F_\alpha^+(k) = 0$ 视作 $\alpha$ 的方程。每个 $k$ 给出一组 $\{\alpha_n(k)\}$；连接成轨迹画在复 $\alpha$ 平面是 Regge 现象在势模型上的具体实现。

## 小结与 next-step

这一篇是理论闭环轨主线第 D 篇，承接前面的 $S$ 矩阵、Green 算符、分波投影、Friedrichs 模型，启接后面的有效力程定理（E 篇）与色散关系。Jost 函数把"散射的解析结构"这件事在径向方程层面操作化，本质是给 $f_l(k)$ 提供一个完整的复 $k$ 平面延拓框架。

这一篇做的事：

- 引入 Jost 解 $f_l^\pm$ 与规则解 $\phi_l$，定义 Jost 函数 $F_l^\pm(k)$（远场展开 + Wronskian 两个等价定义）；
- 推出 $S_l(k) = F_l^-(k)/F_l^+(k)$，$f_l$ 极点 = $F_l^+$ 零点；
- 把零点按位置分类：正虚轴（束缚态）、负虚轴（虚态）、实轴 $k = 0$（阈值零能态）、下半第四象限（共振）；
- 用论域原理证 Levinson 定理 $\delta_l(0) - \delta_l(\infty) = (n_l + n_l^{1/2})\pi$；
- 把教学轨上 03 / 05 / 08 三个例子的极点搜索算法归到统一的 $F_l^+ = 0$ 框架；
- 简介 Coulomb 修补（畸变 Jost 解）与 Regge 极点（复 $l$ 平面延拓）。

next-step：

- 数值 Jost 函数计算，把 Volterra 积分方程迭代到稳态，画 $F_l^+(k)$ 在复 $k$ 平面的零点分布。指向 `examples/13_jost_demo`，覆盖 Yukawa 与 Hulthén 两个解析可控的例子。
- 有效力程理论的系统化：把 $k\cot\delta_l(k)$ 的低能展开 $k\cot\delta_l = -1/a_l + r_l k^2/2 + O(k^4)$ 通过 $F_l^+$ 在 $k = 0$ 附近的 Taylor 展开 derive 出来，与 Levinson 定理合并讲。指向后续主线 E 篇 effective_range_levinson.zh.md。
- $S$ 矩阵在复 $E$ 平面的解析结构与色散关系：从 $S_l(E)$ 的 unitarity cut + 束缚态极点写出 $N/D$ 表象、Mandelstam 表象、固定 $t$ 色散关系。强子物理 Roy 方程的源头。
- Regge 极点的具体例子：Yukawa 势的 Regge 轨迹数值计算，看轨迹随耦合强度的变化；与 dispersion relation + 高能极限的对接。
- 多通道推广：耦合通道 $S$ 矩阵的 Jost 矩阵 $\mathcal F^+(k)$，零点条件 $\det\mathcal F^+(k) = 0$ 给共振极点。延伸到核反应里的 R 矩阵理论。
- Gamow 态的归一化：复极点对应不可归一化的右本征态（指数发散波函数），通过 RHS / Gelfand 三重定义内积。把 `friedrichsModel.zh.md:580` 的 RHS 框架在径向 Jost 极点处具体化，画 Gamow 波函数 $\phi_l(k_n, r)$ 的实部、虚部、外推区域。
- $S$ 矩阵 product 表象：上半 $k$ 平面解析、零点全部在正虚轴的事实让 $F_l^+(k)$ 接受类似 Hadamard 因式分解 $F_l^+(k) = e^{ikc}\prod_n (1 - k/i\kappa_n) \cdot (\text{无零点解析})$ 的写法。这是 $N/D$ 表象（$f_l = N(k)/D(k)$，$D$ 自带束缚态零点结构）的解析根源，下一篇主线 E 篇会用到。
- 反演问题（Marchenko / Gel'fand-Levitan）：给定 $S_l(k)$ 在实轴的所有 $k$ 上的值加上束缚态能量与归一化常数，能否唯一恢复 $V(r)$？答案在数学上是肯定的（短程势条件下），构造方法即 Marchenko 积分方程，输入正是 $F_l^+(k)$ 的零点位置与实轴幅度。这把"势 $\to$ 散射数据"的正问题反过来做。
- 把 Jost 框架推广到自旋耦合通道（${}^3 S_1$-${}^3 D_1$ 张量耦合）的 Jost 矩阵，看 $\det\mathcal F^+(k) = 0$ 给的束缚态（氘核）在两通道波函数振幅上的具体表现。这一条直接接到核结构与 NN 散射的低能定理。
