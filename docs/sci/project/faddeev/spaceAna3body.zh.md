# 量子三体的空间结构和解法

求解量子三体问题时，最容易产生的混乱，不是公式太多，而是**很多名字根本不在同一个层次上**。

我们常常把下面这些词放在一起比较：

* Schrödinger equation；
* Faddeev；
* AGS；
* CDCC；
* hyperspherical harmonics；
* coordinate space / momentum space；
* FEM、B-spline、DVR；
* wave packet；
* Coulomb-Sturmian；
* separable expansion；
* GMRES、Lanczos、Arnoldi。

但这些东西有的在回答“**方程怎么组织**”，有的在回答“**空间怎么表示**”，有的在回答“**究竟截掉了什么**”，还有的只是在回答“**最后那台矩阵怎么解**”。

如果不先分层，很容易得到一种错觉：

> Faddeev、CDCC、B-spline、Coulomb-Sturmian 好像都是几种互相竞争的“三体算法”。

其实不是。

本文的主线只有一句话：先分清你在改写什么，再讨论你在近似什么。

整篇文章都可以放进下面这条链：

$$

\begin{array}{c}
\text{物理 Hilbert 空间}\\[1mm]
\downarrow\\[1mm]
\text{对称性与通道结构}\\[1mm]
\downarrow\\[1mm]
\text{方程架构：Schrödinger / Faddeev / AGS / projected Schrödinger}\\[1mm]
\downarrow\\[1mm]
\text{表示：coordinate / momentum / hyperspherical}\\[1mm]
\downarrow\\[1mm]
\text{有限化：grid / FEM / spline / spectral / wave packet / CS / low rank}\\[1mm]
\downarrow\\[1mm]
\text{散射边界条件}\\[1mm]
\downarrow\\[1mm]
\text{有限维线性代数}
\end{array}
$$

真正理解三体计算，关键不是记方法名，而是每看到一个方法都问四个问题：

1. 它改变的是**方程结构**，还是只改变**表示**？
2. 它是一个**精确重写**，还是一个**近似截断**？
3. 它真正压缩的是**波函数空间**，还是**算符**？
4. 三体散射的**无穷远边界条件**到底放在哪里？

下面我们一层一层地把这条链走完。

---

## 第一章 空间结构：三种完全不同的“分解”

三体理论里到处都在用“分解”这个词，但它至少有三种完全不同的数学含义。把它们分开，后面的讨论才不会混。

### 1.1 去掉质心：六个自由度变成两组相对坐标

三个粒子本来有九个空间自由度。质心运动与内部结构无关，可以分离出去，于是只剩**六个相对自由度**。

描述这六个自由度最常用的方式是 Jacobi 坐标：先任选两个粒子组成一个 pair，用

$$
\mathbf x
$$

描述这个 pair 的内部相对运动，再用

$$
\mathbf y
$$

描述第三个粒子（spectator）相对 pair 质心的运动。

例如对于 $n+p+A$，一种常见选择是

$$
\mathbf x=\mathbf r_n-\mathbf r_p,
$$

$$
\mathbf y=\mathbf r_A-
\frac{m_n\mathbf r_n+m_p\mathbf r_p}{m_n+m_p}.
$$

直观地说：$\mathbf x$ 看“中子和质子离多远”，$\mathbf y$ 看“氘核（np 的质心）离原子核多远”。

### 1.2 第一种分解：Tensor product——自由度的分解

忽略自旋等内部自由度时，相对运动空间可以写为

$$

\mathcal H_{\rm rel}
\simeq
L^2(\mathbb R^3_x)
\otimes
L^2(\mathbb R^3_y).

$$

这里的 $\otimes$（tensor product）表示：

> $\mathbf x$ 和 $\mathbf y$ 是两个**独立**的自由度，完整状态需要**同时**描述它们。

一个态是“一个 $x$ 的函数”乘上“一个 $y$ 的函数”的叠加；测度是 $d^3x\,d^3y$；内积是先对 $x$ 积分再对 $y$ 积分。

如果加入 spin、isospin，结构只是继续 tensor product：

$$
\mathcal H
=
L^2(\mathbf x)
\otimes
L^2(\mathbf y)
\otimes
\mathcal H_{\rm spin}
\otimes
\mathcal H_{\rm isospin}
\otimes\cdots.
$$

这是**自由度的分解**：空间变大是因为粒子多、自由度多。

### 1.3 第二种分解：Direct sum——对称性导致的分块

三体 Hamiltonian 通常与总角动量、宇称、同位旋等守恒量对易：

$$
[H,J^2]=0,
\qquad
[H,\Pi]=0.
$$

守恒量意味着：Hamiltonian 不会把一个 $J^\pi T$ sector 里的态“泄露”到另一个 sector。于是 Hilbert 空间可以写成

$$

\mathcal H
=
\bigoplus_{J^\pi T}
\mathcal H_{J^\pi T}.

$$

这里的 $\oplus$（direct sum）表示：

> 不同 $J^\pi T$ 的子空间**互不相交、互不混合**，可以各自独立求解。

这是真正的空间直和。数值上，这意味着我们先算 $J^\pi=0^+$，再算 $1^-$……每个 sector 是一个独立的小问题，最后把结果按统计权重加起来。

在一个固定 $J$ sector 内，再做 partial-wave expansion：

$$
\Psi^{JM}
=
\sum_c
u_c(x,y)\,
\mathcal Y_c^{JM}
(\hat x,\hat y,\sigma,\tau).
$$

这里 $\mathcal Y_c^{JM}$ 是把两份轨道角动量（$l$ 对 $\mathbf x$、$\lambda$ 对 $\mathbf y$）与自旋耦合到总 $J$ 的角向基函数；求和指标 $c$ 是 **channel label**，可能包含

$$
l,\;s,\;j,\;\lambda,\;I,\ldots
$$

注意：这些量**通常并不分别守恒**，它们只是构造固定 $J^\pi T$ sector 基底的标签。真正守恒的只有 $J^\pi$（和 $T$）。

固定 $J$ 之后，问题的空间结构变成

$$

\mathcal H_J
\simeq
\bigoplus_c
\left[
L^2(\mathbb R_+^x)
\otimes
L^2(\mathbb R_+^y)
\right].

$$

也就是说，原来的六维空间问题被整理成：

> 一组**离散** channel label $c$，外加两个**连续** radial variables $x,y$。

角向已经全部被对称性“吃掉”了，剩下的连续问题只有二维。这是所有三体计算的共同出发点。

### 1.4 第三种“分解”：Faddeev——既非 tensor product，也非 direct sum

Faddeev 理论写

$$

\Psi=\psi_1+\psi_2+\psi_3.

$$

这看起来也像一种“分解”，但它与上面两种**完全不是一回事**：

* 一般并没有 $\langle\psi_\alpha|\psi_\beta\rangle=0$；
* 也不能写 $\mathcal H=\mathcal H_1\oplus\mathcal H_2\oplus\mathcal H_3$；
* 三个 $\psi_\alpha$ 都是**同一个**三体 Hilbert 空间里的完整三体函数。

Faddeev 做的不是“把空间切块”，而是把总波函数按 pair interaction topology 重新组织。

具体为什么这样做、这样做换来了什么，我们在第三章详细推导。这里先记住：三种“分解”对应三个层次——自由度、对称性、方程结构。

### 1.5 三套 Jacobi 坐标不是三个空间

三个粒子可以有三套 Jacobi partition：

$$
(23)+1,
\qquad
(31)+2,
\qquad
(12)+3,
$$

分别记为

$$
(\mathbf x_1,\mathbf y_1),
\quad
(\mathbf x_2,\mathbf y_2),
\quad
(\mathbf x_3,\mathbf y_3).
$$

它们并不是三个不同的 Hilbert 空间，而是**同一个**相对运动空间的三套坐标：

$$
\mathcal H_1\simeq\mathcal H_2\simeq\mathcal H_3,
$$

彼此由 Jacobi transformation（一个线性的坐标变换加上 Jacobian）联系。

一个好的类比是：

> 同一个平面，你可以用 Cartesian coordinates，也可以用 polar coordinates；坐标不同，但点还是那些点。

所以千万不要写成

$$
\mathcal H
=
\mathcal H_1\oplus\mathcal H_2\oplus\mathcal H_3.
$$

