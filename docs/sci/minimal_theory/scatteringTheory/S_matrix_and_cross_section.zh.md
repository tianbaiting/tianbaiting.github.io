# S 矩阵、渐近态与散射截面

这篇笔记按 Taylor《Scattering Theory》的主线重写，目标不是堆公式，而是先把几件最容易混淆的事彻底分开：

1. 自由态不是渐近散射态。
2. 基矢不是物理态。
3. `S` 矩阵元是算符在某组基底下的核；可测概率要先回到波包与投影算符。

全文都在非相对论、短程相互作用、薛定谔表象下讨论。设

$$
H = H_0 + V, \qquad H_0 = \frac{p^2}{2\mu}.
$$

这里 $H_0$ 是自由哈密顿量，$V$ 是局域或短程势。严格地说，$H$ 与 $H_0$ 作用在同一个抽象 Hilbert 空间上；散射理论中的区别不是“有两个不同的态空间”，而是“同一个空间上有两套不同的动力学角色”：

- 用 $H_0$ 的本征态做参考，给入射和出射通道贴标签。
- 用 $H$ 的真实演化描述实验中真正发生的散射。

如果这两层不分开，后面关于渐近态、Lippmann-Schwinger 方程、`S` 矩阵和微分截面的所有说法都会变得含糊。

## 1. 先把四类对象分开

散射理论中最常见的四类对象如下。

1. 自由广义基矢：$|\alpha\rangle$，由 $H_0|\alpha\rangle = E_\alpha |\alpha\rangle$ 定义，$\delta$ 归一化，不可归一化；它的身份是通道标签和坐标轴。
2. 自由波包：$|\phi\rangle = \int d\alpha\, g(\alpha)|\alpha\rangle$，由 $H_0$ 的基底叠加得到，可归一化；它是可制备的自由参考态。
3. 入/出散射广义本征态：$|\psi_\alpha^{(\pm)}\rangle$，满足 $H|\psi_\alpha^{(\pm)}\rangle = E_\alpha |\psi_\alpha^{(\pm)}\rangle$ 并带有入/出边界条件，仍然是 $\delta$ 归一化；它是精确散射态的定态基矢。
4. 真实散射波包：$|\Psi\rangle$ 或 $|\Psi(t)\rangle$，由完整哈密顿量 $H$ 的动力学定义，可归一化；它才是实验中的物理态。

必须反复强调两点：

- 单个 $|\alpha\rangle$ 不是物理态。它像平面波一样是广义本征矢，只是坐标轴。
- 单个 $|\psi_\alpha^{(\pm)}\rangle$ 也不是可归一化的实验态。它是完整哈密顿量 $H$ 的广义本征矢，用来展开真正的散射波包。

所以“基矢”和“物理态”的区别，不是自由理论才有、相互作用理论就没有；两边都有。自由侧有 $|\alpha\rangle$，相互作用侧有 $|\psi_\alpha^{(\pm)}\rangle$。真正可测的总是波包，而不是单个广义本征矢。

## 2. 基底只是坐标，不是物理对象

设 $\{|\alpha\rangle\}$ 是 $H_0$ 的一组完备广义本征态。$\alpha$ 可以是：

- 动量 $\mathbf p$；
- 能量与角动量 $(E,l,m)$；
- 或者更一般的一组通道量子数。

它们满足

$$
H_0 |\alpha\rangle = E_\alpha |\alpha\rangle, \qquad
\langle \alpha | \alpha' \rangle = \delta(\alpha-\alpha').
$$

因此它们本身不属于通常意义下的 Hilbert 空间，而属于配备 Hilbert 空间中的广义向量。它们的作用是：

1. 标记守恒量或通道量子数。
2. 提供展开任意自由波包的基底。
3. 给 `S`、`T` 这类算符提供矩阵表示。

真正的自由物理态必须是归一化波包：

$$
|\phi\rangle = \int d\alpha\, g(\alpha)|\alpha\rangle,
\qquad
\int d\alpha\, |g(\alpha)|^2 = 1.
$$

同样，真正的散射物理态也必须是散射广义本征态的波包叠加：

$$
|\Psi^{(+)}[g]\rangle
=
\int d\alpha\, g(\alpha)\, |\psi_\alpha^{(+)}\rangle,
$$

或者

