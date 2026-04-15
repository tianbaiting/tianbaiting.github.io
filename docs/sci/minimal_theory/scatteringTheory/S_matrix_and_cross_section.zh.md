# S 矩阵与散射截面

本文按照 Taylor 教科书的逻辑链条，正面建立非相对论散射理论的核心框架。全文只用薛定谔表象。

**贯穿全文的核心区分**：

| 名称 | 记号 | 身份 | 角色 |
|:--|:--|:--|:--|
| 通道基矢 / 自由参考态 | $\|\alpha\rangle$ | $H_0$ 的广义本征矢 | **坐标轴 / 标签** |
| 自由波包 | $\|\phi\rangle = \int g(\alpha)\|\alpha\rangle\,d\alpha$ | 归一化的自由态 | 渐近条件的**参考对象** |
| 入出态 / 渐近态 | $\|\psi_\alpha^{(\pm)}\rangle = \Omega_\pm\|\alpha\rangle$ | $H$ 的广义本征矢 | **物理散射态** |
| 时变态 | $\|\Psi(t)\rangle = e^{-iHt}\|\Psi(0)\rangle$ | 真实演化的波包 | 实验中的**被测对象** |

> 渐近态不是自由态。
> 渐近态是完整哈密顿量 $H$ 的精确态，它在远时极限与某个自由参考传播不可区分，但在有限时间、有限距离内与自由态完全不同。

## 0. 散射问题的物理图景

设两体经由短程势 $V(r)$ 散射。在质心系中，问题约化为一个粒子被固定势 $V$ 散射，哈密顿量为

$$
H = H_0 + V, \qquad H_0 = \frac{p^2}{2\mu}
$$

其中 $\mu$ 是约化质量。

散射的时间演化图像：

1. **远过去** $t \to -\infty$：粒子远离散射中心，$V \approx 0$，真实传播与自由传播不可区分。
2. **有限时间**：粒子进入相互作用区，受 $V$ 作用发生散射。
3. **远未来** $t \to +\infty$：粒子再次远离，$V \approx 0$，真实传播再次与某个自由传播不可区分。

关键在于：在第 1 步和第 3 步中，我们并没有"关掉" $V$。$V$ 始终存在于哈密顿量中；只是粒子在远处时几乎不感受到它。因此，远过去和远未来的态仍然是 $H$（而非 $H_0$）的态。

## 1. 通道基矢：坐标轴，不是物理态

自由哈密顿量 $H_0$ 的广义本征态记为

$$
H_0 |\alpha\rangle = E_\alpha |\alpha\rangle
$$

这里的 $|\alpha\rangle$ 可以是平面波 $|\mathbf{p}\rangle$，也可以是自由球面波 $|E,l,m\rangle$，或任何一组完整的自由状态标签。

它们的性质：

- **$\delta$-归一化的广义本征矢**：$\langle \alpha | \alpha' \rangle = \delta(\alpha - \alpha')$。
- **不可归一化**：单个 $|\alpha\rangle$ 不是 Hilbert 空间中的物理态。
- **作用是标签和坐标轴**：用来标记动量、角动量、自旋等量子数，并作为展开其他态的基底。

所以 $\{|\alpha\rangle\}$ 是自由参考空间中的一组坐标轴。任何可归一化的自由态——即真正的物理自由波包——都是这些坐标轴上的"矢量"：

$$
|\phi\rangle = \int d\alpha\; g(\alpha)\, |\alpha\rangle, \qquad \int |g(\alpha)|^2\, d\alpha = 1
$$

**判据**：

- 基矢 $|\alpha\rangle$：$\delta$-归一化，数学对象；不能直接出现在概率公式里。
- 波包 $|\phi\rangle$：平方可积，物理对象；可以谈它"被测量到"的概率。

## 2. 渐近条件（Asymptotic Condition）

这是整个散射理论的出发公设（Taylor §2.5）。

**渐近条件**：对于散射问题中的每一个物理态 $|\Psi\rangle$（$H$ 下演化的真实态），存在两个归一化的自由波包 $|\phi_\text{in}\rangle$ 和 $|\phi_\text{out}\rangle$，使得

