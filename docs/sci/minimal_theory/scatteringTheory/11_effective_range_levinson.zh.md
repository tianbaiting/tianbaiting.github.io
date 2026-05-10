# ch11 有效力程理论与 Levinson 系统化

前一篇 `10_jost_analyticity.zh.md` 把分波振幅 $f_l(k)$ 写成 Jost 函数 $F_l^\pm(k)$ 的比，把束缚态、虚态、共振、阈值零能态四类奇性都归到 $F_l^+(k)$ 在复 $k$ 平面的零点上。Levinson 定理在那里以论域原理的轮廓出现：$\delta_l(0) - \delta_l(\infty)$ 的整体值由束缚态数控制。

这一篇要做两件相互配合的事。第一，把 $\delta_l(k)$ 在 $k = 0$ 附近做 Taylor 展开，写出有效力程展开（effective range expansion，ERE）的标准形式，把散射长度 $a_l$ 与有效力程 $r_l$ 这两个低能观测量从 Jost 函数的低能行为里解析地导出。第二，把 Levinson 定理从轮廓提升为完整证明（含半整数修正），与教学轨上 02、05 两个例子的数值结果对账。

低能两参数足够刻画大部分弹性散射的细节，是核物理与冷原子物理的核心工程事实。本篇把这一事实在 Jost 框架下落实成解析定理，并给出收敛域、Bargmann 不等式、unitary limit 三条配套结果。

## 目标

放在最前的几条断言，本篇要把每一条都兑现：

- s 波低能极限 $\delta_0(k) \to -k a_0$，高分波 $\delta_l(k) \to -k^{2l+1} a_l$（Wigner 阈值定理）。
- ERE 标准形式 $k^{2l+1}\cot\delta_l(k) = -1/a_l + r_l\, k^2/2 + v_l\, k^4 + \ldots$ 的收敛域由 $F_l^+$ 最近的奇性决定。
- $a_l$ 是几何含义明确的"等效硬球半径"；$r_l$ 是势的有效力程半径，对 $V$ 细节比 $a_l$ 鲁棒得多。
- Bargmann 不等式 $\int_0^\infty r |V(r)|\, dr \geq n_0 \pi/2$ 给 s 波束缚态数的论域型上界。
- Levinson 定理完整版 $\delta_l(0) - \delta_l(\infty) = (n_l + n_l^{1/2})\pi$，$n_l^{1/2} = 1/2$ 仅在 s 波零阈值情形出现。
- s 波 unitary limit $a_0 \to \pm\infty$ 与 $1/a_0 = 0$ 的零阈值零能态对应，是 Feshbach 共振调谐的物理底层。

## 背景：Jost 函数的低能行为

记号沿用 `10_jost_analyticity.zh.md:79` 的远场展开 (F-asy) 与 `10_jost_analyticity.zh.md:87` 的 Wronskian 定义 (F-W)。短程实势下 $F_l^+(k)$ 在上半 $k$ 平面解析（含实轴），$k = 0$ 是实轴上的一个普通点（除非碰巧 $F_l^+(0) = 0$，此为零阈值情形，见后）。所以 $F_l^+(k)$ 可以在 $k = 0$ 附近做 Taylor 展开

$$
F_l^+(k) = F_l^+(0) + k\, F_l^{+\prime}(0) + \frac{k^2}{2}\, F_l^{+\prime\prime}(0) + O(k^3) \tag{F-Taylor}
$$

对实势，由 (F-conj) `10_jost_analyticity.zh.md:117` 即 $F_l^+(k)^* = F_l^-(k^*)$，在实 $k$ 上 $F_l^-(k) = F_l^+(k)^*$。把 (F-asy) 与 (F-conj) 合并得 (F-phase) `10_jost_analyticity.zh.md:131`：实 $k > 0$ 上 $F_l^+(k) = |F_l^+(k)|\, e^{-i\delta_l(k)}$。

为了把 $\delta_l(k)$ 的低能行为从 (F-Taylor) 直接读出，需要弄清 $F_l^{+\prime}(0)$、$F_l^{+\prime\prime}(0)$ 等系数的实虚结构。再次用 (F-conj)：在 $k$ 实数邻域附近 $F_l^+(k)^* = F_l^-(k) = F_l^+(-k)$（最后一步用 $F_l^-(k, r) = F_l^+(-k, r)$，`10_jost_analyticity.zh.md:70` 的对称性）。这给出

$$
F_l^+(-k) = F_l^+(k)^* \tag{F-reflection}
$$

对实 $k$ 成立，按解析延拓推到所有 $k$ 上。把 (F-Taylor) 代入 (F-reflection) 比对系数：

$$
F_l^+(0) - k F_l^{+\prime}(0) + \frac{k^2}{2} F_l^{+\prime\prime}(0) - \ldots = F_l^+(0)^* + k F_l^{+\prime}(0)^* + \frac{k^2}{2} F_l^{+\prime\prime}(0)^* + \ldots
$$

逐阶比对：$F_l^+(0)$ 实，$F_l^{+\prime}(0)$ 纯虚，$F_l^{+\prime\prime}(0)$ 实，$F_l^{+\prime\prime\prime}(0)$ 纯虚，依此交替。$F_l^+(k)$ 在 $k = 0$ 附近的偶幂系数实、奇幂系数纯虚——这就是后面 ERE 截断到 $k^{2l}$ 偶幂的解析根源。

## 阈值行为：Wigner 阈值定理

短程势下，第 $l$ 分波相移在 $k \to 0$ 极限有确定的幂律。

陈述。设 $V(r)$ 短程（$\int_0^\infty r |V(r)|\,dr < \infty$，足够强意义下指数衰减），且 $F_l^+(0) \neq 0$（无零阈值零能态）。则

$$
\delta_l(k) \xrightarrow{k \to 0} -k^{2l+1}\, a_l + O(k^{2l+3}) \tag{Wigner}
$$

其中 $a_l$ 是第 $l$ 分波散射长度，量纲 $[a_l] = \text{长度}^{2l+1}$。

