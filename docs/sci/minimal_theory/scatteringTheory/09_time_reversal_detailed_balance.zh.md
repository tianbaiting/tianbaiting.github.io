# ch09 时间反演与细致平衡

`06_polarization_formalism.zh.md:470` 一节给了字称守恒对 M 矩阵结构的约束，时间反演那一段（`06_polarization_formalism.zh.md:492`）只勾勒了一个不变性条件 (T) 与两条直接推论；本篇把它展开成完整的形式链：从反幺正算符 $\Theta$ 的代数性质出发，导出 Møller 算符在 T 反演下的交换关系 $\Theta\Omega_+\Theta^{-1}=\Omega_-$，进而得到 $\Theta S \Theta^{-1} = S^\dagger$、T 矩阵的反互关系 $T_{\beta\alpha} = T_{\alpha'\beta'}$、截面间的细致平衡公式（含自旋统计因子）以及极化观测量的 T 约束。

定位：本篇是"理论闭环轨"的第 1 篇形式补全。前提是 `03_S_matrix_and_cross_section.zh.md` 的 Møller / S / T 链条与 `06_polarization_formalism.zh.md` 的 M 矩阵 / 自旋张量基底；不再重复其推导。`06_polarization_formalism.zh.md:295` 给出的 $A_y = 2\,\mathrm{Re}(a^*b)/(|a|^2+|b|^2)$ 中"为什么是 Re 而不是 Im"这一约定根源，本篇要把字称约束与 T 反演的双重叠加单独抽出做一次干净的代数推导。

约定：$\hbar = 1$；$\Theta$ 表示完整的多粒子时间反演算符（含自旋部分）；自旋 1/2 取 $\Theta = i\sigma_y K$、自旋 $j$ 取 $\Theta = e^{-i\pi J_y} K$（$K$ 是相对于 $|j,m\rangle$ 基的复共轭算符），相位约定 Condon-Shortley。粒子标记 $\alpha = (\mathbf k, m_a, m_A; \text{species})$ 对应入射通道，$\beta$ 对应出射通道；$\alpha' = \Theta \alpha$ 表示动量与自旋全部反向后的"T 共轭"通道。

主参考：Taylor《Scattering Theory》第 17 章（Time Reversal and Detailed Balance），Newton《Scattering Theory of Waves and Particles》第 7 章；Sakurai《Modern QM》第 4.4 节给反幺正算符代数；Goldberger–Watson《Collision Theory》第 6 章给 detailed balance 的算符形式。

## 反幺正算符 Θ 的基本代数

### 反幺正性的定义

线性算符 $A$ 满足 $A(\alpha|\phi\rangle + \beta|\psi\rangle) = \alpha A|\phi\rangle + \beta A|\psi\rangle$。反线性（antilinear）算符把标量复共轭

$$
A(\alpha|\phi\rangle + \beta|\psi\rangle) = \alpha^* A|\phi\rangle + \beta^* A|\psi\rangle. \tag{antilin}
$$

幺正算符 $U$ 保持内积 $\langle U\phi|U\psi\rangle = \langle\phi|\psi\rangle$；反幺正（antiunitary）算符 $\Theta$ 把内积复共轭

$$
\langle \Theta\phi | \Theta\psi\rangle = \langle\psi|\phi\rangle = \langle\phi|\psi\rangle^*. \tag{antiunit}
$$

任何反幺正算符可分解为 $\Theta = U K$，其中 $U$ 幺正，$K$ 是某个固定基底下的复共轭算符（$K|n\rangle = |n\rangle$、$K c |n\rangle = c^* |n\rangle$）。$K$ 本身是反幺正的，$U$ 的具体形式由 $\Theta$ 在该基底下的矩阵元决定。

### 与单粒子算符的对易关系

$\Theta$ 对单粒子位置、动量、自旋的作用：

$$
\Theta\, \mathbf r\, \Theta^{-1} = \mathbf r,\qquad
\Theta\, \mathbf p\, \Theta^{-1} = -\mathbf p,\qquad
\Theta\, \mathbf S\, \Theta^{-1} = -\mathbf S. \tag{Theta-1p}
$$

复数 $i$ 在 $\Theta$ 下变号

$$
\Theta\, i\, \Theta^{-1} = -i. \tag{Theta-i}
$$

(Theta-i) 是反线性的直接体现：把任一态 $|\psi\rangle$ 换成 $i|\psi\rangle$ 再作 $\Theta$ 等于先作 $\Theta$ 再乘 $-i$。它使得 $[\mathbf r, \mathbf p] = i$ 这条对易关系在 (Theta-1p) 下保持一致：$\Theta [\mathbf r, \mathbf p] \Theta^{-1} = [\mathbf r, -\mathbf p] = -i$，恰对应右边 $i \to -i$。同理 $[\mathbf S_x, \mathbf S_y] = i\mathbf S_z$ 在 $\mathbf S \to -\mathbf S$、$i \to -i$ 下不变。

### 自旋空间中的具体形式

在 $|j,m\rangle$ 基下取 $K$ 为复共轭。要求 $\Theta J_x \Theta^{-1} = -J_x$、$\Theta J_y \Theta^{-1} = -J_y$、$\Theta J_z \Theta^{-1} = -J_z$。$J_z$、$J_x$ 在 Condon-Shortley 约定下为实矩阵，$J_y$ 纯虚。$K$ 把它们送到 $J_z, J_x, -J_y$；要再变号到 $-J_z, -J_x, J_y$，需配合一次 $\pi$ 角绕 $\hat y$ 旋转

