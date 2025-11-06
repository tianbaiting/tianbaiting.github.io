# 散射理论

## 1. 数学基础 — 希尔伯特空间 (Hilbert Space)
在量子力学中，物理系统的态由希尔伯特空间 $\mathcal{H}$ 中的态矢量描述。希尔伯特空间是带内积 $\langle\cdot|\cdot\rangle$ 的完备矢量空间。

- 内积 (Inner product)：概率幅 $\langle\phi|\psi\rangle$，概率为 $|\langle\phi|\psi\rangle|^2$。
- 完备性 (Completeness)：所有柯西序列收敛于空间内点，保证极限运算良定。
- 可分离 (Separable)：存在可数稠密子集或可数正交归一基。

常见例子：
- 有限维：$\mathbb{C}^n$，如自旋-1/2 系统 $\mathcal{H}=\mathbb{C}^2$：
    $$|\psi\rangle=\alpha|\uparrow\rangle+\beta|\downarrow\rangle=\begin{pmatrix}\alpha\\\beta\end{pmatrix},\quad |\alpha|^2+|\beta|^2=1.$$
    内积 $\langle\phi|\psi\rangle=\phi_1^*\psi_1+\phi_2^*\psi_2$。
- 可数基（例如 $\ell^2$）：平方可和复数序列 $a=(a_1,a_2,\dots)$ 满足 $\sum|a_n|^2<\infty$。例：一维谐振子，基态 $|n\rangle$。
- $L^2(\mathbb{R}^3)$：平方可积波函数 $\psi(\mathbf{x})$，内积
    $$\langle\phi|\psi\rangle=\int_{\mathbb{R}^3}\phi^*(\mathbf{x})\psi(\mathbf{x})\,d^3x.$$
    注意平面波 $e^{i\mathbf{k}\cdot\mathbf{x}}$ 为广义本征矢，需用配备希尔伯特空间（rigged Hilbert space）处理。

## 2. 态的极限与 Møller 算符
在散射理论中“入/出”态通过 $t\to\mp\infty$ 的极限定义。

- 强极限 (strong limit)：$s\text{-}\lim_{n\to\infty}|\psi_n\rangle=|\psi\rangle$ 当且仅当
    $$\lim_{n\to\infty}\||\psi_n\rangle-|\psi\rangle\|=0.$$
- 弱极限 (weak limit)：$w\text{-}\lim_{n\to\infty}|\psi_n\rangle=|\psi\rangle$ 当且仅当对任意固定 $|\phi\rangle\in\mathcal{H}$，
    $$\lim_{n\to\infty}\langle\phi|\psi_n\rangle=\langle\phi|\psi\rangle.$$
强收敛蕴含弱收敛，反之不然。

Møller 算符（要求为强极限）将自由演化态映射到相互作用态：
$$\Omega_\pm=\lim_{t\to\mp\infty} e^{iHt/\hbar}e^{-iH_0 t/\hbar}.$$
入态/出态定义为 $|\psi^{(\pm)}\rangle=\Omega_\pm|\phi\rangle$。

## 3. S、R、T 矩阵
- S 算符（散射算符）：将入态映射到出态
    $$|\psi_{out}\rangle=S|\psi_{in}\rangle,\qquad S=\Omega_-^\dagger\Omega_+.$$
    矩阵元 $S_{fi}=\langle\phi_f|S|\phi_i\rangle$。
- R 算符（Reaction）：去掉未散射的单位部分
    $$S=\mathbf{1}+R.$$
- T 算符（跃迁算符）：通过能量 $\delta$ 把 $R$ 的能量守恒部分分离出来
    $$R_{fi}=-2\pi i\,\delta(E_f-E_i)\,T_{fi},$$
    即
    $$S_{fi}=\delta_{fi}-2\pi i\,\delta(E_f-E_i)\,T_{fi}.$$
    在壳 (on-shell) 的 $T_{fi}$ 可由相互作用势 $V$ 與入态求得：
    $$T_{fi}=\langle\phi_f|V|\psi_i^{(+)}\rangle.$$

## 4. Resolvent（G 算符）与 Lippmann–Schwinger 方程
- 预解算符（Resolvent）：
    $$G(z)=(z-H)^{-1},\qquad G_0(z)=(z-H_0)^{-1},\quad z\in\mathbb{C}.$$
- Dyson 恒等式：
    $$G=G_0+G_0 V G = G_0 + G V G_0.$$
- Lippmann–Schwinger 方程（散射态）：
    $$|\psi^{(\pm)}\rangle=|\phi\rangle+G_0(E\pm i0) V |\psi^{(\pm)}\rangle,$$
    其中 $H_0|\phi\rangle=E|\phi\rangle$，$i0$（$i\epsilon,\ \epsilon\to0^+$）指定边值并保证正确渐进行为。
- T 算符的表示与方程：
    $$T(z)=V+V G(z) V = V + V G_0(z) T(z).$$
    取 $z=E_i+i0$ 得 $T_{fi}=\langle\phi_f|T(E_i+i0)|\phi_i\rangle$。

## 5. 分波 (Partial Waves) — 选取basis
对中心势 $V(\mathbf r)=V(r)$，系统旋转不变，$[H,L^2]=[H,L_z]=0$，可取共同本征态 $|E,l,m\rangle$ 或 $|k,l,m\rangle$。