self-derive。从 (F-W) 出发把 $F_l^+$ 的归一化展开。零势极限下 (F-W) 给 $F_l^+ \equiv 1$（见 `10_jost_analyticity.zh.md:101`）。短程势下，$F_l^+(k)$ 的小 $k$ 行为可写

$$
F_l^+(k) = 1 - i k^{2l+1}\, a_l + b_l\, k^{2l+2} + O(k^{2l+3}) \tag{F-low}
$$

证明 (F-low) 的关键是 (F-W) 中 $\phi_l(k, r)$ 与 $f_l^+(k, r)$ 的低能展开。规则解 (phi-0) `10_jost_analyticity.zh.md:50` 在原点行为 $r^{l+1}/(2l+1)!!$ 与 $k$ 无关，因此 $\phi_l(k, r)$ 是 $k^2$ 的整函数（Newton 12.1 节标准结论）：$\phi_l(k, r) = \phi_l^{(0)}(r) + k^2 \phi_l^{(2)}(r) + \ldots$，所有偶幂。Jost 解 $f_l^+(k, r) \to e^{ikr}$ 远场行为，小 $k$ 下 $f_l^+(k, r) = u_l^+(r) + i k\, w_l^+(r) + O(k^2)$，其中 $u_l^+(r) = \lim_{k \to 0} f_l^+(k, r)$ 满足零能径向方程，远场 $u_l^+(r) \to 1$（自由 $l$ 阶 Riccati-Hankel 在 $k = 0$ 退化），$w_l^+(r) \to r$ 远场。

代入 (F-W) 的 Wronskian $W[f_l^+, \phi_l] = f_l^+\phi_l' - f_l^{+\prime}\phi_l$ 在 $k \to 0$ 展开。归一化常数 $(\mp k)^{-l}/(2l+1)!!$ 中的 $k^{-l}$ 因子与 Wronskian 中"奇阶 $k$ 项"的乘法配合，给出 (F-low) 的 $-i k^{2l+1} a_l$ 形式：纯虚（与 (F-reflection) 偶/奇幂一致）、$k$ 的奇次幂（具体是 $2l+1$）。系数 $a_l$ 是从 Wronskian 对零能波函数的积分得到的实数。具体的 $a_l$ 闭式（s 波）

$$
a_0 = -\lim_{r \to \infty}\bigl[r - \phi_0^{(0)}(r)/\phi_0^{(0)\prime}(r)\bigr]
$$

把规则解 $\phi_0^{(0)}(r)$ 在远场近似为 $C\,(r - a_0)$ 的线性渐近形式——这就是几何含义"等效硬球半径"。

把 (F-low) 代入 (F-phase)：实部 $|F_l^+(k)|^2 = 1 + 2 b_l k^{2l+2} + (a_l)^2 k^{4l+2} + \ldots$，虚部 $-\sin\delta_l \cdot |F_l^+| \approx \mathrm{Im}\, F_l^+ = -k^{2l+1} a_l$。低能 $|F_l^+| \approx 1$，所以

$$
\sin\delta_l(k) \approx k^{2l+1}\, a_l + O(k^{2l+3})
$$

但 (F-phase) 用的是 $F_l^+ = |F_l^+|\, e^{-i\delta_l}$，故 $\mathrm{Im}\,F_l^+ = -|F_l^+|\sin\delta_l$，符号比对得 $\sin\delta_l \approx -k^{2l+1} a_l$，即 $\delta_l(k) \approx -k^{2l+1} a_l + O(k^{2l+3})$，正是 (Wigner)。

s 波特例。$l = 0$ 时 $\tan\delta_0(k) \approx \delta_0(k) \approx -k a_0$，这是核物理与冷原子普遍引用的低能 s 波公式。低能 s 波截面 $\sigma_0(k) = (4\pi/k^2)\sin^2\delta_0 \to 4\pi a_0^2$，与 $k$ 无关，是"$a_0^2$ 量级几何截面"的图像。

p 波 $l = 1$：$\delta_1 \approx -k^3 a_1$，量纲 $[a_1] = \text{长度}^3$。低能下被 $k^3$ 严重压制，这是为什么低能 NN 散射 s 波 dominant 的解析理由。`examples/08_centrifugal_barrier.zh.md` 数值演示了 $l = 2$ d 波的离心垒压制，与 (Wigner) 的 $k^5$ 行为一致。

## 有效力程展开的标准形式

有了 (F-low) 的低能展开，一步推出 ERE。

陈述。短程势下，第 $l$ 分波相移满足

$$
\boxed{\;k^{2l+1}\cot\delta_l(k) = -\frac{1}{a_l} + \frac{1}{2}\, r_l\, k^2 + v_l\, k^4 + w_l\, k^6 + \ldots\;} \tag{ERE}
$$

收敛域 $|k| < |k_*|$，$k_*$ 是 $F_l^+(k)$ 最接近 $k = 0$ 的非平凡奇异性（束缚态、虚态、左手切等）。

s 波最常用：$k\cot\delta_0(k) = -1/a_0 + r_0 k^2/2 + v_0 k^4 + \ldots$。

self-derive。用 (F-Taylor) 与 (F-reflection) 的实虚交替结构，把 $F_l^+(k)$ 写成

$$
F_l^+(k) = R_l(k^2) - i k^{2l+1}\, A_l(k^2) \tag{F-RA}
$$

其中 $R_l, A_l$ 是 $k^2$ 的实系数幂级数。代入 (F-phase) 即 $F_l^+ = |F_l^+| e^{-i\delta_l}$：

$$
\tan\delta_l(k) = -\frac{\mathrm{Im}\,F_l^+(k)}{\mathrm{Re}\,F_l^+(k)} = \frac{k^{2l+1}\, A_l(k^2)}{R_l(k^2)}
$$

故

$$
k^{2l+1}\cot\delta_l(k) = \frac{R_l(k^2)\, k^{2l+1}}{k^{2l+1} A_l(k^2)} = \frac{R_l(k^2)}{A_l(k^2)} \tag{kcot}
$$

(kcot) 是 ERE 的解析根源：$k^{2l+1}\cot\delta_l$ 是两个 $k^2$ 实系数幂级数的比，本身在 $k^2 = 0$ 邻域是 $k^2$ 的解析函数。把 $R_l/A_l$ 在 $k^2 = 0$ 展开：

