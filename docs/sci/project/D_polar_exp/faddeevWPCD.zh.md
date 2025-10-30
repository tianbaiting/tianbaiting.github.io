Wave-packet continuum discretisation for nucleon–nucleon scattering predictions
Nucleon-Nucleon Scattering in a Wave-Packet Formalism
Neutron-deuteron scattering cross sections with chiral NN interactions using wave-packet continuum discretization
Approximating the Three-Nucleon Continuum -Solving the Faddeev equations for statistical inference of chiral forces
Posterior predictive distributions of neutron-deuteron cross sections


https://doi.org/10.1088/1361-6471/ac3cfd

https://doi.org/10.1103/physrevc.106.024001

https://doi.org/10.1103/physrevc.107.014002

https://research.chalmers.se/publication/517065/file/517065_Fulltext.pdf

https://research.chalmers.se/publication/532218/file/532218_Fulltext.pdf


两篇学位论文  和 三篇期刊论文。这五篇论文的核心，就是用一种更“聪明”的计算技巧，即**波包连续谱离散化 (WPCD)**，来解决一个在数值上极其棘手的问题——Faddeev方程。

我会从QM出发，逐步解释为什么需要Faddeev方程，为什么它这么难算，以及"Tic-tac"（这些论文中开发的程序）是如何用 WPCD 方法巧妙解决这个问题的。

### 1. 问题的起点：从薛定谔方程到散射

用薛定谔方程 $H|\psi\rangle = E|\psi\rangle$ 来描述一个系统。对于散射问题，$\hat{H} = \hat{H}_0 + \hat{v}$，其中 $\hat{H}_0$ 是自由粒子的动能，$\hat{v}$ 是相互作用势。

**难题 (Resolvent 登场):**
对于散射问题，我们更关心的是末态 $|\psi^+\rangle$（散射后的状态）与初态 $|\phi\rangle$（自由粒子状态）的联系。

1.  我们可以把薛定谔方程 $(E - \hat{H}_0)|\psi^+\rangle = \hat{v}|\psi^+\rangle$ 变形。
2.  在数学上，我们可以“除以” $(E - \hat{H}_0)$，得到一个积分方程，这就是 **Lippmann-Schwinger (LS) 方程** 。
3.  这个方程里会出现一个算符 $\hat{G}_0(E) = (E - \hat{H}_0)^{-1}$ 。这个 $\hat{G}_0(E)$ 就是**自由 resolvent (解算子)**。它本质上只是一个数学工具，用来描述自由粒子如何在能量为 $E$ 时从一个地方传播到另一个地方。

这个方程求解的是**T-matrix (T矩阵)**。T矩阵直接告诉我们从初态散射到末态的概率幅。

---

### 2. 为什么需要 Faddeev 方程？(三体问题)

**难题 (LS 方程的失效):**
LS 方程对于两个粒子（比如 n-p 散射）的散射问题处理得很好。但当你试图用它来解决三个粒子（比如 n-d 散射）的问题时，这个方程在数学上会**失效** 。它的积分核“不够紧凑”，导致方程没有唯一的解 。

**Faddeev 的解决方案:**
L. Faddeev 在1960年提出，不能直接求解总的 T 矩阵，而是必须把它拆成三个部分 $T = T_1 + T_2 + T_3$。然后，他推导出了一组**耦合的积分方程**来分别求解这三个部分。这就是 **Faddeev 方程** 。

在实际计算中，我们常用的是它的一个等价形式，称为 **AGS 方程** (Alt, Grassberger, Sandhas 提出)。这些论文中的 "Tic-tac" 程序就是为了求解 AGS 方程而编写的 。

AGS 方程的形式可以抽象地写成： $\hat{U} = \hat{A} + \hat{K} \times \hat{U}$ 。
这里 $\hat{U}$ 是我们想求的跃迁算符（它与T矩阵相关），$\hat{A}$ 是驱动项（已知），$\hat{K}$ 是一个复杂的积分“核”。