三套 Jacobi 坐标之所以重要，不是因为它们“产生了三个空间”，而是因为**不同的 cluster topology 在不同的 Jacobi 坐标下最自然**。

例如 $(23)+1$ 这个通道的渐近区域是

$$
x_1\sim\text{finite},
\qquad
y_1\to\infty,
$$

即“23 抱成一团、1 跑到无穷远”。这个几何结构在 $(x_1,y_1)$ 坐标里一眼就能看见；换到另外两套坐标里，它会变得面目模糊。

这正是 Faddeev 要利用的东西。

### 1.6 基底和子空间必须严格区分

在进入各种方法之前，还要澄清一对容易混淆的概念。

假设

$$
\mathcal H_x=L^2(x),
$$

我们选择一组函数

$$
\phi_1,\phi_2,\ldots,\phi_N.
$$

这些是 **basis functions**。它们张成

$$
V_N
=
\operatorname{span}
\{\phi_1,\ldots,\phi_N\}
\subset\mathcal H_x.
$$

真正参与近似的，是这个有限维 **subspace** $V_N$，而不是基底本身。对应的 projector（对正交基）为

$$
P_N
=
\sum_{n=1}^N
|\phi_n\rangle\langle\phi_n|.
$$

因此应当牢记：basis 是描述子空间的坐标，subspace 才是物理/数值近似本身。

如果只是换了一组基底，但

$$
\operatorname{span}\{\phi_n\}
=
\operatorname{span}\{\tilde\phi_n\},
$$

那么 model space 没有改变，近似结果也不会变。反之，只有增加新的独立方向，

$$
V_N\subset V_{N+1},
$$

才真正扩大了近似空间。

后面会看到：CDCC、wave packet、Coulomb-Sturmian 的争论焦点常常是“选什么基底”，但从数学上看，它们真正定义的是“选什么子空间、截掉什么”。

---

## 第二章 三体问题到底难在哪里

### 2.1 不只是“六维很大”

把质心去掉以后，三体确实是六维相对坐标问题。partial-wave 分解之后剩两个连续径向变量，看似也不算夸张——现代 sparse matrix、FEM、spectral method、GPU 早就能在很多高维问题上工作。

如果三体问题只是“维数高”，它不会直到今天仍然是专门的研究方向。

### 2.2 真正的困难：无穷远不止有一种形状

三体**散射**真正棘手的地方，是 $x,y\to\infty$ 时系统可能处于好几种完全不同的组态：

1. 一个束缚 pair 加一个 spectator：

$$
(23)+1;
$$

2. rearrangement 通道：

$$
(31)+2;
$$

3. 另一种 rearrangement：

$$
(12)+3;
$$

4. 三个粒子都互相远离（breakup）：

$$
1+2+3;
$$

5. 如果带电，Coulomb 长程相互作用在无穷远仍然存在。

每一种组态在渐近区都有自己特有的波函数形状（束缚态尾巴、Coulomb 波、振荡的 breakup 波前）。所以难点在于：三体散射有多个彼此不同的 asymptotic topology。

一个好的三体方法，往往不是单纯把矩阵做小，而是在**组织这些不同的无穷远结构**。

### 2.3 精确重写与近似截断：最重要的一张表

现在可以给出整篇文章里最核心的一张表。它回答的问题是：各种常见操作，到底是**精确的重新表述**，还是**引入了近似**？

| 操作 | 本质 | 是否引入近似 |
|---|---|---|
| 换 Jacobi 坐标 | representation change | 否 |
| coordinate $\leftrightarrow$ momentum Fourier transform | representation change | 否 |
| partial-wave decomposition（不截断） | exact basis expansion | 否 |
| Faddeev decomposition | exact equation reorganization | 否 |
| AGS reformulation | exact operator reformulation | 否 |
| hyperspherical coordinate change | representation / factorization | 否 |
| channel truncation $J,l,\lambda\leq\cdots$ | model-space truncation | 是 |
| CDCC continuum discretization | cluster model-space projection | 是 |
| finite grid / FEM / spline basis | finite-dimensional approximation | 是 |
| wave-packet discretization | continuum coarse graining | 是 |
| Coulomb-Sturmian truncation | finite spectral model space | 是 |
| separable finite-rank $t$ | operator compression | 是 |

很多概念上的混乱，正来自把“**重写问题**”和“**近似问题**”混为一谈：

* Faddeev 分解是精确的——它只是把 Schrödinger 方程重新组织成等价形式；
* CDCC 的 continuum discretization 是近似——它真的丢掉了 model space 之外的物理。

两者处在不同的层次，所以“Faddeev 和 CDCC 哪个好”这个问题本身就不完整：更合理的问法是“在同一个层次上，它们各自的选择是什么、代价是什么”。

---

## 第三章 方程架构：Schrödinger、CDCC、Faddeev、AGS

现在进入链条的第三层：**用什么样的方程来组织问题**。这一层的选择（Schrödinger / Faddeev / AGS / projected Schrödinger）都是精确的方程重写，真正的近似在后面两层才出现。

### 3.1 最直接的办法：直接解三体 Schrödinger 方程

Hamiltonian 写成

$$
H
=
H_0+V_{12}+V_{23}+V_{31},
$$

其中 $H_0$ 是三体自由相对运动动能。直接求解

$$
(E-H)\Psi=0.
$$

最直接的离散办法是两个 radial directions 都选有限维子空间：

$$
L^2(x)
\rightarrow
V_x^{N_x},
\qquad
L^2(y)
\rightarrow
V_y^{N_y},
$$

于是

$$
\mathcal H
\rightarrow
V_x^{N_x}\otimes V_y^{N_y},
$$

波函数展开为

$$
\Psi_N(x,y)
=
\sum_{ij}
C_{ij}
B_i(x)C_j(y).
$$

最终得到矩阵问题。对 bound state，是广义本征值问题：

$$

HC=ESC.

$$

对散射问题（给定入射通道的 driven equation），是线性方程组：

$$

A(E)C=B.

$$

这种方法对 bound state 很自然：束缚态是 $L^2$ 的，有限 basis 加得足够多就能收敛。

对于 scattering，麻烦来了：第二章列出的 elastic、rearrangement、breakup、Coulomb 长程，全部藏在**同一个** $\Psi$ 里，纠缠在一起。用一套坐标、一个有限 box 去同时逼近所有这些渐近行为，代价非常高。

这正是 CDCC 和 Faddeev 各自出手的地方。

### 3.2 CDCC：截断一个 tensor factor

考虑 $n+p+A$。CDCC（Continuum Discretized Coupled Channels）首先做一个**物理上的选择**：认定 $(np)+A$ 是最重要的 partition——中子和质子组成 projectile（例如氘核），与靶 $A$ 碰撞。

于是 Hilbert 空间写为

$$

\mathcal H
=
\mathcal H_{np}
\otimes
\mathcal H_R.

$$

其中

$$
\mathcal H_{np}=L^2(r)
$$

描述 projectile 内部运动（$r$ 是 $n$–$p$ 距离），

$$
\mathcal H_R=L^2(R)
$$

描述 projectile–target 相对运动。

#### 3.2.1 CDCC 的核心是 model-space projection

CDCC 首先做的是

$$

\mathcal H_{np}
\longrightarrow
P_{\rm int}\mathcal H_{np}.

$$

也就是只保留 projectile internal space 的一个有限 model space：

$$
P_{\rm int}
=
\sum_{n=1}^{N}
|\phi_n\rangle\langle\phi_n|.
$$

这些 $\phi_n$ 可以是：

* true bound states（真实的氘核基态等）；
* continuum bins（把连续谱按动量区间切块平均）；
* pseudostates（对角化某个辅助 Hamiltonian 得到的离散近似态）；
* Gaussian expansion states；
* THO states（transformed harmonic oscillator）；
* Sturmian states；
* box states（放在有限盒子里对角化）。

这些是不同的 **basis construction**，但共同点是它们定义了同一个东西——projector $P_{\rm int}$。

因此 CDCC model space 是

$$

\mathcal H_{\rm CDCC}
=
P_{\rm int}\mathcal H_{np}
\otimes
\mathcal H_R,

$$

即

$$

P_{\rm int}\otimes I_R.

$$

也就是说：

> projectile 内部自由度被压缩成有限个 channel，而 projectile–target 分离 $R$ 仍保留为连续变量。

