# 极化形式与自旋观测量

`partial_wave_projection.zh.md` 的最后一节给了带自旋耦合通道的 LS 方程，但停在 $T^J_{l'l}(k', k; E)$。从这里到一台真实极化谱仪测出 $A_y(\theta)$、$iT_{11}(\theta)$、$T_{20}(\theta)$，中间还有完整一段形式链：T 算符在自旋空间投影为 M 矩阵，密度矩阵把入射极化态参数化，截面公式把 M 矩阵的双线性式翻译成可观测的张量极化系数。本篇就是这一段链。

定位：dpol（氘核极化测量）研究的理论基底。自旋 1 + 自旋 0 的小节是 dpol polarimeter 公式的母方程；自旋 1/2 + 自旋 1/2 的 Wolfenstein 段是 NN 散射输入；时间反演与字称段提供 $A_y$ 非零、$A_x = A_z = 0$ 这类约束的形式根据。

约定：Madison 约定（1971，关于极化矢量与不可约张量极化），Condon-Shortley 相位约定（与分波篇一致），$\hbar = 1$。其它约定（Saclay、Bystricky、Wolfenstein 原始记号）只在做转换时引入。

## 自旋空间与 M 矩阵

### 散射通道与态空间

考察弹性或非弹性两体散射

$$
a + A \;\to\; b + B
$$

入射粒子 $a$ 自旋 $s_a$，靶 $A$ 自旋 $s_A$；出射 $b$、$B$ 自旋 $s_b$、$s_B$。质心系内的相对动量初末为 $\mathbf{k}$、$\mathbf{k}'$，能量 $E = k^2/(2\mu)$（弹性，$|\mathbf{k}'|=|\mathbf{k}|$）或 $|\mathbf{k}'| = k'$（非弹性）。

入射通道 Hilbert 空间分解为

$$
\mathcal{H}_\text{in} = L^2(\mathbb{R}^3) \otimes V_{s_a} \otimes V_{s_A},
\qquad \dim V_{s} = 2s+1
$$

出射通道类似。自旋分量的基取磁量子数本征基 $|s, m\rangle$。

### 从 T 算符到 M 矩阵

`T_and_U_operators.zh.md:380` 给出 on-shell S 矩阵元

$$
\langle \beta | S | \alpha\rangle = \delta_{\beta\alpha} - 2\pi i\, \delta(E_\beta - E_\alpha)\, \langle \beta | T(E_\alpha) | \alpha\rangle
$$

