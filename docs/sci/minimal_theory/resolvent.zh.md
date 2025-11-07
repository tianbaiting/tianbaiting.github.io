# resolvent

## **预解式算符的定义与谱理论基础**

### **1.1 算符、谱与预解集：泛函分析的观点**

在数学物理中，一个物理系统的可观测量（如能量、动量）由一个复Hilbert空间 $H$ 上的线性算符 $T$ 来表示 [1](#ref-1)。这些算符，特别是像哈密顿算符 (Hamiltonian) 这样的能量算符，通常是无界的 (unbounded)，但它们满足一个关键的拓扑性质：它们是“闭算符” (closed operators) [2](#ref-2)。谱理论 (Spectral theory) 的研究必须在这个更广泛的闭算符框架内进行，而不仅仅局限于有界算符 (bounded operators) [3](#ref-3)。

谱理论的核心是理解算符 $(T - \lambda I)$ 的可逆性，其中 $I$ 是恒等算符，$\\lambda$ 是一个复数。

定义 1.1 (预解集)  
算符 $T$ 的预解集 (resolvent set)，记为 $\rho(T)$，是所有复数 $\lambda \in \mathbb{C}$ 的集合，满足以下条件：算符 $(T - \lambda I)$ 是一个双射（即单射且满射），并且其逆算符 $(T - \lambda I)^{-1}$ 是一个在 $H$ 上处处定义（defined everywhere）的有界线性算符 [1](#ref-1)。  

定义 1.2 (谱)  
算符 $T$ 的谱 (spectrum)，记为 $\sigma(T)$，是预解集 $\rho(T)$ 在复平面 $\mathbb{C}$ 上的补集，即 $\sigma(T) = \mathbb{C} \setminus \rho(T)$ [1](#ref-1)。谱 $\sigma(T)$ 总是复平面上的一个闭集 [6](#ref-6)。  


在有限维空间中（例如，$N \times N$ 矩阵），算符 $(T - \lambda I)$ 的可逆性仅仅取决于其行列式是否为零。因此，谱 $\sigma(T)$ 精确地等于 $T$ 的本征值 (eigenvalues) 的集合 [4](#ref-4)。然而，在无限维空间中（例如，量子力学的波函数空间 $L^2(\mathbb{R})$），这一图像被根本性地改变了。一个算符可能是单射的（即没有本征值），但仍然不可逆（例如，它不是满射的）[4](#ref-4)。[4](#ref-4) 中给出的右移算符 (right shift operator) 示例完美地说明了这一点：它没有本征值，但 0 仍然在谱中，因为它不是满射的。因此，谱是本征值概念在无限维空间中的必要推广 [4](#ref-4)。

对于物理学中重要的闭算符（这包括所有有界算符和自伴哈密顿算符），“有界逆算符定理” (Bounded Inverse Theorem) [3](#ref-3] 和“闭图像定理” (Closed Graph Theorem) [3](#ref-3] 极大地简化了定义 1.1。这些定理保证，如果一个闭算符 $T$ 的逆 $T^{-1}$ *存在*（即 $T$ 是双射的），那么 $T^{-1}$ *自动*是有界的。因此，对于我们关心的闭算符，谱 $\sigma(T)$ *就是*使 $(T - \lambda I)$ *不是双射* (not bijective) 的 $\lambda$ 的集合 [3](#ref-3]。

### **1.2 谱的精细结构：逆算符失效的三种模式**

谱 $\sigma(T)$ 之所以存在，是因为 $(T - \lambda I)$ 作为双射的条件（单射、满射、有界逆）至少有一条被破坏了。根据具体是哪条条件失效，谱可以被分解为三个互不相交的子集 [2](#ref-2)。

定义 1.3 (点谱 $\sigma_p(T)$)  
点谱 (Point Spectrum) 是所有 $\lambda \in \mathbb{C}$ 的集合，使得 $(T - \lambda I)$ 不满足单射性 (not injective)。这意味着存在非零向量 $v \in H$ 使得 $T v = \lambda v$ [5](#ref-5)。这些 $\lambda$ 正是传统的本征值。  

定义 1.4 (连续谱 $\sigma_c(T)$)  
连续谱 (Continuous Spectrum) 是所有 $\lambda \in \mathbb{C}$ 的集合，使得 $(T - \lambda I)$ 满足单射性，其值域 $R(T - \lambda I)$ 在 $H$ 中是稠密的 (dense)，但其（在值域上定义的）逆算符是无界的 [5](#ref-5)。  

定义 1.5 (剩余谱 $\sigma_r(T)$)  
剩余谱 (Residual Spectrum) 是所有 $\lambda \in \mathbb{C}$ 的集合，使得 $(T - \lambda I)$ 满足单射性，但其值域 $R(T - \lambda I)$ 在 $H$ 中不是稠密的 [5](#ref-5)。  

*注：对于物理学中最重要的自伴算符 (self-adjoint operators)，可以证明其剩余谱 $\sigma_r(T)$ 是空集。*

这种谱的分解在物理学上具有至关重要的意义。点谱 $\sigma_p(T)$ 通常对应于系统的**束缚态** (Bound States)，例如氢原子中能量量子化的离散能级。连续谱 $\sigma_c(T)$ 则对应于**散射态** (Scattering States)，例如能量可以取 $[0, \infty)$ 区间内任意值的自由粒子，或从势阱中电离的电子 [8](#ref-8)。

### **1.3 预解式算符 $R(z, A)$ 及其解析性质**

谱理论的核心工具——预解式算符——现在可以被定义。

定义 1.6 (预解式)  
对于复参数 $z \in \rho(A)$（即 $z$ 位于预解集中），算符 $A$ 的预解式 (Resolvent)，记为 $R(z, A)$，定义为：

$$R(z, A) = (A - zI)^{-1}$$  
[9](#ref-9)。在物理文献中，特别是在微扰理论和格林函数 (Green's function) 理论中，更常见的约定是 $G(z, A) = (z - A)^{-1}$ [10](#ref-10)。这两种定义仅相差一个负号和 $z$ 的重新标记，但 $G(z)$ 的形式在Lippmann-Schwinger方程中更为自然。本报告将主要采用 $G(z) = (z - A)^{-1}$ 这一约定。

预解式的最重要特性，也是使其成为连接物理与数学的桥梁的特性是：**$G(z, A)$ 是 $\rho(A)$ 上的一个全纯 (holomorphic) 或者说解析 (analytic) 的算符值函数** [8](#ref-8)。

这实现了一个根本性的范式转移 (paradigm shift)。我们不再直接研究算符 $A$（它可能是一个复杂的、无界的微分算符），而是转而研究一个*函数* $G(z)$。$G(z)$ 是一个以复数 $z$ 为变量、以*有界算符*为值的解析函数。

在这个新范式中，算符 $A$ 的谱 $\sigma(A)$，即 $G(z)$ *没有*定义的点集，就是 $G(z)$ 作为解析函数**失去其解析性**的地方。换言之，**算符 $A$ 的谱 $\sigma(A)$ 就是其预解式 $G(z)$ 的奇点 (singularities) 的集合** [7](#ref-7)。

这种将算符谱问题转化为复分析函数奇点问题的思想，就是“预解式形式主义” (Resolvent Formalism) 的精髓 [9](#ref-9]。它允许我们动用复分析中所有强大的工具——柯西积分、留数定理、Plemelj公式等——来“探测”算符 $A$ 的谱结构。

## **第二部分：【核心证明】为什么预解式的奇点包含谱信息？**

本部分将严格证明预解式 $G(z)$ 的两种主要奇点类型（极点和割线）如何分别编码了算符 $A$ 的离散谱（本征值）和连续谱。

### **2.1 证明 (I): 离散谱 (极点) 与 Riesz 投影**

**论点**：谱的孤立点（即孤立的本征值）对应于预解式 $G(z)$ 的**极点** (Poles) [12](#ref-12)。

对于许多物理系统，例如束缚在势阱中的粒子，其哈密顿算符具有“紧预解式” (compact resolvent)，这意味着它们的谱*只*由孤立的本征值构成 [16](#ref-16)。

证明 2.1 (Riesz 投影的定义)  
假设 $E_n$ 是算符 $A$ 的谱 $\sigma(A)$ 中的一个孤立点。这意味着我们可以找到一个半径足够小的简单闭合围道 (contour) $C_n$，它在复平面上只包围 $E_n$，而将谱的其余所有部分都排除在外 [9](#ref-9]。  
我们利用复分析中的柯西积分，定义一个算符 $P_n$，称为 Riesz 投影 (Riesz projection) [18](#ref-18]：

$$P_n = \frac{1}{2\pi i} \oint_{C_n} G(z, A) dz = \frac{1}{2\pi i} \oint_{C_n} (z - A)^{-1} dz$$  
[9](#ref-9)。（注：使用 $G(z) = (z-A)^{-1}$ 约定，积分为正号。若使用 $R(z)=(A-zI)^{-1}$，则积分前需加负号 [9](#ref-9]。）

证明 2.2 ( $P_n$ 是一个投影算符)  
我们现在必须证明 $P_n$ 确实是一个投影算符，即它满足幂等性： $P_n^2 = P_n$。

1. 工具：证明的关键是“第一预解式恒等式”（或 Hilbert 恒等式）。对于任意 $z, w \in \rho(A)$：  
   $G(z) - G(w) = (z - A)^{-1} - (w - A)^{-1} = (z - A)^{-1} [ (w - A) - (z - A) ] (w - A)^{-1}$  
   $G(z) - G(w) = G(z) (w - z) G(w)$  
   或 $G(w) G(z) = \frac{G(w) - G(z)}{z - w}$ [8](#ref-8)。  
2. 推导：我们取两个围道 $C_n$ 和 $C_n'$，它们都只包围 $E_n$，并且 $C_n$ 严格位于 $C_n'$ 内部 [18](#ref-18]。  
   $$ P_n^2 = \left( \frac{1}{2\pi i} \oint_{C_n'} G(w) dw \right) \left( \frac{1}{2\pi i} \oint_{C_n} G(z) dz \right) = \frac{1}{(2\pi i)^2} \oint_{C_n'} \oint_{C_n} G(w) G(z) dz dw $$  
3. 应用预解式恒等式：

   $$P_n^2 = \frac{1}{(2\pi i)^2} \oint_{C_n'} \oint_{C_n} \frac{G(w) - G(z)}{z - w} dz dw$$  
4. 我们将积分分为两部分：  
   $$ P_n^2 = \frac{1}{(2\pi i)^2} \oint_{C_n'} G(w) \left( \oint_{C_n} \frac{dz}{z - w} \right) dw - \frac{1}{(2\pi i)^2} \oint_{C_n} G(z) \left( \oint_{C_n'} \frac{dw}{z - w} \right) dz $$  
5. **计算内层积分**（利用柯西积分公式）：  
   * 在第一项中， $w$ 位于*外部*围道 $C_n'$ 上，而 $z$ 位于*内部*围道 $C_n$ 上。因此 $w$ 始终在 $C_n$ 的*外部*。根据柯西定理， $\oint_{C_n} \frac{dz}{z - w} = 0$。  
   * 在第二项中， $z$ 位于*内部*围道 $C_n$ 上，而 $w$ 位于*外部*围道 $C_n'$ 上。$z$ 始终在 $C_n'$ 的*内部*。根据柯西积分公式， $\oint_{C_n'} \frac{dw}{z - w} = - \oint_{C_n'} \frac{dw}{w - z} = - (2\pi i)$。  
6. 将结果代回：  
 
   $$ P_n^2 = \frac{1}{(2\pi i)^2} \oint_{C_n'} G(w) (0) dw - \frac{1}{(2\pi i)^2} \oint_{C_n} G(z) (-2\pi i) dz $$ 
   
   $$ P_n^2 = 0 + \frac{1}{2\pi i} \oint_{C_n} G(z) dz = P_n $$  
   证明 $P_n^2 = P_n$ 完毕 [18](#ref-18]。

证明 2.3 ( $P_n$ 投影到本征子空间)  
可以进一步证明，Riesz 投影 $P_n$ 与算符 $A$ 是对易的 ($AP_n = P_n A$) [12](#ref-12]，并且 $P_n$ 的值域 (Range) 恰好是对应于本征值 $E_n$ 的（广义）本征子空间 [18](#ref-18]。对于自伴算符，这就是本征子空间。如果 $E_n$ 是非简并的， $P_n$ 就是 $|\psi_n\rangle\langle \psi_n|$。  

核心结论 (I)：  
上述证明揭示了预解式极点的深刻含义。我们想知道一个孤立本征值 $E_n$ 及其本征态 $|\psi_n\rangle$。预解式 $G(z)$ 在 $z = E_n$ 处有一个极点。通过围绕这个极点进行围道积分（即计算留数 (Residue)），我们严格地恢复了投影算符 $P_n$。  
因此，离散谱的信息被完整地编码在 $G(z)$ 的极点中：

* **极点的位置 (Location) $\implies$ 本征值 (Eigenvalue) $E_n$。**  
* **极点的留数 (Residue) $\implies$ 到本征子空间的投影算符 (Projection) $P_n$** [15](#ref-15]。

### **2.2 证明 (II): 连续谱 (割线) 与 Stone 公式**

**论点**：连续谱 $\sigma_c(A)$ 对应于预解式 $G(z)$ 的**分支割线** (Branch Cut) [8](#ref-8]。

对于自伴算符（如哈密顿算符），谱 $\sigma(A)$ 完全位于实轴 $\mathbb{R}$ 上 [8](#ref-8]。连续谱通常表现为实轴上的一个区间，例如自由粒子的 $[0, \infty)$ [8](#ref-8)。（尽管它也可以是更复杂的集合，如康托尔集 [22](#ref-22]。）

直观理解 (连续的极点)：  
一个孤立的极点 $G(z) \sim (z-E_n)^{-1}$ 对应一个离散能级。那么连续谱在复平面上对应什么呢？直观上，连续谱可以被想象为沿着一条线（例如实轴的 $[a, b]$ 段）连续地分布着无穷多个极点。  
[21](#ref-21) 中的一个简单计算完美地展示了这一点：

$$\int_a^b \frac{1}{z-u} du = \log(z-b) - \log(z-a) = \log\left(\frac{z-b}{z-a}\right)$$

等式左边是一个“连续的极点之和”（在 $[a, b]$ 区间内的每个 $u$ 处，都有一个留数为 $du$ 的极点）。等式右边是一个具有 $[a, b]$ 分支割线的对数函数。这个例子表明，极点的连续分布在复分析中自然地产生了分支割线。因此，连续谱在 $G(z)$ 的解析结构中表现为分支割线 [21](#ref-21]。  

证明 2.4 (Stone 公式)  
Stone 公式（或 Stone-von Neumann 公式）是上述直觉的严格数学表述。它将 $G(z)$ 跨越实轴（割线）的不连续性（或“跳跃”）与谱测量 (Spectral Measure) $E(\lambda)$ 直接联系起来 [8](#ref-8]。  
根据谱定理，对于自伴算符 $A$，存在一个唯一的投影值谱测量 $E(\lambda)$，使得 $A$ 可以被分解为 $A = \int_{-\infty}^\infty \lambda dE(\lambda)$。$E(\Delta)$ 表示投影到谱位于区间 $\Delta$ 内的子空间上的投影算符。

Stone 公式指出，这个谱测量 $E(\Delta)$ 可以通过 $G(z)$ 在实轴上方和下方的极限来恢复 [24](#ref-24]。令 $G(\lambda \pm i0) = \lim_{\epsilon \to 0^+} G(\lambda \pm i\epsilon)$。对于任意区间 $(a, b)$，我们有：

$$ \frac{E((a, b)) + E([a, b])}{2} = \lim_{\epsilon \to 0^+} \frac{1}{2\pi i} \int_a^b [G(\lambda - i\epsilon) - G(\lambda + i\epsilon)] d\lambda $$  

这个公式是复分析中 Sokhotski–Plemelj 定理的算符版本，它表明 $G(z)$ 跨越实轴的“跳跃” $\\text{Disc}[G(\lambda)] = G(\lambda+i0) - G(\lambda-i0)$（注意符号约定）与谱测量 $dE_\lambda$ 成正比。 

证明 2.5 (Stone 公式的推导草图)  
这个公式的推导可以优雅地通过泛函演算 (Functional Calculus) 完成 [24](#ref-24]。

1. 我们希望计算的积分 $F_\epsilon(A) = \frac{1}{2\pi i} \int_a^b [G(\lambda - i\epsilon) - G(\lambda + i\epsilon)] d\lambda$ 实际上是 $A$ 的一个函数，$F_\epsilon(A) = f_\epsilon(A)$。  
   
2. 我们只需分析对应的标量函数 $f_\epsilon(t)$（其中 $t$ 是实变量，代表 $A$ 的谱值）：  
   
   $$ f_\epsilon(t) = \frac{1}{2\pi i} \int_a^b \left( \frac{1}{t - (\lambda - i\epsilon)} - \frac{1}{t - (\lambda + i\epsilon)} \right) d\lambda $$  
3. 合并分式： 
    
   $$ f_\epsilon(t) = \frac{1}{2\pi i} \int_a^b \frac{(t - \lambda - i\epsilon) - (t - \lambda + i\epsilon)}{(t - \lambda)^2 + \epsilon^2} d\lambda = \frac{1}{2\pi i} \int_a^b \frac{-2i\epsilon}{(t - \lambda)^2 + \epsilon^2} d\lambda $$ $$ f_\epsilon(t) = \frac{1}{\pi} \int_a^b \frac{\epsilon}{(t - \lambda)^2 + \epsilon^2} d\lambda $$  
4. 这是一个洛伦兹分布 (Lorentzian) 或柯西分布 (Cauchy distribution) 的积分，它是 $\\delta$-函数的一个表示。积分 $f_\epsilon(t)$ 可以被精确计算：  
   
   $$ f_\epsilon(t) = \frac{1}{\pi} \left[ \arctan\left(\frac{b - t}{\epsilon}\right) - \arctan\left(\frac{a - t}{\epsilon}\right) \right] $$  
5. 在 $\epsilon \to 0^+$ 的极限下， $\arctan(x/\epsilon)$ 趋向于一个阶梯函数 $\frac{\pi}{2} \text{sgn}(x)$。因此：  
   
   $$ \lim_{\epsilon \to 0^+} f_\epsilon(t) = \frac{1}{\pi} \left( \frac{\pi}{2} \text{sgn}(b-t) - \frac{\pi}{2} \text{sgn}(a-t) \right) = \begin{cases} 1 & \text{if } t \in (a,b) \\ 1/2 & \text{if } t = a \text{ or } t = b \\ 0 & \text{otherwise} \end{cases} $$  
6. 这个极限函数 $\chi_{(a,b)}(t)$ 正是区间 $(a,b)$ 的特征函数（在端点处取平均值）。  
7. 根据泛函演算的谱映射定理，算符的极限 $\lim_{\epsilon \to 0^+} F_\epsilon(A)$ 就是 $\chi_{(a,b)}(A)$。根据谱定理， $\chi_{(a,b)}(A)$ *正是*谱投影 $E((a,b))$（加上端点贡献）。**证明完毕** [24](#ref-24]。

核心结论 (II)：  
Stone 公式严格地证明了连续谱的信息被完整地编码在 $G(z)$ 的分支割线中：

* **割线的位置 (Location) $\implies$ 连续谱 (Continuous Spectrum) $\sigma_c(A)$。**  
* **割线上的不连续性 (Discontinuity) $\implies$ 谱密度 (Spectral Density) $dE_\lambda / d\lambda$** [24](#ref-24]。


### 证明共振态是什么




### **总结：谱与奇点的对应关系**

第二部分的两个核心证明清晰地回答了“为什么预解式能给出谱信息”的问题。下表总结了这一深刻的对应关系：

| 谱的类型 (Spectrum Type) | 物理图像 (Physical Picture) | 预解式 G(z) 的奇点类型 (Singularity Type) | 奇点揭示的信息 (Information Revealed) | 关键数学工具 (Key Mathematical Tool) |
| :---- | :---- | :---- | :---- | :---- |
| **点谱 $\sigma_p(A)$** (Discrete) | 束缚态 (Bound States) | **极点 (Pole)** [12](#ref-12) | **位置**: 本征值 $E_n$ **留数**: 投影算符 $P_n = | \psi_n\rangle\langle \psi_n |
| **连续谱 $\sigma_c(A)$** (Continuous) | 散射态 (Scattering States) | **分支割线 (Branch Cut)** [8](#ref-8) | **位置**: 连续谱区间 $ |  |

## **第三部分：微扰理论的预解式推导：从恒等式到级数**

现在我们转向用户的第二个问题：如何使用预解式理论进行微扰求解。我们将展示预解式形式主义如何为Rayleigh-Schrödinger微扰理论（RSPT）提供了最自然和最严谨的推导基础。

### **3.1 微扰设置与历史脉络**

微扰理论的核心思想是将一个复杂（但“可解”）的系统的哈密顿算符 $H_0$ 加上一个“小”的微扰 $V$ [26](#ref-26)。总哈密顿算符为：

$$H = H_0 + V$$

我们的目标是，在已知 $H_0$ 的本征值 $E_n^{(0)}$ 和本征态 $|\psi_n^{(0)}\rangle$ 的情况下，近似求解 $H$ 的本征值 $E_n$ 和本征态 $|\psi_n\rangle$。  
正如用户查询中所指出的，这一方法的历史脉络深刻地根植于物理学的发展：

1. **Rayleigh (19世纪)**: 约翰·斯特拉特，即瑞利勋爵 (Lord Rayleigh)，在其巨著《声学理论》(The Theory of Sound) 中，首次系统地研究了物理系统的微扰。他研究了振动弦（如小提琴弦）由于密度存在“轻微的不均匀性” (small inhomogeneities) $V$ 而引起的基频（本征值）的漂移 [27](#ref-27)。  
2. **Schrödinger (1926)**: 埃尔温·薛定谔 (Erwin Schrödinger) 在其1926年奠定波动力学的系列论文中，明确引用了Rayleigh的工作 [27](#ref-27]。他将Rayleigh的方法从经典声学推广到量子力学，用以计算（例如）外加电场（微扰 $V$）如何导致氢原子能级（本征值）发生移动，即著名的斯塔克效应 (Stark effect) [27](#ref-27)。  
3. **Kato (1949)**: 尽管Rayleigh-Schrödinger (RS) 理论在物理学中取得了巨大成功，但在数学上，它在近半个世纪里都只是一个“形式级数” (formal series)，其收敛性和严谨性存疑 [32](#ref-32]。直到1949年左右，加藤敏夫 (Tosio Kato) [30](#ref-30] 和 Franz Rellich [30](#ref-30] 才为其提供了坚实的数学基础。Kato在其划时代的著作《线性算符的微扰理论》(Perturbation Theory for Linear Operators) [34](#ref-34] 中，系统地发展了基于预解式算符的微扰理论，彻底解决了这一问题 [30](#ref-30]。

### **3.2 预解式恒等式 (Dyson方程)**

预解式方法的核心是建立未微扰预解式 $G_0(z)$ 和完整预解式 $G(z)$ 之间的精确关系。  
令 $G(z) = (z - H)^{-1}$ 且 $G_0(z) = (z - H_0)^{-1}$。  
推导 3.1 (第二预解式恒等式)  
该恒等式的推导是纯粹的算符代数：

1. 从 $G(z)$ 和 $G_0(z)$ 的定义开始：  
   $G_0^{-1}(z) = z - H_0$  
   $G^{-1}(z) = z - H = z - (H_0 + V) = (z - H_0) - V = G_0^{-1}(z) - V$  
2. 因此，我们得到 $G_0^{-1}(z) - G^{-1}(z) = V$。  
3. 在这条恒等式的左侧乘以 $G_0(z)$，右侧乘以 $G(z)$：  
   $G_0(z) [ G_0^{-1}(z) - G^{-1}(z) ] G(z) = G_0(z) V G(z)$  
4. 展开左侧：  
   $G_0(z) G_0^{-1}(z) G(z) - G_0(z) G^{-1}(z) G(z) = G_0(z) V G(z)$  
5. 利用 $G_0 G_0^{-1} = I$ 和 $G^{-1} G = I$：  
   $I \cdot G(z) - G_0(z) \cdot I = G_0(z) V G(z)$  
6. 结果：

   $$G(z) = G_0(z) + G_0(z) V G(z)$$  
   [10](#ref-10)。这被称为第二预解式恒等式（或Dyson方程）。

这个恒等式是整个微扰理论的基石。它以一种非微扰的、精确的形式，将复杂的 $G(z)$（我们想知道其极点）与已知的 $G_0(z)$ 和微扰 $V$ 联系起来。

这个恒等式在物理学的不同分支中以不同的名称出现，显示了其普适性：

* 在量子散射理论中，它被称为 **Lippmann-Schwinger 方程** [11](#ref-11]。  
* 在量子场论和多体物理学中，它被称为 **Dyson 方程** [41](#ref-41]。

预解式形式主义提供了一个统一的语言，将束缚态微扰（RSPT）和散射问题（Born近似）无缝地联系在同一个数学框架下。

### **3.3 Born-Neumann 级数：$G(z)$ 的迭代展开**

Dyson方程 $G = G_0 + G_0 V G$ 是一个 $G(z)$ 的自洽方程。求解它的最直接方法是迭代法 [11](#ref-11]：

1. 将右侧的 $G$ 替换为整个方程：  
   $G = G_0 + G_0 V (G_0 + G_0 V G)$  
2. 展开并再次迭代：  
   $G = G_0 + G_0 V G_0 + G_0 V G_0 V (G_0 + G_0 V G)$  
3. 无限次迭代下去，我们得到一个无穷级数：

   $$G(z) = G_0(z) + G_0(z) V G_0(z) + G_0(z) V G_0(z) V G_0(z) + \dots$$  
   [11](#ref-11]。

这个级数在数学上被称为 **Neumann 级数** (Neumann series) [7](#ref-7]，在物理学中被称为 **Born 级数** (Born series) [39](#ref-39]。如果截取到 $V$ 的一阶， $G \approx G_0 + G_0 V G_0$，这就对应于散射理论中的 Born 近似 [39](#ref-39]。

然而，这个级数在应用于束缚态微扰时，存在一个 **灾难性的问题**。

Born 级数是一个几何级数，其收敛的充分条件是其“公比”的范数小于 1，即 $\|V G_0(z)\| < 1$ [7](#ref-7]。但是，我们使用预解式的*目的*是研究 $H$ 的本征值 $E_n$。$E_n$ 通常非常接近 $H_0$ 的本征值 $E_n^{(0)}$。而 $E_n^{(0)}$ 恰好是 $G_0(z)$ 的一个*极点*（根据第二部分）！

这意味着，当我们让 $z \to E_n^{(0)}$ 时， $G_0(z)$ 的范数会发散 $\|G_0(z)\| \to \infty$ [7](#ref-7]。因此，Born 级数 $G = \sum G_0 (V G_0)^n$ 在我们最关心的点（即 $H_0$ 的谱附近）是*灾难性发散*的。

**结论**：直接使用 Born 级数来寻找*新*极点（即 $H$ 的本征值）是行不通的。这正是 Rayleigh 和 Schrödinger 的形式推导中“除以零”问题的数学根源 [45](#ref-45]。我们需要一个更精巧的工具来系统地处理 $z = E_n^{(0)}$ 处的奇异性。这个工具正是 Kato 的严谨框架的核心。

## **第四部分：【完整推导】Rayleigh-Schrödinger 微扰理论**

我们将展示如何利用预解式形式主义，特别是通过引入投影算符和约化预解式，来严格且系统地推导RSPT的完整级数。

### **4.1 Kato 的严谨框架：利用投影算符**

Kato 和 Rellich 的核心思想是 [30](#ref-30]，我们不应该直接展开 $G(z)$ 本身，因为 $G(z)$ 在我们关心的点附近是奇异的。相反，我们应该研究由 $G(z)$ 的围道积分定义的*投影算符* $P_n$ [33](#ref-33]。

我们引入一个微扰参数 $\lambda$， $H(\lambda) = H_0 + \lambda V$。我们想求解的是 $H(\lambda)$ 的新本征值 $E_n(\lambda)$ 和新投影 $P_n(\lambda)$，它们都是 $\lambda$ 的函数。

Kato-Rellich 理论 [32](#ref-32] 证明了一个深刻的定理：如果 $E_n^{(0)}$ 是 $H_0$ 的一个孤立本征值，并且微扰 $V$ 是（相对 $H_0$）“解析”的，那么 $E_n(\lambda)$ 和 $P_n(\lambda)$ *也是* $\lambda$ 的**解析函数**（至少在 $\lambda=0$ 附近的一个邻域内是收敛的幂级数） [14](#ref-14]。

这意味着我们可以写：

$$E_n(\lambda) = E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} + \dots$$  
[27](#ref-27)

$$P_n(\lambda) = P_n^{(0)} + \lambda P_n^{(1)} + \lambda^2 P_n^{(2)} + \dots$$

我们的任务就是求解这些展开式的系数 $E_n^{(k)}$ 和 $P_n^{(k)}$。这在复平面上的图像是：$G_0(z)$ 在 $z=E_n^{(0)}$ 处的极点，在微扰 $V$ 的作用下，“漂移” (shift) 到了 $G(z, \lambda)$ 在 $z=E_n(\lambda)$ 处的新极点 [48](#ref-48]。

### **4.2 划分 (Partitioning) 方法**

推导 RSPT 最清晰、最有力的方法是 Feshbach-Löwdin 划分方法 [26](#ref-26]。这种方法自然地引出了 Kato 的关键工具，并能统一处理简并和非简并情况。

推导 4.1 (导出 $H_{eff}$)  
为简单起见，我们设 $E_n^{(0)}$ 是非简并的。

1. 定义投影算符 $P$ 和 $Q$：  
   $P = P_n^{(0)} = |\psi_n^{(0)}\rangle\langle \psi_n^{(0)}|$ （投影到我们关心的未微扰态）  
   $Q = I - P = \sum_{k \neq n} |\psi_k^{(0)}\rangle\langle \psi_k^{(0)}|$ （投影到所有其他态的正交子空间）[26](#ref-26]。  
2. $P$ 和 $Q$ 与 $H_0$ 对易 ($PH_0 = H_0 P$)，但与 $V$ 不对易。  
3. 我们将完整的薛定谔方程 $(H_0 + \lambda V) |\psi\rangle = E |\psi\rangle$ 插入一个 $I = P + Q$，并分别用 $P$ 和 $Q$ 作用于方程的左侧 [26](#ref-26]：  
   (a) $P (H_0 + \lambda V) (P + Q) |\psi\rangle = E P |\psi\rangle$  
   (b) $Q (H_0 + \lambda V) (P + Q) |\psi\rangle = E Q |\psi\rangle$  
4. 展开 (a) 式（利用 $PH_0 Q = 0$ 和 $PH_0 P = E_n^{(0)} P$）：  
   $(E_n^{(0)} P + \lambda PVP) P\|\psi\rangle + \lambda PVQ Q\|\psi\rangle = E P\|\psi\rangle$  
5. 展开 (b) 式（利用 $QH_0 P = 0$）：  
   $(Q H_0 Q + \lambda QVQ) Q\|\psi\rangle + \lambda QVP P\|\psi\rangle = E Q\|\psi\rangle$  
6. 从 (b) 式中形式上解出 $Q\|\psi\rangle$：  
   $$[ E - Q H_0 Q - \lambda QVQ ] Q\|\psi\rangle = \lambda QVP P\|\psi\rangle$$  
   $$Q\|\psi\rangle = (E - H_0 - \lambda QVQ)^{-1} Q \cdot (\lambda QVP) P\|\psi\rangle$$  
   （注意： $(E - H_0 - \lambda QVQ)^{-1}$ 的逆只在 $Q$ 空间中计算）  
7. 将 $Q\|\psi\rangle$ 的这个精确表达式代回到 (a) 式中：  
   $(E_n^{(0)} P + \lambda PVP) P\|\psi\rangle + \lambda PVQ \left[ (E - H_0 - \lambda QVQ)^{-1} Q \cdot (\lambda QVP) \right] P\|\psi\rangle = E P\|\psi\rangle$  
8. 这是一个只在 $P$ 空间中（在本例中是一维的）的精确本征方程：

   $$H_{eff}(E, \lambda) P|\psi\rangle = E P|\psi\rangle$$

   其中，有效哈密顿算符 (Effective Hamiltonian) $H_{eff}$ 为：

   $$H_{eff}(E, \lambda) = E_n^{(0)} P + \lambda PVP + \lambda^2 PVQ (E - H_0 - \lambda QVQ)^{-1} Q QVP$$

这个方程是精确的，但 $H_{eff}$ 自身又依赖于 $E$（在分母中），这是一个隐式方程。

* **Brillouin-Wigner 理论** [49](#ref-49]：通过迭代求解这个隐式方程 $E = f(E)$，得到 BW 级数。  
* **Rayleigh-Schrödinger 理论** [49](#ref-49]：通过在 $H_{eff}(E)$ 的分母中*也*将 $E$ 按 $\lambda$ 展开 ($E = E_n^{(0)} + \lambda E_n^{(1)} + \dots$)，然后逐阶收集 $\lambda$ 的幂，得到 RSPT 级数。这是我们接下来要做的。

### **4.3 约化预解式 (The Reduced Resolvent)**

RSPT 的核心就是展开 $H_{eff}$ 中的那个逆算符。其 $\\lambda^0$ 阶近似为 $(E_n^{(0)} - H_0)^{-1} Q$。这个算符在 $Q$ 空间（即 $k \neq n$ 的子空间）上是良定义的，但在 $P$ 空间上是发散的。

定义 4.1 (约化预解式 $S_n$)  
我们定义约化预解式 (Reduced Resolvent) $S_n$（在 Kato 的文献中常记为 $S$） [30](#ref-30] 为：

$$S_n \equiv Q (E_n^{(0)} - H_0)^{-1} Q$$

这个算符 $S_n$ 完美地对应于标准 RSPT 教科书中的形式和：

$$S_n = \sum_{k \neq n} \frac{|\psi_k^{(0)}\rangle\langle \psi_k^{(0)}|}{E_n^{(0)} - E_k^{(0)}}$$

Kato 的关键贡献在于 [30](#ref-30]，他证明了 $G_0(z)$ 在 $z=E_n^{(0)}$ 附近的洛朗展开 (Laurent expansion) 总是可以（在算符范数下）分解为：

$$G_0(z) = \frac{P_n^{(0)}}{z - E_n^{(0)}} + S(z)$$

其中 $S(z)$ 是在 $z=E_n^{(0)}$ 处全纯的部分。约化预解式 $S_n$ 就是这个全纯部分在该点的取值 $S_n = S(E_n^{(0)})$ [30](#ref-30]。它是一个严格定义的有界算符，它取代了所有非严谨的“除以 $(E_n - E_k)$” 的无穷求和 [45](#ref-45]。

### **4.4 能量与波函数的系统推导**

现在我们准备收获成果。我们将 $H_{eff}$ 中的逆算符 $G_Q(E, \lambda) \equiv (E - H_0 - \lambda QVQ)^{-1} Q$ 展开。

推导 4.2 ($G_Q$ 的展开)  
$$ G_Q(E, \lambda) = \left( (E_n^{(0)} - H_0) + (\lambda E_n^{(1)} + \lambda^2 E_n^{(2)} + \dots) - \lambda QVQ \right)^{-1} Q $$  
利用算符恒等式 $(A+B)^{-1} = (I + A^{-1}B)^{-1} A^{-1} \\approx (I - A^{-1}B) A^{-1}$，并只保留到 $\\lambda^0$ 阶（因为 $G_Q$ 总是与 $\\lambda^2$ 相乘）：

$$G_Q(E, \lambda) = (E_n^{(0)} - H_0)^{-1} Q + \mathcal{O}(\lambda)$$  
$$G_Q(E, \lambda) = S_n + \mathcal{O}(\lambda)$$

（因为 $Q$ 算符使得 $(E_n^{(0)} - H_0)^{-1}$ 的极点消失了）。  
推导 4.3 (能量 $E_n^{(1)}, E_n^{(2)}$)  
我们将 $H_{eff}$ 作用在 $|\psi_n^{(0)}\rangle$ 上并取内积（对于非简并情况，这给出了标量本征值 $E$）：

$$E_n = \langle \psi_n^{(0)} | H_{eff}(E, \lambda) | \psi_n^{(0)} \rangle$$

$$E_n = \langle \psi_n^{(0)} \| (E_n^{(0)} P + \lambda PVP + \lambda^2 PVQ G_Q(E, \lambda) QVP) \| \psi_n^{(0)} \rangle $$

利用 $P|\psi_n^{(0)}\rangle = |\psi_n^{(0)}\rangle$ 和 $Q|\psi_n^{(0)}\rangle = 0$：

$$  
E_n = E_n^{(0)} + \lambda \langle \psi_n^{(0)} | V | \psi_n^{(0)} \rangle + \lambda^2 \langle \psi_n^{(0)} | V Q G_Q(E, \lambda) Q V | \psi_n^{(0)} \rangle $$

1. 一阶能量 $E_n^{(1)}$ [27](#ref-27]：  
   比较 $\lambda^1$ 的系数：

   $$E_n^{(1)} = \langle \psi_n^{(0)} | V | \psi_n^{(0)} \rangle$$  
2. 二阶能量 $E_n^{(2)}$ [27](#ref-27]：  
   比较 $\lambda^2$ 的系数。我们需要 $G_Q(E, \lambda)$ 的 $\lambda^0$ 阶近似，即 $S_n$：  

   $$ E_n^{(2)} = \langle \psi_n^{(0)} | V Q (S_n) Q V | \psi_n^{(0)} \rangle = \langle \psi_n^{(0)} | V S_n V | \psi_n^{(0)} \rangle $$  
   （因为 $S_n = Q S_n Q$）。  
   代入 $S_n$ 的求和形式：

   $$ E_n^{(2)} = \sum_{k \neq n} \langle \psi_n^{(0)} | V | \psi_k^{(0)} \rangle \frac{1}{E_n^{(0)} - E_k^{(0)}} \langle \psi_k^{(0)} | V | \psi_n^{(0)} \rangle $$  

   $$ E_n^{(2)} = \sum_{k \neq n} \frac{|\langle \psi_k^{(0)} | V | \psi_n^{(0)} \rangle|^2}{E_n^{(0)} - E_k^{(0)}} $$

推导 4.4 (波函数 $|\psi_n^{(1)}\rangle$)  
完整的波函数是 $|\psi_n\rangle = P|\psi_n\rangle + Q|\psi_n\rangle$。我们使用“中间归一化” (intermediate normalization)，即 $P|\psi_n\rangle = |\psi_n^{(0)}\rangle$（所有 $\\lambda$ 阶的修正都在 $Q$ 空间中）。  
我们需要 $Q|\psi_n\rangle$ 的 $\\lambda^1$ 阶项，记为 $|\psi_n^{(1)}\rangle = Q |\psi_n^{(1)}\rangle$ [50](#ref-50]。  
从推导 4.1 的 (6) 式：

$$Q|\\psi\\rangle = G\_Q(E, \\lambda) \\cdot (\\lambda QVP) P|\\psi\\rangle$$  
$$Q|\\psi\\rangle = \\lambda G\_Q(E, \\lambda) V |\\psi\_n^{(0)}\\rangle$$

我们需要 $\\lambda^1$ 阶的项。我们使用 $G\_Q$ 的 $\\lambda^0$ 阶近似 $S\_n$：

$$ |\psi_n^{(1)}\rangle = \[ \lambda G_Q(E, \lambda) V |\psi_n^{(0)}\rangle \]{\mathcal{O}(\lambda^1)} = S_n V |\psi_n^{(0)}\rangle $$

$$代入 S_n 的求和形式：$$
|\psi_n^{(1)}\rangle = \sum_{k \neq n} |\psi_k^{(0)}\rangle \frac{\langle \psi_k^{(0)} | V | \psi_n^{(0)} \rangle}{E_n^{(0)} - E_k^{(0)}} $$

这个过程（Kato-Rellich 理论的计算方面）是完全严谨的 [14](#ref-14]。它不仅*证明*了 RSPT 级数的存在性 [46](#ref-46]，而且还提供了一个*系统*的算法来计算任意阶的修正 [35](#ref-35]。

### **4.5 简并情况的处理**

标准 RSPT 教科书通常需要一个完全独立的章节来处理简并微扰理论 (degenerate perturbation theory) [27](#ref-27]。

预解式方法的真正威力在于，它**统一**了简并和非简并情况。

在 $E_n^{(0)}$ 是 $m$ 维简并的情况下，推导 4.1 和 4.2 *保持完全不变*。唯一的区别是：

1. $P = P_n^{(0)}$ 不再是一维投影，而是投影到 $m$ 维的简并子空间。  
2. $H_{eff}(E, \lambda) P\|\psi\rangle = E P\|\psi\rangle$ 不再是一个标量方程，而是一个 $m \times m$ 的**矩阵本征值问题**。

我们来看一阶近似：

$$H_{eff}(E, \lambda) \approx E_n^{(0)} P + \lambda PVP$$

$H_{eff}$ 的本征值 $E \approx E_n^{(0)} + \lambda E^{(1)}$ 必须满足：

$$(E_n^{(0)} P + \lambda PVP) P|\psi\rangle = (E_n^{(0)} + \lambda E^{(1)}) P|\psi\rangle$$  
$$\lambda (PVP) P|\psi\rangle = \lambda E^{(1)} P|\psi\rangle$$

这等价于：在简并子空间 $P$ 中，求解 $PVP$ 算符的本征值 $E^{(1)}$。这正是标准教科书中“在简并子空间中对角化微扰 $V$”的步骤。  
因此，简并情况只是 $H_{eff}$ 的 $P$ 空间维数 $m > 1$ 的情况。非简并情况是 $m=1$ 的平凡特例。Kato 的预解式方法 [37](#ref-37]（以及 [26](#ref-26) 中的划分方法）从一开始就统一处理了这两种情况。

## **第五部分：结论与展望**

### **5.1 总结：预解式——连接解析函数论与线性算符的桥梁**

本报告从泛函分析的基础出发，系统地回答了用户关于预解式算符 $G(z, A) = (z - A)^{-1}$ 的核心问题。预解式是现代数学物理的基石 [8](#ref-8]，它将线性算符 $A$ 的（通常很棘手的）谱理论问题，巧妙地转化为了复值函数 $G(z)$ 的（相对易于处理的）解析性质问题。

我们已经严格证明了：

1. “为什么预解式的极点...能给出那些信息？”  
   答案：因为算符的孤立本征值（点谱）被定义为 $G(z)$ 的极点。如 Riesz 投影（第二部分，证明 2.2）所示，通过留数定理，极点的位置给出了本征值 $E_n$，而极点的留数则严格地给出了到该本征子空间的投影算符 $P_n$ [14](#ref-14]，后者完整地编码了本征态的信息。  
2. “为什么预解式的...割线能给出那些信息？”  
   答案：因为算符的连续谱被定义为 $G(z)$ 的分支割线 [8](#ref-8]。如 Stone 公式（第二部分，证明 2.5）所示，通过 Sokhotski–Plemelj 定理，预解式 $G(z)$ 跨越这条割线的不连续性（“跳跃”）就是谱密度函数 $dE_\lambda / d\lambda$ [24](#ref-24]，它编码了连续谱“本征态”的分布。  
3. “如何使用预解式理论进行微扰求解？”  
   答案：我们将 $H = H_0 + V$ 的微扰问题转化为 $G_0$ 到 $G$ 的微扰问题。通过 $P/Q$ 空间划分 [26](#ref-26] 和 Kato 的约化预解式 $S_n$ [30](#ref-30]，我们绕过了 $G_0$ 在 $E_n^{(0)}$ 处的奇异性，从而严格且系统地推导了 Rayleigh-Schrödinger 微扰理论的所有标准公式（$E_n^{(1)}, E_n^{(2)}, |\psi_n^{(1)}\rangle$），并统一了简并与非简并情况（第四部分）。

### **5.2 超越微扰：预解式在现代数学物理中的应用**

预解式形式主义的应用远不止于RSPT，它已渗透到数学物理的各个前沿领域：

* **散射理论 (Scattering Theory)**: 预解式 $G(z)$ 在连续谱割线上的边界值（“跳跃”）与 $T$ 矩阵和 $S$ 矩阵（散射矩阵）直接相关，是计算散射截面的核心 [10](#ref-10]。  
* **随机矩阵理论 (Random Matrix Theory)**: 在混沌和无序系统中，人们研究的不是单个 $G(z)$，而是预解式的系综平均 $\langle G(z) \rangle$。这个平均预解式满足的方程（Dyson方程的矩阵形式）决定了能级的普适统计分布 [42](#ref-42]。  
* **谱几何与数论 (Spectral Geometry & Number Theory)**: 在黎曼曲面上，Laplace 算符的预解式（格林函数）及其谱行列式，与数论中的 $L$-函数（如 Riemann Zeta 函数）深刻相关。$L$-函数的零点（“谱”）与预解式的极点（共振）之间存在着对应关系 [8](#ref-8]。

从19世纪 Rayleigh 对声波的经典研究 [29](#ref-29]，到20世纪 Schrödinger 的量子论 [27](#ref-27] 和 Kato 的泛函分析 [30](#ref-30]，再到21世纪对量子混沌与数论的探索 [8](#ref-8]，预解式形式主义始终是连接物理直觉与数学严谨性的最强大、最普适的工具之一。

#### **引用的著作**

<a id="ref-1"></a>1. Spectrum and resolvent of bounded linear operators | Functional Analysis Class Notes， [https://fiveable.me/functional-analysis/unit-8/spectrum-resolvent-bounded-linear-operators/study-guide/OcHYnGLAxbZAkIkV](https://fiveable.me/functional-analysis/unit-8/spectrum-resolvent-bounded-linear-operators/study-guide/OcHYnGLAxbZAkIkV)  
<a id="ref-2"></a>2. Resolvent set - Wikipedia， [https://en.wikipedia.org/wiki/Resolvent_set](https://en.wikipedia.org/wiki/Resolvent_set)  
<a id="ref-3"></a>3. Spectrum (functional analysis) - Wikipedia， [https://en.wikipedia.org/wiki/Spectrum_(functional_analysis)](https://en.wikipedia.org/wiki/Spectrum_\(functional_analysis\))  
<a id="ref-4"></a>4. Spectrum (functional analysis)， [https://www.impan.pl/~pmh/teach/algebra/additional/spectrum.pdf](https://www.impan.pl/~pmh/teach/algebra/additional/spectrum.pdf)  
<a id="ref-5"></a>5. 1 A Note on Spectral Theory， [https://www.math.chalmers.se/Math/Grundutb/CTH/tma401/0304/spectraltheory.pdf](https://www.math.chalmers.se/Math/Grundutb/CTH/tma401/0304/spectraltheory.pdf)  
<a id="ref-6"></a>6. The Resolvent of an Operator - UW Math Department - University of Washington， [https://sites.math.washington.edu/~hart/m556/Lecture1.pdf](https://sites.math.washington.edu/~hart/m556/Lecture1.pdf)  
<a id="ref-7"></a>7. Why should I look at the resolvent formalism and think it is a useful tool for spectral theory?， [https://mathoverflow.net/questions/372538/why-should-i-look-at-the-resolvent-formalism-and-think-it-is-a-useful-tool-for-s](https://mathoverflow.net/questions/372538/why-should-i-look-at-the-resolvent-formalism-and-think-it-is-a-useful-tool-for-s)  
<a id="ref-8"></a>8. Etudes of the resolvent.pdf - Stony Brook Mathematics Department ...， [https://www.math.stonybrook.edu/~leontak/Etudes%20of%20the%20resolvent.pdf](https://www.math.stonybrook.edu/~leontak/Etudes%20of%20the%20resolvent.pdf)  
<a id="ref-9"></a>9. Resolvent formalism - Wikipedia， [https://en.wikipedia.org/wiki/Resolvent\_formalism](https://en.wikipedia.org/wiki/Resolvent_formalism)  
<a id="ref-10"></a>10. NOTES ON 1-PARTICLE SCATTERING 1\. The resolvent and the propagator Given a Hamiltonian ˆH, the resolvent and time-propagator ar， [http://wwwteor.mi.infn.it/\~molinari/NOTES/Notes\_on\_1\_particle\_scattering.pdf](http://wwwteor.mi.infn.it/~molinari/NOTES/Notes_on_1_particle_scattering.pdf)  
<a id="ref-11"></a>11. Copyright cG 2019 by Robert G. Littlejohn Physics 221B Spring ...， [https://bohr.physics.berkeley.edu/classes/221/1112/notes/lippschw.pdf](https://bohr.physics.berkeley.edu/classes/221/1112/notes/lippschw.pdf)  
<a id="ref-12"></a>12. Resolvent 81 Resolvent Let V be a finite-dimensional vector space and L G C(V). If Q /G σ(L), then the operator L - QI is inver， [https://sites.math.washington.edu/\~burke/crs/554/notes/ch16.pdf](https://sites.math.washington.edu/~burke/crs/554/notes/ch16.pdf)  
<a id="ref-13"></a>13. Spectral theory - Wikipedia， [https://en.wikipedia.org/wiki/Spectral\_theory](https://en.wikipedia.org/wiki/Spectral_theory)  
<a id="ref-14"></a>14. Perturbation Theory - Niels Benedikter， [https://nielsbenedikter.de/advmaphys2/pert-theory.pdf](https://nielsbenedikter.de/advmaphys2/pert-theory.pdf)  
<a id="ref-15"></a>15. Beyond the Spectral Theorem: Spectrally Decomposing Arbitrary Functions of Nondiagonalizable Operators， [https://csc.ucdavis.edu/\~cmg/papers/bst.pdf](https://csc.ucdavis.edu/~cmg/papers/bst.pdf)  
<a id="ref-16"></a>16. functional analysis - Why are nonzero eigenvalues of a compact ...， [https://math.stackexchange.com/questions/2880361/why-are-nonzero-eigenvalues-of-a-compact-operator-poles-of-its-resolvent](https://math.stackexchange.com/questions/2880361/why-are-nonzero-eigenvalues-of-a-compact-operator-poles-of-its-resolvent)  
<a id="ref-17"></a>17. Compact resolvents 1\. Application of perturbation theory， [https://www-users.cse.umn.edu/\~garrett/m/fun/compact\_resolvent.pdf](https://www-users.cse.umn.edu/~garrett/m/fun/compact_resolvent.pdf)  
<a id="ref-18"></a>18. reference request \- Eigenprojection as Contour Integral over ...， [https://math.stackexchange.com/questions/153690/eigenprojection-as-contour-integral-over-resolvent](https://math.stackexchange.com/questions/153690/eigenprojection-as-contour-integral-over-resolvent)  
<a id="ref-19"></a>19. Residue of trace of resolvent \- linear algebra \- Math Stack Exchange， [https://math.stackexchange.com/questions/1786324/residue-of-trace-of-resolvent](https://math.stackexchange.com/questions/1786324/residue-of-trace-of-resolvent)  
<a id="ref-20"></a>20. 80 Linear Algebra and Matrix Analysis Resolvent Let V be a finite-dimensional vector space and L G C(V). If c /G σ(L), then the， [https://sites.math.washington.edu/\~greenbau/Math\_554/Course\_Notes/ch1.6.pdf](https://sites.math.washington.edu/~greenbau/Math_554/Course_Notes/ch1.6.pdf)  
<a id="ref-21"></a>21. quantum mechanics \- Resolvent Operator in QM \- Physics Stack ...， [https://physics.stackexchange.com/questions/339111/resolvent-operator-in-qm](https://physics.stackexchange.com/questions/339111/resolvent-operator-in-qm)  
<a id="ref-22"></a>22. Proof that the continuous part of a spectrum really is "interval like"? \- Math Stack Exchange， [https://math.stackexchange.com/questions/3849562/proof-that-the-continuous-part-of-a-spectrum-really-is-interval-like](https://math.stackexchange.com/questions/3849562/proof-that-the-continuous-part-of-a-spectrum-really-is-interval-like)  
<a id="ref-23"></a>23. Computing Spectral Measures and Spectral Types \- DAMTP， [https://www.damtp.cam.ac.uk/user/mjc249/pdfs/SpecMeasuresMJC.pdf](https://www.damtp.cam.ac.uk/user/mjc249/pdfs/SpecMeasuresMJC.pdf)  
<a id="ref-24"></a>24. functional analysis \- Proving Stone's Formula for Constructively ...， [https://math.stackexchange.com/questions/1009409/proving-stones-formula-for-constructively-obtaining-the-spectral-measure-for-a](https://math.stackexchange.com/questions/1009409/proving-stones-formula-for-constructively-obtaining-the-spectral-measure-for-a)  
<a id="ref-25"></a>25. fa.functional analysis \- Spectral measure and Stone's theorem ...， [https://mathoverflow.net/questions/150913/spectral-measure-and-stones-theorem](https://mathoverflow.net/questions/150913/spectral-measure-and-stones-theorem)  
<a id="ref-26"></a>26. Chapter 17\. Time-Independent Perturbation Theory of Non ...， [https://people.chem.ucsb.edu/metiu/horia/OldFiles/QM2015/Ch17QM.pdf](https://people.chem.ucsb.edu/metiu/horia/OldFiles/QM2015/Ch17QM.pdf)  
<a id="ref-27"></a>27. Perturbation theory (quantum mechanics) \- Wikipedia， [https://en.wikipedia.org/wiki/Perturbation\_theory\_(quantum\_mechanics)](https://en.wikipedia.org/wiki/Perturbation_theory_\(quantum_mechanics\))  
<a id="ref-28"></a>28. RAYLEIGH-SCHR¨ODINGER PERTURBATION ... \- Hikari Ltd， [https://www.m-hikari.com/mccartin.pdf](https://www.m-hikari.com/mccartin.pdf)  
<a id="ref-29"></a>29. The pre-history of 20th century acoustics: the legacy of Lord Rayleigh， [https://dael.euracoustics.org/confs/fa2023/data/articles/000143.pdf](https://dael.euracoustics.org/confs/fa2023/data/articles/000143.pdf)  
<a id="ref-30"></a>30. Tosio Kato's work on non-relativistic quantum mechanics: part 1， [https://d-nb.info/1159765766/34](https://d-nb.info/1159765766/34)  
<a id="ref-31"></a>31. 1926-Schrodinger.pdf， [https://ee.sharif.edu/\~sarvari/25290/1926-Schrodinger.pdf](https://ee.sharif.edu/~sarvari/25290/1926-Schrodinger.pdf)  
<a id="ref-32"></a>32. Fifty years of eigenvalue perturbation theory \- ResearchGate， [https://www.researchgate.net/publication/239991927\_Fifty\_years\_of\_eigenvalue\_perturbation\_theory](https://www.researchgate.net/publication/239991927_Fifty_years_of_eigenvalue_perturbation_theory)  
<a id="ref-33"></a>33. On the perturbation theory of closed linear operators. \- Project Euclid， [https://projecteuclid.org/journals/journal-of-the-mathematical-society-of-japan/volume-4/issue-3-4/On-the-perturbation-theory-of-closed-linear-operators/10.2969/jmsj/00430323.pdf](https://projecteuclid.org/journals/journal-of-the-mathematical-society-of-japan/volume-4/issue-3-4/On-the-perturbation-theory-of-closed-linear-operators/10.2969/jmsj/00430323.pdf)  
<a id="ref-34"></a>34. Perturbation Theory， [https://webhomes.maths.ed.ac.uk/\~v1ranick/papers/kato1.pdf](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/kato1.pdf)  
<a id="ref-35"></a>35. Kato perturbation expansion in classical mechanics and an explicit expression for a Deprit generator. \- arXiv， [https://arxiv.org/pdf/1307.3368](https://arxiv.org/pdf/1307.3368)  
<a id="ref-36"></a>36. Perturbation Theory， [https://dl.icdst.org/pdfs/files3/a7adfee17f4de1980378c675da417acd.pdf](https://dl.icdst.org/pdfs/files3/a7adfee17f4de1980378c675da417acd.pdf)  
<a id="ref-37"></a>37. Perturbation Theory for Linear Operators \- Ruda's Personal Wiki， [https://wiki.ruda.city/Perturbation-Theory-for-Linear-Operators](https://wiki.ruda.city/Perturbation-Theory-for-Linear-Operators)  
<a id="ref-38"></a>38. Resolvent Formulas, Special and General 98 \- RIMS, Kyoto University， [https://www.kurims.kyoto-u.ac.jp/\~kyodo/kokyuroku/contents/pdf/1234-8.pdf](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1234-8.pdf)  
<a id="ref-39"></a>39. Born series - Wikipedia， [https://en.wikipedia.org/wiki/Born\_series](https://en.wikipedia.org/wiki/Born_series)  
<a id="ref-40"></a>40. 11.7 Levinson's Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278 11.8 Breit-Wigner Resonances . . . . - Jin Lei， [https://jinlei.fewbody.com/teaching/qm1\_12.pdf](https://jinlei.fewbody.com/teaching/qm1_12.pdf)  
<a id="ref-41"></a>41. Dyson series - Wikipedia， [https://en.wikipedia.org/wiki/Dyson\_series](https://en.wikipedia.org/wiki/Dyson_series)  
<a id="ref-42"></a>42. Self-consistent Dyson equation and self-energy functionals: An analysis and illustration on the example of the Hubbard atom | Phys. Rev. B， [https://link.aps.org/doi/10.1103/PhysRevB.96.045124](https://link.aps.org/doi/10.1103/PhysRevB.96.045124)  
<a id="ref-43"></a>43. The Matrix Dyson Equation in random matrix theory， [http://www.mat.uniroma3.it/users/giuliani/public\_html/Ischia\_Summer\_School/contenuti\_sito/slides/Erdos.pdf](http://www.mat.uniroma3.it/users/giuliani/public_html/Ischia_Summer_School/contenuti_sito/slides/Erdos.pdf)  
<a id="ref-44"></a>44. Neumann series of resolvent operator - Math Stack Exchange， [https://math.stackexchange.com/questions/5053150/neumann-series-of-resolvent-operator](https://math.stackexchange.com/questions/5053150/neumann-series-of-resolvent-operator)  
<a id="ref-45"></a>45. Resolvent Operator Formulation of Stationary State Perturbation ...， [https://pubs.aip.org/aip/jcp/article-pdf/40/7/1891/18832611/1891\_1\_online.pdf](https://pubs.aip.org/aip/jcp/article-pdf/40/7/1891/18832611/1891_1_online.pdf)  
<a id="ref-46"></a>46. First-order Perturbation Theory for Eigenvalues and Eigenvectors - arXiv， [https://arxiv.org/pdf/1903.00785](https://arxiv.org/pdf/1903.00785)  
<a id="ref-47"></a>47. A general formula for Rayleigh-Schroedinger perturbation energy utilizing a power series expansion of the quantum mechanical Hamiltonian - UNT Digital Library， [https://digital.library.unt.edu/ark:/67531/metadc679930/](https://digital.library.unt.edu/ark:/67531/metadc679930/)  
<a id="ref-48"></a>48. Perturbing scattering resonances in non-Hermitian systems: a， [https://arxiv.org/html/2408.11360v1](https://arxiv.org/html/2408.11360v1)  
<a id="ref-49"></a>49. Resolvent operator approach to many-body perturbation theory. II ...， [https://pubs.aip.org/aip/jcp/article-pdf/76/4/1979/18934698/1979\_1\_online.pdf](https://pubs.aip.org/aip/jcp/article-pdf/76/4/1979/18934698/1979_1_online.pdf)  
<a id="ref-50"></a>50. Rayleigh-Schr\"odinger many-body perturbation theory for density functionals: A unified treatment of one- and two-electron perturbations | Phys. Rev. A - Physical Review Link Manager， [https://link.aps.org/doi/10.1103/PhysRevA.78.022510](https://link.aps.org/doi/10.1103/PhysRevA.78.022510)  
<a id="ref-51"></a>51. Given a perturbation of a symmetric matrix, find an expansion for the eigenvalues， [https://math.stackexchange.com/questions/626425/given-a-perturbation-of-a-symmetric-matrix-find-an-expansion-for-the-eigenvalue](https://math.stackexchange.com/questions/626425/given-a-perturbation-of-a-symmetric-matrix-find-an-expansion-for-the-eigenvalue)  
<a id="ref-52"></a>52. Rayleigh-Schrödinger Perturbation Theory， [https://www.chemistry.tcd.ie/assets/pdf/ss/DAMB/DAMB%20SS/PERTURBATION%20THEORY.pdf](https://www.chemistry.tcd.ie/assets/pdf/ss/DAMB/DAMB%20SS/PERTURBATION%20THEORY.pdf)  
<a id="ref-53"></a>53. NUMERICAL METHODS FOR LARGE EIGENVALUE PROBLEMS Second edition Yousef Saad - College of Science and Engineering， [https://www-users.cse.umn.edu/~saad/eig_book_2ndEd.pdf](https://www-users.cse.umn.edu/~saad/eig_book_2ndEd.pdf)  
<a id="ref-54"></a>54. [2510.21947] Asymptotics for eigenvalues of one-dimensional Dirac operators in the weak coupling limit - arXiv， [https://arxiv.org/abs/2510.21947](https://arxiv.org/abs/2510.21947)  
<a id="ref-55"></a>55. [1307.3368] Kato perturbation expansion in classical mechanics and an explicit expression for a Deprit generator - arXiv， [https://arxiv.org/abs/1307.3368](https://arxiv.org/abs/1307.3368)  
<a id="ref-56"></a>56. Analytic properties of Resolvents - arXiv， [https://arxiv.org/pdf/1907.01444](https://arxiv.org/pdf/1907.01444)