$$
e^{-i\pi J_y} J_z e^{i\pi J_y} = -J_z,\qquad e^{-i\pi J_y} J_x e^{i\pi J_y} = -J_x,\qquad e^{-i\pi J_y} J_y e^{i\pi J_y} = J_y.
$$

故

$$
\Theta = e^{-i\pi J_y}\, K \tag{Theta-j}
$$

整体相位可调；上面这个选择给 $\Theta|j,m\rangle = (-1)^{j-m}|j,-m\rangle$（self-derive：用 $d^j_{-m,m}(\pi) = (-1)^{j-m}$）。对自旋 1/2 等价于

$$
\Theta = i\sigma_y K,\qquad \Theta|\tfrac12, \tfrac12\rangle = |\tfrac12, -\tfrac12\rangle,\quad \Theta|\tfrac12, -\tfrac12\rangle = -|\tfrac12, \tfrac12\rangle.
$$

### Θ² 与 Kramers 简并

直接计算

$$
\Theta^2 = e^{-i\pi J_y} K\, e^{-i\pi J_y} K = e^{-i\pi J_y}\, e^{+i\pi J_y}\, K^2 = e^{-2\pi i J_y}\cdot 1 = (-1)^{2j}.
$$

中间用了 $K e^{-i\pi J_y} K = e^{+i\pi J_y}$（$J_y$ 在 CS 约定下纯虚）与 $K^2 = 1$。结论

$$
\Theta^2 = \begin{cases} +1, & 2j \in 2\mathbb{Z}\ (\text{整数自旋})\\ -1, & 2j \in 2\mathbb{Z}+1\ (\text{半整数自旋}) \end{cases}\tag{Theta-sq}
$$

半整数自旋下 $\Theta^2 = -1$ 是 Kramers 简并的根源：若 $H$ 与 $\Theta$ 对易、且不存在外加破 T 的场（典型为外磁场），则 $|\psi\rangle$ 与 $\Theta|\psi\rangle$ 必然正交且简并

$$
\langle\psi | \Theta\psi\rangle = \langle\Theta\psi | \Theta^2\psi\rangle^* = \langle\Theta\psi | -\psi\rangle^* = -\langle\psi|\Theta\psi\rangle \;\Rightarrow\; 0.
$$

第一步用 (antiunit)，第二步用 $\Theta^2 = -1$。整数自旋则无此 forced degeneracy。

### [H, Θ] = 0 的判据

非相对论哈密顿量 $H = \mathbf p^2/(2m) + V(\mathbf r) + V_{LS}\,\mathbf L\!\cdot\!\mathbf S + V_T(\hat r, \mathbf S_1, \mathbf S_2) + \cdots$。每一项在 (Theta-1p) 下变换：$\mathbf p^2$ 偶、$V(\mathbf r)$ 偶、$\mathbf L\!\cdot\!\mathbf S = \mathbf r\times\mathbf p\cdot\mathbf S$ 偶（$\mathbf L$ 与 $\mathbf S$ 同时变号）、张量力 $\mathbf S_1\!\cdot\!\hat r\,\mathbf S_2\!\cdot\!\hat r$ 偶。故强相互作用与电磁相互作用（无外加 $\mathbf B$）下 $\Theta H \Theta^{-1} = H$。

T 对易破坏的典型情形：

- 外加磁场。$\mathbf B$ 是赝矢量，但极化矩 $\boldsymbol\mu\!\cdot\!\mathbf B$ 中 $\boldsymbol\mu \propto \mathbf S$ 在 T 下变号，$\mathbf B$（视为外参数）不动，故该项变号——破坏 T 对易，但若把 $\mathbf B$ 视为动力学量（包含产生 $\mathbf B$ 的电流），则 $\mathbf B \to -\mathbf B$ 整体仍 T 不变。
- 弱相互作用 CP 破坏（CKM 复相位、$\theta_{\text{QCD}}$、新物理）。在散射中体现为微小的 T 破坏振幅（量级 $\lesssim 10^{-4}$）。
- 不可逆耗散（开放系统、密度矩阵的 Lindblad 演化）——但这超出 unitary 散射理论的范畴。

本篇默认 $[\Theta, H] = 0$、$[\Theta, H_0] = 0$（自由演化平移、动能项均 T 不变）。

## Møller 算符在 Θ 下的变换

### Ω± 互换

`03_S_matrix_and_cross_section.zh.md:138` 给的强极限定义

$$
\Omega_+ = \operatorname*{s\text{-}lim}_{t\to-\infty} e^{iHt} e^{-iH_0 t},\qquad \Omega_- = \operatorname*{s\text{-}lim}_{t\to+\infty} e^{iHt} e^{-iH_0 t}.
$$

用 $\Theta$ 共轭。先看有限时刻的 $W(t) = e^{iHt} e^{-iH_0 t}$：

$$
\Theta W(t) \Theta^{-1} = \Theta e^{iHt} \Theta^{-1}\cdot \Theta e^{-iH_0 t}\Theta^{-1} = e^{-iH t}\cdot e^{+iH_0 t} = W(-t).
$$

第二步用 $\Theta i \Theta^{-1} = -i$ 与 $\Theta H \Theta^{-1} = H$、$\Theta H_0 \Theta^{-1} = H_0$。所以