把通道指标 $\alpha, \beta$ 具体化为 $\alpha = (\mathbf{k}, m_a, m_A)$、$\beta = (\mathbf{k}', m'_b, m'_B)$。在自旋空间的固定磁量子数子集上抽出 $T$ 的矩阵元，并按 `S_matrix_and_cross_section.zh.md:307` 的振幅约定 $f = -(2\pi)^2 \mu\, t$，定义 M 矩阵

$$
M_{m'_b m'_B;\, m_a m_A}(\mathbf{k}', \mathbf{k}) \equiv f_{m'_b m'_B;\, m_a m_A}(\mathbf{k}'\leftarrow \mathbf{k}) \tag{M}
$$

它是一个 $(2s_b+1)(2s_B+1) \times (2s_a+1)(2s_A+1)$ 的矩阵，以行为出射自旋指标 $(m'_b, m'_B)$，以列为入射自旋指标 $(m_a, m_A)$，矩阵元是 $(\mathbf{k}', \mathbf{k})$ 的函数（在弹性散射中只依赖 $\hat{\mathbf{k}}', \hat{\mathbf{k}}$ 与能量）。

约定坐标系：取 $\hat{\mathbf{k}} = \hat{\mathbf{z}}$，则 M 只依赖 $(\theta, \phi)$，其中 $\theta = \angle(\hat{\mathbf{k}}, \hat{\mathbf{k}}')$、$\phi$ 是出射方向相对参考方位的方位角（Madison 约定取入射极化矢量沿 $\hat{\mathbf{y}}$ 时 $\phi = 0$ 在散射平面内）。

### 旋转协变性

$T$ 算符旋转不变（假设强相互作用旋转对称），故对任意 $\mathcal{R} \in SO(3)$

$$
M(\mathcal{R}\hat{\mathbf{k}}', \mathcal{R}\hat{\mathbf{k}}) = D^{(s_b)}(\mathcal{R}) \otimes D^{(s_B)}(\mathcal{R})\; M(\hat{\mathbf{k}}', \hat{\mathbf{k}})\; D^{(s_a)\dagger}(\mathcal{R}) \otimes D^{(s_A)\dagger}(\mathcal{R}) \tag{R}
$$

其中 $D^{(s)}(\mathcal{R})$ 是自旋 $s$ 的不可约旋转矩阵（即 `partial_wave_projection.zh.md:226` 的 Wigner D 函数）。这条协变性约束 M 的算符结构：M 必须能写成 $\hat{\mathbf{k}}, \hat{\mathbf{k}}'$ 的标量与自旋张量算符的双线性组合。

### 与分波展开的衔接

把 $T$ 矩阵元在耦合分波基 $|k; (l\, s)\, J\, M\rangle$ 中分解，再用球谐函数与 CG 系数把磁量子数指标换回，得到 M 矩阵的分波展开

$$
M_{m'_b m'_B;\, m_a m_A}(\hat{\mathbf{k}}', \hat{\mathbf{k}}) = \frac{4\pi}{2ik} \sum_{J, l, l', s, s'} \cdots\, \bigl[\delta_{l'l}\delta_{s's} - S^J_{l's',ls}(k)\bigr]\, Y_{l'\!,m_l'}(\hat{\mathbf{k}}')\, Y^*_{l, m_l}(\hat{\mathbf{k}})\, \langle l'm_l', s'm_s' | JM\rangle\, \langle l m_l, s m_s | JM\rangle
$$

（自旋耦合 $s = s_a \otimes s_A$ 至总通道自旋；磁量子数约束 $m_l + m_s = M = m_l' + m_s'$。）这是 `partial_wave_projection.zh.md:396` 中耦合通道 $T^J_{l'l}$ 经自旋外积投影的"本征"形式。

具体的自旋情形（1/2×0、1/2×1/2、1×0）只是这条公式在不同 $s, s'$ 下的具体化。下面把每种情形的 M 矩阵写出闭合形式。

## 极化与密度矩阵

### 一般密度矩阵

入射粒子的极化态由密度矩阵描述：

$$
\rho_\text{in} = \rho_a \otimes \rho_A,
\qquad
\rho_a^\dagger = \rho_a,\ \mathrm{Tr}\,\rho_a = 1,\ \rho_a \succeq 0
$$

纯态 $|s, m\rangle$ 对应 $\rho = |s, m\rangle\langle s, m|$。一般混合态需要用算符基底展开。

不可约球张量算符 $T_{kq}^{(s)}$（$k = 0, 1, \ldots, 2s$；$q = -k, \ldots, k$）按 Lakin–Madison 约定满足

$$
\mathrm{Tr}\bigl[T_{kq}^{(s)\dagger}\, T_{k'q'}^{(s)}\bigr] = (2s+1)\,\delta_{kk'}\,\delta_{qq'},
\qquad
T_{00}^{(s)} = I
$$

矩阵元由 Wigner-Eckart 给出

$$
\langle s, m' | T_{kq}^{(s)} | s, m\rangle = \sqrt{2k+1}\, \langle s\,m,\, k\,q | s\,m'\rangle
$$

任何自旋 $s$ 的密度矩阵展开为

$$
\rho = \frac{1}{2s+1} \sum_{k=0}^{2s} \sum_{q=-k}^{k} t_{kq}^*\, T_{kq}^{(s)},
\qquad
t_{kq} = \mathrm{Tr}\bigl[T_{kq}^{(s)}\, \rho\bigr] \tag{rho-T}
$$

$t_{kq}$ 是不可约张量极化分量（rank $k$，分量 $q$），实验里直接对应可观测极化。$t_{00} = 1$ 由 $\mathrm{Tr}\,\rho = 1$ 给定。

### 自旋 1/2

只有 $k = 0, 1$。$T^{(1/2)}_{1q}$ 与 Pauli 矩阵 $\boldsymbol{\sigma}$ 的球张量分量

$$
\sigma_{\pm 1} = \mp \frac{1}{\sqrt 2}(\sigma_x \pm i\sigma_y),\quad \sigma_0 = \sigma_z
$$

成比例：$T^{(1/2)}_{1q} = \sqrt{3/2}\, \sigma_q$。代入 $\text{(rho-T)}$ 得到熟悉的形式

$$
\rho = \frac{1}{2}(I + \mathbf{P} \cdot \boldsymbol{\sigma}),
\qquad
\mathbf{P} = \mathrm{Tr}(\rho\, \boldsymbol{\sigma}) \tag{rho-half}
$$

$|\mathbf{P}| \le 1$，$|\mathbf{P}| = 1$ 即纯态。

### 自旋 1（deuteron）

$k = 0, 1, 2$。引入自旋 1 算符 $\mathbf{S}$（$3\times 3$ 矩阵；$\mathbf{S}^2 = 2$，注意不是 Pauli），$T^{(1)}_{1q} \propto S_q$（球张量分量），$T^{(1)}_{2q} \propto [\mathbf{S}\otimes\mathbf{S}]_{2q}$（对称无迹组合）。在球张量约定下 $\text{(rho-T)}$ 给出

$$
\rho = \frac{1}{3}\Bigl[I + \frac{3}{2}\sum_{q} (-1)^q\, p_{1,-q}\, S_q + \sum_{q} (-1)^q\, p_{2,-q}\, T^{(1)}_{2q}\Bigr] \tag{rho-1}
$$

其中

$$
p_{kq} = t_{kq} = \mathrm{Tr}\bigl[T^{(1)}_{kq}\, \rho\bigr]
$$

是不可约极化分量。约束 $|p_{1q}| \le \sqrt{2}$，$|p_{2q}| \le$（特定数；纯态边界从 $\rho \succeq 0$ 解出）。

### 自旋 1 的 Cartesian 形式

并行常用的 Cartesian 参数化为

$$
\rho = \frac{1}{3}\bigl[I + \tfrac{3}{2}\, \mathbf{P} \cdot \mathbf{S} + \tfrac{1}{3}\sum_{ij} P_{ij}\, (S_i S_j + S_j S_i - \tfrac{4}{3}\delta_{ij} I)\bigr] \tag{rho-1-C}
$$

$\mathbf{P} = \langle \mathbf{S}\rangle = \mathrm{Tr}(\rho\, \mathbf{S})$ 是 Cartesian 矢量极化（与 spin-1/2 的 $\mathbf{P}$ 同记号但物理量不同：spin-1 取值 $|\mathbf{P}| \le 1$）。$P_{ij}$ 是对称无迹张量

$$
P_{ij} = \mathrm{Tr}\bigl[\rho\, \tfrac{3}{2}(S_i S_j + S_j S_i - \tfrac{4}{3}\delta_{ij} I)\bigr],
\qquad P_{ij} = P_{ji},\; \sum_i P_{ii} = 0
$$

球张量与 Cartesian 之间的转换（self-derive）：直接对照 $\text{(rho-1)}$ 与 $\text{(rho-1-C)}$ 提取系数。$T^{(1)}_{1q}$ 与 $S_q$ 的球张量分量同步；$T^{(1)}_{2q}$ 与对称组合 $\{S_i S_j\}$ 的球张量分量同步。结果

$$
\begin{aligned}
p_{1,\pm 1} &= \mp\frac{1}{\sqrt 2}(P_x \pm i P_y),\quad p_{1,0} = P_z \\
p_{2,0} &= \frac{1}{\sqrt 6}\bigl(2 P_{zz}\bigr) = \sqrt{\tfrac{2}{3}}\, P_{zz}\quad\text{(用 } P_{zz} = -P_{xx} - P_{yy}\text{)} \\
p_{2,\pm 1} &= \mp\frac{1}{\sqrt 3}(P_{xz} \pm i P_{yz}) \\
p_{2,\pm 2} &= \frac{1}{2\sqrt 3}\bigl[(P_{xx} - P_{yy}) \pm 2i P_{xy}\bigr]
\end{aligned} \tag{cart-sph}
$$

dpol 实验里更习惯报告 $p_y$（矢量极化的 $y$ 分量）和 $p_{xx}, p_{yy}, p_{zz}$（张量极化对角分量）。Madison 约定取量子化轴 $\hat{\mathbf{z}}$ 沿入射方向、$\hat{\mathbf{y}}$ 法向（散射平面外）。

### 反对称约束

$\mathrm{Tr}\,\rho = 1$、$\rho^\dagger = \rho$、$\rho \succeq 0$（$\Leftrightarrow$ 所有特征值 $\ge 0$）三条共同限制了极化参数空间。对自旋 1 是 8 维实参数空间（$3 \times 3$ Hermitian 减去迹归一），分别给 3 个矢量参数 + 5 个张量参数，与不可约分解 $1 \otimes 1 = 0 \oplus 1 \oplus 2$ 维数 $1 + 3 + 5 = 9$ 减去标量的 1 一致。

## 微分截面与极化展开

### 出射密度矩阵

入射密度矩阵 $\rho_\text{in}$ 经过散射后，出射粒子的（未归一）密度矩阵为

$$
\tilde\rho_\text{out}(\hat{\mathbf{k}}') = M(\hat{\mathbf{k}}', \hat{\mathbf{k}})\, \rho_\text{in}\, M^\dagger(\hat{\mathbf{k}}', \hat{\mathbf{k}}) \tag{rho-out}
$$

其迹给出（极化）微分截面

$$
\frac{d\sigma}{d\Omega}(\hat{\mathbf{k}}'; \rho_\text{in}) = \mathrm{Tr}\bigl[M\, \rho_\text{in}\, M^\dagger\bigr] \tag{dsig-pol}
$$

归一的出射密度矩阵 $\rho_\text{out} = \tilde\rho_\text{out}/\mathrm{Tr}\,\tilde\rho_\text{out}$。这条迹公式是所有极化观测量的母公式：把 $\rho_\text{in}$ 的展开 $\text{(rho-T)}$ 代入，把 M 的具体结构代入，再把出射粒子的极化算符 $T_{kq}^{(b,B)}$ 与 $\rho_\text{out}$ 取迹，就得到 analyzing power、polarization transfer、spin correlation 等所有观测量。

### unpolarized 截面

$\rho_\text{in} = I/[(2s_a+1)(2s_A+1)]$ 时，

$$
\frac{d\sigma_0}{d\Omega} = \frac{1}{(2s_a+1)(2s_A+1)}\, \mathrm{Tr}\bigl[M\, M^\dagger\bigr] \tag{dsig0}
$$

这与 `S_matrix_and_cross_section.zh.md:420` 中 spinless 的 $|f|^2$ 公式衔接：当所有自旋为零时 M 退化为标量 $f$，$\mathrm{Tr}$ 退化为乘 1，归一前置因子退化为 1。

### 光学定理（自旋空间版本）

`S_matrix_and_cross_section.zh.md:451` 的光学定理 $\mathrm{Im}\, f(\mathbf{p}\leftarrow\mathbf{p}) = (k/4\pi)\,\sigma_\text{tot}$ 有自旋形式。S 矩阵酉性 $S^\dagger S = \mathbf 1$ 在自旋空间矩阵元上给出

$$
2\,\mathrm{Im}\, M(\hat{\mathbf{k}}, \hat{\mathbf{k}}) = \frac{k}{2\pi} \int d\Omega'\; M^\dagger(\hat{\mathbf{k}}', \hat{\mathbf{k}})\, M(\hat{\mathbf{k}}', \hat{\mathbf{k}}) \quad\text{（弹性）} \tag{opt-spin}
$$

左边是前向 M 矩阵的反 Hermitian 部分（仍是 $(2s_a+1)(2s_A+1) \times (2s_a+1)(2s_A+1)$ 矩阵）。取迹并除以 $(2s_a+1)(2s_A+1)$ 即恢复 unpolarized 总截面与前向振幅迹的关系。两侧未取迹的形式可用于约束极化态依赖的总截面：$\sigma_\text{tot}(\rho_\text{in}) = (4\pi/k)\, \mathrm{Im}\,\mathrm{Tr}[M(\hat{\mathbf{k}},\hat{\mathbf{k}})\,\rho_\text{in}]$。

### Analyzing power 与 polarization transfer 的一般定义

入射极化 $\rho_\text{in}$ 下截面对入射极化的依赖给出 analyzing power。把 $\rho_\text{in}$ 沿 $\text{(rho-T)}$ 展开，

$$
\frac{d\sigma}{d\Omega}(\rho_\text{in}) = \frac{d\sigma_0}{d\Omega}\Bigl[1 + \sum_{k\ge 1, q} t_{kq}^{*(\text{in})}\, \mathcal{A}_{kq}(\theta, \phi)\Bigr] \tag{Akq}
$$

其中

$$
\mathcal{A}_{kq}(\theta, \phi) = \frac{\mathrm{Tr}\bigl[M\, T_{kq}^{(a)} \otimes I_A\, M^\dagger\bigr]}{\mathrm{Tr}[M M^\dagger]}\quad(\text{入射 }a\text{ 的 analyzing power})
$$

类似定义出射粒子的极化 $\langle T_{kq}^{(b)}\rangle_\text{out} = \mathrm{Tr}[\rho_\text{out}\, T_{kq}^{(b)} \otimes I_B]$ 给出出射极化与极化转移。下面三个具体情形把这套抽象公式翻译成可读的标量振幅形式。

## 自旋 1/2 + 自旋 0 的完整形式

最简单非平凡情形：proton（或电子）打 spin-0 靶（如 ${}^{12}\mathrm{C}$、${}^4\mathrm{He}$、$\pi$ 介子）。

### M 矩阵的两振幅展开

旋转协变性 $\text{(R)}$ 与字称守恒（见后文字称段）共同迫使 M 矩阵在 $2 \times 2$ 自旋空间内只能写成

$$
M(\theta, \phi) = a(\theta)\, I + b(\theta)\, \boldsymbol{\sigma} \cdot \hat{\mathbf{n}},
\qquad
\hat{\mathbf{n}} = \frac{\hat{\mathbf{k}} \times \hat{\mathbf{k}}'}{|\hat{\mathbf{k}} \times \hat{\mathbf{k}}'|} \tag{M-half0}
$$

$\hat{\mathbf{n}}$ 是散射平面的法向（取 $\hat{\mathbf{k}} \times \hat{\mathbf{k}}'$，即 Madison 约定的 $\hat{\mathbf{y}}$ 方向当出射在 $xz$ 平面时）。$a, b$ 是 $\theta$ 的复函数（不依赖 $\phi$；$\phi$ 依赖全部由 $\hat{\mathbf{n}}$ 携带）。

### 与分波相移的关系

入射粒子自旋耦合 $\mathbf{j} = \mathbf{l} + \mathbf{s}$，对每个 $l \ge 0$ 有 $j = l \pm 1/2$ 两支，对应分波相移 $\delta_l^\pm$。standard derivation：

$$
a(\theta) = \frac{1}{2ik}\sum_{l=0}^{\infty} \bigl[(l+1)(e^{2i\delta_l^+} - 1) + l(e^{2i\delta_l^-} - 1)\bigr]\, P_l(\cos\theta) \tag{a-pw}
$$

$$
b(\theta) = \frac{1}{2ik}\sum_{l=1}^{\infty} \bigl[e^{2i\delta_l^+} - e^{2i\delta_l^-}\bigr]\, P_l^1(\cos\theta) \tag{b-pw}
$$

$P_l^1$ 是连带 Legendre 函数（$m=1$）。注意 $b(\theta)$ 之所以与 $\hat{\mathbf{n}}$ 而非 $\hat{\mathbf{l}} = \hat{\mathbf{k}} + \hat{\mathbf{k}}'$、$\hat{\mathbf{m}} = \hat{\mathbf{k}}' - \hat{\mathbf{k}}$（粗略）耦合，是字称守恒的直接结果（见 §字称）。

### 截面与极化

把 $\text{(M-half0)}$ 代入 $\text{(rho-out)}$ 与 $\text{(dsig-pol)}$，利用 $\boldsymbol{\sigma}$ 的代数 $\sigma_i \sigma_j = \delta_{ij} I + i \epsilon_{ijk}\sigma_k$：

unpolarized 截面

$$
\frac{d\sigma_0}{d\Omega} = \frac{1}{2}\,\mathrm{Tr}\bigl[(a + b\,\boldsymbol{\sigma}\!\cdot\!\hat{\mathbf{n}})(a^* + b^*\boldsymbol{\sigma}\!\cdot\!\hat{\mathbf{n}})\bigr] = |a|^2 + |b|^2 \tag{sig0-half0}
$$

入射极化 $\rho_\text{in} = \frac{1}{2}(I + \mathbf{P}_\text{in}\cdot\boldsymbol{\sigma})$，

$$
\mathrm{Tr}\bigl[M\,\rho_\text{in}\,M^\dagger\bigr] = (|a|^2 + |b|^2) + \mathbf{P}_\text{in}\cdot \bigl[\,\cdots\,\bigr]
$$

逐项算（self-derive 关键步骤）：

$$
M\,\rho_\text{in}\,M^\dagger = \tfrac{1}{2}(a + b\sigma_n)(I + \mathbf{P}_\text{in}\!\cdot\!\boldsymbol{\sigma})(a^* + b^*\sigma_n)
$$

记 $\sigma_n \equiv \boldsymbol{\sigma}\cdot\hat{\mathbf{n}}$。展开后用 $\sigma_n \boldsymbol{\sigma}\cdot\mathbf{P}\,\sigma_n = 2(\hat{\mathbf{n}}\cdot\mathbf{P})\sigma_n - \boldsymbol{\sigma}\cdot\mathbf{P}$ 与 $\sigma_n \boldsymbol{\sigma}\cdot\mathbf{P} + \boldsymbol{\sigma}\cdot\mathbf{P}\,\sigma_n = 2(\hat{\mathbf{n}}\cdot\mathbf{P}) I$。取迹：

$$
\mathrm{Tr}\bigl[M\,\rho_\text{in}\,M^\dagger\bigr] = (|a|^2 + |b|^2) + 2\,\mathrm{Re}(a^* b)\,\hat{\mathbf{n}}\!\cdot\!\mathbf{P}_\text{in} \tag{tr-half0}
$$

故

$$
\frac{d\sigma}{d\Omega} = \frac{d\sigma_0}{d\Omega}\bigl[1 + \mathbf{P}_\text{in}\!\cdot\!\mathbf{A}(\theta)\bigr],
\qquad
\mathbf{A}(\theta) = A_y(\theta)\,\hat{\mathbf{n}}
$$

$$
A_y(\theta) = \frac{2\,\mathrm{Re}(a^* b)}{|a|^2 + |b|^2} \tag{Ay}
$$

### 关于 $A_y$ 的实部/虚部、正负号约定

self-derive 校验：把 $a = |a|e^{i\alpha}$、$b = |b|e^{i\beta}$ 代入，$2\,\mathrm{Re}(a^* b) = 2|a||b|\cos(\beta - \alpha)$。等价地 $2\,\mathrm{Re}(a^* b) = -2\,\mathrm{Im}(i\, a^* b)$，常见教材（如 Goldberger–Watson）也写成 $-2\,\mathrm{Im}(a b^*)$，因为 $\mathrm{Im}(a b^*) = -\mathrm{Im}(a^* b)$、且 $\mathrm{Re}(a^* b) = \mathrm{Re}(a b^*)$。要出现 $\mathrm{Im}$ 而非 $\mathrm{Re}$，必须把 $\hat{\mathbf{n}}$ 替换为 $i\hat{\mathbf{n}}$ 或在 $b$ 的相位约定上做相应调整。Madison 约定下 $\text{(Ay)}$ 的标准形式就是 $2\,\mathrm{Re}(a^* b)/(|a|^2+|b|^2)$，正号；$\hat{\mathbf{n}}$ 取 $\hat{\mathbf{k}}\times\hat{\mathbf{k}}'$（不归一化前），归一化后给出沿 $+\hat{\mathbf{y}}$（当出射在 $\phi = 0$）。

注：部分文献（如 Roman 的 Advanced QM）写 $A_y = -2\mathrm{Im}(ab^*)/(|a|^2+|b|^2)$。这与 $\text{(Ay)}$ 一致：$-\mathrm{Im}(a b^*) = +\mathrm{Im}(a^* b)$，但与 $\mathrm{Re}(a^* b)$ 通常不等——除非 $b$ 的相位约定隐含 $b \to ib$。$\text{(b-pw)}$ 中 $1/(2ik)$ 携带的 $i$ 把 $b$ 的整体相位转了 $-\pi/2$，于是 $\mathrm{Re}(a^* b) \to \mathrm{Im}(a^* b)$。是否有这个 $i$，取决于 M 与 $f$ 的归一约定。本篇统一沿用 $\text{(M)}$ 即 $M = f$（不把 $1/(2ik)$ 提出来），$\text{(Ay)}$ 含 $\mathrm{Re}$。

### 出射极化与极化转移

出射粒子极化矢量（弹性，自旋 $s_b = 1/2$ 同 $s_a$）：

$$
\mathbf{P}_\text{out} = \frac{\mathrm{Tr}[\rho_\text{out}\,\boldsymbol{\sigma}]}{\mathrm{Tr}\,\rho_\text{out}} = \frac{\mathrm{Tr}[M\,\rho_\text{in}\,M^\dagger\,\boldsymbol{\sigma}]}{\mathrm{Tr}[M\,\rho_\text{in}\,M^\dagger]}
$$

self-derive 得到分量：

$$
\frac{d\sigma_0}{d\Omega}\, \mathbf{P}_\text{out} = \mathrm{Re}(2 a^* b)\,\hat{\mathbf{n}}\,\bigl[1\bigr] + (|a|^2 - |b|^2)\,\mathbf{P}_\text{in}^\parallel + 2|b|^2\,(\hat{\mathbf{n}}\cdot\mathbf{P}_\text{in})\,\hat{\mathbf{n}} - 2\,\mathrm{Im}(a^* b)\,\hat{\mathbf{n}}\times\mathbf{P}_\text{in}
$$

写成系数矩阵 $D_{ij}$：$P_\text{out}^i = (\sigma_0)^{-1}[A^i + \sum_j D^{ij} P_\text{in}^j]\,\sigma_0/(\sigma_0[1+\mathbf{A}\cdot\mathbf{P}_\text{in}])$。极化转移系数 $D^{ij}$ 在 unpolarized 入射时给出诱导极化 $A_y\hat{\mathbf{n}}$、在极化入射时附加自旋翻转/不翻转的分支。

## 自旋 1/2 + 自旋 1/2 的 Wolfenstein 参数化

NN 散射、电子-电子散射等情形。M 矩阵在 $4\times 4$ 自旋空间。

### 散射平面正交基

定义三个单位矢量

$$
\hat{\mathbf{n}} = \frac{\hat{\mathbf{k}}\times\hat{\mathbf{k}}'}{|\hat{\mathbf{k}}\times\hat{\mathbf{k}}'|},\qquad
\hat{\mathbf{l}} = \frac{\hat{\mathbf{k}}+\hat{\mathbf{k}}'}{|\hat{\mathbf{k}}+\hat{\mathbf{k}}'|},\qquad
\hat{\mathbf{m}} = \frac{\hat{\mathbf{k}}'-\hat{\mathbf{k}}}{|\hat{\mathbf{k}}'-\hat{\mathbf{k}}|} \tag{nlm}
$$

$\{\hat{\mathbf{n}}, \hat{\mathbf{l}}, \hat{\mathbf{m}}\}$ 互相正交且 $\hat{\mathbf{n}} \times \hat{\mathbf{l}} = \hat{\mathbf{m}}$（约定下）。$\hat{\mathbf{n}}$ 法向，$\hat{\mathbf{l}}$ 在散射平面内沿"平均传播"方向，$\hat{\mathbf{m}}$ 在散射平面内沿"动量转移"方向。

### Wolfenstein 5 参数形式

字称守恒、时间反演、旋转协变共同约束 M 只能含有限几种自旋张量。对全同粒子情形（NN）还需对称化。一般标准形式（Wolfenstein 1956）：

$$
\begin{aligned}
M(\theta) = \frac{1}{2}\Bigl[
& (a+b)\, I_1 \otimes I_2 \\
& + (a-b)\,(\boldsymbol{\sigma}_1\!\cdot\!\hat{\mathbf{n}})(\boldsymbol{\sigma}_2\!\cdot\!\hat{\mathbf{n}}) \\
& + (c+d)\,(\boldsymbol{\sigma}_1\!\cdot\!\hat{\mathbf{m}})(\boldsymbol{\sigma}_2\!\cdot\!\hat{\mathbf{m}}) \\
& + (c-d)\,(\boldsymbol{\sigma}_1\!\cdot\!\hat{\mathbf{l}})(\boldsymbol{\sigma}_2\!\cdot\!\hat{\mathbf{l}}) \\
& + e\,(\boldsymbol{\sigma}_1+\boldsymbol{\sigma}_2)\!\cdot\!\hat{\mathbf{n}}
\Bigr]
\end{aligned} \tag{Wolf}
$$

5 个独立的复振幅 $a, b, c, d, e$（都依赖 $\theta$ 与能量）。$a, b$ 是不翻转通道，$c, d$ 是双翻转，$e$ 是单翻转（仅沿 $\hat{\mathbf{n}}$）。

不同文献的命名差别：
- Wolfenstein 原文：$a, b, c, d, e$（如上）。
- Saclay 形式：$\{a, b, c, d, e\} \to \{a, b, c, d, e\}$，但定义中包含一个"半偏对易"项；具体替换 $b \leftrightarrow b'$ 等需逐项对照。
- Bystricky–Lehar–Winternitz 1978：用 $a, b, c, d, e$ 但与对易项 $f$ 同时给出（共 5 个独立参数，第 6 个由对称性约束）。

self-derive 转换矩阵（Wolfenstein 到 Saclay）：在两套基底间做线性变换。一组等价的 Wolfenstein 振幅与 Saclay $(N, M, K, P, Q)$ 振幅之间的关系（仅给一例，约定差异常见）：

$$
\begin{pmatrix} N \\ M \\ K \\ P \\ Q \end{pmatrix}
= \begin{pmatrix}
\tfrac12 & \tfrac12 & 0 & 0 & 0 \\
\tfrac12 & -\tfrac12 & 0 & 0 & 0 \\
0 & 0 & \tfrac12 & \tfrac12 & 0 \\
0 & 0 & \tfrac12 & -\tfrac12 & 0 \\
0 & 0 & 0 & 0 & 1
\end{pmatrix}
\begin{pmatrix} a \\ b \\ c \\ d \\ e \end{pmatrix}
$$

（这条转换矩阵的具体行只在固定一对约定后成立；本笔记只给结构，使用时务必对照原始文献符号表。）

### 同位旋分解

NN 散射中两个核子是全同费米子，必须反对称化。同位旋 $T = 0$（自旋三重态、$L$ 偶；自旋单态、$L$ 奇）与 $T = 1$（自旋单态、$L$ 偶；自旋三重态、$L$ 奇）由 Pauli 原理选定可允许的 $(L, S)$。Wolfenstein 振幅 $\{a, b, c, d, e\}$ 在 $T = 0, 1$ 通道分别有独立值，物理过程（pp、nn、np）通过 $T$ 投影组合。

### 与 NN 观测量的关系

主要 NN 观测量：

- $d\sigma_0/d\Omega = \tfrac{1}{4}\mathrm{Tr}[M M^\dagger]$
- analyzing power $A_y$（与 spin-1/2 + 0 同形，由 $e$ 与 $a, b$ 干涉项主导）
- depolarization $D$、polarization rotation $R, A, R', A'$、spin correlation $A_{ij}$、spin transfer $K_{ij}$

完整观测量与 $\{a, b, c, d, e\}$ 的关系矩阵在 PWA（partial wave analysis）程序里使用；最简形式一例

$$
\sigma_0\, A_y = \mathrm{Re}\bigl[(a+b)^* e\bigr]
$$

$$
\sigma_0\, (1 - D_{nn}) = 2\,|e|^2 + \tfrac{1}{2}|c-d|^2 + \tfrac{1}{2}|c+d|^2 - \cdots
$$

（具体每一条等式视约定差出整体因子；在做 PWA 拟合时，必须固定一套约定到底。）

### 与 ${}^3S_1$-${}^3D_1$ 张量耦合的衔接

`partial_wave_projection.zh.md:399` 提到核力张量力使 ${}^3S_1$-${}^3D_1$ 耦合。这一耦合在 Wolfenstein 形式中通过 $c, d$ 的复杂插值进入：偶 $L$、$S = 1$ 的振幅含 $S - D$ 混合相位 $\bar\delta_0, \bar\delta_2, \epsilon_1$（Stapp 等价相移参数），分波 S 矩阵为

$$
S^{J=1} = \begin{pmatrix} \cos 2\epsilon_1\, e^{2i\bar\delta_0} & i\sin 2\epsilon_1\, e^{i(\bar\delta_0+\bar\delta_2)} \\ i\sin 2\epsilon_1\, e^{i(\bar\delta_0+\bar\delta_2)} & \cos 2\epsilon_1\, e^{2i\bar\delta_2} \end{pmatrix}
$$

对应 Wolfenstein 振幅就是把这条分波 S 矩阵与 $J = 0, 2, \ldots$、$S = 0$ 等其它通道结合后再求和。

## 自旋 1 + 自旋 0：deuteron 入射散射

dpol 直接相关：氘核（spin-1）打 spin-0 靶（如 ${}^4\mathrm{He}$、${}^{12}\mathrm{C}$）。通过测量出射极化，反推入射 deuteron 极化（polarimeter）；或反过来用已知极化的 deuteron 探测 analyzing power。

### M 矩阵的张量展开

旋转协变 + 字称守恒约束 M 在 $3 \times 3$ 自旋空间内只能用 $\hat{\mathbf{n}}, \hat{\mathbf{l}}, \hat{\mathbf{m}}$ 与不可约张量 $T^{(1)}_{kq}$ 构造。结果 M 由 4 个独立标量振幅展开（self-derive 计数：$3\times 3 = 9$ 个复矩阵元，旋转协变把方位角剥离剩 $\theta$ 依赖、字称约束去掉一半，剩 4 个）：

$$
M(\theta) = U(\theta)\, I + V(\theta)\, \mathbf{S}\!\cdot\!\hat{\mathbf{n}} + W(\theta)\, \bigl[(\mathbf{S}\!\cdot\!\hat{\mathbf{l}})^2 - (\mathbf{S}\!\cdot\!\hat{\mathbf{m}})^2\bigr] + X(\theta)\, \bigl[(\mathbf{S}\!\cdot\!\hat{\mathbf{l}})(\mathbf{S}\!\cdot\!\hat{\mathbf{m}}) + (\mathbf{S}\!\cdot\!\hat{\mathbf{m}})(\mathbf{S}\!\cdot\!\hat{\mathbf{l}})\bigr] \tag{M-1-0}
$$

注意 $(\mathbf{S}\!\cdot\!\hat{\mathbf{n}})^2$ 不是独立项：$\mathbf{S}^2 = 2\,I$、$(\mathbf{S}\cdot\hat{\mathbf{l}})^2 + (\mathbf{S}\cdot\hat{\mathbf{m}})^2 + (\mathbf{S}\cdot\hat{\mathbf{n}})^2 = 2\,I$，故对角张量算符的迹被吸收到 $U$ 中。

### 张量极化与不可约球张量分量

入射 deuteron 密度矩阵按 $\text{(rho-1)}$ 用 $p_{kq}$ 参数化。dpol 实验里通常给出
- 矢量极化：$p_z = \mathrm{Tr}[\rho\, S_z]$，等价的球张量分量 $p_{1,0} = p_z$、$p_{1,\pm 1} = \mp(p_x \pm i p_y)/\sqrt 2$；
- 张量极化：$p_{zz} = \mathrm{Tr}[\rho\,(3 S_z^2 - 2)]$、$p_{xx} - p_{yy} = \mathrm{Tr}[\rho\,(S_x^2 - S_y^2)]$ 等。

约束：$p_{xx} + p_{yy} + p_{zz} = 0$（无迹），$|p_{1q}|^2$、$|p_{2q}|^2$ 由 $\rho \succeq 0$ 限制。

### Madison 截面公式

把 $\text{(M-1-0)}$ 与 $\text{(rho-1)}$ 代入 $\text{(dsig-pol)}$，按 analyzing power $\text{(Akq)}$ 抽出系数。Madison 约定下完整公式（self-derive，关键是把 $\rho$ 沿球张量基展开后逐项配对）：

$$
\sigma(\theta, \phi) = \sigma_0(\theta)\Bigl[1 + \tfrac{3}{2}\, p_z\, A_y(\theta)\cos\phi - \tfrac{3}{2}\, p_x\, A_y(\theta)\sin\phi + \tfrac{1}{2}\, p_{zz}\, A_{zz}(\theta) + \tfrac{2}{3} (p_{xx} - p_{yy})\, A_{xx-yy}(\theta)\cos 2\phi - \tfrac{4}{3}\, p_{xy}\, A_{xx-yy}(\theta)\sin 2\phi + \cdots\Bigr] \tag{sig-d}
$$

或更紧凑地用不可约球张量分量

$$
\sigma(\theta, \phi) = \sigma_0(\theta)\Bigl[1 + 2\sum_{k=1}^{2}\sum_{q=-k}^{k} (-1)^q\, t_{k,-q}^*\, T_{kq}(\theta)\, e^{iq\phi}\Bigr]
$$

其中 $T_{kq}(\theta)$ 是 analyzing power 不可约张量分量，由迹给出

$$
T_{kq}(\theta) = \frac{\mathrm{Tr}[M\, T^{(1)}_{kq}\, M^\dagger]}{\mathrm{Tr}[M M^\dagger]}
$$

字称守恒约束（见 §字称）使得仅以下分量非零：

$$
i T_{11}(\theta) \neq 0,\quad T_{20}(\theta) \neq 0,\quad T_{21}(\theta) \neq 0,\quad T_{22}(\theta) \neq 0
$$

而 $T_{10} = 0$、$\mathrm{Re}\, T_{11} = 0$（即 $T_{11}$ 纯虚——故记号 $iT_{11}$，使其为实数）。

### $iT_{11}$ 与 $T_{20}, T_{21}, T_{22}$ 的实验意义

dpol 实验中常报告这四个 analyzing power：

- $iT_{11}(\theta)$：vector analyzing power（与 spin-1/2 的 $A_y$ 类似的物理意义）
- $T_{20}(\theta)$：tensor analyzing power，$z$ 方向张量极化的系数
- $T_{21}(\theta)$：tensor analyzing power，混合分量
- $T_{22}(\theta)$：tensor analyzing power，散射平面内的 $xx$-$yy$ 不对称

dpol polarimeter 校准就是测量已知反应（如 ${}^4\mathrm{He}(\vec{d}, d){}^4\mathrm{He}$）在某一能量、某一角度下的 $iT_{11}, T_{2q}$ 表，然后据此把"散射不对称"翻译回"入射 deuteron 极化"。

## 时间反演与字称对称性约束

### 字称守恒

强相互作用守恒字称。字称变换 $\mathcal{P}$ 把 $\mathbf{k} \to -\mathbf{k}$、$\mathbf{k}' \to -\mathbf{k}'$、自旋不变。M 的字称协变性

$$
M(-\hat{\mathbf{k}}', -\hat{\mathbf{k}}) = \eta_a \eta_A \eta_b \eta_B\, M(\hat{\mathbf{k}}', \hat{\mathbf{k}}) \tag{P}
$$

$\eta$ 是粒子内禀字称。在 spin-1/2 + 0 情形，$M$ 对 $\mathbf{k}, \mathbf{k}'$ 的依赖只能通过 $\hat{\mathbf{n}} = \hat{\mathbf{k}}\times\hat{\mathbf{k}}'$（赝矢量，$\mathcal{P}$ 下不变！）以及 $\hat{\mathbf{l}}, \hat{\mathbf{m}}$（真矢量，$\mathcal{P}$ 下变号）。$\boldsymbol{\sigma}$ 是赝矢量（自旋 = 角动量），$\mathcal{P}$ 下不变。可允许的标量项

$$
I,\quad \boldsymbol{\sigma}\cdot\hat{\mathbf{n}}\;(\text{真标量}),\quad \boldsymbol{\sigma}\cdot\hat{\mathbf{l}}\;(\text{赝标量}),\quad \boldsymbol{\sigma}\cdot\hat{\mathbf{m}}\;(\text{赝标量})
$$

字称守恒去掉赝标量项，只剩 $I, \boldsymbol{\sigma}\cdot\hat{\mathbf{n}}$，正是 $\text{(M-half0)}$。

直接推论：
- $A_x = A_z = 0$：散射平面内的极化分量不产生左右不对称（因为该分量正比于赝标量 $\boldsymbol{\sigma}\cdot\hat{\mathbf{l}}$ 之类的项，被字称去除）；
- $A_y \neq 0$：法向极化分量产生左右不对称（这就是 Mott polarimeter、polarimeter 测自旋的物理基础）。

### 时间反演

时间反演 $\mathcal{T}$ 是反幺正算符；在散射中表现为入射出射交换 + 自旋指标共轭。M 矩阵的时间反演不变性

$$
M_{m'_b m'_B; m_a m_A}(-\hat{\mathbf{k}}, -\hat{\mathbf{k}}') = \prod_i (-1)^{s_i - m_i + s'_i - m'_i}\, M^*_{-m_a, -m_A; -m'_b, -m'_B}(\hat{\mathbf{k}}', \hat{\mathbf{k}}) \tag{T}
$$

（$(-)^{s-m}$ 来自 $\mathcal{T}|s, m\rangle = (-1)^{s-m}|s, -m\rangle$）。

直接推论：
- detailed balance：$|M_{f i}(\hat{\mathbf{k}}', \hat{\mathbf{k}})|^2 = |M_{i f}(-\hat{\mathbf{k}}, -\hat{\mathbf{k}}')|^2$ 在自旋-平均后给出 forward-reverse 截面相等；
- analyzing power vs polarization 等同性：在弹性散射中（出射粒子 = 入射粒子的同位姿），$\mathcal{T}$ 给出 $A_y(\theta) = P_y^\text{out}(\theta\,|\,\text{unpol in})$——即用极化束流测的 analyzing power 与用未极化束流测出射极化得到同样的结果。

### 自旋 1 张量极化的字称约束

把 $\text{(P)}$ 应用到 $\text{(M-1-0)}$，$\hat{\mathbf{n}}$ 偶、$\hat{\mathbf{l}}, \hat{\mathbf{m}}$ 奇、$\mathbf{S}$ 偶（赝矢量）。允许项 $I$、$\mathbf{S}\!\cdot\!\hat{\mathbf{n}}$、$(\mathbf{S}\!\cdot\!\hat{\mathbf{l}})^2 - (\mathbf{S}\!\cdot\!\hat{\mathbf{m}})^2$（两个奇相乘给偶）、$(\mathbf{S}\!\cdot\!\hat{\mathbf{l}})(\mathbf{S}\!\cdot\!\hat{\mathbf{m}}) + h.c.$（两个奇相乘）都被允许，但 $\mathbf{S}\!\cdot\!\hat{\mathbf{l}}$、$\mathbf{S}\!\cdot\!\hat{\mathbf{m}}$ 单独被禁止。这正解释了为什么 $\text{(M-1-0)}$ 中没有 $V_l$、$V_m$ 项。

字称守恒进一步推出 $T_{kq}(\theta)$ 中只允许 $q$ 为偶或奇按 $k$ 选定的子集，结合时间反演给出 $T_{10} = 0$、$\mathrm{Re}\, T_{11} = 0$ 等约束。

## 与主线笔记的对账

本篇把以下各处暗示展开成完整的极化形式链：

| 主线知识点 | 对账位置 | 本篇位置 |
|:--|:--|:--|
| on-shell $S = 1 - 2\pi i\,\delta(E)\, T$（自由基底矩阵元） | `T_and_U_operators.zh.md:380` | M 矩阵定义 $\text{(M)}$ |
| 散射振幅 $f = -(2\pi)^2 m\, t$ | `S_matrix_and_cross_section.zh.md:307` | M 矩阵定义 $\text{(M)}$ |
| $d\sigma/d\Omega = |f|^2$（spinless） | `S_matrix_and_cross_section.zh.md:420` | unpolarized 截面 $\text{(dsig0)}$ |
| 光学定理 $\mathrm{Im}\,f(\text{前向}) = (k/4\pi)\sigma_\text{tot}$ | `S_matrix_and_cross_section.zh.md:451` | 自旋空间版本 $\text{(opt-spin)}$ |
| 耦合通道分波 $T^J_{l'l}$（带自旋） | `partial_wave_projection.zh.md:396` | M 矩阵分波展开 |
| ${}^3S_1$-${}^3D_1$ 张量耦合 | `partial_wave_projection.zh.md:399` | Wolfenstein 段末尾 |
| Wigner D 函数（旋转协变） | `partial_wave_projection.zh.md:226` | 协变性 $\text{(R)}$ |
| 球谐函数与 CG 系数（耦合基） | `partial_wave_projection.zh.md:124` | 不可约张量基底 $\text{(rho-T)}$ |

每条都可用 `grep -n` 在源文件中校验。

## next-step

具体后续方向（按优先级排序）：

- 数值实例：`examples/10_polarization_demo.zh.md`，用 spin-1/2 + 0 标度模型（如 Yukawa 加自旋-轨道项）数值算 $a(\theta), b(\theta)$，画出 $A_y(\theta)$ 曲线；展示 spin-1 + 0 用张量势数值计算 $iT_{11}, T_{2q}$。
- dpol polarimeter 校准：${}^4\mathrm{He}(\vec d, d){}^4\mathrm{He}$ 弹性散射的 $iT_{11}, T_{20}, T_{21}, T_{22}$ 表（Madison 1986、IUCF 测量值），与本篇 $\text{(M-1-0)}$ 拟合，提取 $\{U, V, W, X\}$ 振幅。
- ${}^3S_1$-${}^3D_1$ 耦合通道下 Wolfenstein 振幅 $\{a, b, c, d, e\}$ 的具体计算：从 Stapp 相移 $\bar\delta_0, \bar\delta_2, \epsilon_1$ 出发，组合分波 S 矩阵到 M 矩阵，与 Nijmegen / SAID PWA 输出对照。
- 全同粒子反对称化下的 Wolfenstein 形式：pp 散射、对称化 $M(\theta) \to (M(\theta) - M(\pi - \theta))/\sqrt 2$ 类型操作，具体推导每一项振幅在 $\theta \to \pi - \theta$ 下的变换；以及 nn、np 在同位旋投影下的差别。
- 三体推广：$d + p$ 弹性与破坏散射中的 deuteron 极化、Dalitz–Watson 等张量极化观测量；如何把 `partial_wave_projection.zh.md:539` 的 AGS 分波方程结果接到本篇 $\text{(M-1-0)}$ 类的 M 矩阵参数化。
- 含 Coulomb 长程势的修正：Coulomb 相位修正下 M 矩阵的振幅分解（与 `S_matrix_and_cross_section.zh.md:540` 提到的长程势备注衔接），尤其在 dpol on charged target 时不可忽略。
