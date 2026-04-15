# 分波投影与角动量耦合：从抽象算符到数值可解方程

前一篇笔记建立了两体 $T$ 算符和三体 AGS $U_{\beta\alpha}$ 算符的完整算符方程。但算符方程本身无法直接用于数值计算——必须先选取一组量子数表示，将三维矢量方程投影成以径向动量为自变量的一维或二维积分方程。这就是分波投影的全部目的。

本篇的链条是：

- 数学工具（球谐函数、CG 系数、Wigner D 函数）；
- 两体 $T$ 矩阵的分波 Lippmann-Schwinger 方程；
- 三体 Jacobi 坐标系与坐标变换；
- 三体 AGS 方程的分波形式。

全文取 $\hbar = 1$，薛定谔表象。通道标号沿用 $\alpha, \beta, \gamma$；Euler 角用 $(\varphi, \theta, \chi)$ 以避免与通道标号冲突。

## 0. 符号约定与已有结果

两体：

$$
H = H_0 + V, \qquad T(E) = V + V G_0^{(+)}(E)\, T(E)
$$

三体：

$$
H = H_0 + v_1 + v_2 + v_3
$$

通道哈密顿量 $H_\alpha = H_0 + v_\alpha$，其中 $v_1 \equiv v_{23}$，$v_2 \equiv v_{31}$，$v_3 \equiv v_{12}$。嵌入式两体 $T$ 算符：

$$
T_\gamma(E) = v_\gamma + v_\gamma G_0(E)\, T_\gamma(E)
$$

AGS 方程：

$$
U_{\beta\alpha}(E) = \bar\delta_{\beta\alpha}\, G_0^{-1}(E) + \sum_{\gamma} \bar\delta_{\beta\gamma}\, T_\gamma(E)\, G_0(E)\, U_{\gamma\alpha}(E)
$$

以上推导见前文（从波算符到 $T$ 算符，再到三体 AGS 的 $U$ 算符）。本篇只使用这些结论，不重复推导。

## 1. 球谐函数 $Y_{lm}$

### 1.1 定义

采用 Condon-Shortley 相位约定：

$$
Y_{lm}(\theta,\varphi) = (-1)^m \sqrt{\frac{2l+1}{4\pi}\,\frac{(l-m)!}{(l+m)!}}\; P_l^m(\cos\theta)\, e^{im\varphi}
$$

其中 $P_l^m$ 是连带 Legendre 函数，$l = 0,1,2,\ldots$，$m = -l, \ldots, l$。

正交归一：

$$
\int d\Omega\; Y_{lm}^*(\hat{\mathbf{r}})\, Y_{l'm'}(\hat{\mathbf{r}}) = \delta_{ll'}\,\delta_{mm'}
$$

完备性：

$$
\sum_{l=0}^{\infty} \sum_{m=-l}^{l} Y_{lm}^*(\hat{\mathbf{r}}')\, Y_{lm}(\hat{\mathbf{r}}) = \delta(\hat{\mathbf{r}} - \hat{\mathbf{r}}')
$$

### 1.2 基本性质

宇称：

$$
Y_{lm}(-\hat{\mathbf{r}}) = (-1)^l\, Y_{lm}(\hat{\mathbf{r}})
$$

复共轭：

$$
Y_{lm}^*(\hat{\mathbf{r}}) = (-1)^m\, Y_{l,-m}(\hat{\mathbf{r}})
$$

特殊值：

$$
Y_{00} = \frac{1}{\sqrt{4\pi}}, \qquad Y_{l0}(\theta,\varphi) = \sqrt{\frac{2l+1}{4\pi}}\, P_l(\cos\theta)
$$

### 1.3 加法定理

设 $\gamma$ 是 $\hat{\mathbf{r}}$ 与 $\hat{\mathbf{r}}'$ 之间的夹角，则