$$
\Theta W(t) \Theta^{-1} = W(-t). \tag{Theta-W}
$$

取强极限。$\Theta$ 反幺正、连续，故强极限可换：当 $t \to -\infty$ 时 $W(t) \to \Omega_+$，对应 $W(-t) \to \Omega_+$ 中变量替换 $t \to -t$ 给 $t' \to +\infty$，即 $W(-t) \to \Omega_-$。结论

$$
\boxed{\;\Theta\, \Omega_+\, \Theta^{-1} = \Omega_-,\qquad \Theta\, \Omega_-\, \Theta^{-1} = \Omega_+.\;}\tag{Theta-Omega}
$$

物理上，$\Omega_+$ 把"过去看起来像 $|\phi\rangle$"翻译成精确散射态；T 反演把过去与未来对调，自然把 $\Omega_+$ 送到 $\Omega_-$。

### Θ S Θ⁻¹ = S†

由 `03_S_matrix_and_cross_section.zh.md:222` 的 $S = \Omega_-^\dagger \Omega_+$：

$$
\Theta S \Theta^{-1} = \Theta\Omega_-^\dagger\Theta^{-1}\,\Theta\Omega_+\Theta^{-1} = (\Theta\Omega_-\Theta^{-1})^\dagger\,\Omega_- = \Omega_+^\dagger\,\Omega_-.
$$

第一步插入 $\Theta^{-1}\Theta = 1$；第二步用 $(\Theta A \Theta^{-1})^\dagger = \Theta A^\dagger \Theta^{-1}$（self-derive：对反幺正算符，$\Theta A \Theta^{-1}$ 把 $A$ 的伴随变成新算符的伴随，但因为反幺正算符本身满足 $\langle\Theta\phi|\Theta\psi\rangle = \langle\psi|\phi\rangle$，其共轭定义需小心；正确版本是 $(\Theta A \Theta^{-1})^\dagger = \Theta A^\dagger \Theta^{-1}$，可由内积比对验证）。

最后得到 $\Omega_+^\dagger \Omega_- = (\Omega_-^\dagger \Omega_+)^\dagger = S^\dagger$。由 S 酉性 $S^\dagger = S^{-1}$：

$$
\boxed{\;\Theta\, S\, \Theta^{-1} = S^\dagger = S^{-1}.\;}\tag{Theta-S}
$$

等价表述：演化算符 $U(t,t_0) = e^{-iH(t-t_0)}$ 满足 $\Theta U(t, t_0)\Theta^{-1} = U(-t, -t_0) = U(t_0, t)$，对全演化区间取极限即给 $S \to S^\dagger$。

### Θ T Θ⁻¹

`04_T_and_U_operators.zh.md:332` 给出 $T(z) = V + V G(z) V$，$G(z) = (z - H)^{-1}$。$V$ 在 T 下不变（势能对易于 $\Theta$）；$G(z)$ 含 $i$ 隐参数（$z = E + i 0$），故

$$
\Theta G(E + i0) \Theta^{-1} = (E - i0 - H)^{-1} = G(E - i0).
$$

得到

$$
\Theta\, T(E + i0)\, \Theta^{-1} = V + V\, G(E - i0)\, V = T(E - i0). \tag{Theta-T}
$$

注意 $T(E - i0) = T(E + i0)^\dagger$ 当 $V = V^\dagger$（self-derive：从 $T = V + VGV$、$G^\dagger(E+i0) = G(E - i0)$ 直接读出）。所以等价地

$$
\Theta\, T(E + i0)\, \Theta^{-1} = T(E + i0)^\dagger. \tag{Theta-T-dag}
$$

## T 矩阵的反互关系

### 自由基底矩阵元的反互

把 (Theta-T-dag) 对自由基底取矩阵元。设 $|\alpha\rangle = |\mathbf k, m_a, m_A\rangle$、$|\beta\rangle = |\mathbf k', m'_b, m'_B\rangle$，定义共轭标签

$$
|\alpha'\rangle \equiv \Theta|\alpha\rangle = \eta_\alpha\,|-\mathbf k, -m_a, -m_A\rangle
$$

类似 $|\beta'\rangle$。$\eta$ 是 (Theta-j) 中的 $(-1)^{s-m}$ 类相位（具体 $\eta_\alpha = (-1)^{s_a - m_a + s_A - m_A}$）。

由反幺正性

$$
\langle \beta | T | \alpha\rangle = \langle \Theta T \alpha | \Theta\beta\rangle^* \cdot 1 \;\;? 
$$

更稳的写法：$\langle\Theta\phi|\Theta\psi\rangle = \langle\psi|\phi\rangle$，即 $\Theta$ 把 ket 上的标量内积复共轭。具体地

$$
\langle\beta | T | \alpha\rangle = \langle\Theta\beta | \Theta T \alpha\rangle^*\quad(\text{wrong convention})
$$

正确做法是同时考虑 $\Theta$ 既作用在 bra 也作用在 ket 上。直接的等式（self-derive 推导）：

$$
\langle \beta | T(E + i0) | \alpha\rangle = \overline{\langle \Theta\beta | \Theta\, T(E+i0)\, \Theta^{-1}\,\Theta | \alpha\rangle\,}^{\;*} \cdot (\text{wrong})
$$