$$
|\Psi^{(-)}[g]\rangle
=
\int d\alpha\, g(\alpha)\, |\psi_\alpha^{(-)}\rangle.
$$

一句话概括：

- $|\alpha\rangle$ 是自由理论的坐标轴。
- $|\psi_\alpha^{(\pm)}\rangle$ 是完整理论的坐标轴。
- $g(\alpha)$ 这样的包络函数乘上这些坐标轴以后，才得到真正的物理波包。

## 3. 散射问题首先是一个时间相关问题

Taylor 的逻辑起点不是先写 Lippmann-Schwinger 方程，而是先问：

“实验里所谓入射态和出射态，到底是什么意思？”

设系统在远过去是一束远离散射中心的粒子。因为势是短程的，粒子在远处时几乎感觉不到 $V$，所以真实传播会渐近地接近某个自由传播。类似地，在远未来，散射后的粒子远离散射区时，真实传播也会渐近地接近另一个自由传播。

这才是“入态”和“出态”的物理含义。

### 3.1 渐近条件

对每个散射物理态 $|\Psi\rangle$，存在两个归一化自由波包 $|\phi_{\mathrm{in}}\rangle$ 与 $|\phi_{\mathrm{out}}\rangle$，使得

$$
\lim_{t\to -\infty}
\left\|
e^{-iHt}|\Psi\rangle
-e^{-iH_0 t}|\phi_{\mathrm{in}}\rangle
\right\|
=0,
$$

$$
\lim_{t\to +\infty}
\left\|
e^{-iHt}|\Psi\rangle
-e^{-iH_0 t}|\phi_{\mathrm{out}}\rangle
\right\|
=0.
$$

这两条式子是散射理论最核心的定义。它们有几个关键含义：

1. 这是关于归一化波包的陈述，不是关于单个平面波的陈述。
2. 左边始终是完整哈密顿量 $H$ 的真实演化，整个过程中并没有把相互作用“关掉”。
3. 渐近条件说的是远时极限下“不可区分”，并不意味着在有限时间内真实态等于自由态。
4. 同一个真实散射态对应两个不同的自由参考波包：一个描述远过去，一个描述远未来。

因此，渐近态不是自由态。更准确的说法是：

“渐近散射态是在完整动力学下定义的精确态，它在远过去或远未来与某个自由波包的传播不可区分。”

### 3.2 束缚态为什么不在这里面

若 $H$ 有束缚态，它们在 $t\to\pm\infty$ 并不会跑到无穷远去，也不会接近任何自由传播，因此不满足上面的渐近条件。散射理论的 `S` 算符只作用在散射子空间上，而不是整个 Hilbert 空间。

## 4. Møller 算符：把自由参考态映到真实散射态

由渐近条件定义波算符（Møller operators）：

$$
\Omega_+
=
s\text{-}\lim_{t\to -\infty} e^{iHt}e^{-iH_0 t},
\qquad
\Omega_-
=
s\text{-}\lim_{t\to +\infty} e^{iHt}e^{-iH_0 t}.
$$

这里 `s-lim` 是强极限。于是

$$
|\Psi\rangle = \Omega_+ |\phi_{\mathrm{in}}\rangle
=
\Omega_- |\phi_{\mathrm{out}}\rangle.
$$

这说明：

- $\Omega_+$ 取一个自由入射波包，生成与之对应的真实散射波包。
- $\Omega_-$ 取一个自由出射波包，生成与之对应的真实散射波包。

### 4.1 交缠关系

波算符满足

$$
H\Omega_\pm = \Omega_\pm H_0.
$$

所以如果 $|\alpha\rangle$ 是 $H_0$ 的广义本征矢，那么

$$
|\psi_\alpha^{(\pm)}\rangle \equiv \Omega_\pm |\alpha\rangle
$$

就是 $H$ 的广义本征矢，并且

$$
H|\psi_\alpha^{(\pm)}\rangle = E_\alpha |\psi_\alpha^{(\pm)}\rangle.
$$

这就是入态与出态的定态定义。

但这里很容易犯一个错误：把

$$
|\psi_\alpha^{(\pm)}\rangle = \Omega_\pm |\alpha\rangle
$$

理解成“把一个真实物理态从自由态轻微修正了一下”。

这不对。正确理解是：

- $|\alpha\rangle$ 是自由理论的广义基矢。
- $|\psi_\alpha^{(\pm)}\rangle$ 是完整理论的广义基矢。
- $\Omega_\pm$ 给出了两组广义基矢之间的对应关系。

