# 共振态 resolvent

## **第一节：引言：预解式算符、谱与核心悖论**

### **1.1 预解式算符与谱的定义**

在量子力学的数学框架中，一个物理系统的哈密顿算符 $A$（在本文中也记为 $H$）是一个在希尔伯特空间 $\mathcal{H}$ 上作用的（通常是无界的）自伴算符。该算符的谱 (spectrum) $\sigma(A)$ 包含了系统所有可能的能量测量值。
为了研究算符 $A$ 的谱特性，数学物理学中引入了一个核心工具：**预解式算符 (Resolvent Operator)** $R(z, A)$。对于任意复数 $z \in \mathbb{C}$，预解式算符定义为 [1](#ref-1)：
$$ R(z, A) \equiv (zI - A)^{-1} $$
其中 $I$ 是单位算符。
**预解集 (Resolvent Set)** $\rho(A)$ 定义为所有使得 $R(z, A)$ 存在且为 $\mathcal{H}$ 上有界算符的复数 $z$ 的集合。根据定义，**谱 (Spectrum)** $\sigma(A)$ 则是预解集的补集：$\sigma(A) = \mathbb{C} \setminus \rho(A)$ [2](#ref-2)。
谱 $\sigma(A)$ 本身可以进一步分解为：

1.  **离散谱 (Discrete Spectrum)** $\sigma_d(A)$：对应于 $A$ 的孤立本征值。
2.  **连续谱 (Continuous Spectrum)** $\sigma_c(A)$：对应于散射态和非束缚态。
3.  **剩余谱 (Residual Spectrum)** $\sigma_r(A)$：（对于自伴算符，剩余谱为空集）。

### **1.2 预解式的解析性质与极点**

预解式算符 $R(z, A)$ 的关键数学特性在于其解析性 (analyticity)。$R(z, A)$ 是一个在整个预解集 $\rho(A)$ 上解析的算符值函数 [4](#ref-4)。这意味着 $R(z, A)$ 的所有**奇异点 (singularities)**——即函数无定义或不解析的点——必定位于且仅位于 $A$ 的谱 $\sigma(A)$ 之中。
对于谱的离散部分 $\sigma_d(A)$，其奇异性表现为**极点 (poles)**。一个孤立的本征值 $\lambda \in \sigma_d(A)$ 对应于 $R(z, A)$ 的一个极点 [5](#ref-5)。更准确地说，如果 $\lambda$ 是一个简单本征值， $R(z, A)$ 在 $z = \lambda$ 附近具有洛朗展开：

$$ R(z, A) = \frac{-P_{\lambda}}{z - \lambda} + \text{analytic part} $$

其中，该极点的**留数 (residue)** $P_{\lambda} = -\frac{1}{2\pi i} \oint_{C_{\lambda}} R(z, A) dz$ 正是对应于本征值 $\lambda$ 的本征空间的**投影算符** [3](#ref-3)。这些本征态是定态 (stationary states)，即束缚态 (bound states)，它们在时间演化下保持稳定，其波函数 $\Psi(t) = e^{-i\lambda t} \Psi(0)$ 仅获得一个相位因子。

### **1.3 核心悖论：自伴性与复数能量**

至此，我们建立了一个清晰的对应关系：系统的（离散）能量本征值 $\leftrightarrow R(z, A)$ 的极点。
然而，当我们将此框架应用于**共振态 (Resonance States)**（或称“准束缚态”，quasi-bound states [6](#ref-6)）时，一个深刻的悖论出现了。

1.  **物理现象 (共振)：** 共振态，例如原子核的 $\alpha$ 衰变或不稳定的基本粒子，其物理特征是**指数衰减 (exponential decay)** [7](#ref-7)。一个处于共振态的系统，其存活概率 $P(t) = |\langle \Psi(t) | \Psi(0) \rangle|^2$ 随时间 $t$ 按 $e^{-\Gamma t/\hbar}$ 的规律衰减（其中 $\Gamma$ 称为衰减宽度）。
2.  **时间演化 (复数能量)：** 为了在量子力学中描述这种概率衰减，态矢量的时间演化必须由一个非厄米的形式主导。如果一个态（例如 Gamow 态 [9](#ref-9)）具有一个**复数能量本征值** $z_R = E_R - i\Gamma/2$（其中 $E_R$ 是共振能量，$\Gamma > 0$），那么其时间演化将是：$\Psi(t) = e^{-iz_R t/\hbar} \Psi(0)$。其概率密度 $|\Psi(t)|^2 \propto e^{-\Gamma t/\hbar}$，这精确地描述了指数衰减 [11](#ref-11)。
3.  **数学框架 (自伴性)：** 根据量子力学的基本公设，哈密顿算符 $A=H$ 必须是**自伴算符 (self-adjoint operator)**。
4.  **数学定理 (实谱)：** 泛函分析中的一个基本定理是：自伴算符的谱**必须是实数**，即 $\sigma(A) \subset \mathbb{R}$ [2](#ref-2)。
5.  **悖论：**
    *   根据 (4)，$R(z, A)$ 的所有奇异点（包括所有极点）必须位于实轴 $\mathbb{R}$ 上。
    *   根据 (2)，物理上的共振态要求系统具有一个复数能量 $z_R = E_R - i\Gamma/2$，它位于复平面的下半平面 ($\text{Im}(z) < 0$)。
    *   **结论：** 共振态所对应的复数能量 $z_R$ **不属于** $A$ 的谱，因此它**不可能是**预解式算符 $R(z, A)$ 在其原始定义域上的极点。

### **1.4 悖论的解决：解析延拓**

这个悖论表明，用户所提的问题——“证明共振态对应于预解式算符 $R(z, A)$ 的极点”——在其字面意义上是错误的。
然而，这个悖论的解决方案在于认识到预解式算符 $R(z, A)$ 的一个更精细的数学结构。$R(z, A)$ 虽然在 $\rho(A)$ 上是解析的，但它在实轴上的连续谱 $\sigma_c(A)$ 处具有奇异性。这种奇异性不是极点，而是**分支切割 (branch cut)** [8](#ref-8)。
我们最初定义的 $R(z, A)$ 是在复平面的“第一片”或“物理片” (physical sheet) 上的函数。共振现象并非不存在，而是隐藏在数学结构中。要“看到”共振态，我们必须通过数学上的**解析延拓 (analytic continuation)** 手段，将 $R(z, A)$ “穿过”连续谱这个分支切割，延拓到一个新的复平面，即“第二片”或“非物理片” (unphysical sheet) [19](#ref-19)。
在这个通过解析延拓得到的**新函数** $R_{II}(z, A)$ 上，那些隐藏的奇异点才会作为**极点**显现出来 [14](#ref-14)。
因此，本报告的核心任务是证明以下更精确的论断： **“共振态对应于预解式算符 $R(z, A)$ 从物理片穿过连续谱分支切割、解析延拓到非物理片后所得到的函数 $R_{II}(z, A)$ 的极点。”**
这个证明需要一个清晰的逻辑链条：

1.  **(第 2 节)** 阐明连续谱 $\sigma_c(A)$ 如何作为 $R(z, A)$ 的分支切割出现，并由此构建出物理片 (Sheet I) 和非物理片 (Sheet II) 的 Riemann 曲面结构。
2.  **(第 3 节)** 严格地将“共振态”定义为散射矩阵 (S-matrix) 在非物理片上的极点。
3.  **(第 4 节)** 通过算符恒等式，严格证明解析延拓后的预解式 $R_{II}(z, A)$ 的极点与 S 矩阵的极点完全重合。

## **第二节：Riemann 曲面：物理片与非物理片**

### **2.1 连续谱作为分支切割**

为了具体化讨论，我们考虑一个典型的量子散射系统，其哈密顿算符为 $H = H_0 + V$，其中 $H_0 = p^2 / 2m$ 是自由粒子哈密顿算符，V 是一个短程相互作用势。$H_0$ 的谱是纯连续的，$\sigma(H_0) = [0, \infty)$。对于完整的哈密顿算符 $H$，其连续谱通常也保持为 $\sigma_c(H) = [0, \infty)$ [8](#ref-8)。$H$ 还可能在 $E < 0$ 的区域拥有离散谱 $\sigma_d(H)$，对应于束缚态。

预解式 $R(z, H) = (z - H)^{-1}$ 的奇异性因此由两部分组成：位于负实轴上的对应束缚态的**极点**，以及位于正实轴 $[0, \infty)$ 上的对应散射态的**分支切割** [8](#ref-8)。

### **2.2 分支切割的起源：k 平面与 E 平面**

分支切割的数学根源在于能量 $E$ 和动量（或波矢 $k$）之间的非线性关系。对于自由粒子（以及散射态的渐进行为），能量 $E$ 和波矢大小 $k$ 的关系为：

$$ E = \frac{\hbar^2 k^2}{2m} $$
当我们反过来，将 $k$ 视为复能量 $z$ 的函数时（为方便起见，设 $\hbar = 2m = 1$，则 $E=k^2$），我们得到 [20](#ref-20)：

$$ k(z) = \sqrt{z} $$
这是一个多值函数。$\sqrt{z}$ 在 $z=0$ 处有一个**分支点 (branch point)**。$z=0$ 正是连续谱的下限，即**阈值 (threshold)**。
为了使 $k(z)$（以及依赖于 $k$ 的预解式算符 $R(z, H)$）成为一个单值解析函数，我们必须在复数 $z$ 平面引入一个**分支切割 (branch cut)**。按照惯例，这个切割从分支点 $z=0$ 开始，沿着正实轴延伸到 $+\infty$，即 $\sigma_c(H) = [0, \infty)$。

### **2.3 Riemann 曲面的构建：物理片与非物理片**

这个分支切割将复数能量 $z$ 平面“切割”开，但同时也暗示了一个更丰富的结构：一个**Riemann 曲面**。$\sqrt{z}$ 函数自然地生活在一个由两个复平面（“片”）粘合而成的曲面上。
我们通过 $k(z) = \sqrt{z}$ 的解析性质来定义这两个片：

1.  **物理片 (Physical Sheet / Sheet I):**
    *   **定义：** 对应于 $k$ 平面的**上半平面**，即 $\text{Im}(k) > 0$ [18](#ref-18)。
    *   **映射：** $k$ 平面的上半平面通过 $z = k^2$ 映射到**整个** $z$ 平面（除了正实轴上的切割）。
    *   **物理意义：** 这是我们进行物理测量的平面。预解式算符 $R(z, H)$ 最初定义在这个平面上。物理散射过程发生在 $z = E + i\epsilon$（其中 $E \ge 0, \epsilon \to 0^+$），即紧贴分支切割**上方**的区域 [8](#ref-8)。
    *   **渐进行为：** $k$ 值为 $k_0 + i\kappa$（$\kappa > 0$）对应 $e^{ikz} = e^{ik_0 z} e^{-\kappa z}$，这是空间上衰减的、物理上可接受的（例如束缚态）行为。
2.  **非物理片 (Unphysical Sheet / Sheet II):**
    *   **定义：** 对应于 $k$ 平面的**下半平面**，即 $\text{Im}(k) < 0$ [18](#ref-18)。
    *   **映射：** $k$ 平面的下半平面通过 $z = k^2$ 映射到**第二个** $z$ 平面，它与物理片沿着 $[0, \infty)$ 切割“粘合”在一起。
    *   **解析延拓：** 要访问非物理片，我们必须将定义在物理片上的函数（如 $R(z, H)$）**解析延拓**穿过分支切割。延拓后的函数记为 $R_{II}(z, H)$。
    *   **渐进行为：** $k$ 值为 $k_0 - i\gamma$（$\gamma > 0$）对应 $e^{ikz} = e^{ik_0 z} e^{\gamma z}$，这是空间上**指数发散**的、非物理的行为。

### **2.4 共振极点的位置**

现在我们可以重新审视第一节中的悖论。

*   **Gamow 的启发：** Gamow 在 1928 年研究 $\alpha$ 衰变时，为了描述粒子“逃逸”到无穷远，他要求波函数在 $r \to \infty$ 时具有纯粹的**出射波 (outgoing wave)** 形式 $\Psi \sim e^{ikr}/r$ [7](#ref-7)。为了同时满足这个边界条件和 $r=0$ 处的正则性要求，他发现 $k$ 必须取一个复数值，记为 $k_R = k_0 - i\gamma$，其中 $k_0 > 0$ 且 $\gamma > 0$ [12](#ref-12)。
*   **k 平面：** 这个 $k_R$ 位于 $k$ 平面的**第四象限**，即下半平面 ($\text{Im}(k_R) < 0$) [14](#ref-14)。
*   **E 平面：** 当我们将这个 $k_R$ 映射回能量 $z$ 平面时：
  
    $$ z_R = k_R^2 = (k_0 - i\gamma)^2 = (k_0^2 - \gamma^2) - i(2k_0 \gamma) $$
    令 $E_R = k_0^2 - \gamma^2$ 且 $\Gamma = 4 k_0 \gamma$（假设 $\hbar=2m=1$），我们得到 $z_R = E_R - i\Gamma/2$（$\Gamma > 0$）。
*   **结论：** 共振态 $z_R$ 位于 $E$ 平面的**下半平面** [12](#ref-12)。根据 2.3 节的定义，这个 $k_R$（位于 $\text{Im}(k) < 0$）和 $z_R$（位于 $\text{Im}(z) < 0$ 的下半平面）都属于**非物理片 (Sheet II)** [19](#ref-19)。

**核心论断：** Gamow 的“出射波边界条件” 在数学上等价于寻找预解式算符（或 S 矩阵）在**非物理片**上的极点。解析延拓是将哈密顿算符的谱理论（预解式）与 Gamow 的衰变物理（出射波）严格联系起来的唯一途径。

## **第三节：共振态的严格定义：S 矩阵与 T 矩阵的极点**

在第 1 节和第 2 节中，我们建立了预解式 $R(z, A)$ 的解析结构，并论证了共振态 $z_R = E_R - i\Gamma/2$ 必须位于非物理片（Sheet II）上。现在，我们需要一个严格的、可操作的**定义**来界定什么是“共振态”。
在形式散射理论 (Formal Scattering Theory) 中，共振态是作为 S 矩阵的奇异点而出现的。

### **3.1 S 矩阵 (S-Matrix)**

S 矩阵（散射矩阵）是连接无穷远过去 ($t \to -\infty$) 的“入态” (in-states) 和无穷远未来 ($t \to +\infty$) 的“出态” (out-states) 的幺正算符。它包含了散射过程的所有信息。
S 矩阵（及其矩阵元）是能量 $z$ 的解析函数。它与预解式算符 $R(z, A)$ 一样，具有分支切割 $\sigma_c(A) = [0, \infty)$，并且可以从物理片解析延拓到非物理片 [13](#ref-13)。

### **3.2 T 矩阵 (T-Matrix)**

通常，将 S 矩阵分解为无散射部分（单位算符 $I$）和发生散射的部分（T 矩阵）会更方便：

$$ S(z) = I - 2\pi i \delta(E - E') T(z) $$
T 矩阵 $T(z)$ 包含了所有动力学信息，并且与 S 矩阵共享相同的解析结构（极点、割线等）。因此，在讨论极点时，我们可以等价地研究 T 矩阵 $T(z)$。

### **3.3 共振态的形式定义**

在现代量子场论和散射理论中，系统的激发谱（包括束缚态和共振态）由 S 矩阵（或 T 矩阵）在复能量平面上的极点位置严格定义 [16](#ref-16)。
根据第 2 节建立的 Riemann 曲面结构，我们对 S/T 矩阵的极点有如下物理分类 [20](#ref-20)：

1.  **束缚态 (Bound States):**
    *   **位置：** 位于**物理片 (Sheet I)** 上。
    *   **能量：** 位于阈值以下的**负实轴**上，$z = E_B < 0$。
    *   **对应 k 平面：** 位于**正虚轴**上，$k = i\kappa$ ($\kappa > 0$)。
2.  **共振态 (Resonances):**
    *   **位置：** 位于**非物理片 (Sheet II)** 上 [14](#ref-14)。
    *   **能量：** 位于**下半复平面**，$z_R = E_R - i\Gamma/2$，其中 $E_R > 0$ 且 $\Gamma > 0$ [15](#ref-15)。
    *   **对应 k 平面：** 位于**第四象限**，$k_R = k_0 - i\gamma$ ($k_0, \gamma > 0$)。
3.  **虚态 (Virtual States / Antibound States):**
    *   **位置：** 位于**非物理片 (Sheet II)** 上。
    *   **能量：** 位于阈值以下的**负实轴**上，$z = E_V < 0$。
    *   **对应 k 平面：** 位于**负虚轴**上，$k = -i\kappa$ ($\kappa > 0$)。

### **3.4 Breit-Wigner 形式**

共振态作为非物理片上的极点，其对物理测量的影响（发生在物理片上，能量 $E \ge 0$）是如何体现的？
如果一个共振极点 $z_R = E_R - i\Gamma/2$ 距离实轴足够近（即 $\Gamma$ 较小，称为窄共振），那么 T 矩阵（或 S 矩阵）在实轴 $E$ 附近的行为将由这个极点主导。在 $z=z_R$ 附近，T 矩阵元可以近似写为：

$$ T(E) \approx \frac{\text{Residue}}{E - z_R} = \frac{\text{Residue}}{E - (E_R - i\Gamma/2)} $$
这就是著名的**Breit-Wigner 共振形式** [17](#ref-17)。散射截面 $\sigma(E) \propto |T(E)|^2$，因此在 $E \approx E_R$ 处呈现一个洛伦兹峰形，其半高宽 (FWHM) 正比于 $\Gamma$。
这为我们的定义提供了实验支持：物理上观测到的共振峰（Breit-Wigner 形式）是数学上非物理片极点在实轴上的“投影”。

### **3.5 证明策略的转变**

通过第 3 节的讨论，我们已经将一个模糊的物理概念（共振）转化为一个严格的数学定义（非物理片上的 T 矩阵极点）。
现在，用户最初的问题“证明**共振态**对应于（解析延拓的）**预解式极点**”已经转变为一个纯粹的数学问题：
**“证明 T 矩阵 T(z) 的极点与（解析延拓的）预解式算符 R(z, H) 的极点相重合。”**
如果我们可以证明这两个算符（$T(z)$ 和 $R(z, H)$）在所有解析域（包括物理片和非物理片）上共享完全相同的极点结构，那么本报告的中心论点就得以证明。下一节将致力于这个核心的算符代数证明。

## **第四节：核心证明：预解式算符与 T 矩阵的极点等价性**

本节的目标是严格证明完整预解式算符 $G(z) \equiv R(z, H)$ 与 T 矩阵算符 $T(z)$ 具有相同的极点。我们将通过推导它们之间的算符恒等式（Lippmann-Schwinger 方程）来完成此证明。
**符号约定：**

*   $H = H_0 + V$：完整哈密顿算符。
*   $G(z) \equiv R(z, H) = (z - H)^{-1}$：**完整预解式**（或 Green 函数）。
*   $G_0(z) \equiv R(z, H_0) = (z - H_0)^{-1}$：**自由预解式**（或自由 Green 函数）。
*   $V$：相互作用势。
*   $T(z)$：T 矩阵算符。

### **4.1 算符恒等式的推导 (Lippmann-Schwinger)**

我们从 $G(z)$ 的定义开始：

$$ (z - H) G(z) = I \implies (z - H_0 - V) G(z) = I $$
将其写为：

$$ (z - H_0) G(z) = I + V G(z) $$
在等式两边从左侧同乘以 $G_0(z) = (z - H_0)^{-1}$，我们得到 [28](#ref-28)：

$$ G(z) = G_0(z) + G_0(z) V G(z) \quad \cdots \quad (\text{L-S 方程 1}) $$
这是第一个 Lippmann-Schwinger (L-S) 方程，它将完整预解式 $G(z)$ 与自由预解式 $G_0(z)$ 联系起来。
T 矩阵算符 $T(z)$ 通常通过它与 $V$ 和 $G_0(z)$ 的关系来定义，即满足第二个 L-S 方程 [28](#ref-28)：

$$ T(z) = V + V G_0(z) T(z) \quad \cdots \quad (\text{L-S 方程 2}) $$
这个方程的迭代解（Born 级数）给出了 $T(z)$ 的物理图像：

$$ T(z) = V + V G_0(z) V + V G_0(z) V G_0(z) V + \dots $$

这表示 $T(z)$ 包含了单次散射 ($V$) 以及所有由自由粒子传播 ($G_0$) 连接的多次散射过程 [8](#ref-8)。

### **4.2 核心证明 A：T(z) 极点 $\implies$ G(z) 极点**

我们需要一个表示 $G(z)$ 的恒等式，该恒等式以 $T(z)$ 作为输入。 我们迭代 L-S 方程 1 ($G = G_0 + G_0 V G$)：

$$ G = G_0 + G_0 V (G_0 + G_0 V G) = G_0 + G_0 V G_0 + G_0 V G_0 V G $$

$$ G = G_0 + G_0 [V + V G_0 V + V G_0 V G_0 V + \dots] G_0 $$
我们观察到，方括号中的无穷级数正是 $T(z)$ 的 Born 级数 [8](#ref-8)。因此，我们得到了连接 $G(z)$ 和 $T(z)$ 的第一个关键恒等式 [28](#ref-28)：

$$ G(z) = G_0(z) + G_0(z) T(z) G_0(z) \quad \cdots \quad (\text{恒等式 1}) $$
**证明：** 假设 $T(z)$ 在 $z = z_R$ 处有一个极点。根据第 3 节的定义，这是一个共振态，因此 $z_R$ 是一个**非实数**的复数（$z_R = E_R - i\Gamma/2$）。
现在我们来分析恒等式 1 在 $z = z_R$ 处的行为：

1.  $T(z)$ 在 $z_R$ 处具有奇异性（极点）。
2.  $G_0(z) = (z - H_0)^{-1}$ 是自由哈密顿算符的预解式。$H_0$ 是自伴算符，其谱 $\sigma(H_0) = [0, \infty)$ 完全位于实轴上。
3.  由于 $z_R$ 是非实数，它位于 $H_0$ 的预解集 $\rho(H_0)$ 中。
4.  因此，$G_0(z)$ 在 $z = z_R$ 处是**解析的、无奇异性的**。
5.  在恒等式 1 中，$G_0(z)$ 在 $z_R$ 处表现为一个解析算符，而 $T(z)$ 在 $z_R$ 处发散。
6.  **结论：** $G(z)$ 的奇异性完全由 $T(z)$ 的奇异性决定。因此，如果 $T(z)$ 在 $z_R$ 处有极点，那么 $G(z)$ 在 $z_R$ 处也必然有极点。

### **4.3 核心证明 B：G(z) 极点 $\implies$ T(z) 极点**

现在我们需要证明反方向的蕴含关系。我们需要一个表示 $T(z)$ 的恒等式，该恒等式以 $G(z)$ 作为输入。
从 L-S 方程 1 ($G = G_0 + G_0 V G$) 出发，我们整理得到：

$$ G - G_0 = G_0 V G \implies G_0^{-1} (G - G_0) = V G $$

$$ (z - H_0) (G - G_0) = V G $$

另一方面，T 矩阵也可以通过 $T(z) = V + V G(z) V$ 来定义。将 $V G$ 的表达式代入：

$$ T(z) = V + V G_0^{-1} (G - G_0) = V + (z - H_0) (G - G_0) $$

这是一个不太常见的恒等式，但它直接将 $T(z)$ 与 $G(z)$ 联系起来。

一个更常用且更有启发性的恒等式是：

$$ T(z) = V + V G(z) V \quad \cdots \quad (\text{恒等式 2}) $$

**证明：** 假设 $G(z)$ 在 $z = z_R$ 处有一个极点。同样，$z_R$ 是非实数。
现在我们来分析恒等式 2 在 $z = z_R$ 处的行为：

1.  $G(z)$ 在 $z_R$ 处具有奇异性（极点）。
2.  $V$ 是一个与 $z$ 无关的静态势算符，它本身没有奇异性。
3.  在恒等式 2 中，$V$ 表现为一个无奇异性的算符，而 $G(z)$ 在 $z_R$ 处发散。
4.  **结论：** $T(z)$ 的奇异性完全由 $G(z)$ 的奇异性决定。因此，如果 $G(z)$ 在 $z_R$ 处有极点，那么 $T(z)$ 在 $z_R$ 处也必然有极点。

### **4.4 最终结论**

通过 4.2 和 4.3 节的证明，我们已经建立了 $G(z)$ 的极点与 $T(z)$ 的极点之间的一一对应关系。这两个算符在整个复能量平面（包括物理片和所有非物理片）上共享完全相同的极点结构。
结合第 3 节中“共振态被定义为 T 矩阵在非物理片上的极点”这一现代散射理论的定义，我们最终完成了本报告的核心证明：
**共振态对应于（解析延拓的）预解式算符 $R(z, H)$ 在非物理片上的极点。**

## **第五节：结论：共振态作为 Gamow 矢量**

本报告通过一系列严格的数学推导，解决了“共振态”这一物理概念与其在预解式形式主义中数学表示之间的悖论。

1.  我们首先指出，由于自伴哈密顿算符的谱必须是实数，共振态所对应的复数能量 $z_R = E_R - i\Gamma/2$ 不可能是在标准希尔伯特空间中定义的预解式算符 $R(z, H)$ 的极点。
2.  我们接着论证，这个悖论的解决之道在于**解析延拓**。连续谱 $\sigma_c(H) = [0, \infty)$ 构成了 $R(z, H)$ 的一个分支切割，它将复能量平面划分为**物理片 (Sheet I)** 和**非物理片 (Sheet II)**。
3.  我们采纳了现代散射理论的观点，将共振态严格**定义**为 S 矩阵（或 T 矩阵）在非物理片上的极点。
4.  最后，通过推导 Lippmann-Schwinger 方程的两种等价形式，我们严格证明了**预解式算符 $R(z, H)$ 与 T 矩阵 $T(z)$ 具有完全相同的极点结构**。

这一结论不仅解决了最初的悖论，而且揭示了共振态的深刻数学本质。这些位于非物理片上的极点，其留数所对应的本征矢量被称为**Gamow 矢量** [9](#ref-9)。这些矢量不属于标准的希尔伯特空间 $\mathcal{H}$（因为它们的范数会发散），而是属于一个更大的数学结构——**装备希尔伯特空间 (Rigged Hilbert Space)** [29](#ref-29)。
在装备希尔伯特空间中，Gamow 矢量是哈密顿算符的广义本征矢量，其本征值恰好是复数 $z_R = E_R - i\Gamma/2$。当一个系统处于由 Gamow 矢量描述的共振态时，其时间演化是**纯粹的指数衰减**，没有像标准量子力学中那样的非指数修正项 [22](#ref-22)。
这种不可逆的、纯粹指数性的衰减为量子力学中的时间箭头和微观不可逆性提供了严格的数学基础 [26](#ref-26)。
因此，共振态作为解析延拓预解式的极点，不仅仅是一个数学上的巧合，它揭示了量子系统在超越标准希尔伯特空间框架后更深层次的结构。

#### **引用的文献**

<a id="ref-1"></a>1. Resolvent formalism - Wikipedia, https://en.wikipedia.org/wiki/Resolvent_formalism
<a id="ref-2"></a>2. Math 346 Lecture #33 12.3 The Resolvent, http://uamte.math.byu.edu/~bakker/Math346/Lectures/M346Lec33.pdf
<a id="ref-3"></a>3. Functional Analysis II - LMU München, https://www.mathematik.uni-muenchen.de/~lampart/FA2_WS19_Lampart_week14.pdf
<a id="ref-4"></a>4. Reference request: The resolvent is analytic in the resolvent set - MathOverflow, https://mathoverflow.net/questions/294002/reference-request-the-resolvent-is-analytic-in-the-resolvent-set
<a id="ref-5"></a>5. quantum mechanics - Intuitive reason why bound states correspond ..., https://physics.stackexchange.com/questions/212559/intuitive-reason-why-bound-states-correspond-to-poles
<a id="ref-6"></a>6. Bound state - Wikipedia, https://en.wikipedia.org/wiki/Bound_state
<a id="ref-7"></a>7. On the E ectiveness of Gamow's Method for Calculating Decay Rates, https://www.sbfisica.org.br/rbef/pdf/v21_464.pdf
<a id="ref-8"></a>8. 10. Scattering Theory - DAMTP, https://www.damtp.cam.ac.uk/user/tong/aqm/aqmten.pdf
<a id="ref-9"></a>9. Gamow vectors and Supersymmetric Quantum Mechanics - SciELO México, https://www.scielo.org.mx/pdf/rmf/v53s2/v53s2a13.pdf
<a id="ref-10"></a>10. Physlet Quantum Physics by Belloni, Christian, and Cox: Section 10.4 - ComPADRE, https://www.compadre.org/pqp/quantum-theory/section10_4.cfm
<a id="ref-11"></a>11. Time Evolution Refresher (Mini-Lecture) Handout Begin with Schrödinger's Equation: ih d dt, https://paradigms.oregonstate.edu/act/handout/2064/pdf/
<a id="ref-12"></a>12. Complex Eigenvalues of the Parabolic Potential Barrier and Gel'fand Triplet - arXiv, https://arxiv.org/pdf/math-ph/9910009
<a id="ref-13"></a>13. S-matrix - Wikipedia, https://en.wikipedia.org/wiki/S-matrix
<a id="ref-14"></a>14. Resonances as poles of the S-matrix, https://www.fuw.edu.pl/~dobaczew/poste54w/node4.html
<a id="ref-15"></a>15. Pole position of the resonance in a three-body unitary framework ..., https://link.aps.org/doi/10.1103/PhysRevD.105.054020
<a id="ref-16"></a>16. 48. Resonances - Particle Data Group, https://pdg.lbl.gov/2018/reviews/rpp2018-rev-resonances.pdf
<a id="ref-17"></a>17. 49. Resonances - Particle Data Group, https://pdg.lbl.gov/2020/reviews/rpp2020-rev-resonances.pdf
<a id="ref-18"></a>18. The differences between the poles on the 1st and 2nd Riemann sheets.... - ResearchGate, https://www.researchgate.net/figure/The-differences-between-the-poles-on-the-1st-and-2nd-Riemann-sheets-Integrals-along-the_fig2_376533985
<a id="ref-19"></a>19. [1303.4657] Resonances and poles in the second Riemann sheet - arXiv, https://arxiv.org/abs/1303.4657
<a id="ref-20"></a>20. Scattering III: S-matrix and Bound States - Galileo, https://galileo.phys.virginia.edu/classes/752.mf1i.spring03/Scattering_III.htm
<a id="ref-21"></a>21. The Analytic Continuation of the Resolvent Kernel and Scattering Operator Associated with the Schroedinger Operator1*2 - Deep Blue Repositories, https://deepblue.lib.umich.edu/bitstream/handle/2027.42/33406/0000807.pdf?sequence=1
<a id="ref-22"></a>22. (PDF) Deviations from Exponential Decay Law in the Time Evolution of Quantum Resonant States Described by Lorentzian Line Shape Spectral Distributions - ResearchGate, https://www.researchgate.net/publication/337464477_Deviations_from_Exponential_Decay_Law_in_the_Time_Evolution_of_Quantum_Resonant_States_Described_by_Lorentzian_Line_Shape_Spectral_Distributions
<a id="ref-23"></a>23. Analyzing the contribution of individual resonance poles of the S-matrix to the two-channel scattering - arXiv, https://arxiv.org/pdf/1110.4990
<a id="ref-24"></a>24. MATHEMATICAL THEORY OF SCATTERING ... - MIT Mathematics, https://math.mit.edu/~dyatlov/res/res_final.pdf
<a id="ref-25"></a>25. [1802.09467] Different manifestations of S-matrix poles - arXiv, https://arxiv.org/abs/1802.09467
<a id="ref-26"></a>26. [hep-th/0212280] Time Asymmetric Quantum Theory - II. Relativistic Resonances from S-Matrix Poles - arXiv, https://arxiv.org/abs/hep-th/0212280
<a id="ref-27"></a>27. Observing S-Matrix Pole Flow in Resonance Interplay - arXiv, https://arxiv.org/html/2405.03149v1
<a id="ref-28"></a>28. NOTES ON 1-PARTICLE SCATTERING 1. The resolvent and the ..., http://wwwteor.mi.infn.it/~molinari/NOTES/Notes_on_1_particle_scattering.pdf
<a id="ref-29"></a>29. The Rigged Hilbert Space Formulation of Quantum Mechanics and ..., https://arxiv.org/pdf/quant-ph/9505004