为了避免约定混乱，直接用算符等式 (Theta-T-dag) 加 $\Theta\beta = \beta'$、$\Theta\alpha = \alpha'$，并用 $\Theta^\dagger = \Theta^{-1}$（反幺正算符）：

$$
\begin{aligned}
\langle \beta'|T(E+i0)|\alpha'\rangle
&= \langle \Theta\beta\,|\,T\,|\,\Theta\alpha\rangle\\
&= \langle\Theta\beta\,|\,\Theta\,(\Theta^{-1}T\Theta)\,|\,\alpha\rangle\\
&= \langle\Theta\beta\,|\,\Theta\,T(E - i0)\,|\,\alpha\rangle\\
&= \langle\beta\,|\,T(E - i0)\,|\,\alpha\rangle^*\\
&= \langle\alpha\,|\,T(E + i0)\,|\,\beta\rangle\,.
\end{aligned} \tag{Trec}
$$

第二步插 $\Theta^{-1}\Theta = 1$；第三步用 (Theta-T)；第四步用 $\Theta$ 反幺正性 $\langle\Theta\phi|\Theta\chi\rangle = \langle\phi|\chi\rangle^*$（这里 $\chi = T(E-i0)|\alpha\rangle$，把 $\Theta$ 提出于 ket 之外得 $\langle\Theta\beta|\Theta\chi\rangle = \langle\beta|\chi\rangle^*$）；第五步用 $\langle\beta|T(E-i0)|\alpha\rangle = \langle\beta|T(E+i0)^\dagger|\alpha\rangle = \langle\alpha|T(E+i0)|\beta\rangle^*$ 与外层共轭抵消。

最终 reciprocity（反互）关系

$$
\boxed{\;\langle\beta'|\,T(E+i0)\,|\alpha'\rangle = \langle\alpha\,|\,T(E+i0)\,|\beta\rangle.\;}\tag{T-reciprocity}
$$

物理含义：从 $\alpha$ 到 $\beta$ 的跃迁振幅，等于其 T 共轭的"反向"跃迁——把 $\alpha\to\beta$ 中所有动量、自旋反向后的 $\beta'\to\alpha'$ 振幅。

### 与 (T) 公式的等价

`06_polarization_formalism.zh.md:497` 给的 M 矩阵形式

$$
M_{m'_b m'_B; m_a m_A}(-\hat{\mathbf k}, -\hat{\mathbf k}') = \prod_i (-1)^{s_i - m_i + s'_i - m'_i}\, M^*_{-m_a, -m_A;\, -m'_b, -m'_B}(\hat{\mathbf k}', \hat{\mathbf k})
$$

正是把 (T-reciprocity) 翻译到 M 矩阵语言：左右两侧的 $(s-m)$ 相位来自 (Theta-j) 的 $\eta$ 因子；下标交换体现 $\alpha \leftrightarrow \beta'$ 的对调；复共轭是 (Trec) 推导第四步留下的。所以本篇 $\text{(T-reciprocity)}$ 与 polarization 篇的 (T) 同一回事，只是抽象层级不同。

## 细致平衡

### 截面间的关系

考虑反应 $a + A \to b + B$（不一定弹性，质量 $m_i$ 可以不同）。质心系入射相对动量 $\mathbf k_a$、出射 $\mathbf k_b$，能量守恒 $E = k_a^2/(2\mu_a) + Q_a = k_b^2/(2\mu_b) + Q_b$（$Q$ 是内禀质量能）。微分截面（自旋已平均）

$$
\frac{d\sigma_{a\to b}}{d\Omega}(\hat{\mathbf k}_b\leftarrow \hat{\mathbf k}_a) = \frac{\mu_a \mu_b}{(2\pi)^2}\,\frac{k_b}{k_a}\,\frac{1}{(2s_a+1)(2s_A+1)}\sum_{m_a,m_A,m_b,m_B}|T_{\beta\alpha}|^2.
$$

逆向反应 $b + B \to a + A$ 截面

$$
\frac{d\sigma_{b\to a}}{d\Omega}(\hat{\mathbf k}_a\leftarrow \hat{\mathbf k}_b) = \frac{\mu_a \mu_b}{(2\pi)^2}\,\frac{k_a}{k_b}\,\frac{1}{(2s_b+1)(2s_B+1)}\sum |T_{\alpha\beta}|^2.
$$

由 (T-reciprocity)：$\sum_{\text{spins}}|T_{\beta\alpha}(\mathbf k'\leftarrow \mathbf k)|^2 = \sum_{\text{spins}}|T_{\alpha'\beta'}(-\mathbf k\leftarrow -\mathbf k')|^2$。再用旋转不变性把 $-\mathbf k, -\mathbf k'$ 整体旋转回到 $\mathbf k, \mathbf k'$（自旋求和已对称地包含所有 $\pm m$，故 $-m \to m$ 标记重命名不影响），得到 $\sum|T_{\beta\alpha}|^2 = \sum|T_{\alpha\beta}|^2$（自旋求和 + T 反演下相等）。代入两个截面公式相除

$$
\boxed{\;
(2s_a+1)(2s_A+1)\,k_a^2\,\frac{d\sigma_{a\to b}}{d\Omega} = (2s_b+1)(2s_B+1)\,k_b^2\,\frac{d\sigma_{b\to a}}{d\Omega}.
\;}\tag{detbal}
$$