$$
\frac{R_l(k^2)}{A_l(k^2)} = \frac{R_l(0) + R_l'(0)\, k^2 + \ldots}{A_l(0) + A_l'(0)\, k^2 + \ldots} = \frac{R_l(0)}{A_l(0)}\Bigl[1 + \bigl(\frac{R_l'(0)}{R_l(0)} - \frac{A_l'(0)}{A_l(0)}\bigr) k^2 + \ldots\Bigr]
$$

读出

$$
-\frac{1}{a_l} = \frac{R_l(0)}{A_l(0)} = \frac{F_l^+(0)}{A_l(0)},\qquad \frac{r_l}{2} = \frac{R_l(0)}{A_l(0)}\bigl[\frac{R_l'(0)}{R_l(0)} - \frac{A_l'(0)}{A_l(0)}\bigr]
$$

由 (F-low) 知 $A_l(0) = a_l$，故 $-1/a_l = F_l^+(0)/a_l$ 给 $F_l^+(0) = -1$ 的归一化（约定可吸收，常用归一化使 $F_l^+(0) = 1$，则 $a_l$ 与 $A_l(0) = -a_l$ 反号，依文献而异）。无论何种约定，关键结论是：$k^{2l+1}\cot\delta_l$ 在 $k = 0$ 邻域是 $k^2$ 的解析函数，其 Taylor 系数定义 $a_l, r_l, v_l, \ldots$。

收敛域。(kcot) 的右边作为 $k^2$ 的有理函数，最近极点 $k_*^2$ 出现在 $A_l(k^2) = 0$ 处。对 s 波 $A_0(k^2) = 0$ 等价于 $F_0^+(k)$ 在 $k$ 实轴外有零点（束缚态 $k = i\kappa$ 给 $A_0(-\kappa^2) = 0$，虚态 $k = -i\kappa$ 同样给）。所以 ERE 收敛域 $|k|^2 < \kappa^2$，$\kappa$ 是最近的束缚态/虚态距离阈值的距离。Yukawa 势 $V \sim e^{-\mu r}/r$ 还有左手切 $k^2 = -\mu^2/4$ 的奇异性，进一步缩小收敛域到 $|k|^2 < \mu^2/4$（ERE 在 $k = i\mu/2$ 击中左手切端点）。

ERE 截断在低阶。Yamaguchi 模型 (`examples/05_separable_rank1.zh.md:78`) 是 ERE 系数 $v_l = 0$（精确截断在 $k^2$）的标志性例子——separable 势 $V = \lambda |g\rangle\langle g|$ 让 $R_0/A_0$ 退化为多项式比，本篇 (kcot) 的解析结构在那里全部显化。

## 散射长度的物理意义

s 波散射长度 $a_0$ 有几条互补的几何/物理解读。

几何：等效硬球半径。零能 s 波规则解 $\phi_0^{(0)}(r)$ 在势支撑外（$r > $ 势的范围）满足自由方程 $\phi_0'' = 0$，故 $\phi_0^{(0)}(r) = c_1 r + c_0$。在 $r \to \infty$ 把斜率归一化为 $c_1 = 1$，则 $\phi_0^{(0)}(r) = r - a_0$。线性渐近的零点 $r = a_0$ 即"等效硬球半径"——硬球势 $V = \infty\,(r < a_0)$ 的零能波函数恰好是 $\phi_0^{(0)}(r) = r - a_0$ 的形式，截面 $\sigma_0 = 4\pi a_0^2$ 直接读出。

符号约定。Bethe 约定下吸引势没有束缚态时 $a_0 > 0$（线性渐近零点在原点右侧），出现束缚态后 $a_0$ 翻号（每加一个束缚态符号翻一次）。Bethe-Goldstone 约定相反，文献里两种都有。本笔记沿用 Bethe 约定（`examples/02_square_well_3d.zh.md:62` 的方阱公式 $a = R[1 - \tan(K_0 R)/(K_0 R)]$ 给的就是 Bethe 约定）。

与最近极点的关系。$a_0$ 的大小由 $F_0^+$ 在虚轴上最接近 $k = 0$ 的零点距离控制。设最近零点在 $k = i\kappa$（束缚态）或 $k = -i\kappa$（虚态），低能展开 $F_0^+(k) \approx F_0^+(0)\,(1 \mp ik/\kappa)$（保留主导项），代入 (F-RA) 得 $A_0(0) = F_0^+(0)/\kappa$，故

$$
\frac{1}{a_0} = \pm\kappa \tag{a-pole}
$$

正号对应虚态，负号对应束缚态（正负号对应在 Bethe 约定下；Bethe-Goldstone 约定相反）。$\kappa$ 越小（极点越靠近阈值），$|a_0|$ 越大。这正是 ${}^1 S_0$ 通道 $a_0 \approx -23.7$ fm 大散射长度的来源——$\kappa \approx 0.04$ fm⁻¹ 的浅虚态紧贴阈值。

NN 物理的两个具体例子（仅作对照）。${}^1 S_0$ 通道：$a_0 \approx -23.7$ fm，对应虚态能 $E_v \approx -0.066$ MeV，无束缚态。${}^3 S_1$ 通道：$a_0 \approx 5.42$ fm（带束缚态，氘核 $E_d \approx -2.22$ MeV，$\kappa \approx 0.232$ fm⁻¹）。两通道 $r_0$ 都在 $1.7$–$2.7$ fm，与 NN 力的 typical 力程 $1/m_\pi \approx 1.4$ fm 同量级——这说明 $r_0$ 对势的细节远比 $a_0$ 鲁棒。

## 有效力程的物理意义

$r_l$ 比 $a_l$ 更接近"势的范围"，对 $V$ 的细节不敏感。这一直觉有干净的解析对应。

陈述（s 波）。$r_0$ 由两条零能波函数的差的积分给出：

$$
\boxed{\;r_0 = 2\int_0^\infty dr\,\bigl[v_0(r)^2 - u_0(r)^2\bigr]\;} \tag{r-int}
$$