$$
\lim_{t \to -\infty} \left\| e^{-iHt} |\Psi\rangle - e^{-iH_0 t} |\phi_\text{in}\rangle \right\| = 0
$$

$$
\lim_{t \to +\infty} \left\| e^{-iHt} |\Psi\rangle - e^{-iH_0 t} |\phi_\text{out}\rangle \right\| = 0
$$

逐条解读：

1. **这是关于波包的陈述**。$|\phi_\text{in}\rangle$ 和 $|\phi_\text{out}\rangle$ 是归一化的自由波包，不是平面波基矢。渐近条件说的是两个波包在远时极限下的范数之差趋于零，而范数只对可归一化的态有定义。
2. **真实态始终在 $H$ 下演化**。左边的 $e^{-iHt}|\Psi\rangle$ 是包含相互作用的完整演化，不是把 $V$ 关掉后的自由演化。
3. **"不可区分"是在 $t \to \pm\infty$ 意义下的**。在有限时间内，$e^{-iHt}|\Psi\rangle$ 和 $e^{-iH_0 t}|\phi_\text{in}\rangle$ 一般完全不同——粒子正处于散射区。
4. **同一个真实态 $|\Psi\rangle$ 对应两个不同的自由波包**。$|\phi_\text{in}\rangle$ 描述了远过去的渐近行为，$|\phi_\text{out}\rangle$ 描述了远未来的渐近行为。散射的全部信息就蕴含在 $|\phi_\text{in}\rangle \to |\phi_\text{out}\rangle$ 的映射中。
5. **束缚态被排除在外**。渐近条件只对散射态（连续谱态）成立。如果 $H$ 有束缚态，那些态在 $t \to \pm\infty$ 时不会"跑到远处"，没有自由波包与之对应。

## 3. Møller 算符

### 3.1 定义

渐近条件的等价写法是

$$
|\Psi\rangle = \lim_{t \to -\infty} e^{iHt} e^{-iH_0 t} |\phi_\text{in}\rangle
$$

（这通过在两边乘 $e^{iHt}$ 并取 $t \to -\infty$ 极限从渐近条件的第一式推出。）

由此定义 **Møller 算符**（也叫波算符）：

$$
\Omega_+ = \operatorname*{s-lim}_{t \to -\infty} e^{iHt} e^{-iH_0 t}
$$

$$
\Omega_- = \operatorname*{s-lim}_{t \to +\infty} e^{iHt} e^{-iH_0 t}
$$

这里 "s-lim" 表示强算符极限：对每个固定的归一化态 $|\phi\rangle$，$\Omega_\pm |\phi\rangle$ 作为 Hilbert 空间中的矢量收敛。

于是渐近条件可以简洁地写成：

$$
|\Psi\rangle = \Omega_+ |\phi_\text{in}\rangle = \Omega_- |\phi_\text{out}\rangle
$$

### 3.2 物理含义

$\Omega_+$ 做的事情是：

> 给定一个自由波包 $|\phi_\text{in}\rangle$（你在远过去"看到"的样子），找到那个在完整动力学下会演化成在 $t \to -\infty$ 时与这个自由波包不可区分的真实散射态。

换句话说，$\Omega_+$ 把自由参考空间中的态（标签）映射到完整物理空间中的散射态（物理态）。

$\Omega_-$ 的含义类似，只是参考时刻换成了 $t \to +\infty$。

### 3.3 关键性质

**等距性**。$\Omega_\pm$ 保持内积：

$$
\langle \Omega_\pm \phi | \Omega_\pm \chi \rangle = \langle \phi | \chi \rangle
$$

这意味着 $\Omega_\pm^\dagger \Omega_\pm = \mathbf{1}$（自由空间上的恒等算符）。

**一般不酉**。如果 $H$ 存在束缚态，则 $\Omega_\pm$ 的值域不覆盖整个 Hilbert 空间（束缚态不在值域中）。此时 $\Omega_\pm \Omega_\pm^\dagger \neq \mathbf{1}$。