这就是细致平衡（detailed balance）公式。注意角变量：左边在 $\hat{\mathbf k}_b\leftarrow\hat{\mathbf k}_a$ 处取值，右边在 $\hat{\mathbf k}_a\leftarrow\hat{\mathbf k}_b$ 处取值，两侧的散射角（$\theta = \angle$ 入射出射）相同。

### 弹性散射的退化情形

弹性 $a + A \to a + A$，$m_b = m_a$、$s_b = s_a$、$\mu_b = \mu_a$、$k_b = k_a$、$Q_b = Q_a$。(detbal) 退化为

$$
\frac{d\sigma}{d\Omega}(\theta) = \frac{d\sigma}{d\Omega}(\theta).
$$

平凡，因为弹性散射的"反向反应"就是其本身。这说明细致平衡只对真正不同的入出射通道（反应、转移、重排）才有非平凡含义——例如 $p + p \to d + \pi^+$ 与 $d + \pi^+ \to p + p$ 间的截面比较。

### 历史角色

(detbal) 在反应核物理中的早期应用：从已测得的 $\pi^+ d \to pp$ 反推 $pp \to \pi^+ d$（前者实验上更易因为 $\pi^+$ 束流容易，后者直接测 $\pi^+$ 角分布需要 close-target 几何）。配上自旋统计因子 $(2\cdot 0 + 1)(2\cdot 1 + 1) / [(2\cdot 1/2+1)^2 \cdot 1/2!] = 3/2$（$1/2!$ 来自 $pp$ 全同），(detbal) 给出两侧截面的精确比，常作为 $s_\pi = 0$ 的实验检验。

## 极化观测量的 T 约束

### A_y 的双重约束推导

回到 spin-1/2 + spin-0 弹性散射。`06_polarization_formalism.zh.md:237` 的 M 矩阵在字称约束下为 $M = a\,I + b\,\boldsymbol\sigma\!\cdot\!\hat{\mathbf n}$。在 (T-reciprocity) 下要求