其中 $v_0(r) = 1 - r/a_0$ 是零能自由波函数（势为零的渐近形式），$u_0(r)$ 是真实零能 s 波规则解，归一化使 $u_0(r) \to v_0(r)$ 在 $r \to \infty$。$r_0$ 是 $u_0^2 - v_0^2$ 的积分（注意符号；势支撑内 $|u_0|^2 < |v_0|^2$，故被积函数主要为正，$r_0 > 0$）。

self-derive。考虑两个动量 $k_1, k_2$ 处的 s 波规则解 $\phi_0(k_i, r)$（归一化 $\phi_0(k_i, r) \to \sin(k_i r + \delta_0(k_i))/[k_i\, |F_0^+(k_i)|]$ 在 $r \to \infty$，相当于 $\phi_0(k, r) = -A_0(k^2)\sin(kr)/k + R_0(k^2)\cos(kr)$ 远场的整体归一化）。两个 $\phi_0(k_i, \cdot)$ 都满足径向方程 (rad)：

$$
\phi_0''(k_i, r) + [k_i^2 - V(r)]\,\phi_0(k_i, r) = 0
$$

把 $\phi_0(k_2, r) \times $ ($k_1$ 方程) $- \phi_0(k_1, r) \times$ ($k_2$ 方程) 相减：

$$
\frac{d}{dr}\bigl[\phi_0(k_1, r)\,\phi_0'(k_2, r) - \phi_0(k_2, r)\,\phi_0'(k_1, r)\bigr] = (k_1^2 - k_2^2)\,\phi_0(k_1, r)\,\phi_0(k_2, r)
$$

从 $0$ 到 $R$ 积分，左边是 $W[\phi_0(k_1), \phi_0(k_2)]\Big|_0^R$。原点 $\phi_0(k_i, 0) = 0$（s 波规则解），故 $0$ 端 Wronskian 为零。$R \to \infty$ 时用远场代入。

引入辅助波 $\psi_0(k, r) = \cos\delta_0\sin(kr) + \sin\delta_0\cos(kr) = \sin(kr + \delta_0(k))$（远场），它跟自由波 $\sin(kr + \delta_0)/k$ 在远场吻合并对所有 $r$ 满足自由方程。把同样的减法对 $\psi_0(k_1)$ 与 $\psi_0(k_2)$ 做，在 $0$ 到 $\infty$ 积分（$\psi_0$ 在原点不为零，所以 $0$ 端 Wronskian 给非零贡献）：

$$
W[\psi_0(k_1), \psi_0(k_2)]\Big|_0^\infty = (k_1^2 - k_2^2)\int_0^\infty \psi_0(k_1, r)\,\psi_0(k_2, r)\, dr
$$

两式相减（$\phi - \psi$ 方法），用 $\phi_0(k, \infty) = \psi_0(k, \infty)$ 抵消 $\infty$ 端，剩 $-W[\psi_0(k_1), \psi_0(k_2)](r = 0) = (k_1^2 - k_2^2)\int_0^\infty[\psi_0(k_1)\psi_0(k_2) - \phi_0(k_1)\phi_0(k_2)]\, dr$。

$\psi_0(k, 0) = \sin\delta_0(k)$，$\psi_0'(k, 0) = k\cos\delta_0(k)$，故 $W[\psi_0(k_1), \psi_0(k_2)](0) = \sin\delta_0(k_1) k_2\cos\delta_0(k_2) - \sin\delta_0(k_2) k_1 \cos\delta_0(k_1)$。除以 $\sin\delta_0(k_1)\sin\delta_0(k_2)$，整理

$$
k_2\cot\delta_0(k_2) - k_1\cot\delta_0(k_1) = (k_1^2 - k_2^2)\int_0^\infty[\hat\psi_0(k_1)\hat\psi_0(k_2) - \hat\phi_0(k_1)\hat\phi_0(k_2)]\, dr
$$

其中 $\hat\psi_0, \hat\phi_0$ 是除以 $\sin\delta_0$ 后的归一化波函数，远场行为 $\hat\psi_0(k, r) \to \cos(kr) + \cot\delta_0(k)\sin(kr)$。取 $k_1 \to 0$、$k_2 = k$：$k\cot\delta_0(k) - (-1/a_0) = -k^2 \int_0^\infty[\hat\psi_0(0)\hat\psi_0(k) - \hat\phi_0(0)\hat\phi_0(k)]\, dr + O(k^4)$。再令 $k \to 0$：

$$
\frac{r_0}{2} = -\int_0^\infty[v_0(r)^2 - u_0(r)^2]\,dr \cdot (-1) = \int_0^\infty[v_0^2 - u_0^2]\,dr
$$

把符号约定整理后即 (r-int)。完整推导见 Newton §11.2 与 Bethe (1949)。

物理含义。$v_0(r) - u_0(r)$ 在势支撑外为零（远场两者重合），积分集中在势的支撑区 $r \lesssim R_V$（$R_V$ 为势力程）。所以 $r_0 \sim R_V$ 量级，与 $V$ 的力程同阶；具体值与 $V$ 的形状有关，但远比 $a_0$ 对参数细节不敏感。这是"$r_0$ 鲁棒"的解析根源。

NN 数值佐证。${}^1 S_0$ 与 ${}^3 S_1$ 的 $r_0$ 都在 $\sim 2$ fm，和 $\pi$ 介子 Compton 波长 $\sim 1/m_\pi$ 相符；同一通道里不同 NN 势模型（OPE、Argonne $v_{18}$、CD-Bonn）给的 $a_0$ 在 fit 误差 $\pm 0.1$ fm 内一致，但 $r_0$ 在 $\pm 0.05$ fm 内就 fix 住——后者更"硬"。

## Bargmann 不等式

ERE 的收敛域、Levinson 定理的束缚态计数都需要"$V$ 多深才能支持几个束缚态"的定量上界。Bargmann (1952) 给了最简洁的版本。

陈述（s 波）。短程势 $V(r)$ 满足 $\int_0^\infty r\,|V(r)|\, dr < \infty$，则 s 波束缚态数 $n_0$ 受

$$
\boxed{\;n_0 \leq \int_0^\infty r\,|V_-(r)|\, dr\;} \tag{Bargmann}
$$