**渐近完备性**。如果 $\Omega_+$ 和 $\Omega_-$ 的值域相同（都等于散射子空间），则称系统满足**渐近完备性**。物理上这意味着：任何一个在远过去看起来自由的态，在远未来也看起来自由——没有粒子永远被困在相互作用区。对短程势，渐近完备性成立。

**交缠（intertwining）关系**：

$$
H \Omega_\pm = \Omega_\pm H_0
$$

这说明：如果 $|\alpha\rangle$ 是 $H_0$ 的能量为 $E_\alpha$ 的广义本征矢，则 $\Omega_\pm |\alpha\rangle$ 是 $H$ 的相同能量的广义本征矢。因此，

$$
|\psi_\alpha^{(\pm)}\rangle \equiv \Omega_\pm |\alpha\rangle
$$

是 $H$ 的广义本征矢，满足

$$
H |\psi_\alpha^{(\pm)}\rangle = E_\alpha |\psi_\alpha^{(\pm)}\rangle
$$

这就是**入态**（$+$）和**出态**（$-$）的定义。

### 3.4 再次强调：入出态是什么，不是什么

- $|\psi_\alpha^{(+)}\rangle$ 是完整 $H$ 的广义本征矢。它**不是**自由态。
- "$+$" 标记来自 $\Omega_+$，即远过去（$t \to -\infty$）的渐近条件。所以"入态"是指在远过去与自由参考态 $|\alpha\rangle$ 匹配的那个散射态。
- $|\alpha\rangle$ 只是用来标记 $|\psi_\alpha^{(+)}\rangle$ 的坐标。真正的物理对象是 $|\psi_\alpha^{(+)}\rangle$。
- $\{|\psi_\alpha^{(+)}\rangle\}$ 和 $\{|\psi_\alpha^{(-)}\rangle\}$ 各自构成散射子空间的一组完备基底（这从 $\Omega_\pm$ 的等距性和渐近完备性推出）。

## 4. S 算符

### 4.1 定义

同一个物理态 $|\Psi\rangle$ 对应两个自由波包：

$$
|\Psi\rangle = \Omega_+ |\phi_\text{in}\rangle = \Omega_- |\phi_\text{out}\rangle
$$

用 $\Omega_-^\dagger$ 作用于第一个等式：

$$
|\phi_\text{out}\rangle = \Omega_-^\dagger \Omega_+ |\phi_\text{in}\rangle
$$

（这里用到了 $\Omega_-^\dagger \Omega_- = \mathbf{1}$。）

定义 **S 算符**：

$$
S \equiv \Omega_-^\dagger \Omega_+
$$

它将入射自由波包映射到出射自由波包：

$$
|\phi_\text{out}\rangle = S |\phi_\text{in}\rangle
$$

### 4.2 S 算符的身份

$S$ 是定义在**自由参考空间**上的算符：输入和输出都是自由波包。它编码了散射的全部信息——把远过去的"标签"翻译成远未来的"标签"。

但 $S$ 本身不直接作用于真实的时变态。真实动力学由 $H$ 生成；$S$ 是这个动力学在自由参考空间上的"投影"。

### 4.3 S 的酉性

如果渐近完备性成立（$\Omega_+$ 和 $\Omega_-$ 的值域相同），则 $S$ 是酉的：

$$
S^\dagger S = S S^\dagger = \mathbf{1}
$$

物理含义：概率守恒。"进来多少概率，出去多少概率"。

### 4.4 S 矩阵元

在通道基矢上展开：

$$
S_{\beta\alpha} \equiv \langle \beta | S | \alpha \rangle = \langle \beta | \Omega_-^\dagger \Omega_+ | \alpha \rangle = \langle \psi_\beta^{(-)} | \psi_\alpha^{(+)} \rangle
$$

这条等式的两端：

- 左边是 $S$ 算符在**自由参考基底**中的矩阵元——一个纯粹的坐标表示。
- 右边是**入态和出态**（$H$ 的广义本征矢）之间的内积——真正的物理重叠。