**这一步才是 CDCC 真正的物理近似。** 它假设：把入射通道之外最重要的物理（projectile 破碎、激发）压缩进 $(np)+A$ 这个 partition 的有限内部空间，就足以描述散射。

#### 3.2.2 为什么标准 CDCC 变成 coupled ODE？

展开

$$
\Psi(r,R)
\approx
\sum_n
\phi_n(r)\chi_n(R).
$$

把它代入 Schrödinger 方程，两边左乘 $\langle\phi_n|$ 对 $r$ 投影（这是标准的 Galerkin 步骤），得到

$$
\left[
T_R+\epsilon_n-E
\right]\chi_n(R)
+
\sum_m
V_{nm}(R)\chi_m(R)
=0,
$$

其中 $\epsilon_n$ 是 $\phi_n$ 的内部能量，

$$
V_{nm}(R)
=
\langle\phi_n|
\,U_{nA}+U_{pA}\,
|\phi_m\rangle(R)
$$

是作用在 $R$ 上的耦合势。做 partial waves 之后，这就是一组普通的 coupled radial ODE，可以用 Numerov 之类的方法传播求解。

但要注意，coupled ODE 不是 CDCC 的定义，而只是常见的 numerical realization。它出现的唯一原因是：内部坐标 $r$ 已被有限维化（$\phi_n$），而 $R$ 还保持连续，所以剩下的是一组关于 $\chi_n(R)$ 的常微分方程。

#### 3.2.3 CDCC 完全可以进一步 finite-dimensionalize

完全可以再把 $R$ 离散：

$$
L^2(R)
\rightarrow
P_RL^2(R),
$$

于是

$$

P_{\rm int}\otimes P_R,

$$

展开为

$$
\Psi
=
\sum_{ni}
C_{ni}\phi_n(r)B_i(R).
$$

此时 CDCC 不再需要 coupled ODE，而直接变成 finite-dimensional Galerkin problem：

$$
A(E)C=B.
$$

因此原则上可以有：

* FEM-CDCC；
* B-spline CDCC；
* DVR-CDCC；
* spectral CDCC；
* wave-packet CDCC；
* momentum-space CDCC。

这些“变体”改变的都只是 $R$ 方向的数值表示，CDCC 的物理定义始终来自 **projectile continuum model-space projection**，而不是来自 Numerov 或 coupled differential equation。

### 3.3 Faddeev：按相互作用拓扑重组方程

Faddeev 走的是另一条路：它不偏爱任何 partition，而是把 Hamiltonian 的结构本身利用起来。

考虑

$$
H=H_0+V_1+V_2+V_3,
$$

其中

$$
V_1=V_{23},
\qquad
V_2=V_{31},
\qquad
V_3=V_{12}.
$$

Schrödinger 方程是

$$
(E-H_0)\Psi
=
(V_1+V_2+V_3)\Psi.
$$

#### 3.3.1 推导：从 Schrödinger 到 Faddeev components

令自由 resolvent

$$
G_0(E)
=
\frac{1}{E-H_0+i0}.
$$

用 $G_0$ 作用在方程两边（对束缚态，$\Psi\in L^2$，齐次解没有贡献，这一步是严格的）：

$$
\Psi
=
G_0(V_1+V_2+V_3)\Psi.
$$

现在定义 Faddeev components

$$

\psi_\alpha
=
G_0V_\alpha\Psi,
\qquad
\alpha=1,2,3.

$$

那么立刻有

$$
\Psi
=
\psi_1+\psi_2+\psi_3.
$$

（对散射问题，右边还要加上入射项，这不改变方程的结构。）

把 $\Psi=\sum_\beta\psi_\beta$ 代回定义式：

$$
\psi_\alpha
=
G_0V_\alpha\psi_\alpha
+
G_0V_\alpha
\sum_{\beta\neq\alpha}\psi_\beta.
$$

第一项正是 $\alpha$ 自己这个 pair 的两体 Lippmann–Schwinger 结构。把这部分“收编”进 two-body $t$ operator（在 Jacobi 坐标的 pair 变量上定义）：

$$
t_\alpha
=
V_\alpha+V_\alpha G_0 t_\alpha,
$$

就得到标准的 Faddeev 方程：

$$

\psi_\alpha
=
G_0t_\alpha
\sum_{\beta\neq\alpha}\psi_\beta.

$$

注意最后的形式里，每个 component 只与**另外两个** component 耦合，而自己 pair 内部的无穷多次反复散射已经被 $t_\alpha$ 精确求和。

#### 3.3.2 这一步到底解决了什么？

Faddeev 不是为了“把一个六维函数变成三个更小的函数”——三个 $\psi_\alpha$ 各自仍然是完整的三体函数。

真正的收益是**多重散射级数的重组**。如果直接用 Schrödinger 方程做 Born 展开，得到的是

$$
G_0(V_1+V_2+V_3)G_0(V_1+V_2+V_3)\cdots
$$

所有可能的散射序列（粒子 1 撞 2、然后 2 撞 3、然后又是 1 撞 2……）混在一起，这个级数在三体情形收敛性很差（这正是两体理论直接推广到三体失败的地方）。

Faddeev 重组之后：

$$
V_{23}\text{ 内部的所有反复作用}
\quad\longrightarrow\quad
t_1\text{（被精确求和）}\longrightarrow \psi_1,
$$

$$
V_{31}\text{ 内部的所有反复作用}
\quad\longrightarrow\quad
\psi_2,
$$

$$
V_{12}\text{ 内部的所有反复作用}
\quad\longrightarrow\quad
\psi_3,
$$

剩下的耦合只描述 pair 之间的**交替**。所以比“相互作用责任分解”更准确的说法是：

Faddeev 按 pair-scattering topology 组织多重散射。

#### 3.3.3 components 不是正交子空间

再强调一次结构上的要点。一般并不存在

$$
\langle\psi_\alpha|\psi_\beta\rangle=0,
$$

也不能写

$$
\mathcal H
=
\mathcal H_1\oplus\mathcal H_2\oplus\mathcal H_3.
$$

三个 Faddeev components 都属于同一个完整三体 Hilbert 空间。区别只是：$\psi_1$ 专门组织 pair (23) 的散射，$\psi_2$ 组织 (31)，$\psi_3$ 组织 (12)。

Faddeev 分解的是相互作用责任，而不是正交空间。

这也解释了一个实际问题：如果想简单地“把三套 Jacobi 坐标的 basis 加在一起”来表示波函数，会得到 overcomplete 的集合；Faddeev 正是通过 interaction topology 明确每个成分“负责什么”，从而避免了这种混乱。

#### 3.3.4 为什么这对散射边界条件特别有用？

每个 component 都可以放在最自然的 Jacobi 坐标中：

$$
\psi_1(x_1,y_1),
\qquad
\psi_2(x_2,y_2),
\qquad
\psi_3(x_3,y_3).
$$

例如 $(23)+1$ 通道的渐近区是

$$
x_1\sim\text{pair size},
\qquad
y_1\to\infty.
$$

这个结构在 $(x_1,y_1)$ 中非常简单：$x_1$ 方向是束缚态尾巴，$y_1$ 方向是出射波。如果你坚持用唯一一套坐标描述所有 rearrangement channels，那么其中一些渐近区域会变得非常扭曲。

所以 Faddeev 的优势不在于“公式漂亮”，而在于让每一种 cluster asymptotics 都在自己的 natural coordinates 中出现。

这直接回应了第二章的困难：多个 asymptotic topology 被分门别类地组织起来了。

#### 3.3.5 一个重要限制：普通 Faddeev 最舒服的是短程相互作用

对于 short-range potential，Faddeev kernel 的数学性质很好（compactness 等）。

但 Coulomb

$$
V_C(r)\sim\frac1r
$$

衰减太慢，长程尾巴在“无穷远”仍然在起作用，会破坏 short-range 理论中的许多理想性质。这就是为什么三个带电粒子或含显著 Coulomb 的三体问题里，常常要使用：

* screened Coulomb + renormalization（屏蔽后重整）；
* Faddeev–Merkuriev splitting（把势拆成短程和长程部分分别处理）；
* Coulomb-distorted basis / resolvent（把 Coulomb 放进传播子或基底）；
* Coulomb-Sturmian 等专门表示。

这不是“数值小技巧”，而是长程相互作用**改变了散射理论的解析结构**：Coulomb 势下的渐近波不是平面波加球面波，而是 Coulomb 波函数 $F_l(\eta,kr)$、$G_l(\eta,kr)$。

