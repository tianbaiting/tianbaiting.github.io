# 升降算符的构造


> 从代数结构到谐振子与角动量的统一处理

---

## 0. 动机

给定哈密顿量 $H$，求本征值通常需要在坐标表象中解偏微分方程。但若谱具有"等间距结构"，就可以提出一个更经济的问题：

> 能否找到算符 $a$，使得 $a|E\rangle \propto |E - \lambda\rangle$？即用纯代数运算代替求解微分方程。

这个思路的出发点是**对易关系**，而非波函数的具体形式。

---

## 1. 一般理论

### 1.1 什么样的算符可以构造升降算符？

并非所有哈密顿量都能构造升降算符。以下是使构造成立的充分条件，以及背后的物理与数学含义。

**条件一：谱具有等间距结构**

若 $H$ 的本征值满足 $E_n = E_0 + n\lambda$（$\lambda > 0$ 为常数），则升降算符必然存在。等间距是升降算符存在的最强信号——它直接对应于某个"步长为 $\lambda$ 的移位对称性"。

反例：若谱为 $E_n \sim n^2$（如无限深势阱），相邻能级差 $E_n - E_{n-1} = (2n-1)\lambda$ 依赖于 $n$，不存在满足 $[H,a] = -\lambda a$ 的常系数降算符。

**条件二：$H$ 可以因式分解**

若能写出

$$H = a^\dagger a + \varepsilon_0$$

其中 $[a, a^\dagger]$ 是**常数或 $H$ 本身的简单函数**，则升降算符可以构造。因式分解的关键约束是：

$$[H, a] = [a^\dagger a,\, a] = [a^\dagger, a]\, a$$

只有当 $[a^\dagger, a]$ 是常数（Heisenberg 代数）或正比于某守恒量（$\mathfrak{su}(2)$ 等），右侧才正比于 $a$，升降算符才成立。

**条件三：系统具有某个连续对称性的李代数结构**

若 $H$ 或目标算符是某个李代数 $\mathfrak{g}$ 的 Casimir 元（与所有生成元对易），而待对角化的量是 $\mathfrak{g}$ 的 Cartan 子代数元（即可以同时对角化的极大交换子代数），则 Cartan 元的"根向量"（root vectors）扮演升降算符的角色。

具体地：设 $H_0$ 是 Cartan 元，$e_\alpha$ 是根向量，则 $[H_0, e_\alpha] = \alpha \cdot e_\alpha$，$\alpha$ 称为根。升降算符的构造就是找这些根向量。

**实际判断步骤**

| 问题 | 若是 | 若否 |
|------|------|------|
| 谱是否等间距？ | 直接寻找 $[H,a]=-\lambda a$ | 考虑形变/非线性升降算符（超出本文） |
| $H$ 是否可写成 $p^2/2m + V(x)$？ | 尝试 $a = \alpha x + \beta p$ | 考虑矩阵形式或抽象李代数 |
| $V(x)$ 是否为二次型（谐振子）或库仑型（氢原子）？ | 存在精确升降算符 | SUSY 量子力学可系统处理 |
| 系统是否有旋转对称性？ | 用 $L_\pm = L_x \pm iL_y$ | 考察具体的对称群 |

### 1.2 核心定义

设 $H$ 是 Hilbert 空间上的自伴算符。若算符 $a$ 满足

$$[H \, a] = -\lambda\, a, \qquad \lambda \in \mathbb{C} \setminus \{0\},$$

则称 $a$ 为 $H$ 关于步长 $\lambda$ 的**降算符**。若 $[H, a^\dagger] = +\bar\lambda\, a^\dagger$，则 $a^\dagger$ 为**升算符**。

对 $[H,a]=-\lambda a$ 取厄米共轭，利用 $H^\dagger = H$，立即得 $[H, a^\dagger] = +\bar\lambda\, a^\dagger$。因此**降算符的厄米共轭自动成为升算符**。

### 1.3 伴随映射的视角

对易关系 $[H, a] = -\lambda a$ 有一个更深的数学解读。定义**伴随映射**（adjoint map）：

$$\mathrm{ad}_H : X \longmapsto [H, X],$$

这是算符空间上的一个**线性映射**——它把算符映到算符，而且保持线性：

$$\mathrm{ad}_H(\alpha X + \beta Y) = \alpha\,[H, X] + \beta\,[H, Y].$$

在这个视角下，$[H, a] = -\lambda a$ 就是：

$$\boxed{\mathrm{ad}_H(a) = -\lambda\, a,}$$

即 $a$ 是线性映射 $\mathrm{ad}_H$ 的**特征向量**，$-\lambda$ 是对应的**特征值**。

因此，**寻找升降算符的问题，就是对 $\mathrm{ad}_H$ 这个线性映射做谱分解的问题。**