自由基矢 $|\alpha\rangle$、$|\beta\rangle$ 只是坐标轴。真正的物理内容在 $|\psi^{(\pm)}\rangle$ 里。

## 5. 为什么渐近态的内积给出概率

### 5.1 探测器测量的是什么

设实验准备了一个入射波包态

$$
|\Psi_\text{in}\rangle = \Omega_+ |\Phi_\text{in}\rangle
$$

其中 $|\Phi_\text{in}\rangle$ 是归一化的自由波包。

探测器被放在某个方向上，调到接收某个出射通道——即一个归一化的自由波包 $|\chi_\beta\rangle$。这个通道在完整物理空间中对应的态是

$$
|\psi_\beta^{(-)}\rangle = \Omega_- |\chi_\beta\rangle
$$

### 5.2 正确的投影算符

"在远未来探测到出射通道 $|\chi_\beta\rangle$"这件事，在完整物理 Hilbert 空间中对应的投影算符不是在自由基矢上的投影

$$
|\chi_\beta\rangle\langle\chi_\beta| \quad (\text{错误！})
$$

而是 **out-projector**：

$$
Q_\beta^\text{out} = |\psi_\beta^{(-)}\rangle \langle \psi_\beta^{(-)}| = \Omega_- |\chi_\beta\rangle \langle \chi_\beta| \Omega_-^\dagger
$$

为什么？因为探测器工作在远未来的渐近区。它测到的"自由粒子"实际上是在完整 $H$ 下演化的散射态，只不过这个散射态在远未来与 $|\chi_\beta\rangle$ 的自由传播不可区分。所以正确的本征态是出态 $|\psi_\beta^{(-)}\rangle$，而非自由态 $|\chi_\beta\rangle$。

### 5.3 概率公式

由 Born 规则：

$$
P_{\beta \leftarrow \text{in}} = \langle \Psi_\text{in} | Q_\beta^\text{out} | \Psi_\text{in} \rangle = |\langle \psi_\beta^{(-)} | \Psi_\text{in} \rangle|^2
$$

将 $|\Psi_\text{in}\rangle = \Omega_+ |\Phi_\text{in}\rangle$ 代入：

$$
\langle \psi_\beta^{(-)} | \Psi_\text{in} \rangle = \langle \chi_\beta | \Omega_-^\dagger \Omega_+ | \Phi_\text{in} \rangle = \langle \chi_\beta | S | \Phi_\text{in} \rangle
$$

因此

$$
P_{\beta \leftarrow \text{in}} = |\langle \chi_\beta | S | \Phi_\text{in} \rangle|^2
$$

**总结**：概率之所以由 $S$ 矩阵元（或等价地由入出态的内积）给出，不是因为渐近态是自由态（它不是），而是因为：

1. 探测器测量的是远未来的渐近通道；
2. 渐近通道在物理空间中的正确投影是 out-projector $Q_\beta^\text{out}$；
3. out-projector 的本征态正是出态 $|\psi_\beta^{(-)}\rangle$；
4. 因此 Born 规则自然给出入出态的内积；
5. 由波算符的等距性，这个内积可以等价地写成自由参考空间中的 $S$ 矩阵元。

### 5.4 对一个末态窗口的推广

若探测器接收的不是单个通道而是一片末态区域 $\Delta$，则在自由参考空间中定义

$$
\Pi_\Delta = \int_\Delta d\beta\; |\beta\rangle\langle\beta|
$$

对应的物理 out-projector 为

$$
Q_\Delta^\text{out} = \Omega_- \Pi_\Delta \Omega_-^\dagger
$$

概率为

$$
P_\Delta = \langle \Phi_\text{in} | S^\dagger \Pi_\Delta S | \Phi_\text{in} \rangle
$$

这条式子比单个矩阵元更根本：Born 规则作用在物理 out-projector 上，$S^\dagger \Pi_\Delta S$ 只是这个物理投影在自由参考空间中的表示。

### 5.5 为什么有限时间下自由基底展开系数不是概率