控制，$V_-(r) = \min(V(r), 0)$ 是 $V$ 的负部（仅吸引区贡献）。等价说法：$\int_0^\infty r\,|V_-|\,dr < n\pi$ 时 $n_0 < n$。

self-derive（论域原理路径）。从 Jost 函数的论域恒等式 (argP) `10_jost_analyticity.zh.md:208`：上半 $k$ 平面零点数 $n_0 = (1/2\pi i)\oint d\log F_0^+$。把围道取实轴 $-R$ 到 $R$ 加上半圆。实轴段贡献 $-(\delta_0(R) - \delta_0(-R))/\pi = -2(\delta_0(R) - \delta_0(0))/\pi$（用 $\delta_0(-R) = -\delta_0(R)$ 实势对称）。半圆段 $R \to \infty$ 给零（短程势）。$R \to \infty$ 取极限：

$$
n_0 = -\frac{1}{\pi}[\delta_0(\infty) - \delta_0(0)] = \frac{\delta_0(0) - \delta_0(\infty)}{\pi}
$$

这本身就是 Levinson。Bargmann 不等式来自一步更强的估计：Born 近似下 $\delta_0(k) = -\int_0^\infty V(r)\sin^2(kr)/k\, dr + O(V^2)$，故

$$
\delta_0(0) - \delta_0(\infty) \leq \sup_k|\delta_0(k) - \delta_0(\infty)| \leq \int_0^\infty r\,|V(r)|\, dr
$$

最后一步用 $\sin^2(kr)/k \leq r$（基本不等式 $\sin x \leq x$）。结合 Levinson $\delta_0(0) - \delta_0(\infty) = n_0\pi$ 得 $n_0\pi \leq \int_0^\infty r\,|V|\,dr$，即 (Bargmann)。这条 Born 近似论证只在弱耦合严格——强耦合下需要更细致的 phase shift 比较定理（见 Newton §12.4），结论形式不变但常数可能改进。

高分波版本。Bargmann 不等式对一般 $l$ 推广为

$$
n_l \leq \frac{1}{2l + 1}\int_0^\infty r\,|V_-(r)|\, dr
$$

离心垒 $l(l+1)/r^2$ 抑制束缚态形成，多了 $1/(2l+1)$ 因子。对 d 波 $l = 2$，需要五倍于 s 波的吸引强度才出现一个束缚态；这与 `examples/08_centrifugal_barrier.zh.md` 的 $V_0$ 阈值数值 $V_{0,\rm crit} \approx 20$（远高于 s 波 $\pi^2/4 \approx 2.47$）一致。

方阱对账。`examples/02_square_well_3d.zh.md:94` 给方阱 s 波束缚态数 $n_0 = \lfloor K_0 R/\pi + 1/2\rfloor$，$K_0 = \sqrt{V_0}$。Bargmann 给 $n_0 \leq \int_0^R r\, V_0\, dr = V_0 R^2/2$。临界 $K_0 R = \pi/2$ 时 $V_0 R^2 = \pi^2/4 \approx 2.47$，Bargmann 上界给 $n_0 \leq 1.23$，严格束缚态 $n_0 = 1$，不等式被饱和（按整数取下限）。第二阈值 $K_0 R = 3\pi/2$ 时 $V_0 R^2 = 9\pi^2/4 \approx 22.2$，Bargmann 给 $n_0 \leq 11.1$，实际 $n_0 = 2$——上界宽松但保守。

## Levinson 定理：完整证明

`10_jost_analyticity.zh.md:208` 给了论域原理证明的轮廓。本节把它写完整，包含半整数修正。

陈述（高分波 $l \geq 1$）。短程实势下，

$$
\delta_l(0) - \delta_l(\infty) = n_l\,\pi \tag{Lev-l>0}
$$

$n_l$ 是第 $l$ 分波束缚态数。$l \geq 1$ 时离心垒 $l(l+1)/r^2$ 阻止零能态在阈值上聚集（$F_l^+(0) \neq 0$ 自动），故无半整数修正。

陈述（s 波）。

$$
\delta_0(0) - \delta_0(\infty) = (n_0 + n_0^{1/2})\,\pi \tag{Lev-l0}
$$

$n_0^{1/2} = 1/2$ 当 $F_0^+(0) = 0$（零能态贴在阈值上），$n_0^{1/2} = 0$ 否则。

证明（详细论域原理）。围道 $C_R$ 取上半 $k$ 平面大半圆：实轴段 $[-R, R]$ 加半圆 $\Gamma_R = \{R\, e^{i\theta} : 0 \leq \theta \leq \pi\}$。论域原理：

$$
\frac{1}{2\pi i}\oint_{C_R}\frac{F_l^{+\prime}(k)}{F_l^+(k)}\, dk = N_l(R) \tag{argP-detail}
$$

$N_l(R)$ 是 $F_l^+$ 在 $C_R$ 内零点计重数。

第一步：上半平面零点结构。`10_jost_analyticity.zh.md:169` 证明了短程实势下 $F_l^+$ 上半平面零点必在正虚轴；正虚轴零点对应束缚态（`10_jost_analyticity.zh.md:163`）。所以 $R \to \infty$ 取极限 $N_l(\infty) = n_l$，第 $l$ 分波束缚态数。

第二步：实轴段。沿实轴从 $-R$ 到 $+R$，

$$
\int_{-R}^{R}\frac{F_l^{+\prime}}{F_l^+}\, dk = \log F_l^+(R) - \log F_l^+(-R)
$$

实势对称 $F_l^+(-k) = F_l^+(k)^*$（(F-reflection)），故 $\log F_l^+(-R) = \log F_l^+(R)^* = \log|F_l^+(R)| - i\arg F_l^+(R)$。代入：

$$
\log F_l^+(R) - \log F_l^+(-R) = 2 i\,\arg F_l^+(R)
$$

按 (F-phase) $\arg F_l^+(R) = -\delta_l(R)$（实 $k > 0$）。所以实轴段贡献

$$
\int_{-R}^{R}\frac{F_l^{+\prime}}{F_l^+}\, dk = -2 i\,\delta_l(R) + 2 i\,\delta_l(0) = 2i\,[\delta_l(0) - \delta_l(R)]
$$