$$
P_l(\cos\gamma) = \frac{4\pi}{2l+1} \sum_{m=-l}^{l} Y_{lm}^*(\hat{\mathbf{r}}')\, Y_{lm}(\hat{\mathbf{r}}) \tag{AT}
$$

这条恒等式把单个 Legendre 多项式分解成两个方向上的球谐函数乘积之和，是分波投影中最常用的工具。

### 1.4 Rayleigh 平面波展开

将平面波 $e^{i\mathbf{k}\cdot\mathbf{r}}$ 按球谐函数展开：

$$
e^{i\mathbf{k}\cdot\mathbf{r}} = 4\pi \sum_{l=0}^{\infty} \sum_{m=-l}^{l} i^l\, j_l(kr)\, Y_{lm}^*(\hat{\mathbf{k}})\, Y_{lm}(\hat{\mathbf{r}}) \tag{RW}
$$

其中 $j_l$ 是球 Bessel 函数。当 $\hat{\mathbf{k}} = \hat{\mathbf{z}}$ 时，只有 $m=0$ 项存活：

$$
e^{ikr\cos\theta} = \sum_{l=0}^{\infty} (2l+1)\, i^l\, j_l(kr)\, P_l(\cos\theta)
$$

证明思路：$e^{i\mathbf{k}\cdot\mathbf{r}}$ 只依赖 $\hat{\mathbf{k}} \cdot \hat{\mathbf{r}} = \cos\gamma$，所以可以展开为 $\sum_l a_l(kr) P_l(\cos\gamma)$。用加法定理 $\text{(AT)}$ 把 $P_l(\cos\gamma)$ 拆成双方向的 $Y_{lm}$ 乘积。径向系数 $a_l$ 由 $j_l$ 的正交性确定。

## 2. Clebsch-Gordan 系数与 3j、6j 符号

### 2.1 角动量耦合基变换

两个角动量 $\mathbf{J}_1$ 和 $\mathbf{J}_2$ 的联合空间有两组自然基：

- 非耦合基 $|j_1 m_1;\, j_2 m_2\rangle$：$J_1^2$、$J_{1z}$、$J_2^2$、$J_{2z}$ 的共同本征态；
- 耦合基 $|j_1 j_2;\, J M\rangle$：$J_1^2$、$J_2^2$、$\mathbf{J}^2$、$J_z$ 的共同本征态，其中 $\mathbf{J} = \mathbf{J}_1 + \mathbf{J}_2$。

Clebsch-Gordan (CG) 系数是这两组基之间的变换系数：

$$
|j_1 j_2;\, J M\rangle = \sum_{m_1, m_2} \langle j_1 m_1,\, j_2 m_2 | J M\rangle\; |j_1 m_1;\, j_2 m_2\rangle \tag{CG}
$$

选择定则：

- $M = m_1 + m_2$
- $|j_1 - j_2| \le J \le j_1 + j_2$（三角条件 $\Delta(j_1 j_2 J)$）

CG 系数在 Condon-Shortley 约定下取为实数。

### 2.2 正交性与对称性

正交关系（对 $m_1, m_2$ 求和）：

$$
\sum_{m_1, m_2} \langle j_1 m_1,\, j_2 m_2 | J M\rangle\, \langle j_1 m_1,\, j_2 m_2 | J' M'\rangle = \delta_{JJ'}\,\delta_{MM'}
$$

正交关系（对 $J, M$ 求和）：

$$
\sum_{J, M} \langle j_1 m_1,\, j_2 m_2 | J M\rangle\, \langle j_1 m_1',\, j_2 m_2' | J M\rangle = \delta_{m_1 m_1'}\,\delta_{m_2 m_2'}
$$

交换对称性：

$$
\langle j_2 m_2,\, j_1 m_1 | J M\rangle = (-1)^{j_1+j_2-J}\, \langle j_1 m_1,\, j_2 m_2 | J M\rangle
$$

$m$ 全反转：

$$
\langle j_1,\!-m_1;\, j_2,\!-m_2 | J,\!-M\rangle = (-1)^{j_1+j_2-J}\, \langle j_1 m_1,\, j_2 m_2 | J M\rangle
$$

### 2.3 Wigner 3j 符号

3j 符号把 CG 系数重写成对三个角动量完全对称的形式：

$$
\begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix}
= \frac{(-1)^{j_1 - j_2 - m_3}}{\sqrt{2j_3+1}}\; \langle j_1 m_1,\, j_2 m_2 | j_3,\!-m_3\rangle \tag{3j}
$$

选择定则：$m_1 + m_2 + m_3 = 0$，以及 $\Delta(j_1 j_2 j_3)$。

3j 符号的优势在于对称性更高：

- 偶置换列不变：$\begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix} = \begin{pmatrix} j_2 & j_3 & j_1 \\ m_2 & m_3 & m_1 \end{pmatrix} = \begin{pmatrix} j_3 & j_1 & j_2 \\ m_3 & m_1 & m_2 \end{pmatrix}$
- 奇置换乘相位 $(-1)^{j_1+j_2+j_3}$
- $m$ 全反转乘相位 $(-1)^{j_1+j_2+j_3}$

在多体计算中，3j 符号的高对称性使公式更紧凑。

### 2.4 球谐函数乘积的耦合

两个球谐函数的乘积可以展开为单个球谐函数：

$$
Y_{l_1 m_1}(\hat{\mathbf{r}})\, Y_{l_2 m_2}(\hat{\mathbf{r}}) = \sum_{L,M} \sqrt{\frac{(2l_1+1)(2l_2+1)}{4\pi(2L+1)}}\; \langle l_1 0,\, l_2 0 | L 0\rangle\, \langle l_1 m_1,\, l_2 m_2 | L M\rangle\; Y_{LM}(\hat{\mathbf{r}})
$$

其中 $\langle l_1 0,\, l_2 0 | L 0\rangle$ 要求 $l_1 + l_2 + L$ 为偶数。这条公式在分波展开的乘积项中反复出现。

### 2.5 Racah 系数与 6j 符号