- 平面波的分波展开：
    $$e^{i\mathbf{k}\cdot\mathbf{r}}=\sum_{l=0}^\infty\sum_{m=-l}^l 4\pi i^l j_l(kr) Y_{lm}^*(\hat{\mathbf k}) Y_{lm}(\hat{\mathbf r}).$$
    若 $\hat{\mathbf k}=\hat{\mathbf z}$：
    $$e^{ikz}=\sum_{l=0}^\infty(2l+1)i^l j_l(kr)P_l(\cos\theta).$$
- 相移 (phase shift)：每一分波在远场产生相移 $\delta_l(k)$：
    - 自由径向波：$R_l(r)\sim\sin(kr-l\pi/2)$
    - 散射后：$R_l(r)\sim\sin(kr-l\pi/2+\delta_l)$
- 散射振幅与分波展开：
    $$f(\theta)=\sum_{l=0}^\infty (2l+1) f_l(k) P_l(\cos\theta),$$
    其中
    $$f_l(k)=\frac{e^{i\delta_l}\sin\delta_l}{k}=\frac{1}{k\cot\delta_l-ik}.$$
分波法将三维问题化为若干径向一维问题（求 $\delta_l$），低能下常只需少数几个分波。

## 6. 角动量叠加 & Hilbert 空间叠加


当粒子具有内部自由度（如自旋）或我们考虑多个粒子的系统时，需要用到希尔伯特空间的叠加。

Hilbert 空间叠加 (Tensor Product):
如果一个系统由两个子系统 1 和 2 组成（例如，一个粒子的轨道运动 $\mathcal{H}_{orb}$ 和它的自旋 $\mathcal{H}_{spin}$），那么复合系统的希尔伯特空间是两个子系统希尔伯特空间的张量积 (Tensor Product)：

$$\mathcal{H} = \mathcal{H}_1 \otimes \mathcal{H}_2$$

如果 $\{|i\rangle_1\}$ 是 $\mathcal{H}_1$ 的基，$\{|j\rangle_2\}$ 是 $\mathcal{H}_2$ 的基，那么 $\mathcal{H}$ 的一组基是 $\{|i\rangle_1 \otimes |j\rangle_2\}$，常简记为 $|i, j\rangle$。

例子: 一个自旋 $s$ 的粒子在空间中运动。

$\mathcal{H} = \mathcal{H}_{orbital} \otimes \mathcal{H}_{spin} \cong L^2(\mathbb{R}^3) \otimes \mathbb{C}^{2s+1}$

一个态矢量可以写为 $|\psi\rangle$，其波函数为 $\psi(\mathbf{x}, m_s) = \langle \mathbf{x}, m_s | \psi \rangle$，是一个 $(2s+1)$ 分量的自旋波函数。

角动量叠加 (Angular Momentum Addition):
这是张量积空间中一个极其重要的应用。假设子系统 1 有角动量 $\mathbf{J}_1$，子系统 2 有角动量 $\mathbf{J}_2$。
总角动量算符定义在 $\mathcal{H}$ 上：

$$\mathbf{J} = \mathbf{J}_1 \otimes \mathbf{1} + \mathbf{1} \otimes \mathbf{J}_2 \quad (\text{简记为 } \mathbf{J} = \mathbf{J}_1 + \mathbf{J}_2)$$

基的变换:
在 $\mathcal{H}$ 空间中，我们有两组常用的基：

- 非耦合基 (Uncoupled Basis): $|j_1, m_1; j_2, m_2\rangle$
它们是 $J_1^2, J_{1z}, J_2^2, J_{2z}$ 的共同本征矢。

- 耦合基 (Coupled Basis): $|j_1, j_2; J, M\rangle$
它们是 $J_1^2, J_2^2, J^2, J_z$ 的共同本征矢。（注意 $J^2 = (\mathbf{J}_1+\mathbf{J}_2)^2$）

这两组基通过 Clebsch-Gordan (CG) 系数 $\langle j_1 m_1, j_2 m_2 | J M \rangle$ 进行变换：

$$|j_1, j_2; J, M\rangle = \sum_{m_1, m_2} \langle j_1 m_1, j_2 m_2 | J M \rangle |j_1, m_1; j_2, m_2\rangle$$

在散射理论中的应用:
当相互作用 $V$ 不仅仅是中心势 $V(r)$，而是包含自旋相关的项时（例如 自旋-轨道耦合 $V_{SO} \propto \mathbf{L} \cdot \mathbf{S}$）：

$H$ 不再与 $\mathbf{L}$ 和 $\mathbf{S}$ 单独对易。

$L^2$ 和 $S_z$ 不再是守恒量。

但是，如果 $V$ 仍然是旋转不变的（例如 $\mathbf{L} \cdot \mathbf{S}$ 项），$H$ 仍然与总角动量 $\mathbf{J} = \mathbf{L} + \mathbf{S}$ 对易。

$[H, J^2] = 0, \quad [H, J_z] = 0$

在这种情况下，分波展开的正确 basis 不再是 $|l, m_l\rangle$，而是耦合基 $|l, s; J, M\rangle$。

散射在 $J$ 和 $M$ 表象下是对角的（$J$ 和 $M$ 守恒），但S矩阵元 $\langle l', s; J, M | S | l, s; J, M \rangle$ 可能在 $l$ 上非对角（即 $l$ 不守恒，例如在张量势作用下）。