这个视角统一了前面的所有讨论：

- **零特征值**的特征向量满足 $[H, C] = 0$，即与 $H$ 对易的守恒量。
- **非零特征值**的特征向量就是升降算符，特征值的大小给出步长。
- 在李代数语言中，$\mathrm{ad}_H$ 的特征分解就是**根空间分解**（root space decomposition）：Cartan 元 $H$ 的伴随作用把李代数分解为根空间，根向量就是升降算符，根就是步长。

**例：** 对谐振子，取 $N = a^\dagger a$，在 $\{a,\, a^\dagger,\, N\}$ 张成的空间上：

$$\mathrm{ad}_N(a) = [a^\dagger a,\, a] = -a, \qquad \mathrm{ad}_N(a^\dagger) = [a^\dagger a,\, a^\dagger] = +a^\dagger, \qquad \mathrm{ad}_N(N) = 0.$$

三个算符恰好是 $\mathrm{ad}_N$ 的特征向量，特征值分别为 $-1,\, +1,\, 0$。升降算符并非偶然发现，而是 $\mathrm{ad}_N$ 的特征分解的必然结果。

### 1.4 定理1：本征值移位

**定理1 ** 设 $[H,a] = -\lambda a$，$H|E\rangle = E|E\rangle$。则：

- 若 $a|E\rangle \neq 0$，则 $H(a|E\rangle) = (E-\lambda)(a|E\rangle)$
- 若 $a^\dagger|E\rangle \neq 0$，则 $H(a^\dagger|E\rangle) = (E+\bar\lambda)(a^\dagger|E\rangle)$

**证明：**

$$H(a|E\rangle) = (aH + [H,a])|E\rangle = aH|E\rangle - \lambda a|E\rangle = (E - \lambda)\,a|E\rangle. \quad \blacksquare$$

这说明了升降算符两种等价定义， $[H,a] = -\lambda a$，$a | E \rangle = (E-\lambda) |E\rangle$


### 1.5 谱的截断：为什么升降不能无限进行？

升降算符每施加一次，本征值移动一个步长。但物理系统的谱不可能真的无限延伸——**Hilbert 空间的正定内积**对谱的范围施加了刚性约束。根据截断方式的不同，可分为两类。

**单侧截断（谐振子型）**

对 Heisenberg 代数 $[a, a^\dagger] = 1$，粒子数算符 $\hat{N} = a^\dagger a$ 是**正半定**的：

$$\langle \psi |\hat{N}| \psi \rangle = \langle \psi | a^\dagger a | \psi \rangle = \| a|\psi\rangle \|^2 \geq 0.$$

因此 $\hat{N}$ 的本征值 $n \geq 0$，存在基态 $a|0\rangle = 0$。但升算符方向没有类似约束——$a^\dagger$ 可以无限施加，谱向上无界。

物理上，这对应于谐振子的能量没有上限。代数上，这是因为 Heisenberg 代数没有 Casimir 算符来约束谱的另一侧。

**双侧截断（角动量型）**

对 $\mathfrak{su}(2)$ 代数，Casimir 算符 $\mathbf{L}^2$ 提供了**额外的全局约束**。由于 $L_x^2 + L_y^2$ 是正半定算符：

$$\mathbf{L}^2 - L_z^2 = L_x^2 + L_y^2 \geq 0 \implies m^2\hbar^2 \leq \hbar^2 \ell(\ell+1),$$

因此 $|m| \leq \ell$，$m$ 被**上下同时截断**。存在最高权态 $L_+|\ell,\ell\rangle = 0$ 和最低权态 $L_-|\ell,-\ell\rangle = 0$。

物理上，角动量分量不能超过角动量的总大小。代数上，这是 $\mathfrak{su}(2)$ 作为**紧致**李群的李代数，其有限维不可约表示必然是有限维的——Casimir 值固定后，权（即 $m$ 值）的范围是有限的。

**一般判据**

| 代数类型 | 截断方式 | 关键约束 | 表示维数 |
|----------|----------|----------|----------|
| Heisenberg $[a, a^\dagger]=1$ | 单侧（下界） | $a^\dagger a \geq 0$ | 无穷维 |
| $\mathfrak{su}(2)$：$[L_+,L_-]=2\hbar L_z$ | 双侧 | $\mathbf{L}^2 - L_z^2 \geq 0$ | $2\ell+1$（有限维） |
| $\mathfrak{su}(1,1)$（非紧致） | 单侧（下界） | Casimir 值固定，但谱无上界 | 无穷维 |

> **核心要点**：升降算符的谱是否有界，不取决于升降算符本身，而取决于**代数结构中正定性约束的数量**。一个正定性条件（$a^\dagger a \geq 0$）给出单侧截断；若 Casimir 提供第二个正定性条件（$\mathbf{L}^2 - L_z^2 \geq 0$），则双侧截断，表示变为有限维。