当三个角动量 $\mathbf{J}_1$、$\mathbf{J}_2$、$\mathbf{J}_3$ 耦合成总角动量 $\mathbf{J}$ 时，存在不同的耦合顺序。两种自然顺序为：

- 先耦合 $\mathbf{J}_1 + \mathbf{J}_2 = \mathbf{J}_{12}$，再耦合 $\mathbf{J}_{12} + \mathbf{J}_3 = \mathbf{J}$；
- 先耦合 $\mathbf{J}_2 + \mathbf{J}_3 = \mathbf{J}_{23}$，再耦合 $\mathbf{J}_1 + \mathbf{J}_{23} = \mathbf{J}$。

这两组基之间的重耦合系数（recoupling coefficient）定义了 6j 符号：

$$
\langle (j_1 j_2) j_{12},\, j_3;\, J \,|\, j_1,\, (j_2 j_3) j_{23};\, J \rangle
= (-1)^{j_1+j_2+j_3+J}\, \sqrt{(2j_{12}+1)(2j_{23}+1)}\;
\begin{Bmatrix} j_1 & j_2 & j_{12} \\ j_3 & J & j_{23} \end{Bmatrix} \tag{6j}
$$

6j 符号的对称性：

- 任意两列交换不变
- 上下两行中任意两对同时交换不变

在三体散射中，不同 Jacobi 坐标集之间的角动量重耦合正是由 6j 符号编码——这是它出现在三体分波方程中的根本原因。

三角条件：6j 符号非零要求 $(j_1, j_2, j_{12})$、$(j_1, J, j_{23})$、$(j_2, j_3, j_{23})$、$(j_{12}, j_3, J)$ 四个三元组均满足三角不等式。

## 3. Wigner D 函数（旋转矩阵）

### 3.1 定义

旋转算符 $\hat{R}(\varphi, \theta, \chi)$ 按 $zyz$ Euler 角参数化为

$$
\hat{R}(\varphi, \theta, \chi) = e^{-i\varphi J_z}\, e^{-i\theta J_y}\, e^{-i\chi J_z}
$$

Wigner D 矩阵是旋转算符在角动量本征态上的矩阵元：

$$
D^j_{m'm}(\varphi, \theta, \chi) = \langle j, m' |\, \hat{R}(\varphi, \theta, \chi) \,| j, m \rangle = e^{-im'\varphi}\, d^j_{m'm}(\theta)\, e^{-im\chi} \tag{D}
$$

其中 $d^j_{m'm}(\theta)$ 是 Wigner 小 d 矩阵（reduced rotation matrix），仅含极角 $\theta$ 的依赖。

### 3.2 与球谐函数的关系

球谐函数是 D 函数的特殊情形：

$$
Y_{lm}(\theta, \varphi) = \sqrt{\frac{2l+1}{4\pi}}\; D^{l\,*}_{m\,0}(\varphi, \theta, 0) \tag{DY}
$$

物理含义：$Y_{lm}$ 描述的是把 $\hat{\mathbf{z}}$ 方向（$m' = 0$）旋转到 $(\theta, \varphi)$ 方向时，投影量子数 $m$ 的变换振幅。这一关系将球谐函数和旋转矩阵统一起来：所有涉及球谐函数角度积分的恒等式，都可以从 D 函数的群论性质推出。

### 3.3 基本性质

幺正性：

$$
\sum_{m''} D^j_{m'\!m''}(\mathcal{R})^*\, D^j_{m''\!m}(\mathcal{R}) = \delta_{m'm}
$$

复合：

$$
D^j_{m'm}(\mathcal{R}_1 \mathcal{R}_2) = \sum_{m''} D^j_{m'\!m''}(\mathcal{R}_1)\, D^j_{m''\!m}(\mathcal{R}_2)
$$

复共轭：

$$
D^j_{m'm}(\mathcal{R})^* = (-1)^{m'-m}\, D^j_{-m'\!,-m}(\mathcal{R})
$$

正交积分（对全 Euler 角积分）：

$$
\int d\mathcal{R}\; D^{j_1}_{m_1'\!m_1}(\mathcal{R})^*\, D^{j_2}_{m_2'\!m_2}(\mathcal{R}) = \frac{8\pi^2}{2j_1+1}\; \delta_{j_1 j_2}\,\delta_{m_1' m_2'}\,\delta_{m_1 m_2}
$$

其中 $d\mathcal{R} = \frac{1}{8\pi^2}\sin\theta\, d\varphi\, d\theta\, d\chi$（归一化使得 $\int d\mathcal{R} = 1$）。

### 3.4 D 函数乘积的 CG 分解

两个 D 函数的乘积可以用 CG 系数展开为单个 D 函数：

$$
D^{j_1}_{m_1'\!m_1}(\mathcal{R})\, D^{j_2}_{m_2'\!m_2}(\mathcal{R}) = \sum_J \langle j_1 m_1',\, j_2 m_2' | J,\, m_1'+m_2'\rangle\, \langle j_1 m_1,\, j_2 m_2 | J,\, m_1+m_2\rangle\, D^J_{m_1'+m_2',\, m_1+m_2}(\mathcal{R})
$$

这条公式是 $\text{(DY)}$ 和球谐函数耦合公式在旋转群上的推广。在三体散射中，当从一个 Jacobi 坐标集变换到另一个时，动量方向的旋转用 D 函数描述，而 D 函数乘积的 CG 分解正是角动量重耦合系数的来源。

## 4. 两体 $T$ 矩阵的分波投影

### 4.1 动量表象与分波基

动量本征态 $|\mathbf{k}\rangle$ 满足 $\langle \mathbf{k'}|\mathbf{k}\rangle = \delta^{(3)}(\mathbf{k'} - \mathbf{k})$。定义分波基 $|k, l, m\rangle$：

$$
|\mathbf{k}\rangle = \sum_{l,m} Y_{lm}^*(\hat{\mathbf{k}})\; |k, l, m\rangle
$$

归一化为

$$
\langle k', l', m' | k, l, m\rangle = \frac{\delta(k'-k)}{k^2}\; \delta_{l'l}\,\delta_{m'm}
$$