#### 3.3.6 Faddeev 不是一种数值方法

Faddeev 方程抽象地写为

$$
X=B+K(E)X,
$$

即

$$

[1-K(E)]X=B.

$$

这里 $X$ 是 Faddeev component vector。注意，到这里仍然没有规定：

* 用坐标空间还是动量空间；
* FEM 还是 spline；
* grid 还是 spectral；
* wave packet 还是 Coulomb-Sturmian。

这些都是下一层的问题。因此：

Faddeev 是 equation architecture，不是 discretization scheme。

### 3.4 AGS：再往 operator level 提升一步

Faddeev 通常直接求 wavefunction components $\psi_\alpha$。AGS（Alt–Grassberger–Sandhas）更直接地求 channel-to-channel transition operators：

$$
U_{\beta\alpha}.
$$

典型结构为

$$
U_{\beta\alpha}
=
(1-\delta_{\beta\alpha})G_0^{-1}
+
\sum_\gamma
(1-\delta_{\beta\gamma})
t_\gamma G_0U_{\gamma\alpha}.
$$

从逻辑上可以这样理解：

$$

\begin{array}{ccc}
\text{Schrödinger}
&\to&
\text{Faddeev}\\
\Psi
&&
\psi_1,\psi_2,\psi_3\\[2mm]
&&\downarrow\\[-1mm]
&&
\text{AGS}\\
&&
U_{\beta\alpha}
\end{array}
$$

它们的差别不在“用了不同 mesh”，而在于**未知量处于不同抽象层**：波函数 → Faddeev 分量 → 跃迁算符。

当最终目标本来就是 scattering amplitudes、$S$ matrix、transition matrix 时，operator formulation 往往最自然——$U_{\beta\alpha}$ 在适当的矩阵元下直接给出物理的振幅，而不需要先解出完整的波函数。

### 3.5 波函数路线 vs 算符路线：两种求解思路的结构对比

上一节末尾说“未知量处于不同抽象层”。这个差别值得单独展开：它不是实现细节之争，而是贯穿整个散射理论的**两条根本路线**——求**态**（wavefunction route）还是求**算符**（operator route）。CDCC、直接 Schrödinger、Faddeev 都属于前者，AGS 是后者在三体里的标准形态。

#### 3.5.1 两体热身：同一个方程的两种读法

这对关系在两体散射里就已经完整存在。Lippmann–Schwinger 方程有两种等价写法（两体情形的详细推导见同目录的《faddeev方程 的 Wave-packet continuum discretisation》一文）。

**求态的读法**——未知量是散射态：

$$
|\psi^+\rangle
=
|\phi\rangle
+
G_0^{(+)}V|\psi^+\rangle.
$$

**求算符的读法**——未知量是 T-matrix：

$$
T
=
V+VG_0^{(+)}T.
$$

两者的桥梁是一个定义：

$$
T|\phi\rangle
\equiv
V|\psi^+\rangle,
$$

即“用 $T$ 作用在自由入射态上”打包了“用 $V$ 作用在含全部散射效应的真实态上”。两个方程的核结构完全相同（都是 $VG_0^{(+)}$ 的迭代），信息上互相等价：知道态可以恢复算符，知道算符也能恢复散射态：

$$
|\psi^+\rangle
=
|\phi\rangle+G_0^{(+)}T|\phi\rangle.
$$

但**直接产出**和**数值形态**很不一样——这正是三体里要对比的东西。

三体把这对关系原样放大：

$$

\underbrace{\text{Schrödinger / Faddeev}}_{\text{求 }\Psi,\ \psi_\alpha}
\quad\longleftrightarrow\quad
\underbrace{\text{AGS}}_{\text{求 }U_{\beta\alpha}}.

$$

#### 3.5.2 未知量的“家”：态空间 vs 算符空间

第一条结构差别是未知量生活的空间。

**波函数路线**：$\Psi\in\mathcal H$——就是第一章里构造的态空间。partial-wave 加 momentum representation 之后，$\psi(p,q)$ 是 **2 个连续变量**的函数。

**算符路线**：$U_{\beta\alpha}$ 是 Hilbert 空间上的算符，属于算符空间 $\mathcal B(\mathcal H)$（严格说由于奇异结构它并不有界，但作为“家”的定位是对的）。它的矩阵元

$$
U(p,q;p',q')
$$

是 **4 个连续变量**的函数。

$$

\psi(p,q):\ 2\ \text{个变量};
\qquad
U(p,q;p',q'):\ 4\ \text{个变量。}

$$

初看算符路线“更大”。但指标结构给出了补偿。

Faddeev 的自然指标是 **pair component** $\alpha=1,2,3$：三个分量，每个都是完整的三体函数，合起来描述**一个**态。AGS 的自然指标是 **channel 对** $(\beta,\alpha)$：一个矩阵，行标末态通道，列标初态通道。

rearrangement 通道，在态的语言里是渐近行为，在算符的语言里是矩阵下标。

“从初态 $\alpha$ 散射到末态 $\beta$（可能是 elastic、rearrangement 或 breakup）的振幅是多少”——这类问题在算符语言里是最自然的提问方式：它就是矩阵的一个元素。而在态的语言里，同一个信息藏在波函数尾部的渐近匹配中，需要额外步骤才能取出来。

#### 3.5.3 各自直接产出什么

**波函数路线的产出是完整的态结构**：

* 密度分布、内部几何、两体关联；
* 动量谱、breakup 流；
* 任意期望值 $\langle O\rangle=\langle\Psi|O|\Psi\rangle$。

但振幅不直接在手里：需要额外的渐近 matching 或投影，才能从 $\Psi$ 的尾部提取出 $S$ matrix。

**算符路线的产出是实验量的原生形式**：

* on-shell 矩阵元直接给出振幅，进而 $S$ matrix 与截面（至一个随约定变化的归一化因子）；
* 束缚态和共振态表现为 $U(E)$ 在复能量平面上的极点。

但态的结构信息基本丢失：算符知道的只是“从哪来、到哪去、幅值多少”，不再回答“束缚态长什么样”。

于是选择路线的第一个判据是：

你要的是态的结构，还是截面？

#### 3.5.4 边界条件住在哪

第二条判据是散射边界条件的实现位置（第六章会展开，这里先给结构性结论）。

* **波函数路线**：散射条件“住”在实空间的无穷远——$\Psi$ 的尾部必须长成出射波的样子，或者通过 $G_0^{(+)}$ 隐式赋予；
* **算符路线**：散射条件“住”在复能量平面的解析结构里——$+i0$ 处方规定边界的走向，物理内容体现在极点位置与留数中。

波函数在实空间的无穷远处“看见”散射，算符在复能量平面上“看见”散射。

#### 3.5.5 束缚态问题的对比

对 bound state，两条路线的求解形态也很不一样：

* **态路线**：$HC=ESC$，广义本征值问题。能量和波函数**同时**得到——本征向量就是物理波函数，一举两得；
* **算符路线**：扫描能量，找

$$
\lambda[K(E)]=1
$$

或等价地 Fredholm 行列式条件

$$
\det[1-K(E)]=0.
$$

能量找到了，波函数还要另外恢复。

这就是为什么做束缚态结构研究的人偏爱波函数路线，做反应截面的人偏爱算符路线——这不是品味问题，而是产出直接对准目标的问题。

#### 3.5.6 数值形态的典型配对

把本层选择（求态还是求算符）与第四章的表示层选择交叉，得到四格（参见 §5.6）：

| 路线 × 表示 | 典型数值形态 |
|---|---|
| 波函数 × coordinate | coupled PDE，sparse 矩阵（微分算符局域） |
| 波函数 × momentum | 积分方程，unknown $\psi(p,q)$，dense 核 |
| 算符 × momentum | 积分方程，unknown $U(p,q;p',q')$，dense 核、奇异结构、on-shell 后处理 |
| 算符 × coordinate | 少见（Green 函数的坐标表示） |

注意四种组合在逻辑上都存在，“AGS 必须 momentum space”并不成立——只是 momentum space 里 free resolvent 和 two-body $t$ 矩阵最简单（§4.2），所以算符路线几乎总是选它。**路线与表示是两个独立的选择，不要绑死。**

#### 3.5.7 一张对照表