---

### 3. 如何在数值上解它？(表象的选择)

**难题 (从算符到矩阵):**
$\hat{U} = \hat{A} + \hat{K} \times \hat{U}$ 是一个算符方程。要在计算机上解它，我们必须选择一个**基底（表象）**，把它变成一个巨大的矩阵方程：$\mathbf{U} = \mathbf{A} + \mathbf{K} \mathbf{U}$ 。

**传统方法 (MI - 矩阵求逆):**

1.  **选择基底：**
    * **动量表象：** 因为散射问题在动量空间中更简洁，所以我们通常选择动量基底。对于三体问题，这需要两个动量：粒子对的内部相对动量 $p$ 和第三个粒子相对于该粒子对的动量 $q$ 。
    * **分波展开：** 为了进一步简化，我们使用“分波表象”。由于核力基本不破坏总角动量 $J$，我们可以把问题分解成一块一块的，每一块对应一个特定的总角动量 $J$ 和宇称 $\Pi$ 。
2.  **离散化：**
    * 动量 $p$ 和 $q$ 是连续的，这使得矩阵无限大。传统方法使用**高斯积分 (Gaussian Quadrature)**，用有限个（例如 $N_p=30, N_q=40$ 个）离散的动量点来近似连续的积分。
3.  **求解：**
    * 这样，我们就得到了一个 (非常大，但有限) 的矩阵方程 $\mathbf{U} = \mathbf{A} + \mathbf{K} \mathbf{U}$。
    * 我们可以把它写成 $(\mathbf{I} - \mathbf{K})\mathbf{U} = \mathbf{A}$，然后通过**矩阵求逆 (MI)** 来解出 $\mathbf{U}$ 。

**传统方法的致命缺陷：**
这个方法极其困难，主要有两个原因：

1.  **移动奇异点 (Singularities):** 积分核 $\mathbf{K}$ 中包含了 $\hat{G}_0(E)$。$\hat{G}_0$ 在 $E=E_0$ 处有奇点（极点）。在三体问题中，这个奇点的位置会随着积分动量 $p, q$ 的变化而“移动”，这在数值处理上是公认的噩梦。
2.  **计算成本：** 你必须为**每一个**你感兴趣的散射能量 $E$ 重新构建和求解一次这个巨大的矩阵方程。 如果想得到一条散射截面曲线（包含几百个能量点），计算量将是灾难性的。

---

### 4. Tic-tac 和 WPCD 方法如何解决这个问题

Tic-tac 程序使用了一种完全不同的基底——**波包连续谱离散化 (WPCD)** 基底——来绕开上述所有难题。

**WPCD 的核心思想：**

1.  **改变基底：**
    * 我们不再使用单个动量 $p$ 作为基底，而是使用“**波包**” $|x_i\rangle$ 。
    * 一个波包 $|x_i\rangle$ 并不代表一个精确的动量，而是代表一个动量**区间**或“**bin**”（例如，从 $k_i$ 到 $k_{i+1}$ 的所有动量）。
    * 这就像是用一堆直方图的“柱子”来近似连续的动量谱。

2.  **改变方程 (关键一步)：**
    * WPCD 不使用 $\hat{G}_0$（自由解算子），而是巧妙地转向使用 $\hat{G} = (E - \hat{H})^{-1}$（**全解算子**）。
    * **怎么做到？** 在三体问题中，Faddeev 方程的核心是**两体 T 矩阵**（描述两个粒子在第三个粒子旁观下的散射）。
    * Tic-tac 首先在 WPCD 基底下求解**两体问题** ($H_2|\psi\rangle = E_2|\psi\rangle$)。在离散的波包基底下，这变成了一个标准的**矩阵对角化**问题。
    * 对角化得到的本征态 $|z_i\rangle$ 被称为“**散射波包**”(SWPs)。这个 SWP 基底 $\left\{|z_i\rangle\right\}$ **构成了一个 $\hat{H}_2$ 的近似本征基底**。