完备性：

$$
\mathbf{1} = \int d^3k\; |\mathbf{k}\rangle\langle\mathbf{k}| = \sum_{l,m} \int_0^\infty dk\, k^2\; |k, l, m\rangle\langle k, l, m|
$$

坐标表示与球 Bessel 函数的关系：

$$
\langle \mathbf{r} | k, l, m\rangle = \sqrt{\frac{2}{\pi}}\; j_l(kr)\, Y_{lm}(\hat{\mathbf{r}})
$$

这正是 Rayleigh 展开 $\text{(RW)}$ 的分波分解形式。

### 4.2 中心势下的分波展开

若 $V = V(r)$ 为中心势，则 $T(E)$ 与 $\mathbf{L}^2$、$L_z$ 对易。因此

$$
\langle k', l', m' | T(E) | k, l, m\rangle = T_l(k', k; E)\; \delta_{l'l}\,\delta_{m'm}
$$

将 $|\mathbf{k}\rangle$ 的分波展开代入：

$$
\langle \mathbf{k'} | T(E) | \mathbf{k}\rangle = \sum_{l,m} Y_{lm}(\hat{\mathbf{k'}})\, T_l(k', k; E)\, Y_{lm}^*(\hat{\mathbf{k}})
$$

由加法定理 $\text{(AT)}$：

$$
\langle \mathbf{k'} | T(E) | \mathbf{k}\rangle = \sum_{l=0}^{\infty} \frac{2l+1}{4\pi}\, T_l(k', k; E)\, P_l(\cos\theta_{k'k}) \tag{PW-T}
$$

反过来，利用 $P_l$ 的正交性可以提取分波分量：

$$
T_l(k', k; E) = 2\pi \int_{-1}^{1} d(\cos\theta)\; P_l(\cos\theta)\, \langle \mathbf{k'} | T(E) | \mathbf{k}\rangle
$$

### 4.3 分波 Lippmann-Schwinger 方程

从算符方程 $T = V + VG_0^{(+)}T$ 出发，在分波基中取矩阵元并插入完备性：

$$
T_l(k', k; E) = V_l(k', k) + \int_0^\infty dq\, q^2\; \frac{V_l(k', q)\, T_l(q, k; E)}{E - q^2/(2\mu) + i0} \tag{LS-pw}
$$

这里 $\mu$ 是两体约化质量，$V_l(k', k) = \langle k', l, m | V | k, l, m\rangle$ 是势的分波矩阵元。

对局域中心势 $V(r)$，利用坐标表示可以计算：

$$
V_l(k', k) = \frac{2}{\pi} \int_0^\infty dr\, r^2\; j_l(k'r)\, V(r)\, j_l(kr)
$$

关键在于：**原本是三维矢量积分方程，经过分波投影后变成了以 $k$、$k'$ 为自变量的一维积分方程。** 对每个 $l$，方程独立。数值上只需对 $q$ 积分做离散化（如 Gauss 求积），就得到线性代数方程组。

积分核中 $q^2/(2\mu) = E + i0$ 处的奇异点需要特别处理：通常用主值积分加余项的方法，或沿复平面做围道变形。

### 4.4 On-shell $T$ 矩阵元、相移与 $S$ 矩阵

在能壳上 $k' = k$，$E = k^2/(2\mu)$。散射振幅的分波展开为

$$
f(\theta) = \sum_{l=0}^{\infty} (2l+1)\, f_l(k)\, P_l(\cos\theta)
$$

其中

$$
f_l(k) = \frac{e^{i\delta_l}\sin\delta_l}{k}
$$

$\delta_l(k)$ 是第 $l$ 分波的相移。on-shell $T$ 矩阵元与相移的关系为

$$
T_l(k, k; E_k) = -\frac{1}{\pi\mu k}\; e^{i\delta_l}\sin\delta_l = -\frac{f_l(k)}{\pi\mu}
$$

分波 $S$ 矩阵为

$$
S_l(k) = 1 - 2\pi i\, \mu k\, T_l(k, k; E_k) = e^{2i\delta_l} \tag{S-pw}
$$

$|S_l| = 1$ 反映了弹性散射中的幺正性（概率守恒）。对非弹性散射，$|S_l| < 1$，可引入非弹性参数 $\eta_l$，写成 $S_l = \eta_l\, e^{2i\delta_l}$。

### 4.5 带自旋的情形

若粒子带自旋 $s$，相互作用含自旋-轨道耦合或张量力，则 $[H, \mathbf{L}^2] \neq 0$，但 $[H, \mathbf{J}^2] = 0$（$\mathbf{J} = \mathbf{L} + \mathbf{S}$，假设旋转不变）。

正确的基是耦合基 $|k;\, (l\, s)\, J\, M\rangle$，其中 $l$ 和 $s$ 先耦合成 $J$。$T$ 矩阵在此基中不再对 $l$ 对角：

$$
\langle k';\, (l'\, s)\, J\, M | T(E) | k;\, (l\, s)\, J\, M\rangle = T^J_{l'l}(k', k; E)
$$

分波 LS 方程变成关于 $l$、$l'$ 的耦合通道积分方程：

$$
T^J_{l'l}(k', k; E) = V^J_{l'l}(k', k) + \sum_{l''} \int_0^\infty dq\, q^2\; \frac{V^J_{l'l''}(k', q)\, T^J_{l''l}(q, k; E)}{E - q^2/(2\mu) + i0}
$$

例如核力中的张量力使 $l$ 和 $l \pm 2$ 分波耦合（${}^3S_1$-${}^3D_1$ 耦合）。每个 $J$ 块仍然是独立的一维积分方程组。

## 5. 三体 Jacobi 坐标系

### 5.1 三个 Jacobi 集的定义

三个粒子质量 $m_1, m_2, m_3$，总质量 $M = m_1 + m_2 + m_3$。质心系中有两组独立的相对动量。对每个粒子标号 $\alpha = 1, 2, 3$，定义 Jacobi 集 $\alpha$：

**Jacobi 集 1**（对 $(23)$，旁观者 1）：

- $\mathbf{p}_1$：粒子 2 和 3 之间的相对动量，约化质量 $\mu_1 = \dfrac{m_2 m_3}{m_2 + m_3}$
- $\mathbf{q}_1$：粒子 1 相对于 $(23)$ 质心的动量，约化质量 $\nu_1 = \dfrac{m_1(m_2 + m_3)}{M}$

**Jacobi 集 2**（对 $(31)$，旁观者 2）和**集 3**（对 $(12)$，旁观者 3）完全类比，循环置换 $1 \to 2 \to 3$。

一般地：$\mu_\alpha$ 是不含粒子 $\alpha$ 的那对粒子的约化质量，$\nu_\alpha$ 是粒子 $\alpha$ 相对该对质心的约化质量。

动能在每个 Jacobi 集中都是对角的：

$$
H_0 = \frac{p_\alpha^2}{2\mu_\alpha} + \frac{q_\alpha^2}{2\nu_\alpha}
$$

对子势 $v_\alpha$ 仅依赖对内相对坐标，因而在 Jacobi 集 $\alpha$ 中只依赖 $\mathbf{p}_\alpha$（或其共轭坐标），与 $\mathbf{q}_\alpha$ 无关。

前一篇笔记中通道参考态 $|\Phi_\alpha(q_\alpha)\rangle = |\phi_\alpha\rangle \otimes |q_\alpha\rangle$ 的含义在这里变得具体：$|\phi_\alpha\rangle$ 是 $v_\alpha$ 支配的对内束缚态（关于动量 $\mathbf{p}_\alpha$），$|q_\alpha\rangle$ 是旁观者的相对运动（关于动量 $\mathbf{q}_\alpha$）。

### 5.2 Jacobi 集之间的坐标变换

从集 $\alpha$ 到集 $\beta$ 的变换是线性的：

$$
\begin{pmatrix} \mathbf{p}_\beta \\ \mathbf{q}_\beta \end{pmatrix}
=
\begin{pmatrix} c_{11} & c_{12} \\ c_{21} & c_{22} \end{pmatrix}
\begin{pmatrix} \mathbf{p}_\alpha \\ \mathbf{q}_\alpha \end{pmatrix}
$$

系数 $c_{ij}$ 由质量比确定。引入质量标度（mass-scaled）动量

$$
\tilde{\mathbf{p}}_\alpha = \frac{\mathbf{p}_\alpha}{\sqrt{\mu_\alpha}}, \qquad \tilde{\mathbf{q}}_\alpha = \frac{\mathbf{q}_\alpha}{\sqrt{\nu_\alpha}}
$$

则动能变为 $H_0 = \frac{1}{2}(\tilde{p}_\alpha^2 + \tilde{q}_\alpha^2)$，且集间变换成为正交旋转：

$$
\begin{pmatrix} \tilde{\mathbf{p}}_\beta \\ \tilde{\mathbf{q}}_\beta \end{pmatrix}
=
\begin{pmatrix} -\cos\phi_{\beta\alpha} & \sin\phi_{\beta\alpha} \\ -\sin\phi_{\beta\alpha} & -\cos\phi_{\beta\alpha} \end{pmatrix}
\begin{pmatrix} \tilde{\mathbf{p}}_\alpha \\ \tilde{\mathbf{q}}_\alpha \end{pmatrix}
\tag{JT}
$$

其中运动学旋转角 $\phi_{\beta\alpha}$ 仅由质量比决定：

$$
\sin\phi_{\beta\alpha} = \frac{m_\gamma}{\sqrt{(m_\alpha + m_\gamma)(m_\beta + m_\gamma)}} \cdot \frac{M}{\sqrt{\mu_\alpha \nu_\alpha \mu_\beta \nu_\beta / (\mu_\alpha \nu_\alpha)}}
$$

（这里 $\gamma$ 是 $\{1,2,3\} \setminus \{\alpha,\beta\}$ 的那个标号。）对等质量情形 $m_1 = m_2 = m_3$，$\phi_{\beta\alpha} = \pi/3$。

正交性保证了三体相空间体积元在变换下不变，即 Jacobian 为 1。

### 5.3 为什么 AGS 方程需要不同的 Jacobi 集

AGS 方程的核 $T_\gamma G_0 U_{\gamma\alpha}$ 中，$T_\gamma$ 作用在对子 $\gamma$ 的空间中——它在 Jacobi 集 $\gamma$ 中是"对角"的（只依赖 $\mathbf{p}_\gamma$）。但 $U_{\gamma\alpha}$ 的输入标签属于集 $\alpha$。因此计算核的矩阵元时，必须在不同 Jacobi 集之间做变换。

这正是三体问题的核心技术难点：不同对子散射各自在自己的 Jacobi 集中最简单，但 AGS 方程把它们耦合在了一起。分波投影的任务就是把这个集间变换也投影到角动量分量上。

## 6. 三体分波分解

### 6.1 角动量耦合方案

在 Jacobi 集 $\alpha$ 中，相关的角动量有：

- $l_\alpha$：对内轨道角动量（$\mathbf{p}_\alpha$ 方向的分波）
- $\lambda_\alpha$：旁观者轨道角动量（$\mathbf{q}_\alpha$ 方向的分波）
- 若粒子带自旋：$s_\alpha$（对内自旋耦合）、$\sigma_\alpha$（旁观者自旋）

典型的耦合方案（$LS$ 耦合）：

$$
\mathbf{l}_\alpha + \mathbf{s}_\alpha = \mathbf{j}_\alpha \qquad (\text{对子总角动量})
$$

$$
\mathbf{j}_\alpha + \boldsymbol{\lambda}_\alpha = \mathbf{J} \qquad (\text{三体总角动量})
$$

（若旁观者有自旋，可进一步先耦合 $\mathbf{j}_\alpha + \boldsymbol{\sigma}_\alpha = \mathbf{I}_\alpha$，再 $\mathbf{I}_\alpha + \boldsymbol{\lambda}_\alpha = \mathbf{J}$。为简化记号，下面只写无自旋或自旋已并入 $j_\alpha$ 的情形。）

记集体离散量子数为

$$
\mathcal{L}_\alpha = \{l_\alpha,\, \lambda_\alpha,\, j_\alpha\}
$$

三体分波基态记为

$$
|p_\alpha,\, q_\alpha;\, \mathcal{L}_\alpha,\, J\, M\rangle
$$

归一化：

$$
\langle p_\alpha',\, q_\alpha';\, \mathcal{L}_\alpha',\, J'\, M' | p_\alpha,\, q_\alpha;\, \mathcal{L}_\alpha,\, J\, M\rangle = \frac{\delta(p_\alpha' - p_\alpha)}{p_\alpha^2}\; \frac{\delta(q_\alpha' - q_\alpha)}{q_\alpha^2}\; \delta_{\mathcal{L}_\alpha' \mathcal{L}_\alpha}\, \delta_{J'J}\, \delta_{M'M}
$$

### 6.2 $T_\gamma$ 在三体空间中的分波表示

$T_\gamma$ 只作用于对子 $\gamma$ 的内部自由度。在集 $\gamma$ 的分波基中：

$$
\langle p_\gamma',\, q_\gamma';\, \mathcal{L}_\gamma',\, JM \,|\, T_\gamma(z_\gamma) \,|\, p_\gamma,\, q_\gamma;\, \mathcal{L}_\gamma,\, JM\rangle
=
\frac{\delta(q_\gamma' - q_\gamma)}{q_\gamma^2}\; \delta_{\lambda_\gamma' \lambda_\gamma}\;
t_{l_\gamma}^{j_\gamma}(p_\gamma', p_\gamma;\, z_\gamma)\;
\delta_{j_\gamma' j_\gamma}
$$

其中

$$
z_\gamma = E - \frac{q_\gamma^2}{2\nu_\gamma}
$$

是对子 $\gamma$ 的可用子能量（sub-energy），$t_{l_\gamma}^{j_\gamma}$ 是已在第 4 节中求解的两体分波 $T$ 矩阵。

物理上：旁观者动量 $q_\gamma$ 守恒，旁观者角动量 $\lambda_\gamma$ 守恒，$T_\gamma$ 只改变对内动量大小 $p_\gamma$。

### 6.3 AGS 方程的分波形式

将 AGS 算符方程投影到分波基，得到（省略 $JM$ 标签，$J$ 守恒，$M$ 不出现在方程中）：

$$
U^{J}_{\mathcal{L}_\beta \mathcal{L}_\alpha}(p_\beta, q_\beta;\, p_\alpha, q_\alpha;\, E)
=
Z^{J}_{\mathcal{L}_\beta \mathcal{L}_\alpha}(p_\beta, q_\beta;\, p_\alpha, q_\alpha;\, E)
$$

$$
+\; \sum_{\gamma}\, \sum_{\mathcal{L}_\gamma} \int_0^\infty dp_\gamma\, p_\gamma^2 \int_0^\infty dq_\gamma\, q_\gamma^2\;
Z^{J}_{\mathcal{L}_\beta \mathcal{L}_\gamma}(p_\beta, q_\beta;\, p_\gamma, q_\gamma;\, E)\;
\tau^J_{\mathcal{L}_\gamma}(p_\gamma, q_\gamma;\, E)\;
U^{J}_{\mathcal{L}_\gamma \mathcal{L}_\alpha}(p_\gamma, q_\gamma;\, p_\alpha, q_\alpha;\, E)
\tag{AGS-pw}
$$

这里：

- $\tau^J_{\mathcal{L}_\gamma}$ 包含两体 $T$ 矩阵和自由传播子的乘积：

$$
\tau^J_{\mathcal{L}_\gamma}(p_\gamma, q_\gamma; E) = t_{l_\gamma}^{j_\gamma}(p_\gamma, p_\gamma'; E - q_\gamma^2/(2\nu_\gamma)) \times G_0(\ldots)
$$

（具体形式取决于方程的积分变量选取。）

- $Z^{J}_{\mathcal{L}_\beta \mathcal{L}_\gamma}$ 是 Born 项（driving term），包含 Jacobi 坐标变换和角动量重耦合，下一小节展开。

注意方程的结构：每个 $J$ 块独立，但 $\mathcal{L}$ 通道之间耦合。自变量是两组径向动量 $(p, q)$，所以这是**二维积分方程**——比两体的一维方程复杂得多，但已经从原始的六维（两个三维矢量）降到了二维。

### 6.4 Jacobi 坐标变换的分波矩阵元

AGS 方程核心的技术难题是计算从集 $\gamma$ 到集 $\beta$ 的变换在分波基中的矩阵元。这一矩阵元分成两步：

**第一步：运动学变换。** 由 $\text{(JT)}$，在质量标度动量空间中，集间变换是二维旋转。对于给定的 $(\tilde{p}_\gamma, \tilde{q}_\gamma)$ 和 $(\tilde{p}_\beta, \tilde{q}_\beta)$，两组矢量之间的关系由旋转角 $\phi_{\beta\gamma}$ 和一个方位角（$\hat{\mathbf{p}}_\gamma$ 与 $\hat{\mathbf{q}}_\gamma$ 之间的夹角 $x = \hat{\mathbf{p}}_\gamma \cdot \hat{\mathbf{q}}_\gamma$）确定。运动学部分归结为对这个角度 $x$ 的一维积分。

**第二步：角动量重耦合。** 从 $\{l_\gamma, \lambda_\gamma, j_\gamma\}$ 变换到 $\{l_\beta, \lambda_\beta, j_\beta\}$ 涉及重耦合系数。具体地，Born 项中的角动量部分为：

$$
\mathcal{G}^{J}_{\mathcal{L}_\beta \mathcal{L}_\gamma}(x) = \sum \text{(依赖于 $x$ 的 Legendre 多项式)} \times \text{(6j 符号)}
$$

更明确地写：

$$
\mathcal{G}^{J}_{\mathcal{L}_\beta \mathcal{L}_\gamma}(x) = \sum_{\Lambda} (2\Lambda+1)\, P_\Lambda(x)\; (-1)^{l_\gamma + \lambda_\beta + J}
\; \hat{j}_\gamma\, \hat{j}_\beta\, \hat{\Lambda}
\begin{Bmatrix} l_\gamma & \lambda_\gamma & J \\ \lambda_\beta & l_\beta & \Lambda \end{Bmatrix}
\langle l_\gamma 0,\, \Lambda 0 | l_\beta 0\rangle \langle \lambda_\gamma 0,\, \Lambda 0 | \lambda_\beta 0\rangle
$$

其中 $\hat{j} = \sqrt{2j+1}$，$x$ 是 $\hat{\mathbf{p}}_\gamma \cdot \hat{\mathbf{q}}_\gamma$ 方向的夹角余弦，$\Lambda$ 是中间角动量。

6j 符号在这里的角色：它编码了从"先耦合 $l_\gamma$ 和 $\lambda_\gamma$"到"先耦合 $l_\beta$ 和 $\lambda_\beta$"的基变换——正是第 2.5 节中角动量重耦合的直接应用。

CG 系数 $\langle l 0, \Lambda 0 | l' 0\rangle$ 要求 $l + \Lambda + l'$ 为偶数，这来源于球谐函数耦合中的宇称守恒。

完整的 Born 项把运动学和角动量部分组合起来：

$$
Z^{J}_{\mathcal{L}_\beta \mathcal{L}_\gamma}(p_\beta, q_\beta;\, p_\gamma, q_\gamma;\, E) = \bar\delta_{\beta\gamma} \int_{-1}^{1} dx\; \mathcal{G}^{J}_{\mathcal{L}_\beta \mathcal{L}_\gamma}(x)\; \frac{\delta(\tilde{p}_\beta - \tilde{p}_\beta(p_\gamma, q_\gamma, x))\, \delta(\tilde{q}_\beta - \tilde{q}_\beta(p_\gamma, q_\gamma, x))}{(\text{Jacobian})} \times G_0^{-1}
$$

实际数值实现中，这些 $\delta$ 函数通过运动学关系被消解——对 $x$ 的积分变成关于 $p_\gamma$、$q_\gamma$ 和一个角度的联合求积。

## 7. 从分波方程到数值实现

### 7.1 为什么分波投影有效

核心原因：旋转不变性。

若哈密顿量与总角动量 $\mathbf{J}$ 对易，则 $J$ 和 $M$ 是好量子数。投影到 $J$ 子空间后：

- 两体：三维矢量方程 → 每个 $l$ 的一维积分方程
- 三体：六维矢量方程 → 每个 $J$ 的二维积分方程（连续自变量 $p, q$），外加离散通道求和（$\mathcal{L}$）

在低能散射中，高分波的贡献因离心位垒而被压低。实际计算中只需截断到 $l_{\max}$、$\lambda_{\max}$ 有限值。

### 7.2 数值方程的结构

**两体：** 对 $\text{(LS-pw)}$，将 $q$ 积分用 $N$ 点 Gauss 求积离散化：

$$
T_l(k_i, k; E) = V_l(k_i, k) + \sum_{j=1}^{N} w_j\, q_j^2\; \frac{V_l(k_i, q_j)\, T_l(q_j, k; E)}{E - q_j^2/(2\mu) + i0}
$$

这是 $N$ 维线性方程组。对于分母中的奇异点（$q_0^2/(2\mu) = E$），常用的处理方法：

- 主值-余项（subtraction）方法：将被积函数减去奇异点处的值再积分，奇异贡献解析处理
- 围道旋转（contour rotation）：将 $q$ 积分路径从实轴旋转到复平面，避开奇异点

**三体：** 对 $\text{(AGS-pw)}$，两个连续变量 $(p, q)$ 各用 $N_p$、$N_q$ 点离散化，得到 $(N_p \times N_q \times N_{\mathcal{L}})$ 维矩阵方程。典型计算中 $N_p, N_q \sim 30\text{-}60$，$N_{\mathcal{L}}$ 取决于截断的分波数目。

### 7.3 完整链条

把从抽象算符到数值计算的全部步骤压缩成一条链：

$$
\underbrace{T = V + VG_0 T}_{\text{算符方程}}
\;\xrightarrow{\text{角动量工具}}\;
\underbrace{T_l(k',k;E)}_{\text{分波投影}}
\;\xrightarrow{\text{Gauss 求积}}\;
\underbrace{(V - T)^{-1} = G_0}_{\text{线性代数}}
$$

三体：

$$
\underbrace{U_{\beta\alpha} = \bar\delta_{\beta\alpha} G_0^{-1} + \sum T_\gamma G_0 U_{\gamma\alpha}}_{\text{AGS 算符方程}}
\;\xrightarrow[\text{6j 重耦合}]{\text{Jacobi 变换}}\;
\underbrace{U^J_{\mathcal{L}_\beta\mathcal{L}_\alpha}(p,q;p',q')}_{\text{分波 AGS}}
\;\xrightarrow{\text{二维离散化}}\;
\underbrace{\text{矩阵方程}}_{\text{线性代数}}
$$

每一步的数学工具都已在前面各节给出：球谐函数提供分波基，CG 系数和 6j 符号处理角动量耦合与重耦合，Wigner D 函数处理坐标旋转，Jacobi 坐标将三体运动学分解为对内和旁观者自由度。