它本质上是“换基并附上正确的边界条件”，不是把单个不可归一化平面波直接当成实验里的入射束。

### 4.2 等距性与散射子空间

在散射子空间上，$\Omega_\pm$ 是等距映射：

$$
\Omega_\pm^\dagger \Omega_\pm = \mathbf 1.
$$

若渐近完备成立，则

$$
\mathrm{Ran}\,\Omega_+ = \mathrm{Ran}\,\Omega_- = \mathcal H_{\mathrm{scatt}},
$$

并且

$$
\Omega_\pm \Omega_\pm^\dagger = P_{\mathrm{scatt}}.
$$

这时 `S` 算符在自由侧是酉的。

## 5. `S` 算符活在自由参考表象里

同一个真实散射波包既可以写成

$$
|\Psi\rangle = \Omega_+|\phi_{\mathrm{in}}\rangle,
$$

也可以写成

$$
|\Psi\rangle = \Omega_-|\phi_{\mathrm{out}}\rangle.
$$

于是

$$
|\phi_{\mathrm{out}}\rangle
=
\Omega_-^\dagger \Omega_+ |\phi_{\mathrm{in}}\rangle.
$$

定义

$$
S \equiv \Omega_-^\dagger \Omega_+.
$$

所以 `S` 算符的真正身份是：

“把远过去的自由参考数据映成远未来的自由参考数据。”

它不是完整动力学的时间演化算符。完整动力学永远由 $e^{-iHt}$ 生成；`S` 是把真实散射过程投影到自由通道标签上的结果。

### 5.1 `S` 矩阵元是什么

在自由广义基底上，

$$
S_{\beta\alpha}
\equiv
\langle \beta|S|\alpha\rangle
=
\langle \psi_\beta^{(-)} | \psi_\alpha^{(+)}\rangle.
$$

这条公式很重要，但更重要的是如何解释它：

- 左边是 `S` 算符在自由基底中的核。
- 右边是两套不同边界条件下的散射广义本征态的重叠。

两边都不是“两个可归一化实验态的普通内积”。它们都是分布意义下的核。

### 5.2 为什么说它只是核，不是裸概率

若直接把 $S_{\beta\alpha}$ 中的 $\alpha,\beta$ 看成两个单平面波通道，那么这只是一个分布核。真正有物理意义的是把它和波包包络函数卷起来：

$$
\mathcal A[\chi,\phi]
\equiv
\langle \chi|S|\phi\rangle
=
\iint d\beta\, d\alpha\;
\chi^*(\beta)\, S_{\beta\alpha}\, \phi(\alpha),
$$

其中 $|\phi\rangle$、$|\chi\rangle$ 都是归一化自由波包。

只有这样经过波包卷积后的振幅，才是实验上可用的跃迁幅。

因此：

- “basis” 是 $|\alpha\rangle$、$|\beta\rangle$ 这样的坐标轴。
- “physical state” 是 $|\phi\rangle$、$|\chi\rangle$ 这样的归一化波包。
- `S_{\beta\alpha}` 是核，不是单独可测的概率。

## 6. 为什么概率必须用 out-projector 来写

设实验制备了一个入射自由波包 $|\phi_{\mathrm{in}}\rangle$。相应的真实散射态是

$$
|\Psi\rangle = \Omega_+ |\phi_{\mathrm{in}}\rangle.
$$

若探测器在远未来选择某个出射自由波包 $|\chi\rangle$，那么对应的物理投影不是

$$
|\chi\rangle\langle\chi|
$$

本身，而是

$$
Q_\chi^{\mathrm{out}}
=
\Omega_- |\chi\rangle\langle\chi| \Omega_-^\dagger.
$$

原因很简单：探测器看到的是完整动力学在远未来形成的出射通道，而不是“把相互作用完全删掉后”的自由态。

于是 Born 规则给出

$$
P_{\chi\leftarrow \phi_{\mathrm{in}}}
=
\langle\Psi|Q_\chi^{\mathrm{out}}|\Psi\rangle
=
\left|\langle \chi|S|\phi_{\mathrm{in}}\rangle\right|^2.
$$

这条式子才是 `S` 矩阵元进入概率公式的真正原因。

### 6.1 对连续末态窗口的写法