在某个有限时刻 $t$，真实态总可以在自由基底上展开：

$$
|\Psi(t)\rangle = \int d\alpha\; c_t(\alpha)\, |\alpha\rangle
$$

但 $|c_t(\alpha)|^2$ 一般**不能**解释为"发现系统处于散射末态 $\alpha$ 的概率"，原因有三：

1. **这只是坐标展开**。$|\alpha\rangle$ 是自由参考基底，不是 out-projector 的本征态。
2. **通道尚未分离**。在有限时间内，系统可能仍处在相互作用区内，自由基底系数不对应任何清晰的通道探测。
3. **$\delta$-归一化的问题**。$|\alpha\rangle$ 是广义本征矢，$|c_t(\alpha)|^2$ 是概率密度，直接取模平方会碰到 $\delta$ 函数平方。

## 6. Lippmann-Schwinger 方程与定态散射 ket

### 6.1 从时域到定态

在 §3 中，入态的定义是通过波算符和远时极限给出的（时域定义）。对于定态散射问题，我们需要一个不显含时间的方程。

用通道基矢 $|\alpha\rangle$ 作为 $\Omega_+$ 的输入，定义入态

$$
|\psi_\alpha^{(+)}\rangle = \Omega_+ |\alpha\rangle
$$

由交缠关系 $H\Omega_+ = \Omega_+ H_0$，它满足

$$
H |\psi_\alpha^{(+)}\rangle = E_\alpha |\psi_\alpha^{(+)}\rangle
$$

即 $(E_\alpha - H_0 - V)|\psi_\alpha^{(+)}\rangle = 0$，也就是

$$
(E_\alpha - H_0)|\psi_\alpha^{(+)}\rangle = V |\psi_\alpha^{(+)}\rangle
$$

### 6.2 Lippmann-Schwinger 方程

上式的形式解需要 $(E_\alpha - H_0)$ 的逆，但 $E_\alpha$ 在 $H_0$ 的连续谱上，所以必须加 $i\epsilon$ 处方做正则化。由入射边界条件（outgoing spherical wave），正确的处方是

$$
|\psi_\alpha^{(+)}\rangle = |\alpha\rangle + G_0^+(E_\alpha)\, V\, |\psi_\alpha^{(+)}\rangle
$$

其中

$$
G_0^+(E) = \frac{1}{E - H_0 + i\epsilon}
$$

是自由推迟 Green 算符。

**再次强调**：

- $|\alpha\rangle$ 是自由参考态，是输入的标签/坐标。
- $|\psi_\alpha^{(+)}\rangle$ 是完整 $H$ 的广义本征矢，是输出的物理态。
- LS 方程将两者联系起来，但它们有本质区别。

出态的 LS 方程类似，只是用 $G_0^-(E) = 1/(E - H_0 - i\epsilon)$：

$$
|\psi_\alpha^{(-)}\rangle = |\alpha\rangle + G_0^-(E_\alpha)\, V\, |\psi_\alpha^{(-)}\rangle
$$

### 6.3 坐标表示

对势散射，取 $|\alpha\rangle = |\mathbf{k}\rangle$（动量本征态），LS 方程在坐标空间中为

$$
\psi_{\mathbf{k}}^{(+)}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} + \int d^3r'\; G_0^+(\mathbf{r}, \mathbf{r}'; E_k)\, V(\mathbf{r}')\, \psi_{\mathbf{k}}^{(+)}(\mathbf{r}')
$$

其中 $G_0^+(\mathbf{r}, \mathbf{r}'; E) = -\frac{\mu}{2\pi\hbar^2} \frac{e^{ik|\mathbf{r}-\mathbf{r}'|}}{|\mathbf{r}-\mathbf{r}'|}$。

在远场 $r \to \infty$ 下，利用 $|\mathbf{r} - \mathbf{r}'| \approx r - \hat{\mathbf{r}} \cdot \mathbf{r}'$：

$$
\psi_{\mathbf{k}}^{(+)}(\mathbf{r}) \xrightarrow{r \to \infty} e^{i\mathbf{k}\cdot\mathbf{r}} + f(\hat{\mathbf{r}}, \mathbf{k})\, \frac{e^{ikr}}{r}
$$

其中散射振幅

$$
f(\hat{\mathbf{r}}, \mathbf{k}) = -\frac{\mu}{2\pi\hbar^2} \int d^3r'\; e^{-i\mathbf{k}_f \cdot \mathbf{r}'}\, V(\mathbf{r}')\, \psi_{\mathbf{k}}^{(+)}(\mathbf{r}')
$$