由基态出发递推得第 $n$ 激发态：

$$|n\rangle = \frac{(a^\dagger)^n}{\sqrt{n!}}|0\rangle, \qquad E_n = E_0 + n\lambda.$$

### 1.6 因式分解法：系统构造 $a$

将 $H$ 写成

$$H = a^\dagger a + \varepsilon_0,$$

则 $[H, a] = [a^\dagger a, a] = [a^\dagger, a] a$。

只要 $[a^\dagger, a] = -1$（Heisenberg 代数），即得 $[H, a] = -a$，步长 $\lambda = 1$（乘以能量量纲后为 $\hbar\omega$ 等）。

构造的核心任务因此变为：**找一对 $(a, a^\dagger)$ 使得 $a^\dagger a \approx H - \varepsilon_0$ 且 $[a, a^\dagger]$ 是常数**。

---

## 2. 应用一：一维谐振子

### 2.1 哈密顿量与因式分解动机

$$H = \frac{p^2}{2m} + \frac{1}{2}m\omega^2 x^2.$$

这是 $\frac{p^2}{2m} + \frac{m\omega^2 x^2}{2}$ 两个平方之和。经典情形 $A^2 + B^2 = (A+iB)(A-iB)$，但 $[x,p] = i\hbar \neq 0$，因式分解产生余项。令：

$$a \equiv \sqrt{\frac{m\omega}{2\hbar}}\,x + \frac{i}{\sqrt{2m\omega\hbar}}\,p, \qquad
a^\dagger \equiv \sqrt{\frac{m\omega}{2\hbar}}\,x - \frac{i}{\sqrt{2m\omega\hbar}}\,p.$$

### 2.2 推导对易关系

利用 $[x,p] = i\hbar$，$[x,x]=[p,p]=0$：

$$[a,\, a^\dagger]
= \frac{m\omega}{2\hbar} \cdot 0
- \frac{i}{\sqrt{2m\omega\hbar}} \cdot \sqrt{\frac{m\omega}{2\hbar}} [x,p]
+ \frac{i}{\sqrt{2m\omega\hbar}} \cdot \sqrt{\frac{m\omega}{2\hbar}} [p,x]
= \frac{-i(i\hbar)}{2\hbar} + \frac{i(-i\hbar)}{2\hbar} = \frac{1}{2} + \frac{1}{2} = 1.$$

$$\boxed{[a,\, a^\dagger] = 1.}$$

### 2.3 将 $H$ 用 $a, a^\dagger$ 表示

计算 $a^\dagger a$，利用 $[p,x] = -i\hbar$ 处理交叉项：

$$a^\dagger a = \frac{m\omega}{2\hbar}x^2 + \frac{p^2}{2m\omega\hbar} + \frac{i}{2\hbar}[p,x] \cdot (-1)
= \frac{H}{\hbar\omega} - \frac{1}{2}.$$

因此：

$$\boxed{H = \hbar\omega\!\left(a^\dagger a + \frac{1}{2}\right) \equiv \hbar\omega\!\left(\hat{N} + \frac{1}{2}\right).}$$

粒子数算符 $\hat{N} \equiv a^\dagger a$ 满足 $\hat{N}|n\rangle = n|n\rangle$。

### 2.4 谱

$$[H,\, a] = \hbar\omega\,[a^\dagger a,\, a] = \hbar\omega\,(-1)\,a = -\hbar\omega\, a. \quad \text{步长} = \hbar\omega.$$

基态能量（由 $a|0\rangle=0$ 得 $\hat{N}|0\rangle=0$）：

$$E_0 = \frac{1}{2}\hbar\omega.$$

第 $n$ 激发态：

$$|n\rangle = \frac{(a^\dagger)^n}{\sqrt{n!}}|0\rangle, \qquad E_n = \hbar\omega\!\left(n + \frac{1}{2}\right), \qquad n = 0, 1, 2, \ldots$$

矩阵元（由 $[a,a^\dagger]=1$ 和归一化递推）：

$$a|n\rangle = \sqrt{n}\,|n-1\rangle, \qquad a^\dagger|n\rangle = \sqrt{n+1}\,|n+1\rangle.$$

---

## 3. 应用二：角动量

### 3.1 角动量代数

角动量算符 $(L_x, L_y, L_z)$ 满足（旋转群 $\mathrm{SO}(3)$ 的李代数）：

$$[L_i,\, L_j] = i\hbar\,\varepsilon_{ijk}\,L_k.$$

目标：同时对角化 $\mathbf{L}^2 = L_x^2+L_y^2+L_z^2$ 和 $L_z$（两者对易，可共同对角化）。