|  | 波函数路线 | 算符路线 |
|---|---|---|
| 未知量 | $\Psi$ / $\psi_\alpha$ | $U_{\beta\alpha}$ / $T$ |
| 所在空间 | $\mathcal H$（态空间） | $\mathcal B(\mathcal H)$（算符空间） |
| 变量数（partial wave 后） | $\psi(p,q)$：2 | $U(p,q;p',q')$：4 |
| 自然指标 | pair component $\alpha$ | channel 对 $(\beta,\alpha)$ |
| rearrangement 通道 | 渐近行为，需 matching 提取 | 矩阵下标，自动并列 |
| 直接产出 | 态结构（密度、动量谱、$\langle O\rangle$） | 振幅、$S$ matrix、截面 |
| 获取振幅 | 渐近 matching / 投影 | on-shell 取值即得 |
| 束缚态 | $HC=ESC$，附带波函数 | $\lambda[K(E)]=1$ / $\det[1-K]=0$ |
| 散射条件位置 | 实空间无穷远 | 复能量面解析结构 |
| 典型数值形态 | coordinate：sparse PDE | momentum：dense 积分方程 |

#### 3.5.8 进阶：off-shell 自由度与 partition 依赖

最后一点在读文献和比较计算结果时特别有用。

波函数路线的解是唯一的（至整体相位）：$\Psi$ 就是一个态，不依赖任何约定。

算符路线的解则不然。$U_{\beta\alpha}(E)$ 作为完整的算符，包含大量 **off-shell** 信息——初末动量不在能量壳上的矩阵元。而这些信息：

* **物理上不可观**：可观测量（截面、振幅）只依赖 on-shell 取值；
* **依赖 partition/channel 约定**：两篇文章的 AGS 算符即使 on-shell 振幅完全一致，off-shell 行为也可以不同。

所以比较两个 AGS 计算时，先确认 channel 与 partition 约定是否相同。

反过来，这片“不可观但可自由选择”的空间正是算符路线独有的操作余地：§5.9 的 separable expansion 之所以合法，就是因为 off-shell 自由度可以被拿来简化计算而不损失任何 on-shell 物理——只有当未知量本来就是算符时，“压缩算符”才是一个不改变可观测量的合法操作。

### 3.6 CDCC 与 Faddeev 的核心区别

现在可以给出最核心的对比：

> CDCC：先选一个物理上重要的 cluster partition，再截断它的内部 continuum；
> Faddeev：不偏爱任何一个 pair，把所有 pair-scattering topology 显式并列组织。

更严格地说：

* Faddeev decomposition 在完整三体 Hamiltonian 下首先是**精确重写**；
* CDCC 的 $P_{\rm int}$ 是一个 **model-space approximation**。

所以两者并不处于完全相同的层次：CDCC 是 model-space projection 的思想，Faddeev 是 equation decomposition 的思想。

它们不是简单互斥的“两个算法”——原则上你甚至可以做“Faddeev 架构 + 类 CDCC 的基底”，只要分清哪一步是重写、哪一步是截断。

---

## 第四章 表示层：coordinate、momentum、hyperspherical

有了方程架构之后，下一步才是选择 representation。**这一步本身不产生任何物理近似**——就像同一个向量用不同坐标系写出来，向量本身没变。

### 4.1 Coordinate space

写成

$$
\psi_\alpha
=
\psi_\alpha(x_\alpha,y_\alpha),
$$

partial-wave 分解后是

$$
u_{\alpha c}(x,y).
$$

在坐标空间里，局域势的作用是最简单的乘法：

$$
[V\psi](x)=V(x)\psi(x),
$$

但 kinetic energy 是微分算符。因此 coordinate-space Faddeev 通常成为 coupled 2D PDE。

### 4.2 Momentum space

做 Fourier transform：

$$
(x,y)
\longleftrightarrow
(p,q).
$$

自由 Hamiltonian 变成对角的乘法算符：

$$
H_0
=
\frac{p^2}{2\mu_x}
+
\frac{q^2}{2\mu_y}.
$$

于是自由 resolvent

$$
G_0^{(+)}(E)
=
\frac{1}{E-H_0+i0}
$$

的结构非常直接（在 $E$ 固定时，它是 $(p,q)$ 的有理函数）。Faddeev 方程变成积分方程：