如果探测器不是选择单个波包，而是选择一片末态区域 $\Delta$，在自由参考表象中写

$$
\Pi_\Delta = \int_\Delta d\beta\, |\beta\rangle\langle\beta|,
$$

那么对应的物理投影是

$$
Q_\Delta^{\mathrm{out}}
=
\Omega_- \Pi_\Delta \Omega_-^\dagger,
$$

其概率为

$$
P_\Delta
=
\langle \phi_{\mathrm{in}} | S^\dagger \Pi_\Delta S | \phi_{\mathrm{in}} \rangle.
$$

这比“直接看某个平面波分量的模平方”更根本，因为它先定义了物理上的探测事件，再把它翻译到自由通道表象。

### 6.2 为什么有限时间下的自由展开系数不是散射概率

在任意有限时刻，

$$
|\Psi(t)\rangle = \int d\alpha\, c_t(\alpha)\, |\alpha\rangle
$$

总是成立，但 $|c_t(\alpha)|^2$ 一般不能解释成“处在末态 $\alpha$ 的概率”，因为：

1. $|\alpha\rangle$ 只是自由参考基底，不是此时此刻的物理散射投影本征态。
2. 有限时间下不同通道通常还没有真正分离。
3. 对连续谱而言，$|c_t(\alpha)|^2$ 是密度而不是普通概率，单点取值没有直接实验意义。

## 7. 定态散射态与 Lippmann-Schwinger 方程

时间相关图像建立之后，才有必要转到定态图像。

取一个自由广义本征矢 $|\alpha\rangle$，满足

$$
H_0|\alpha\rangle = E_\alpha |\alpha\rangle.
$$

对应的入态与出态满足

$$
|\psi_\alpha^{(+)}\rangle = |\alpha\rangle + \frac{1}{E_\alpha-H_0+i0}\,V\,|\psi_\alpha^{(+)}\rangle,
$$

$$
|\psi_\alpha^{(-)}\rangle = |\alpha\rangle + \frac{1}{E_\alpha-H_0-i0}\,V\,|\psi_\alpha^{(-)}\rangle.
$$

这就是 Lippmann-Schwinger 方程。

### 7.1 `+` 号与“入态”为何不矛盾

很多初学者会卡在这里：为什么“入态”用的是 $+i0$，而不是 $-i0$？

原因是：

- $|\psi_\alpha^{(+)}\rangle$ 按定义是在远过去与自由入射通道匹配的散射态。
- 但它在空间无穷远的定态渐近形式，必须包含一个向外传播的散射球面波。
- 正是 $+i0$ 选择了这个 outgoing boundary condition。

所以：

- “入态”说的是它在 $t\to -\infty$ 的匹配方式。
- “outgoing spherical wave”说的是它作为定态解在空间无穷远处的边界条件。

这两个说法不矛盾，反而正是同一件事的时间图像与定态图像。

### 7.2 坐标表象下的含义

对势散射，取 $|\alpha\rangle = |\mathbf k\rangle$，则