$$
M(-\hat{\mathbf k}, -\hat{\mathbf k}')_{m'\to m'',\,m\to m'''} = (-1)^{1/2-m+1/2-m'}\, M^*_{-m, -m'''; -m''', -m'}(\hat{\mathbf k}', \hat{\mathbf k})
$$

（此处自旋 0 靶的 $m_A$ 求和已平凡化）。把 $M = a\,I + b\,\sigma_n$ 代入。$\hat{\mathbf k}\to -\hat{\mathbf k}$、$\hat{\mathbf k}'\to -\hat{\mathbf k}'$ 下 $\hat{\mathbf n} = \hat{\mathbf k}\times\hat{\mathbf k}'/|\cdot| \to \hat{\mathbf n}$（两个负号抵消）。$\sigma_n$ 在自旋翻转下 $i\sigma_y \sigma_n^* (i\sigma_y)^{-1} = -\sigma_n^* (i\sigma_y)(i\sigma_y)^{-1} = \sigma_n$（self-derive：$\sigma_y$ 反对易于 $\sigma_x, \sigma_z$，对易于自身；$\boldsymbol\sigma^* = (\sigma_x, -\sigma_y, \sigma_z)$）。

具体计算 $\Theta M \Theta^{-1}$：

$$
\Theta\,(a\,I + b\,\boldsymbol\sigma\!\cdot\!\hat{\mathbf n})\,\Theta^{-1} = a^*\,I + b^*\,\Theta\,\boldsymbol\sigma\!\cdot\!\hat{\mathbf n}\,\Theta^{-1} = a^*\,I + b^*\,(-\boldsymbol\sigma)\!\cdot\!(-\hat{\mathbf n}^*) = a^*\,I + b^*\,\boldsymbol\sigma\!\cdot\!\hat{\mathbf n}.
$$

中间用了 $\Theta\,\boldsymbol\sigma\,\Theta^{-1} = -\boldsymbol\sigma$、$\Theta\,\hat{\mathbf n}\,\Theta^{-1} = \hat{\mathbf n}^*$（实矢量在 $K$ 下不变，但写作 $\hat{\mathbf n}^*$ 强调它来自 c-数）；负负相消。再加上 (T-reciprocity) 要求 $M(\mathbf k',\mathbf k) \leftrightarrow M(-\mathbf k, -\mathbf k')$（旋转不变把它送回 $M(\mathbf k', \mathbf k)$ 自身），得到

$$
a(\theta) = a^*(\theta) \cdot (\text{or some constraint})
$$

——但这显然太强（$a, b$ 一般是复数）。实际的约束更微妙：(T-reciprocity) 不是 $M = M^T$ 而是 $M(\mathbf k'\!\leftarrow\!\mathbf k) = M^T(-\mathbf k\!\leftarrow\!-\mathbf k')$，把入出标签也对调。对 $a I + b\sigma_n$ 形式的 spin-1/2 + 0 M 矩阵，这一约束自动满足（self-derive：$M$ 对 $(\mathbf k, \mathbf k')$ 与对入出自旋指标的依赖通过 $\sigma_n$ 共同携带；T 反演把两者一同送过去再送回来，给出恒等式）。

### 为何 A_y = Re 而非 Im

`06_polarization_formalism.zh.md:295` 的 $A_y = 2\,\mathrm{Re}(a^*b)/(|a|^2+|b|^2)$ 中"Re"的根源：

字称约束去掉 M 矩阵中赝标量项 $\boldsymbol\sigma\!\cdot\!\hat{\mathbf l}, \boldsymbol\sigma\!\cdot\!\hat{\mathbf m}$，剩下的 $a\,I + b\,\sigma_n$ 是字称允许的最一般形式。计算 $A_y \propto \mathrm{Tr}[M\sigma_n M^\dagger]$ 直接得 $a^*b + ab^* = 2\,\mathrm{Re}(a^*b)$。

T 反演的额外贡献：要求 $a, b$ 满足某种 reciprocity。在弹性 spin-1/2 + 0 散射中，T 反演结合旋转不变性自动满足，没有给 $a, b$ 添加新约束（即 T 在这一情形下"trivially" 满足）。所以 $A_y$ 的"Re"完全来自字称（决定 M 的代数结构）和分波展开中 $1/(2ik)$ 的相位选取（决定 $a, b$ 是 $\mathrm{Re}(a^*b)$ 还是 $\mathrm{Im}(a^*b)$）。

但在更复杂情形（spin-1/2 × spin-1/2、spin-1 × spin-0 等），T 反演给出独立约束。例：spin-1/2 + spin-1/2 NN 散射的 Wolfenstein 5 振幅 $\{a, b, c, d, e\}$ 中，若不强加 T 反演只用字称 + 旋转，独立振幅本是 6 个；T 反演把"对易项 $f$"约束为零或写成其它 5 项的线性组合，从而把独立参数个数压回 5。

### Spin-1 张量极化的 T 约束

`06_polarization_formalism.zh.md:451` 给出字称约束下 spin-1 + spin-0 的 analyzing power 张量 $T_{kq}$ 中非零分量

$$
i T_{11},\; T_{20},\; T_{21},\; T_{22}
$$

而 $T_{10} = 0$、$\mathrm{Re}\,T_{11} = 0$ 来自字称 + T 反演的合成约束。详细来看：

- 字称：$T_{kq}(\theta) = (-1)^{k+q}\,T_{k,-q}^*(\theta)$（self-derive：$\hat{\mathbf n}\to\hat{\mathbf n}$，$T_{kq}$ 在 $\hat{\mathbf n}\to -\hat{\mathbf n}$ 下变 $(-1)^k$，再加复共轭来自 $\hat{\mathbf n}^* = \hat{\mathbf n}$ 但 azimuthal 方向 $\phi\to\pi-\phi$ 给 $q\to-q$ 加 $(-1)^q$）。
- T 反演：$T_{kq}(\theta) = (-1)^q\, T_{k,-q}^*(\theta)$（self-derive 类似但 azimuthal 翻转的来源是入出对调 + 旋转回来）。

两个约束乘除得 $T_{kq} = (-1)^k\,T_{kq}$，即 $T_{kq} = 0$ 当 $k$ 奇 + $q = 0$（特别 $T_{10} = 0$）。$\mathrm{Re}\,T_{11} = 0$ 来自字称要求 $T_{11} = -T_{1,-1}^*$、T 要求 $T_{11} = -T_{1,-1}^*$（合作给 $T_{11} = -T_{11}^*$，纯虚）。

实验记号 $iT_{11}$（带 $i$）是为了让 vector analyzing power 取实值；选择来自上面的"纯虚"性质。

### 极化转移系数的 reciprocity

`06_polarization_formalism.zh.md:309` 定义出射极化矢量 $\mathbf P_\text{out}$。极化转移系数 $D_{ij}$（入射极化沿 $j$、出射极化沿 $i$）满足 T 反演下的关系

$$
D_{ij}(\hat{\mathbf k}'\leftarrow\hat{\mathbf k}) = D_{ji}(-\hat{\mathbf k}\leftarrow -\hat{\mathbf k}'). \tag{D-rec}
$$

特别地，"$D_{NN}$"（双方 $\hat n$ 方向）在 T 反演下对自身。结合字称（保 $\hat n$）后给出在弹性散射中 $D_{NN}(\theta)$ 是实函数且在 $\theta\to\pi-\theta$ 下满足额外 symmetry（仅当全同粒子或自伴反应）。

### Analyzing power 与 induced polarization 等同性

弹性散射，spin-1/2 + spin-0：T 反演给

$$
A_y(\theta) = P_y(\theta\,|\,\text{unpolarized in}) \tag{Ay-Py}
$$

self-derive：$P_y(\text{unpol}) = \mathrm{Tr}[M M^\dagger \sigma_n]/\mathrm{Tr}[M M^\dagger] = (a^*b + ab^*)/(|a|^2+|b|^2) = 2\,\mathrm{Re}(a^*b)/(|a|^2+|b|^2)$，恰为 $A_y$。这是 (T-reciprocity) 的 spin-1/2 specific 体现。物理上：用 polarized beam 测 analyzing power 与用 unpolarized beam 测 induced polarization 等价——这对 polarimeter 校准是关键，避免直接产生 polarized beam 的复杂性。

## 极化观测量的实验约束

### 三角不等式

入射密度矩阵 $\rho_\text{in} \succeq 0$ 蕴含极化矢量长度 $|\mathbf P_\text{in}| \le 1$（spin-1/2）、$|p_z| \le 1$ 与张量极化的 $\rho \succeq 0$ 给出的多面体约束（spin-1）。出射密度矩阵也满足 $\rho_\text{out} \succeq 0$，故 $|\mathbf P_\text{out}| \le 1$。

由 $\mathbf P_\text{out} = \mathbf A + D \mathbf P_\text{in}$（spin-1/2 + 0，矩阵形式），$|\mathbf P_\text{out}| \le 1$ 对所有 $|\mathbf P_\text{in}| \le 1$ 给出对 $\{A_y, D_{ij}\}$ 的约束。具体一例（self-derive）：

$$
A_y^2 + D_{nn}^2 \le 1 + 2 A_y D_{nn}\cdot\xi
$$

其中 $\xi$ 与具体测量配置有关；更通用的 Wolfenstein-Ashkin 不等式可由 $\rho_\text{out}$ 的 $2\times 2$ 矩阵 positivity 直接读出。

### T + 字称下的独立观测量计数

spin-1/2 + spin-0 弹性：复振幅 $a, b$ 各 1 个复数共 4 实自由度，扣去整体相位剩 3 个；M 矩阵的 8 个实矩阵元由 3 个独立参数确定。可观测量：$d\sigma_0/d\Omega, A_y, D_{nn}$ 共 3 个（$D_{ll}, D_{mm}$ 等可由 $D_{nn}$ 与字称约束给出，不独立）。

spin-1/2 + spin-1/2 弹性（NN）：5 个复振幅 - 1 整体相位 = 9 实自由度。完整观测量集（PWA 标准）：$d\sigma_0/d\Omega, A_y, P, D, R, A, R', A', A_{xx}, A_{yy}, A_{xz}, C_{nn}, \ldots$，共约 11 个 standard 观测量与 9 个独立参数关系——超定，作为 PWA 一致性检验。

spin-1 + spin-0 弹性（dpol）：4 个复振幅 - 1 = 7 实自由度。观测量 $d\sigma_0/d\Omega$、$iT_{11}, T_{20}, T_{21}, T_{22}$（5 个 analyzing power）、polarization transfer 多个，共测得超定。

## T 破缺与 CP 破坏

实验上 T 破缺多通过寻找"T-odd 关联"测试。散射理论中典型的 T-odd 三重积关联

$$
\langle \mathbf p_1\!\cdot\!(\mathbf p_2\times\mathbf S)\rangle
$$

在精确 T 不变下应为零（而 final-state interaction 可产生类 T-odd 但实际 T 不变的"伪信号"，需细致区分）。

中子 EDM $d_n$：$d_n\,\mathbf S\!\cdot\!\mathbf E$ 在 T 下变号（$\mathbf E \to \mathbf E$、$\mathbf S \to -\mathbf S$），故 $d_n \neq 0$ 直接破 T。当前实验上限 $d_n < 1.8\times 10^{-26}\,e\,\mathrm{cm}$（PSI 2020），强约束 CP 破坏新物理。

中子 $\beta$ 衰变 $D$ 项：角分布中含 $D\,\mathbf p_e\!\cdot\!(\mathbf p_\nu\times\mathbf S_n)/E$，T 变换下变号。实验测得 $D = (-1.2 \pm 2.0)\times 10^{-4}$，与 SM 预言一致。

散射中的 T 破缺，量级 $\lesssim 10^{-4}$，对极化测量精度要求高时（如低能 NN 散射的 polarized observables 极致测量）需要在分析中显式考虑；常规 dpol 测量不必。

## 多通道 T 反演

### 反应通道下的 detailed balance

`04_T_and_U_operators.zh.md:519` 的 AGS 跃迁算符 $U_{\beta\alpha}$ 描述三体（或多通道两体）从入射通道 $\alpha$ 到出射通道 $\beta$ 的有效跃迁。T 反演在通道空间中把 $\alpha\leftrightarrow\beta'$、$\beta\leftrightarrow\alpha'$ 对调

$$
\Theta\, U_{\beta\alpha}(E)\, \Theta^{-1} = U_{\alpha'\beta'}^\dagger(E) \tag{Theta-U}
$$

类比 (Theta-T-dag)。具体到反应 $a + (BC) \to b + (CA)$ 类型的转移反应，T 反演给

$$
(2J_a + 1)(2J_{BC} + 1)\, k_a^2\, \frac{d\sigma_{a\to b}}{d\Omega} = (2J_b + 1)(2J_{CA} + 1)\, k_b^2\, \frac{d\sigma_{b\to a}}{d\Omega} \tag{detbal-3}
$$

其中 $J$ 是各通道的有效自旋（含两体束缚态内部自旋耦合）。这是把 (detbal) 推到 reactive 通道的形式。

### 与 Friedrichs / 分波耦合的衔接

`01_friedrichsModel.zh.md:79` 单通道模型不显式涉及 detailed balance（弹性退化平凡）；推广到多通道 Friedrichs（一个离散态耦合多个连续谱）时，连续谱通道间的截面满足 (detbal)。

`05_partial_wave_projection.zh.md:396` 的耦合通道分波 LS 方程 $T^J_{l'l}$ 是"通道指标 = $(l, s)$"的版本。T 反演给出 $T^J_{l'l, s's}(k', k) = T^J_{ll', ss'}(k, k')$（指标对调 + 动量交换；自旋张量已经对称化到分波基底里），这是 (T-reciprocity) 在分波基底下的具体形式。Stapp 等价相移参数 $\bar\delta_l$、$\epsilon_J$ 实数性的根源即此（self-derive：T 反演让 $S^J$ 在适当基底下对称，对称酉矩阵可参数化为 Stapp 形式）。

## 与主线笔记的对账

| 主线知识点 | 对账位置 | 本篇位置 |
|:--|:--|:--|
| Møller 算符强极限定义 | `03_S_matrix_and_cross_section.zh.md:138` | (Theta-Omega) 推导 |
| $S = \Omega_-^\dagger\Omega_+$ | `03_S_matrix_and_cross_section.zh.md:222` | (Theta-S) 推导 |
| on-shell $S = 1 - 2\pi i\delta(E) T$ | `04_T_and_U_operators.zh.md:380` | (T-reciprocity) 矩阵元化 |
| $T = V + V G V$ | `04_T_and_U_operators.zh.md:332` | (Theta-T) 推导 |
| $f = -(2\pi)^2 \mu\, t$ | `03_S_matrix_and_cross_section.zh.md:307` | 截面公式 (detbal) |
| $d\sigma/d\Omega = |f|^2$ | `03_S_matrix_and_cross_section.zh.md:420` | (detbal) 推导 |
| 光学定理 $\mathrm{Im}\,f = (k/4\pi)\sigma_\text{tot}$ | `03_S_matrix_and_cross_section.zh.md:451` | T 反演下保持（酉性） |
| M 矩阵字称约束 (P) | `06_polarization_formalism.zh.md:477` | $A_y$ 双重约束分析 |
| M 矩阵 T 反演约束 (T) | `06_polarization_formalism.zh.md:497` | (T-reciprocity) 翻译 |
| spin-1/2 + 0 的 $A_y$ | `06_polarization_formalism.zh.md:295` | $A_y = \mathrm{Re}$ 推导 |
| 张量极化 $T_{kq}$ 非零分量 | `06_polarization_formalism.zh.md:454` | spin-1 T 约束 |
| 出射极化 $\mathbf P_\text{out}$ | `06_polarization_formalism.zh.md:309` | (D-rec) 极化转移 |
| Wolfenstein 5 振幅 | `06_polarization_formalism.zh.md:342` | 独立观测量计数 |
| 耦合通道 $T^J_{l'l}$ | `05_partial_wave_projection.zh.md:396` | 分波 reciprocity |
| AGS 跃迁算符 $U_{\beta\alpha}$ | `04_T_and_U_operators.zh.md:519` | (Theta-U) |
| Friedrichs 离散-连续耦合 | `01_friedrichsModel.zh.md:79` | 多通道 detailed balance |

每条均可用 `grep -n` 在源文件中校验。

## next-step

本篇给的形式约束在配套例子篇中数值化的几个具体方向（按优先级）：

- 多通道 Friedrichs 的数值 detailed balance 验证：扩展 `examples/09_feshbach_two_channel`（若存在）或新建 `examples/12_detailed_balance_demo.zh.md`，构造离散态 + 双连续谱（不同色阈、不同质量）的可解 Friedrichs 模型，数值取通道对 $(c_1, c_2)$ 间的截面，校验 $k_1^2\,\sigma_{1\to 2} = k_2^2\,\sigma_{2\to 1}$（自旋退化为零的简化版），并扫过共振附近观察 detailed balance 在峰旁的精确成立。
- $A_y = P_y$ 等同性的数值演示：在 Yukawa + spin-orbit 模型中数值算 $a(\theta), b(\theta)$，画 $A_y(\theta)$ 与从 unpolarized beam 推出的 $P_y(\theta)$ 重合曲线，作为 (Ay-Py) 的可视化。
- Stapp 相移参数的实数性：从带张量耦合的 ${}^3S_1$-${}^3D_1$ NN 势数值解耦合通道 LS 方程，提取 $S^{J=1}$ 矩阵；把 (Theta-T) 翻译为对 $S$ 的对称性约束（$S^{J=1}$ 的 off-diagonal 元相等），数值验证 $S^J = S^{J\,T}$ 到机器精度。
- T 破缺信号的计算：在 $D = 0$ 的 SM 计算之上引入小 T 破缺扰动 $\delta H$，数值算反应中子 $\beta$ 衰变的 $D$ 项作为 $\delta H$ 的函数；与 T-保持基底下 final-state interaction 给出的"伪 T-odd"信号区分。
- 三体 detailed balance：把 (detbal-3) 应用到 $d + p \to {}^3\mathrm{He} + \gamma$ 与 $\gamma + {}^3\mathrm{He} \to d + p$ 间的截面比较；与 AGS `04_T_and_U_operators.zh.md:598` 数值解的 $U_{\beta\alpha}$ 矩阵元一致性检验。
- Coulomb 修正下的 T 反演：长程 Coulomb 相位 $\sigma_l$ 是实的、与 T 反演兼容；但 Coulomb-renormalized T 矩阵 $T^\text{SR}$ 的反互关系需仔细处理（`07_coulomb_scattering.zh.md:326` 已用 $\psi_C^{(-)} = [\psi_C^{(+)}(-\mathbf k)]^*$ 暗示这一点）。明确写出 long-range + short-range 分解下 (T-reciprocity) 的修正版本。
- dpol 测量的极化转移系数 reciprocity 校准：实验上对 ${}^4\mathrm{He}(\vec d, \vec d){}^4\mathrm{He}$ 弹性散射测 $D_{ij}(\theta)$ 全表，校验 (D-rec) 在 $\theta \to \theta$（弹性）下的简化版本，作为 polarimeter 系统误差的诊断。