$$
\psi_c(p,q)
=
\sum_{c'}
\int dp'\,dq'\,
K_{cc'}(p,q;p',q')
\psi_{c'}(p',q').
$$

代价是：local coordinate-space potential 变成 momentum-space nonlocal kernel $V(p,p')$——原来是“每点乘一个数”，现在是“每个点耦合到所有点”。

因此可以粗略记：coordinate space 里 local interaction 简单、传播难；momentum space 里 free propagation、resolvent、$t$-matrix 都简单，代价是作用势变成 nonlocal kernel。

coordinate 和 momentum 是 representation，不是两种不同的 Faddeev 理论。

### 4.3 Hyperspherical coordinates：重新 factorize 六维空间

除了 cluster 分解，还可以采用六维 hyperspherical coordinates：

$$
\rho=\sqrt{x^2+y^2},
$$

加上五个 hyperangles $\Omega_5$。于是

$$

L^2(\mathbb R^6)
\simeq
L^2(\rho)
\otimes
L^2(S^5).

$$

展开

$$
\Psi(\rho,\Omega)
=
\sum_K
u_K(\rho)Y_K(\Omega),
$$

其中 $K$ 是 grand angular momentum，$Y_K$ 是 hyperspherical harmonics。然后截断 hyperangular basis：

$$
K\le K_{\max}.
$$

而 $\rho$ 仍保持连续，于是得到 coupled hyperradial equations。

这与 CDCC 恰好构成一组结构上的对照：

$$
\text{CDCC:}
\qquad
P_{\rm internal}\otimes I_R,
$$

$$
\text{HH:}
\qquad
I_\rho\otimes P_{\Omega}.
$$

两者都在做“某一部分自由度有限化、另一部分保持连续”，只不过 Hilbert-space factorization 完全不同：CDCC 按物理 cluster 切，HH 按几何尺度（总大小 $\rho$ vs 内部形状 $\Omega$）切。

各自的代价也来自这个选择：CDCC 对“privileged partition 不明显”的体系不自然；HH 对 cluster 渐近（$x$ 小 $y$ 大）的描述收敛可能慢，因为 cluster 结构在超球坐标里不是自然变量。

---

## 第五章 有限化：你究竟把哪个无限维对象变成有限维

这一层才轮到 FEM、B-spline、spectral、wave packet、Coulomb-Sturmian 等。它们首先回答同一个问题：

> 我用什么有限集合来表示本来无限维的函数空间？

### 5.1 Grid / finite difference：直接存函数值

选 grid 点

$$
x_i,
\qquad
y_j,
$$

未知量直接是

$$
u_{cij}=u_c(x_i,y_j).
$$

导数变成 differentiation matrix：

$$
\frac{d^2}{dx^2}
\longrightarrow
D_x^{(2)}.
$$

最终得到

$$
A\mathbf u=\mathbf b.
$$

它的直觉最简单：

> 不问函数由什么 basis 组成，直接问它在很多离散点上的值。

### 5.2 FEM：用很多局部低阶函数拼起来

构造局域 trial spaces：

$$
V_x=\operatorname{span}\{B_i(x)\},
\qquad
V_y=\operatorname{span}\{C_j(y)\},
$$

于是

$$
V_N=V_x\otimes V_y,
$$

展开

$$
u_c(x,y)
\approx
\sum_{ij}
C_{cij}B_i(x)C_j(y).
$$

然后做 Galerkin projection：

$$
\langle B_iC_j|
(E-H)|\Psi_N\rangle=0,
$$

得到矩阵方程。

FEM 的重要特点是 **local support**：每个基函数只在一小块区域非零，因此微分算子产生的矩阵是 sparse 的。从 Hilbert-space 角度：

FEM = 选择局域、分片的 finite-dimensional trial subspace。

### 5.3 B-spline：兼具局域性和高阶光滑性

B-spline 不是新的三体理论。它只是选

$$
V_x=\operatorname{span}\{B_i(x)\}
$$

作为 radial approximation space。它的典型优点是：

* compact/local support；
* 高阶 smoothness；
* mesh placement 灵活（可以在波函数变化剧烈的区域加密）；
* differential matrices 稀疏；
* 很适合半无限 radial coordinate。

因此

$$

\text{B-spline Faddeev}
=
\text{Faddeev equation}
+
\text{B-spline radial representation}.

$$

### 5.4 Global spectral expansion：用少量全局函数描述整个区域

写

$$
u(x)
\approx
\sum_{n=0}^{N}
c_n\phi_n(x),
$$

例如

$$
\phi_n=
\text{Chebyshev, Legendre, Laguerre},\ldots
$$

如果解足够 smooth，global basis 可能用很少的自由度取得很高的精度（指数收敛）。

应当区分两个词：

* **basis expansion / Galerkin representation** 是很广的概念，FEM、B-spline、spectral 都属于它；
* 经典 **spectral method** 通常强调 global high-order basis 与快速收敛。

FEM 强调 local basis，spectral method 强调 global basis——这是精度与稀疏性之间的经典取舍。

### 5.5 Momentum-space quadrature

对 momentum-space Faddeev 积分方程，最直接的办法是 quadrature：

$$
p\rightarrow p_i,
\qquad
q\rightarrow q_j,
$$

$$
\int dp\,p^2f(p)
\approx
\sum_i
w_ip_i^2f(p_i).
$$

最终得到

$$

\psi_{cij}
=
\sum_{c'i'j'}
K_{cij,c'i'j'}
\psi_{c'i'j'},

$$

或者

$$

(I-K)\psi=b.

$$

### 5.6 稀疏 vs 稠密：coordinate 与 momentum 的数值代价

Coordinate FEM：

$$
A_{cij,c'i'j'}C_{c'i'j'}
=
b_{cij}.
$$

Momentum quadrature：

$$
(I-K)_{cij,c'i'j'}
\psi_{c'i'j'}
=
b_{cij}.
$$

所以到了最低层，**绝大多数方法最终都是有限维 linear algebra**。但矩阵结构不同：

* coordinate local operators 往往产生 **sparse** 矩阵；
* momentum-space kernels 往往产生 **dense / nonlocal** 矩阵。

这直接决定了后面究竟采用什么线性代数方法（见第八章）。

### 5.7 Wave packet：不是“把积分点离散”，而是直接造 continuum model space

与简单 quadrature 不同，wave packet 真正构造 $L^2$ basis。

把 momentum continuum 分成区间

$$
\Delta_i=[p_i,p_{i+1}],
$$

定义 wave packet

$$
|X_i\rangle
=
\frac{1}{\sqrt{N_i}}
\int_{\Delta_i}
dp\,f_i(p)|p\rangle.
$$

spectator 方向类似：

$$
|Y_j\rangle
=
\frac{1}{\sqrt{M_j}}
\int_{\Delta_j}
dq\,g_j(q)|q\rangle.
$$

注意每个 $|X_i\rangle$ 都是**平方可积**的正常化态——这是它和“存格点值”的本质区别。于是你真正构造了一个有限维 $L^2$ model space：

$$

V_N
=
\operatorname{span}
\{|X_iY_j\rangle\},

$$

对应 projector

$$
P_N
=
\sum_{ij}
|X_iY_j\rangle
\langle X_iY_j|.
$$

所以 wave-packet method 与其理解成“特殊 quadrature”，不如理解成把连续谱按有限能量区间 coarse grain，得到一组正常化的 $L^2$ states。

这也是它与 CDCC continuum binning 很接近的地方：

$$
|\phi_n\rangle
\sim
\int_{\Delta k_n}
dk\,f_n(k)|\psi_k\rangle
$$

结构上完全类似。区别在于离散的彻底程度：

$$
\text{standard CDCC}
\sim
P_x\otimes I_y,
$$

而 fully discretized wave-packet three-body calculation 更像

$$
P_x\otimes P_y.
$$

即 spectator 连续变量也被 packet 化了，整个问题变成纯有限维。

### 5.8 Coulomb-Sturmian：physics-informed basis 到底特殊在哪

这是最容易被一句“physics-informed basis”糊弄过去的地方。先说结论：

Coulomb-Sturmian 不是一种新的 Faddeev 方程，而是一种专门适配 Coulomb $1/r$ 算符结构的离散 radial basis。

#### 5.8.1 构造

假设 radial function 是 $u_l(r)$。任取一组 basis，可以写

$$
u_l(r)
\approx
\sum_{n=0}^{N}
c_n\phi_{nl}(r).
$$

如果选 harmonic-oscillator basis，函数形状天然和 $r^2$ 势联系紧密。如果选 Coulomb-Sturmian，basis 的定义本身包含 $1/r$ 结构。一种常见形式是

$$
S_{nl}(r)
\propto
(2br)^{l+1}
e^{-br}
L_n^{2l+1}(2br),
$$

其中 $b$ 控制 radial scale，$L_n^{2l+1}$ 是伴随 Laguerre 多项式。它们可以看作一类 Sturm–Liouville 问题的本征函数，对应的 radial operator 中显式出现 Coulomb-like $1/r$ 项。

所以所谓 **physics-informed** 不是玄学，而是：

> basis 的构造已经利用了我们事先知道的 Hamiltonian 结构。

#### 5.8.2 “内建 Coulomb”到底内建了什么？

这里必须说得非常精确。

Coulomb-Sturmian basis **并不是**直接把真正的 scattering asymptotics

$$
F_l(\eta,kr),
\qquad
G_l(\eta,kr)
$$

硬塞进 basis。事实上单个 CS basis function 通常仍是指数衰减、属于 $L^2$ 的离散函数。

所以正确的说法不是：

> “CS basis 已经自动具有正确的 Coulomb scattering wave tail。”

而是：

CS basis 对 Coulomb Hamiltonian / Coulomb Green operator 的代数结构特别友好。

这才是它真正的价值：它把“我们早就知道问题里有 $1/r$”这条信息利用在 representation 上，而不是让有限 basis 从零开始重新拟合 Coulomb operator 的结构。

#### 5.8.3 为什么 projector 里会出现 $\langle\widetilde{nl}|$？

Coulomb-Sturmian 常采用 biorthogonal representation：有两套互为 dual 的基

$$
|nl\rangle,
\qquad
|\widetilde{nl}\rangle,
$$

满足

$$
\langle\widetilde{nl}|n'l\rangle
=
\delta_{nn'}.
$$

因此 completeness relation 写成

$$
I
=
\sum_{n=0}^{\infty}
|nl\rangle
\langle\widetilde{nl}|,
$$

截断后才是

$$

P_N
=
\sum_{n=0}^{N}
|nl\rangle
\langle\widetilde{nl}|.

$$

$P_N$ 的意义非常朴素：

> 把本来无限维的 radial function，投影到前 $N+1$ 个 CS functions 张成的 model space 中。

于是

$$
|f\rangle
\longrightarrow
P_N|f\rangle
=
\sum_{n=0}^{N}
|nl\rangle
\langle\widetilde{nl}|f\rangle,
$$

本来一个连续函数 $f(r)$，现在由有限个 coefficient $(c_0,c_1,\ldots,c_N)$ 表示。

#### 5.8.4 三体里真正长什么样？

三体 partial wave 后有两个 radial coordinates，因而更接近

$$
|nl;\nu\lambda\rangle
=
|nl\rangle_x
\otimes
|\nu\lambda\rangle_y.
$$

波函数写成

$$
u_c(x,y)
\approx
\sum_{n\nu}
C_{n\nu}^{(c)}
S_{nl}(x)
S_{\nu\lambda}(y).
$$

于是连续函数 $u_c(x,y)$ 变成 coefficient matrix $C_{n\nu}^{(c)}$。

这就是所谓

$$
\text{Faddeev equation}
+
\text{Coulomb-Sturmian model space}
$$

真正的含义。它不是一句新的物理理论，而是四件不同的事：

1. Faddeev 决定 equation architecture；
2. partial waves 决定 angular/channel representation；
3. CS 决定 radial finite-dimensional representation；
4. Coulomb boundary/Green-function machinery 决定 scattering asymptotics 如何实现。

这四件事不能混在一句话里——尤其是第 4 件：CS 是 Coulomb-adapted basis，但真正的 outgoing Coulomb scattering condition 仍然要由 Green function、matching 或其他散射构造来保证。

### 5.9 Separable expansion：它压缩的不是 wavefunction，而是 operator

这一层与 FEM、B-spline、wave packet 又不完全一样。

前面主要是在近似**态**

$$
|\psi\rangle,
$$

而 separable expansion 更常见的是近似 two-body potential 或 $t$ operator：

$$
t(E)
\approx
\sum_{m,n=1}^{r}
|g_m\rangle
\tau_{mn}(E)
\langle g_n|.
$$

这是一个 finite-rank approximation，$r$ 是 rank。rank-1 时：

$$
t
=
|g\rangle\tau(E)\langle g|.
$$

#### 为什么它能真正降低三体维数？

原始 Faddeev unknown 是

$$
\psi(p,q).
$$

如果

$$
t=|g\rangle\tau\langle g|,
$$

pair momentum dependence 可以被 form factor $g(p)$ 吸收：

$$
\psi(p,q)
\sim
g(p)F(q).
$$

于是

$$
L^2(p)\otimes L^2(q)
$$

被部分压缩成

$$

\mathbb C^{r}
\otimes
L^2(q).

$$

也就是说，原来二维的 unknown $\psi(p,q)$ 可能变成一组一维 spectator functions

$$
F_n(q).
$$

这是**结构性降维**，而不仅仅是 mesh refinement。普通 basis truncation 主要压缩 state space，separable expansion 主要压缩 operator rank——这是两种不同对象的压缩。

---

## 第六章 散射边界条件是独立的一层

这是很多介绍最容易跳过的一步。

对于 bound state，

$$
\Psi\in L^2
$$

是自然的：波函数归一化、在无穷远衰减。任何足够丰富的有限 basis 都能逼近它。

但 scattering eigenstate 严格来说**并不是**普通 $L^2$ normalizable state；它属于 generalized eigenstate 的框架，在无穷远是振荡的、不衰减的。

因此你不能只说：

> “我已经选了 $N$ 个 basis，所以 scattering problem solved。”

还必须回答：

outgoing boundary condition 到底怎么实现？

### 6.1 Coordinate-space philosophy：在大距离直接 matching

显式研究

$$
x,y\to\infty
$$

时

$$
\Psi
\sim
\Psi_{\rm incoming}
+
\Psi_{\rm outgoing},
$$

然后在有限 numerical domain 的外边界，与已知 asymptotic solutions 匹配，提取 $S$ matrix。

这个做法很直观，但三体 breakup 和 Coulomb 会让边界结构很复杂：breakup 渐近不是简单的出射球面波，Coulomb 渐近不是平面波。

### 6.2 Momentum/operator-space philosophy：把 outgoing 条件放进 resolvent

使用

$$

G^{(+)}(E)
=
\frac{1}{E-H+i0}.

$$

其中

$$
+i0
$$

不是装饰符号，而是在能量实轴上选择正确的解析延拓，从而**规定** outgoing-wave boundary condition（这一点与两体 Lippmann–Schwinger 方程中的 $+i\epsilon$ 完全同理）。

因此 coordinate-space 与 operator-space 的根本差别在于：coordinate methods 更多在 real-space infinity 上处理散射，operator methods 更多把散射条件编码在 resolvent 的 analytic structure 中。

对于 Coulomb，这一问尤其重要——长程作用意味着“无穷远”的行为本身就被修改了（Coulomb 相移、对数扭曲的波前）。

---

## 第七章 一个具体例子：同一个 $n+p+A$ 在不同方法里的样子

这一章把前面所有抽象概念落到一个具体问题上。假设 Hamiltonian 是

$$
H
=
H_0
+V_{np}
+U_{nA}
+U_{pA}.
$$

### 7.1 直接 Schrödinger

选一套 Jacobi coordinates $(r,R)$：

$$
(E-H)\Psi(r,R)=0.
$$

你直接面对一个两径向变量、多个 partial-wave channel 的 coupled problem。所有 breakup、rearrangement、elastic 结构都藏在同一个 $\Psi$ 里面。

### 7.2 CDCC

先把 $np$ internal Hamiltonian 离散：

$$
h_{np}\phi_n
=
\epsilon_n\phi_n,
$$

保留有限组 $\{\phi_n\}_{n=1}^{N}$。然后

$$
\Psi(r,R)
\approx
\sum_n
\phi_n(r)\chi_n(R).
$$

于是问题变成 $\chi_0(R),\chi_1(R),\ldots,\chi_N(R)$ 之间的 coupled-channel propagation。它把 breakup continuum 转换成有限个 internal channels。

### 7.3 Coordinate-space Faddeev

写

$$
\Psi
=
\psi_{np}
+
\psi_{nA}
+
\psi_{pA}.
$$

每一个 component 用自己的 Jacobi coordinates：

$$
\psi_{np}(x_{np},y_A),
\qquad
\psi_{nA}(x_{nA},y_p),
\qquad
\psi_{pA}(x_{pA},y_n).
$$

这样 $(np)+A$、$(nA)+p$、$(pA)+n$ 三种 pair topology 都被显式保留，各自在自己的自然坐标里有简单的渐近。

### 7.4 Momentum-space Faddeev / AGS

未知量变成

$$
\psi_\alpha(p,q)
$$

或者 transition operator

$$
U_{\beta\alpha}(p,q;p',q').
$$

free propagation 与 two-body $t$ matrices 在 momentum/operator language 中更自然。

### 7.5 这四种写法之间真正的关系

$$

\begin{array}{ccccc}
& \text{full three-body problem} & \\[1mm]
& \downarrow & \\[1mm]
\text{direct Schr.}
&\qquad&
\text{Faddeev/AGS exact reorganization}
\\[2mm]
\downarrow
&&
\downarrow
\\[2mm]
\text{choose representation}
&&
\text{choose representation}
\\[2mm]
\downarrow
&&
\downarrow
\\[2mm]
\text{grid/basis truncation}
&&
\text{grid/basis/rank truncation}
\end{array}
$$

而 CDCC 则是在 full Schrödinger problem 上先引入一个 physically chosen cluster-space projection。

四种写法求解的是**同一个物理问题**，区别只在于：在哪一层做了什么样的组织和近似。

---

## 第八章 最后的落脚点：所有路线都变成线性代数

一旦你做了 channel truncation、basis truncation、quadrature 或 finite-rank approximation，无限维问题最终都变成有限维对象。

### Bound state

$$
HC=ESC.
$$

求广义本征值问题。

### Driven scattering problem

$$
A(E)C=B.
$$

求线性方程组。

### Faddeev kernel formulation

$$
K(E)C=C.
$$

bound state 可以通过寻找

$$
\lambda_n[K(E)]=1
$$

确定（$E$ 扫描使最大本征值达到 1 的能量）。

然后才轮到真正底层的 numerical linear algebra：

* LU；
* sparse direct solver；
* GMRES；
* BiCGSTAB；
* Arnoldi；
* Lanczos；
* Krylov subspace；
* preconditioner；
* low-rank compression。

到了这一层以后，你处理的是矩阵结构、条件数、稀疏性和迭代收敛。这里已经与“三体物理”部分相当解耦——sparse 矩阵配 direct/Krylov 求解器，dense 矩阵配 GMRES + preconditioning，是纯粹数值线性代数的考量。

---

## 第九章 统一比较与心智地图

### 9.1 一张统一的比较表

把前面所有讨论压缩成一张表：

| 方法 | 方程结构 | 路线 | 空间分解 / 表示 | 真正截断什么 | 主要优势 | 主要难点 |
|---|---|---|---|---|---|---|
| direct Schrödinger | $(E-H)\Psi=0$ | 波函数 | $x\otimes y$ | $P_x\otimes P_y$（grid/basis） | 概念直接 | 多种三体 asymptotics 缠在一起 |
| CDCC | projected Schrödinger | 波函数 | internal $\otimes R$ | $P_{\rm int}\otimes I_R$ | 适合明显 projectile+target 图像 | privileged partition 选择，model-space 收敛 |
| fully discrete CDCC | projected Schrödinger | 波函数 | internal $\otimes R$ | $P_{\rm int}\otimes P_R$ | 直接 Galerkin 矩阵 | 同上，加 $R$ 离散收敛 |
| coordinate Faddeev | Faddeev components | 波函数 | $(x_\alpha,y_\alpha)$ | channels + grid/basis | 各 pair topology 渐近自然 | 实现复杂，Coulomb 麻烦 |
| momentum Faddeev | Faddeev components | 波函数 | $(p_\alpha,q_\alpha)$ | quadrature/basis | resolvent、$t$-matrix 自然 | dense kernel、奇异点处理 |
| wave-packet Faddeev | Faddeev | 波函数 | $(p,q)$ | $P_p\otimes P_q$ | 真正 $L^2$ 离散 continuum | bin 收敛 / 分辨率 |
| separable Faddeev | Faddeev | 波函数（借算符压缩） | pair + spectator | finite-rank $t$ | 结构性降维 | low-rank fidelity |
| AGS | transition operators | 算符 | momentum/operator space | quadrature / separable rank | 直接面向 transition amplitudes | kernel 与奇异性处理 |
| hyperspherical | Schrödinger/Faddeev | 波函数 | $\rho\otimes\Omega_5$ | $I_\rho\otimes P_\Omega$（$K\le K_{\max}$） | 六维几何统一 | cluster asymptotics 收敛可能慢 |
| Coulomb-Sturmian | （通常配 Faddeev） | 波函数 | CS radial basis | $N_{\rm CS}$ | Coulomb 算符表示友好 | scale/收敛，边界条件仍需单独处理 |

这张表比“某某方法是 PDE、某某方法是 matrix”更本质——PDE、integral equation、matrix 最后都只是不同表示下的数值形态。其中「路线」一列回答的是 §3.5 的那条正交轴：未知量是**态**还是**算符**——它与方程结构、表示方式都是独立的选择。

### 9.2 一张分层的心智地图

可以把量子三体计算想成这样一条从上到下的链：

$$

\begin{array}{c}
\textbf{Layer 0: Physics}\\
H_0+V_{12}+V_{23}+V_{31}+V_{123}
\\[3mm]
\downarrow
\\[3mm]
\textbf{Layer 1: Symmetry / Hilbert-space organization}\\
\mathcal H=\bigoplus_{J^\pi T}\mathcal H_{J^\pi T}
\\[3mm]
\downarrow
\\[3mm]
\textbf{Layer 2: Equation architecture}\\
\text{Schrödinger / Faddeev / AGS / CDCC projection}
\\[3mm]
\downarrow
\\[3mm]
\textbf{Layer 3: Representation}\\
(x,y),\;(p,q),\;(\rho,\Omega)
\\[3mm]
\downarrow
\\[3mm]
\textbf{Layer 4: Approximation / compression}\\
P_{\rm ch},\;P_x,\;P_y,\;P_{\rm int},\;K_{\max},\;N_{\rm CS},\;\mathrm{rank}(t)
\\[3mm]
\downarrow
\\[3mm]
\textbf{Layer 5: Scattering realization}\\
\text{matching / }G^{(+)}\text{ / Coulomb treatment}
\\[3mm]
\downarrow
\\[3mm]
\textbf{Layer 6: Linear algebra}\\
HC=ESC,\quad AC=B,\quad [1-K]C=B
\end{array}
$$

这张图最重要的地方不是分类漂亮，而是它告诉你：

> 不同文章真正的“创新点”可能发生在完全不同的层。

一篇文章可能物理方程完全没变，只是换了更好的 basis；另一篇可能 basis 很普通，但重新组织了 integral kernel；还有一篇可能前面全都一样，只是在 Coulomb boundary condition 或 preconditioner 上做了关键突破。把这些层分开，才不会被方法名牵着走。

### 9.3 看到一种新三体方法时，问六个问题

以后读论文，建议不要先问“这属于哪一个流派”，而是按下面六个问题拆。

**问题 1：物理 Hamiltonian 是什么？**

$$
H=H_0+\sum_\alpha V_\alpha
$$

有没有 Coulomb？有没有 three-body force？有没有 optical/nonlocal interaction？

**问题 2：equation architecture 是什么？**

它解的是

$$
(E-H)\Psi=0,
$$

还是

$$
\Psi=\sum_\alpha\psi_\alpha,
$$

还是

$$
U_{\beta\alpha}?
$$

这一层区分 Schrödinger / Faddeev / AGS / projected equations。其中还藏着一个正交的子问题（§3.5）：**未知量是态还是算符？**——前者直接给出态的结构，后者直接给出跃迁振幅，两条路线的产出、边界条件位置和数值形态都不同。

**问题 3：用什么 representation？**

$$
(x,y),
\qquad
(p,q),
\qquad
(\rho,\Omega),
$$

或者某种 mixed representation。这一步本身通常不产生物理近似。

**问题 4：真正截断的是什么？**

可能是

$$
N_{\rm channel},
\qquad
P_x,\;P_y,
\qquad
P_{\rm internal},
\qquad
K_{\max},
\qquad
N_{\rm CS},
\qquad
\operatorname{rank}(t).
$$

**这一层才是真正决定 numerical approximation 的地方。**

**问题 5：散射边界条件怎么实现？**

是 explicit matching？还是 complex scaling？还是 absorbing boundary？还是

$$
G^{(+)}(E)
$$

的 analytic prescription？对于 Coulomb，这一问尤其重要。

**问题 6：最后矩阵怎么解？**

只有到了最后，才问 sparse/dense、direct/iterative、Krylov/preconditioner。

### 9.4 最值得记住的几组“不要混淆”

**Jacobi partitions $\neq$ Hilbert-space direct sum。** 三套 Jacobi coordinates 是同一个空间的三套表示。

**Faddeev decomposition $\neq$ orthogonal decomposition。**

$$
\Psi=\psi_1+\psi_2+\psi_3
$$

是 interaction-topology organization，不是

$$
\mathcal H=\mathcal H_1\oplus\mathcal H_2\oplus\mathcal H_3.
$$

**Faddeev $\neq$ numerical discretization。** Faddeev 决定方程怎样重写。你仍然可以做 coordinate Faddeev、momentum Faddeev、FEM Faddeev、spline Faddeev、wave-packet Faddeev、Coulomb-Sturmian Faddeev、separable Faddeev。

**CDCC $\neq$ coupled ODE。** CDCC 的核心是 $P_{\rm internal}$。coupled radial ODE 只是最常见实现。

**Coulomb-Sturmian $\neq$ Coulomb boundary condition。** CS 是 Coulomb-adapted basis。真正的 outgoing Coulomb scattering condition 仍然要由 Green function、matching 或其他散射构造来保证。

**Separable expansion $\neq$ 普通 basis truncation。** 普通 basis truncation 主要压缩 state space，separable expansion 主要压缩 operator rank。

### 9.5 CDCC 可以从 Faddeev 数值体系借什么？

很多。因为 Faddeev 体系中大量所谓“方法”其实只是 numerical realization，与方程架构正交。CDCC 完全可以借：

$$
\text{FEM},\quad
\text{B-spline},\quad
\text{DVR},\quad
\text{spectral basis},\quad
\text{wave packet},\quad
\text{Coulomb-Sturmian},\quad
\text{momentum-space integral equations},\quad
\text{Krylov / low-rank / separable operator techniques}.
$$

真正不能简单照搬的是 Faddeev 的 **multiple-partition architecture**：不同 Jacobi basis 都属于同一个三体 Hilbert space，简单相加容易 overcomplete。Faddeev 正是通过 interaction topology 来解决这一点。

反过来，Faddeev 体系也可以借 CDCC 的 pseudostate 思想来构造有限的内部基底。分层清楚之后，“借用”变成自然而然的事。

---

## 第十章 总结

如果全文只记四句话，就是下面四句：

第一句：Faddeev 主要解决“怎样组织三体散射 topology”。

第二句：CDCC 主要解决“怎样把一个重要 cluster continuum 压缩成有限 model space”。

第三句：FEM、B-spline、wave packet、Coulomb-Sturmian 等主要解决“怎样把剩余无限维对象数值表示出来”。

第四句：波函数路线回答“态长什么样”，算符路线回答“跃迁振幅是多少”——动手前先想清楚你要哪个。

而贯穿所有方法的核心问题始终是四个：

$$

\begin{array}{c}
\text{我在什么空间里？}\\
\text{我怎样组织相互作用和渐近通道？}\\
\text{我真正截断了什么？}\\
\text{散射边界条件放在哪里？}
\end{array}
$$

一旦这些问题能回答清楚，CDCC、Faddeev、AGS、hyperspherical、FEM、wave packet、Coulomb-Sturmian、separable expansion 就不会再是一堆互相竞争的术语。

它们只是同一个量子三体问题，在**不同数学层次**上的不同选择。