$$
\psi_{\mathbf k}^{(+)}(\mathbf r)
=
\langle \mathbf r|\psi_{\mathbf k}^{(+)}\rangle
=
e^{i\mathbf k\cdot \mathbf r}
+
\int d^3r'\,
G_0^{(+)}(\mathbf r,\mathbf r';E_k)\,
V(\mathbf r')\,
\psi_{\mathbf k}^{(+)}(\mathbf r').
$$

当 $r\to\infty$ 时，

$$
\psi_{\mathbf k}^{(+)}(\mathbf r)
\sim
e^{i\mathbf k\cdot \mathbf r}
+
f(\hat{\mathbf r};\mathbf k)\,\frac{e^{ikr}}{r}.
$$

这条式子的三部分必须严格区分：

1. 整个 $\psi_{\mathbf k}^{(+)}(\mathbf r)$ 是完整哈密顿量 $H$ 的精确广义本征函数。
2. 其中的平面波 $e^{i\mathbf k\cdot\mathbf r}$ 只是用来固定“远过去对应哪一个自由通道”的参考项。
3. 散射振幅 $f(\hat{\mathbf r};\mathbf k)$ 乘上的球面波，是相互作用真正产生的出射部分。

因此不能说“入态就是自由平面波”。更准确的说法是：

“入态是完整动力学的精确散射态，它在空间远区的渐近形式以该平面波作为入射参考项。”

## 8. `T` 算符与 `S` 矩阵元

定义 on-shell `T` 算符：

$$
T(E) = V + V\frac{1}{E-H_0+i0}T(E),
$$

并有

$$
T_{\beta\alpha}(E_\alpha)
=
\langle \beta|T(E_\alpha)|\alpha\rangle
=
\langle \beta|V|\psi_\alpha^{(+)}\rangle.
$$

于是

$$
S_{\beta\alpha}
=
\delta_{\beta\alpha}
-2\pi i\,\delta(E_\beta-E_\alpha)\,T_{\beta\alpha}(E_\alpha).
$$

这条公式告诉我们：

- $\delta_{\beta\alpha}$ 是“不发生散射”的直通项；
- `T` 的 on-shell 矩阵元给出真正的跃迁部分；
- 能量守恒通过 $\delta(E_\beta-E_\alpha)$ 强制实现。

需要注意的是，`T` 与散射振幅 $f$ 之间的数值系数依赖于你采用的平面波归一化约定。不同教材可能写成不同的常数因子；这不影响可测的截面，因为最终物理量由一致的归一化方案决定。

## 9. 从波包极限到微分截面

散射截面本质上是一个波包概念：准备一个动量分布很窄的入射波包，探测某个很小立体角窗口内的出射事件率，然后再取窄包极限。平面波公式只是这个过程的分布极限写法。

对两体势散射，在远场

$$
\psi_{\mathbf k}^{(+)}(\mathbf r)
\sim
e^{i\mathbf k_i\cdot \mathbf r}
+
f(\hat{\mathbf r};\mathbf k_i)\,\frac{e^{ik_f r}}{r}.
$$

入射平面波的概率流密度为

$$
j_{\mathrm{in}} = \frac{\hbar k_i}{\mu}.
$$

出射球面波穿过立体角元 $d\Omega$ 的流率为

$$
d\dot P
=
\frac{\hbar k_f}{\mu}\,
|f(\hat{\mathbf r};\mathbf k_i)|^2\,
d\Omega.
$$

于是微分截面定义为

$$
\frac{d\sigma}{d\Omega}
=
\frac{d\dot P/d\Omega}{j_{\mathrm{in}}}
=
\frac{k_f}{k_i}\,
|f(\hat{\mathbf r};\mathbf k_i)|^2.
$$

对弹性散射，$k_f = k_i$，所以

$$
\frac{d\sigma}{d\Omega} = |f(\theta,\varphi)|^2.
$$

这条公式的物理来源不是“把某个平面波末态的系数取模平方”，而是：

1. 用波包定义入射束和探测窗口。
2. 用渐近区的概率流定义事件率。
3. 在窄包极限下把结果写成散射振幅的局域核。

因此，截面从头到尾都依赖“渐近区中的物理散射通道”，而不是依赖某个抽象基底在有限时间下的展开系数。

## 10. 最后的概念清单

把整篇的核心压缩成下面几句话：

1. $|\alpha\rangle$ 是 $H_0$ 的广义本征矢，是自由通道的标签，不是实验里的物理态。
2. $|\phi\rangle=\int g(\alpha)|\alpha\rangle d\alpha$ 才是可归一化的自由入射或出射波包。
3. $|\psi_\alpha^{(\pm)}\rangle$ 是 $H$ 的广义本征矢，是完整理论中的入/出散射基矢，不是自由态。
4. 真正的实验散射态是波包 $|\Psi\rangle=\Omega_+|\phi_{\mathrm{in}}\rangle=\Omega_-|\phi_{\mathrm{out}}\rangle$。
5. `S=\Omega_-^\dagger\Omega_+` 作用在自由参考表象里，把入射自由波包映成出射自由波包。
6. `S_{\beta\alpha}` 是核，不是裸概率；概率要先对波包做 smear，或者等价地先写出物理的 out-projector。
7. Lippmann-Schwinger 方程中的平面波项是渐近参考项，不是说完整散射态“本来就是自由态”。
8. 微分截面来自渐近概率流与波包极限，最后才写成 $d\sigma/d\Omega = (k_f/k_i)|f|^2$。

如果始终守住这八条区分，那么“自由态、渐近态、基底、物理态、`S` 矩阵、散射截面”之间的逻辑关系就不会再乱。