（约定 $\delta_l(0)$ 是从 $\arg F_l^+(0)$ 取的零起点，相位连续 unwrap 后的值。）

第三步：半圆段。$|k| = R \to \infty$ 时 $F_l^+(k) \to 1$（短程势 Volterra 零阶项主导，`10_jost_analyticity.zh.md:227`），故 $\log F_l^+ \to 0$，半圆段贡献 $\int_{\Gamma_R} d\log F_l^+ \to 0$，相当于 $\delta_l(R) \to \delta_l(\infty)$。

第四步：合并。把 (argP-detail) 取虚部（$N_l$ 是实数，但等式右边乘 $1/(2\pi i)$ 后等于 $N_l$；等式左边实轴段虚部贡献由 $2i[\delta_l(0) - \delta_l(\infty)]$ 给出，半圆段贡献 $0$）：

$$
\frac{1}{2\pi i}\cdot 2 i\,[\delta_l(0) - \delta_l(\infty)] = n_l
\quad\Longrightarrow\quad
\delta_l(0) - \delta_l(\infty) = n_l\,\pi
$$

得 (Lev-l>0)。

第五步：s 波零阈值修正。若 $F_0^+(0) = 0$（阈值零能态），围道在 $k = 0$ 处过零点，标准论域原理的"绕避小半圆"贡献必须计入。在 $k = 0$ 周围用半径 $\epsilon$ 小半圆 $\gamma_\epsilon$ 从下方绕过（取上半平面内绕避，$\gamma_\epsilon = \{\epsilon e^{i\theta} : \pi \to 0\}$），$F_0^+(k) \approx F_0^{+\prime}(0)\, k$ 为简单零点，故

$$
\frac{1}{2\pi i}\int_{\gamma_\epsilon}\frac{F_0^{+\prime}}{F_0^+}\, dk \to \frac{1}{2\pi i}\int_\pi^0\frac{1}{k}\,dk = \frac{1}{2\pi i}\cdot(-i\pi) = -\frac{1}{2}
$$

这一额外的 $-1/2$ 项要从 $N_l$ 的计数里减出来，等价地把 (Lev-l0) 右边加 $1/2 \cdot \pi$，得 $\delta_0(0) - \delta_0(\infty) = (n_0 + 1/2)\pi$。整合写成 $n_0^{1/2} \in \{0, 1/2\}$。$l \geq 1$ 时 $F_l^+(0) \neq 0$（离心垒保证），半整数项不出现。

第六步：高分波的细节。$l \geq 1$ 时 $F_l^+(0)$ 是否非零的论证：(F-W) 中的 Wronskian $W[f_l^+, \phi_l]$ 在 $k = 0$ 不退化，因为 $f_l^+(0, r) \to r^{-l}$（自由 $l$ 阶 Hankel 在 $k = 0$ 退化为 $r^{-l}$，不是常数）与 $\phi_l(0, r) \to r^{l+1}/(2l+1)!!$ 远场行为正好满足 $W \neq 0$ 的非退化条件。所以 $F_l^+(0)$ 一般非零，零阈值修正不会出现。

证明完。这条定理把"低能相移 $\delta_l(0)$"与"束缚态数 $n_l$"连成一个整数关系，是相移代码最常用的 sanity check（见 `10_jost_analyticity.zh.md:241`）。

数值验证：方阱。`examples/02_square_well_3d.zh.md:139` 给出 $V_0 \in \{1, 5, 25, 60\}$ 时 s 波相移 $\delta_0(k\to 0) \in \{0, \pi, 2\pi, 2\pi\}$。$V_0 = 1$（$K_0 R = 1 < \pi/2$）无束缚态，$\delta_0(0) = 0$；$V_0 = 5$（$K_0 R \approx 2.24$，$\pi/2 < K_0 R < 3\pi/2$）一个束缚态，$\delta_0(0) = \pi$；$V_0 = 25$（$K_0 R = 5$）与 $V_0 = 60$（$K_0 R \approx 7.75$，$3\pi/2 < K_0 R < 5\pi/2$）两个束缚态，$\delta_0(0) = 2\pi$。完全契合 (Lev-l0)。

## 零阈值奇点与 unitary limit

s 波 $F_0^+(0) = 0$ 是 ERE 与 Levinson 定理同时出现奇异行为的关键临界点。

零阈值条件。$F_0^+(0) = 0$ 等价于零能 s 波规则解 $u_0(r) = \phi_0^{(0)}(r)$ 在远场是常数（不是 $r$ 的线性函数），即 $\phi_0^{(0)}(r) \to $ 常数。比对 $\phi_0^{(0)}(r) \to r - a_0$ 远场，常数行为对应 $a_0 \to \infty$ 同时线性项系数为零。具体地：$1/a_0 = 0$、$a_0 = \pm\infty$ 是零阈值的解析签名。

ERE 在零阈值的退化。(ERE) 形式

$$
k\cot\delta_0(k) = -\frac{1}{a_0} + \frac{r_0}{2}\, k^2 + \ldots = \frac{r_0}{2}\, k^2 + v_0\, k^4 + \ldots
$$

低能下 $k\cot\delta_0 \approx r_0 k^2/2$，故 $\cot\delta_0 \approx r_0 k/2$，$\delta_0 \approx \pi/2 - r_0 k/2 \to \pi/2$ 在 $k \to 0$。s 波相移在阈值上跳到 $\pi/2$，不是 $0$ 或 $n\pi$——这是 zero-crossing of phase shift 的特殊情形。

s 波截面。$\sigma_0 = 4\pi\sin^2\delta_0/k^2 \to 4\pi \cdot 1/k^2 = 4\pi/k^2$（$\delta_0 = \pi/2$ 时 $\sin^2 = 1$）。低能 s 波截面发散为 $4\pi/k^2$，称为 unitary limit。这是 s 波弹性散射的最大可能截面（被 unitarity bound $\sigma_l \leq 4\pi(2l+1)/k^2$ 饱和）。