这里 $\mathbf{k}_f = k\hat{\mathbf{r}}$。

**远场渐近形式的解读**：

- 第一项 $e^{i\mathbf{k}\cdot\mathbf{r}}$ 是自由参考平面波——不是物理态的一部分，而是渐近匹配的标签。
- 第二项 $f \cdot e^{ikr}/r$ 是散射出射球面波——这才是散射产生的物理效果。
- 整个 $\psi_{\mathbf{k}}^{(+)}(\mathbf{r})$ 是 $H$ 的精确广义本征函数。

## 7. T 算符

### 7.1 定义

定义 T 算符（壳上跃迁算符）使得 S 矩阵元可以分解为平凡部分和跃迁部分：

$$
\langle \beta | S | \alpha \rangle = \delta_{\beta\alpha} - 2\pi i\, \delta(E_\beta - E_\alpha)\, T_{\beta\alpha}(E_\alpha)
$$

其中

$$
T_{\beta\alpha}(E) = \langle \beta | V | \psi_\alpha^{(+)} \rangle = \langle \psi_\beta^{(-)} | V | \alpha \rangle
$$

### 7.2 物理含义

- $\delta_{\beta\alpha}$：直行项——粒子不散射，出去就是进来的那个态。
- $-2\pi i\, \delta(E)\, T$：跃迁项——粒子真正发生了从 $\alpha$ 到 $\beta \neq \alpha$ 的转变。
- 能量 $\delta$ 函数确保散射是能量守恒的（on-shell condition）。
- $T_{\beta\alpha}$ 是 $V$ 在入态 $|\psi_\alpha^{(+)}\rangle$ 上的矩阵元，编码了所有动力学信息。

### 7.3 关系链

$$
S_{\beta\alpha} = \langle \psi_\beta^{(-)} | \psi_\alpha^{(+)} \rangle \xrightarrow{\text{减去直行}} T_{\beta\alpha} = \langle \beta | V | \psi_\alpha^{(+)} \rangle \xrightarrow{\text{Born 近似}} T_{\beta\alpha}^\text{Born} = \langle \beta | V | \alpha \rangle
$$

Born 近似的含义正是：用自由基矢 $|\alpha\rangle$ 近似替代物理入态 $|\psi_\alpha^{(+)}\rangle$。这再次表明二者的区别。

## 8. 从跃迁率到散射截面

### 8.1 连续谱中的概率密度

当初末态都在连续谱中时，$S_{\beta\alpha}$ 包含 $\delta$ 函数，直接取模平方没有意义。物理可测量是在某个末态窗口 $\Delta$ 中的**跃迁概率**：

$$
P(\alpha \to \Delta) = \int_\Delta d\beta\; |S_{\beta\alpha} - \delta_{\beta\alpha}|^2
$$

对于 $\beta \neq \alpha$ 的跃迁（非前向散射），这简化为

$$
P(\alpha \to \Delta) = \int_\Delta d\beta\; (2\pi)^2\, [\delta(E_\beta - E_\alpha)]^2\, |T_{\beta\alpha}|^2
$$

这里出现了 $[\delta(E)]^2$。标准处理（Taylor §8.3）是用有限时间 $T$ 做正则化：

$$
2\pi\, [\delta(E_\beta - E_\alpha)]^2 \to \delta(E_\beta - E_\alpha) \cdot \frac{T}{2\pi\hbar}
$$

从而得到单位时间跃迁率

$$
\dot{P}(\alpha \to \Delta) = \frac{2\pi}{\hbar} \int_\Delta d\beta\; \delta(E_\beta - E_\alpha)\; |T_{\beta\alpha}|^2
$$