3.  **Faddeev (AGS) 方程的 WPCD 形式：**
    * Tic-tac 在这个“聪明”的 **SWP 基底**上求解 AGS 方程。
    * 方程 $\hat{U} = \hat{A} + \hat{K} \times \hat{U}$ 变成了 $\mathbf{U} = \mathbf{A} + \mathbf{A}\mathbf{G}(E)\mathbf{U}$ 。

**WPCD 带来的巨大优势：**

1.  **奇点消失了：** 在这个基底下，所有的奇点都被解析地（即用公式）处理掉了，或者说被“平均掉”了。计算中不再有奇点问题。
2.  **能量依赖性被分离：**
    * 在 $\mathbf{U} = \mathbf{A} + \mathbf{A}\mathbf{G}(E)\mathbf{U}$ 中，那个巨大的、最难计算的矩阵 $\mathbf{A}$（它包含了所有的核力 $\hat{v}$ 和复杂的置换算符 $\hat{P}$）被证明是**完全不依赖于能量 $E$ 的**。
    * 所有的能量 $E$ 依赖性现在都跑到了 $\mathbf{G}(E)$ 矩阵里。
    * 更妙的是，在 SWP 基底下，$\mathbf{G}(E)$ 是一个**对角矩阵**！它的对角元只是简单的数字 $(E - \epsilon_i)^{-1}$（其中 $\epsilon_i$ 是 SWP 的本征能量）。

**Tic-tac 的最终解法：**

* **问题：** 尽管 $\mathbf{A}$ 不依赖能量，但它太大了（例如 $72000 \times 72000$），根本无法完整存入内存，所以不能用“矩阵求逆”。
* **求解 $\mathbf{U}$：** Tic-tac 使用 **Neumann 级数** (迭代法) 来求解：
    $\mathbf{U} = \mathbf{A} + \mathbf{A}\mathbf{G}(E)\mathbf{A} + \mathbf{A}\mathbf{G}(E)\mathbf{A}\mathbf{G}(E)\mathbf{A} + ...$
    这个过程只需要重复进行矩阵-向量乘法，可以“分段”计算，不需要一次性加载整个 $\mathbf{A}$。
* **收敛问题：** 对于核力，这个级数是**发散的**。
* **最终技巧 (Padé)：** Tic-tac 会先计算这个发散级数的前 20-30 项，然后使用一种叫做 **Padé 近似 (Padé approximant)** 的数学工具，对这个发散级数进行“求和”，从而得到收敛的、正确的物理结果。

### 总结

1.  **传统方法 (MI):**
    * 基底：动量分波基底。
    * 求解：在每个能量 $E$ 点，用积分格点离散化，然后求解一个 $(\mathbf{I} - \mathbf{K})\mathbf{U} = \mathbf{A}$ 矩阵方程。
    * 困难：必须处理奇异点，且**每个能量点都要重算一次**。

2.  **Tic-tac (WPCD):**
    * 基底：波包基底 (WPCD)，并对角化两体问题得到 SWP 基底。
    * 求解：在 SWP 基底下，方程变为 $\mathbf{U} = \mathbf{A} + \mathbf{A}\mathbf{G}(E)\mathbf{U}$。
    * 优势：
        1.  奇异点被解析处理。
        2.  能量依赖性被分离到一个简单的对角矩阵 $\mathbf{G}(E)$ 中。
        3.  **“一次计算，所有能量”**：最耗时的 $\mathbf{A}$ 矩阵计算**只需进行一次**。之后想要求解任意能量 $E$ 的 $\mathbf{U}$，只需要把不同的 $\mathbf{G}(E)$ 代入迭代求解即可。 这就是 WPCD 方法的“内在并行性”。
    * 求解技巧：由于 $\mathbf{A}$ 矩阵太大，使用 Neumann 级数 + Padé 近似来迭代求解。