物理实现。冷原子物理中，磁场调谐让 closed-channel 束缚态能量穿过 open-channel 阈值（Feshbach 共振），$a_0(B)$ 在共振中心 $B_0$ 处发散并改号：

$$
a_0(B) = a_{\rm bg}\Bigl[1 - \frac{\Delta}{B - B_0}\Bigr]
$$

$B \to B_0$ 时 $|a_0| \to \infty$，散射截面饱和到 $4\pi/k^2$。同时 unitary limit 下系统获得离散标度对称性（Efimov physics），三体束缚态出现几何级数 $E_n^{(3)}/E_{n+1}^{(3)} \approx (22.7)^2$ 的谱（Efimov 1970）。这条物理是 Feshbach 共振调谐技术（Chin et al. 2010 Rev. Mod. Phys.）与超冷原子精密测量的核心。

`examples/02_square_well_3d.zh.md:65` 数值演示了同一现象：方阱在 $K_0 R \to \pi/2$ 邻域 $a$ 从 $-\infty$ 跳到 $+\infty$，新束缚态从阈值出来。$K_0 R = \pi/2$ 严格点上 $a = \infty$、$1/a = 0$，正是 unitary limit 的方阱实现。

## 多通道有效力程展开

耦合通道（如 ${}^3 S_1$-${}^3 D_1$ 张量耦合）下，相移 $\delta_l$ 推广为 Stapp 参数 $(\delta_\alpha, \delta_\beta, \epsilon)$（NN 物理标准参数化），$S$ 矩阵是 $2\times 2$ 矩阵。ERE 推广为 $K$ 矩阵的低能展开。

$K$ 矩阵 ERE。多通道 $K$ 矩阵 $K_{ij}(k)$ 满足

$$
K_{ij}(k) = -\bigl[k^{2l_i+1/2} \cot\delta\, k^{2l_j+1/2}\bigr]^{-1}_{ij,\rm eff}
$$

低能展开

$$
K^{-1}_{ij}(k) \approx -\frac{1}{a_{ij}} + \frac{1}{2}\, r_{ij}\, k^2 + O(k^4)
$$

$a_{ij}$ 是矩阵散射长度（$\alpha\alpha$、$\beta\beta$ 对角元、$\alpha\beta$ 非对角元），$r_{ij}$ 同。耦合通道 ERE 共有 $(\dim)\times(\dim+1)/2$ 个独立散射长度（对称矩阵）与同等数量的有效力程。

NN ${}^3 S_1$-${}^3 D_1$。两个分波 $S = l = 0$ 与 $D = l = 2$。Stapp 参数化下 $S$ 矩阵相移分别为 $\delta_S, \delta_D$ 与混合参数 $\epsilon_1$（mixing angle）。$a_S \approx 5.42$ fm（氘核束缚态），$a_D \approx 6.5$ fm³（量纲不同，$l = 2$）；混合参数低能 $\epsilon_1(k) \to k^2/(\ldots)$。详细多通道 ERE 见 `05_partial_wave_projection.zh.md:393` 耦合通道节，这里只给出形式。

## 可解势的 ERE 汇总

把教学轨上几个解析可控势的 ERE 闭式列在这里做对账。

方阱（s 波）。`examples/02_square_well_3d.zh.md:62` 给

$$
a_0 = R\Bigl[1 - \frac{\tan(K_0 R)}{K_0 R}\Bigr]
$$

`examples/02_square_well_3d.zh.md:77` 给 $r_e$ 的解析式

$$
r_0 = R\Bigl(1 - \frac{R^2}{3 a_0^2}\Bigr) - \frac{1}{K_0^2 a_0}\frac{1}{1 - \tan(K_0 R)/(K_0 R)}
$$

数值验证 `examples/02_square_well_3d.zh.md:151`：$V_0 = 2.0$ 时 $a \approx 3.479$，$-1/a \approx -0.287$，$r_e/2 \approx 0.61$，与 $k\cot\delta_0$ vs $k^2$ 数值拟合给的 $-0.280$、$0.610$ 吻合到 2-3 位有效数字。

Yamaguchi（s 波 separable）。`examples/05_separable_rank1.zh.md:94` 给

$$
-\frac{1}{a_0} = -\frac{4\pi\beta^4}{\lambda} - \frac{\beta}{2},\qquad r_0 = \frac{1}{\beta} - \frac{16\pi\beta^2}{\lambda}
$$

ERE 在 Yamaguchi 模型上精确截断在 $k^2$，所有 $v_l, w_l, \ldots = 0$（`examples/05_separable_rank1.zh.md:81`）。这是 separable 势 (kcot) 中 $R_0/A_0$ 退化为多项式比的解析根源。$\lambda = -30, \beta = 1$ 数值验证：$a \approx 12.33$，$r_e \approx 2.68$（`examples/05_separable_rank1.zh.md:155`）。

delta 壳（s 波）。$V = (\gamma/R)\delta(r - R)$，相移闭式 `examples/03_delta_shell.zh.md:73`。低能展开给 $a_0 = R\gamma/(1 + \gamma)$，$r_0 = R\,(1 + \gamma + \gamma^2/3)/(1 + \gamma)^2$ 量级（具体系数依归一化约定）。$\gamma \to -1$ 时 $a_0 \to \pm\infty$，与 unitary limit 对应。

Hulthén 势（s 波，解析可控）。$V(r) = -2\mu\, e^{-\mu r}/(1 - e^{-\mu r})$ 在 $r \to 0$ 行为 $V \sim -2/r$（Coulomb-like），$r \to \infty$ 指数衰减。s 波 Schrödinger 方程可显式解，相移与 $a_0, r_0$ 都有闭式（涉及 digamma 函数）。`examples/13_jost_demo` 计划数值演示 Hulthén 的 Jost 函数零点。

## 与主线笔记的对账