这就是 **Fermi 黄金规则**的散射版本。

### 8.2 散射截面的定义

实验中可控的量是入射流强 $j_\text{in}$，可测的量是出射事件率。截面的定义是

$$
d\sigma = \frac{\dot{P}}{j_\text{in}}
$$

即：单位时间跃迁率除以入射流。这样定义的截面与束流强度无关，是势 $V$ 的内禀性质。

### 8.3 两体弹性散射的微分截面

对约化质量为 $\mu$ 的两体弹性势散射，取入态为 $|\mathbf{k}_i\rangle$。

入射流（平面波 $e^{i\mathbf{k}_i \cdot \mathbf{r}}$ 的概率流密度）：

$$
j_\text{in} = \frac{\hbar k_i}{\mu}
$$

远场出射球面波 $f(\hat{\mathbf{r}}, \mathbf{k}_i)\, e^{ikr}/r$ 在立体角 $d\Omega$ 内的概率流：

$$
d\dot{P} = \frac{\hbar k_f}{\mu}\, |f(\hat{\mathbf{r}}, \mathbf{k}_i)|^2\, d\Omega
$$

因此

$$
\frac{d\sigma}{d\Omega} = \frac{d\dot{P}/d\Omega}{j_\text{in}} = \frac{k_f}{k_i}\, |f(\hat{\mathbf{r}}, \mathbf{k}_i)|^2
$$

对弹性散射 $k_f = k_i$：

$$
\frac{d\sigma}{d\Omega} = |f(\theta, \varphi)|^2
$$

这个公式为什么可测？因为它比较的是：

- **分子**：远未来出射通道中的概率流——由渐近态 $|\psi_{\mathbf{k}_i}^{(+)}\rangle$ 的远场行为决定。
- **分母**：远过去入射通道中的参考流——由自由态标签 $|\mathbf{k}_i\rangle$ 决定。

两者都定义在渐近区，而非相互作用区内部。

### 8.4 散射振幅与 T 矩阵元的关系

将 T 矩阵元与散射振幅联系起来（以 $\hbar = 1$ 单位制）：

$$
f(\hat{\mathbf{r}}, \mathbf{k}) = -4\pi^2 \mu\, T_{\mathbf{k}_f, \mathbf{k}}
$$

其中 $\mathbf{k}_f = k\hat{\mathbf{r}}$。这给出了从算符语言到波函数语言的翻译。

## 9. 总结：概念地图

整个理论的逻辑链条如下：

$$
\boxed{
\text{渐近条件}
\;\xrightarrow{\text{定义}}\;
\Omega_\pm
\;\xrightarrow{\text{定义}}\;
|\psi^{(\pm)}\rangle,\; S
\;\xrightarrow{\text{分解}}\;
T
\;\xrightarrow{\text{除以流}}\;
\sigma
}
$$

贯穿始终的核心区分：

| | 自由参考态 $\|\alpha\rangle$ | 入出态 $\|\psi_\alpha^{(\pm)}\rangle$ |
|:--|:--|:--|
| 满足的方程 | $H_0\|\alpha\rangle = E_\alpha \|\alpha\rangle$ | $H\|\psi_\alpha^{(\pm)}\rangle = E_\alpha \|\psi_\alpha^{(\pm)}\rangle$ |
| 身份 | 坐标轴 / 标签 | 物理散射态 |
| 包含相互作用？ | 否 | 是 |
| 在 S 矩阵中的角色 | 提供表示基底 | 提供物理内积 |

**一句话总结**：渐近态不是自由态。自由态是标签/坐标；入出态是完整 $H$ 下的物理散射态。S 矩阵是散射动力学从物理空间投影到自由参考空间后的表示。概率来自对物理渐近通道子空间的投影（out-projector），而不是来自对自由基底的展开系数。

**约定**：全文对短程势成立。对 Coulomb 等长程势，自由参考传播和波算符的具体形式需要修正，但核心概念结构不变。