### 3.2 构造升降算符

希望找算符满足 $[L_z, L_\pm] = \pm c \cdot L_\pm$。取 $L_x, L_y$ 的复线性组合（将实李代数 $\mathfrak{su}(2)$ 复化）：

$$L_+ \equiv L_x + iL_y, \qquad L_- \equiv L_x - iL_y = (L_+)^\dagger.$$

验证：

$$[L_z,\, L_\pm] = [L_z, L_x] \pm i[L_z, L_y] = i\hbar L_y \pm i(-i\hbar L_x) = \pm\hbar(L_x \pm iL_y) = \pm\hbar L_\pm.$$

$$\boxed{[L_z,\, L_\pm] = \pm\hbar\, L_\pm.} \qquad \text{步长} = \pm\hbar.$$

此外：

$$[L_+, L_-] = 2\hbar L_z, \qquad [\mathbf{L}^2,\, L_\pm] = 0.$$

第二式保证 $L_\pm$ 不改变 $\mathbf{L}^2$ 的本征值。

### 3.3 谱的推导

设 $\mathbf{L}^2|\ell,m\rangle = \lambda|\ell,m\rangle$，$L_z|\ell,m\rangle = m\hbar|\ell,m\rangle$。

**步骤一：上下界。** $\mathbf{L}^2 - L_z^2 = L_x^2 + L_y^2 \geq 0$，故 $\lambda \geq m^2\hbar^2$，$m$ 有界。设最大值为 $\ell$：

$$L_+|\ell, \ell\rangle = 0.$$

**步骤二：确定 $\lambda$。** 利用 $L_- L_+ = \mathbf{L}^2 - L_z^2 - \hbar L_z$ 作用在 $|\ell,\ell\rangle$ 上：

$$0 = (\lambda - \ell^2\hbar^2 - \ell\hbar^2)|\ell,\ell\rangle \implies \lambda = \hbar^2\ell(\ell+1).$$

**步骤三：量子化。** 最小值为 $m_{\min} = -\ell$，从 $\ell$ 到 $-\ell$ 步数为整数，故 $2\ell \in \mathbb{Z}_{\geq 0}$：

$$\ell = 0,\,\tfrac{1}{2},\,1,\,\tfrac{3}{2},\,2,\,\ldots$$

**最终结果：**

$$\mathbf{L}^2|\ell,m\rangle = \hbar^2\ell(\ell+1)|\ell,m\rangle, \qquad L_z|\ell,m\rangle = m\hbar|\ell,m\rangle,$$

$$L_\pm|\ell,m\rangle = \hbar\sqrt{\ell(\ell+1)-m(m\pm1)}\;|\ell,m\pm1\rangle,$$

其中 $m \in \{-\ell,\,-\ell+1,\,\ldots,\,\ell\}$，共 $2\ell+1$ 个本征态。

---

## 4. 两个应用的对比

|  | 谐振子 | 角动量 |
|--|--------|--------|
| 被对角化的算符 | $H$ | $L_z$（在 $\mathbf{L}^2$ 本征空间内） |
| 构造出发点 | 因式分解 $H = a^\dagger a + \varepsilon_0$ | 复化 $L_\pm = L_x \pm iL_y$ |
| 关键对易关系 | $[a, a^\dagger] = 1$ | $[L_z, L_\pm] = \pm\hbar L_\pm$ |
| 步长 | $\hbar\omega$（能量） | $\hbar$（$L_z$ 本征值） |
| 谱的截断 | 单侧（$a\vert 0\rangle = 0$，无上界） | 双侧（$m \in [-\ell, \ell]$，有限个） |
| 代数背景 | Heisenberg 代数 $[a,a^\dagger]=1$ | $\mathfrak{su}(2)$ 李代数 |

---

## 5. 总结：一般构造流程

1. **选目标算符**：确定要对角化的 $H$（或 $L_z$ 等），观察谱是否有等间距或规则步进结构。
2. **写候选形式**：对因式分解型系统，试 $a = \alpha x + \beta p$；对李代数型系统，取实生成元的复线性组合。
3. **计算 $[H,a]$**：要求结果正比于 $a$，由此反解系数。
4. **建立截断条件**：利用物理约束（能量下界、模方非负）确定基态或边界态，量子化谱。
5. **递推归一化**：由 $\langle n|n\rangle = 1$ 和对易关系得 $a|n\rangle$、$a^\dagger|n\rangle$ 的精确矩阵元。

> **核心洞察**：本征值的等间距结构 $\Longleftrightarrow$ 某个对易子等于算符本身，即 $[H, a] = -\lambda a$。这是量子力学代数方法的基石，也是从矩阵力学推广到无穷维算符代数的桥梁。