Jost 函数远场展开 (F-asy) 与 Wronskian 定义 (F-W)：`10_jost_analyticity.zh.md:79` 与 `10_jost_analyticity.zh.md:87`。
$F_l^+$ 与相移的 (F-phase) 关系：`10_jost_analyticity.zh.md:131`。
论域原理证明 Levinson 定理的轮廓：`10_jost_analyticity.zh.md:208` 至 `10_jost_analyticity.zh.md:236`，本篇第 7 节把它写完整。
零阈值修正 (Levinson-mod)：`10_jost_analyticity.zh.md:250`。
分波 $T$ 矩阵与 $\delta_l$ 的 on-shell 关系：`05_partial_wave_projection.zh.md:340` 与 `05_partial_wave_projection.zh.md:369`。
分波 $S$ 矩阵 $S_l = e^{2i\delta_l}$：`05_partial_wave_projection.zh.md:378`。
方阱散射长度闭式：`examples/02_square_well_3d.zh.md:62`。
方阱有效力程闭式：`examples/02_square_well_3d.zh.md:77`。
方阱束缚态计数：`examples/02_square_well_3d.zh.md:94`。
方阱 ERE 数值验证：`examples/02_square_well_3d.zh.md:151`。
Levinson 定理在方阱上的相移图：`examples/02_square_well_3d.zh.md:139`。
Yamaguchi $a_0, r_0$ 闭式：`examples/05_separable_rank1.zh.md:94`。
Yamaguchi ERE 精确截断：`examples/05_separable_rank1.zh.md:81`。
Yamaguchi 数值 $a, r_e$：`examples/05_separable_rank1.zh.md:155`。
Yamaguchi 束缚态 $\kappa$、$E_b$：`examples/05_separable_rank1.zh.md:154`。
delta 壳 s 波相移：`examples/03_delta_shell.zh.md:73`。
d 波束缚态阈值（Bargmann 高分波对账）：`examples/08_centrifugal_barrier.zh.md`。
unitary limit 方阱实现：`examples/02_square_well_3d.zh.md:65`。
${}^1 S_0$ 虚态机制：`10_jost_analyticity.zh.md:165`。
Coulomb 势上 Levinson 定理需修改的提示：`10_jost_analyticity.zh.md:243`。

## 小结与 next-step

这一篇是理论闭环轨主线第 E 篇，承接前篇 Jost 函数解析框架，把它在低能展开层面落实到两个工程参数 $a_l$ 与 $r_l$，并把 Levinson 定理从轮廓提升为完整证明。本篇做的事：

- 从 (F-Taylor) 与 (F-reflection) 推出 $F_l^+(k) = R_l(k^2) - i k^{2l+1} A_l(k^2)$ 的实虚分离结构；
- 直接读出 Wigner 阈值定理 $\delta_l \sim -k^{2l+1} a_l$；
- 把 $k^{2l+1}\cot\delta_l = R_l/A_l$ 视为 $k^2$ 的解析函数，Taylor 展开得 ERE 标准形式；
- 给 $a_l$ 几何含义（等效硬球）、$r_l$ 积分公式 (r-int) 的完整 self-derive；
- Bargmann 不等式的论域原理证明，s 波与高分波双版本；
- Levinson 定理详细证明含 $1/2$ 修正项的小半圆论证；
- s 波 unitary limit 与 Feshbach 共振、Efimov 物理对应；
- 与方阱、Yamaguchi、delta 壳的解析 ERE 对账。

next-step：

- 数值 ERE + Levinson 演示。指向 `examples/14_ere_levinson_demo`：取 Yukawa $V = -V_0\, e^{-\mu r}/r$，Numerov 积分径向方程得 $\delta_0(k)$，画 $k\cot\delta_0$ vs $k^2$ 提取 $a_0, r_0$；扫 $V_0$ 越过 Bargmann 阈值看 $\delta_0(0)$ 阶跃；同时画复 $k$ 平面 $F_0^+$ 零点位置验证 (a-pole) 关系。
- Coulomb-modified ERE。Coulomb 势上 Wigner 阈值变为 $\delta_l \sim -k^{2l+1}\, e^{-2\pi\eta}$（指数压制），ERE 改写为 Coulomb-distorted phase shift 的展开 $C_0^2(\eta) k\cot\delta_0 + 2\eta k\, h(\eta) = -1/a_C + r_C k^2/2 + \ldots$（Bethe-Salpeter；Bethe 1949）。$h(\eta) = \mathrm{Re}\,\psi(i\eta) - \ln\eta$。具体推导与 `07_coulomb_scattering.zh.md` 的畸变波接口。
- 多通道 $K$ 矩阵 ERE 的张量耦合具体形式。${}^3 S_1$-${}^3 D_1$ 系统的 $a_S, a_D, a_{SD}$ 与 $r_S, r_D, r_{SD}$ 完整 fit 到 NN 散射数据。Stapp 参数化与 Blatt-Biedenharn 参数化的 ERE 不一样，需要对账。
- 冷原子 unitary limit 物理。Feshbach 共振调谐曲线 $a_0(B) = a_{\rm bg}[1 - \Delta/(B - B_0)]$ 的解析推导（双通道近似），unitary limit 下 BCS-BEC crossover 与 Tan 关系；Efimov 物理（三体离散标度对称、$E_{n+1}/E_n \approx 1/515$）的 ERE 框架介绍。
- 反演问题与 Marchenko 方程。给定 $\delta_l(k)$ 在所有 $k$ 上的值加束缚态能量与归一化常数，$V(r)$ 唯一确定（Marchenko 1955；Gel'fand-Levitan 1955）。本篇的 ERE 是反演输入的低能拟合表达，是核物理 NN 势构造的标准入口。
- 修改 Levinson 定理的拓展。零阈值零能态的 $1/2$ 项在 NN ${}^1 S_0$ 通道上是渐近 $1/2$（虚态贴近阈值的极限）；与束缚态出现的瞬时阈值贯穿对应。Coulomb 修正下 Levinson 定理改成 $\delta_l(0) - \delta_l(\infty) = (n_l - l - 1)\pi$（Coulomb-Levinson；Martin 1958）。
- $N/D$ 表象与色散关系。把 $f_l = N(k)/D(k)$ 中的 $D$ 自带束缚态零点，与 ERE 的 $k^{2l+1}\cot\delta_l$ 对应；色散关系给 $D(k)$ 的 $N/D$ 解，是后续 F 篇主线（$S$ 矩阵复 $E$ 平面色散关系）的入口。
