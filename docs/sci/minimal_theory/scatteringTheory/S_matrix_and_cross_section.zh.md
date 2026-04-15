# S矩阵、入出态与散射截面：固定在薛定谔表象里

这篇笔记只解决一个问题：

为什么 S 矩阵元或入出态的内积能够给出跃迁概率？

为避免混乱，全文只用薛定谔表象，并严格区分三件事：

- 自由参考态 `|\phi\rangle` 或通道基矢 `|\alpha\rangle`
- 渐进态 / 入出态 `|\psi^{(\pm)}\rangle`
- 有限时间下真正演化的时变态 `|\Psi(t)\rangle`

最重要的纠正先放在最前面：

渐进态不是自由态。

渐进态是完整哈密顿量 $H$ 的精确态，只是在 $t \to \pm\infty$ 时与某个自由参考态具有相同的渐近传播行为。自由态只是用来标记和表示它的参考对象。

## 0. 表象与约定

设

$$
H = H_0 + V
$$

其中 $H_0$ 是自由哈密顿量，$V$ 是短程相互作用。

在薛定谔表象中：

- 态随时间演化；
- 若算符不显含时，则算符不随时间演化；
- 真实动力学由 $H$ 生成；
- 自由参考传播由 $H_0$ 生成。

若 $|\Psi(0)\rangle$ 是真实态，则

$$
|\Psi(t)\rangle = e^{-iHt/\hbar} |\Psi(0)\rangle
$$

若 $|\phi\rangle$ 是自由参考态，则

$$
|\phi(t)\rangle = e^{-iH_0 t/\hbar} |\phi\rangle
$$

请注意：这里的 $|\phi(t)\rangle$ 只是一个自由参考传播，不代表它就是“渐进态”。

## 1. 三类对象必须分开

### 1.1 自由参考态

自由哈密顿量的广义本征态记为

$$
H_0 |\alpha\rangle = E_\alpha |\alpha\rangle
$$

它们的作用首先是通道标签和坐标轴：

- 用来标记动量、自旋、角动量、粒子种类等量子数；
- 用来展开自由波包；
- 通常是 $\delta$ 归一化的广义本征矢。

因此单独的 $|\alpha\rangle$ 只是自由参考基底，不是渐进态。

### 1.2 渐进态 / 入出态

给定一个自由参考态 $|\alpha\rangle$，相应的入态和出态定义为

$$
|\psi_\alpha^{(+)}\rangle = \Omega_+ |\alpha\rangle,
\qquad
|\psi_\alpha^{(-)}\rangle = \Omega_- |\alpha\rangle
$$

其中 $\Omega_\pm$ 是波算符，后面会定义。

这两个态满足：

- 它们是完整哈密顿量 $H$ 的精确态；
- 它们不是自由态；
- 它们只是在远过去或远未来与对应的自由参考传播相匹配。

其时间域定义是

$$
\lim_{t\to -\infty}
\left\|
e^{-iHt/\hbar} |\psi_\alpha^{(+)}\rangle
-
e^{-iH_0 t/\hbar} |\alpha\rangle
\right\|
= 0
$$

以及

$$
\lim_{t\to +\infty}
\left\|
e^{-iHt/\hbar} |\psi_\alpha^{(-)}\rangle
-
e^{-iH_0 t/\hbar} |\alpha\rangle
\right\|
= 0
$$

这正是“渐进态”的真正定义：

它不是自由态，而是一个真实态；只是它在远时极限下与某个自由参考传播不可区分。

### 1.3 有限时间时变态

实验里真正经历时间演化的是波包态，例如

$$
|\Psi(t)\rangle = e^{-iHt/\hbar} |\Psi(0)\rangle
$$

它在有限时间内一般既不是自由态，也不是单个定能渐进态，而是许多入态或出态的叠加。

所以：

- 自由参考态是参考对象；
- 渐进态是完整动力学下的精确入/出态；
- 时变态是实验过程中的真实波包演化。

## 2. 波算符与 S 算符

波算符定义为

$$
\Omega_+ =
\operatorname*{s-lim}_{t\to -\infty}
e^{iHt/\hbar} e^{-iH_0 t/\hbar}
$$

$$
\Omega_- =
\operatorname*{s-lim}_{t\to +\infty}
e^{iHt/\hbar} e^{-iH_0 t/\hbar}
$$

于是

$$
|\psi_\alpha^{(+)}\rangle = \Omega_+ |\alpha\rangle,
\qquad
|\psi_\alpha^{(-)}\rangle = \Omega_- |\alpha\rangle
$$

所以波算符的意义是：

- 输入是自由参考态；
- 输出是完整动力学下的渐进态。

换句话说，渐进态不是 $|\alpha\rangle$，而是 $\Omega_\pm |\alpha\rangle$。

S 算符定义为

$$
S = \Omega_-^\dagger \Omega_+
$$

它作用在自由参考空间上，而不是直接作用在完整动力学的时变态上。

若同一个物理散射过程在过去由参考态 $|\alpha\rangle$ 标记、在未来由参考态 $|\beta\rangle$ 标记，则

$$
\langle \beta | S | \alpha \rangle
=
\langle \psi_\beta^{(-)} | \psi_\alpha^{(+)} \rangle
$$

这条式子很关键。它说明：

- 左边是 S 矩阵在自由参考空间中的表示；
- 右边是两个真正的渐进态的内积。

因此真正有物理意义的是渐进态之间的关系；自由参考态只是把它们表示出来的坐标。

## 3. 为什么渐进态的内积给出概率

这是整篇最核心的地方。

### 3.1 单个出射波包通道

设实验准备了一个入态

$$
|\Psi_{\rm in}\rangle = \Omega_+ |\Phi_{\rm in}\rangle
$$

其中 $|\Phi_{\rm in}\rangle$ 是归一化的自由参考波包。

设探测器被调到接收某个归一化的出射波包通道 $|\chi_\beta\rangle$。相应的物理出态是

$$
|\psi_\beta^{(-)}\rangle = \Omega_- |\chi_\beta\rangle
$$

因为探测器工作在远未来的渐近区，所以“探测到这个出射通道”的物理投影算符不是

$$
|\chi_\beta\rangle \langle \chi_\beta|
$$

而是完整物理空间中的 out-projector

$$
Q_\beta^{\rm out}
=
|\psi_\beta^{(-)}\rangle \langle \psi_\beta^{(-)}|
=
\Omega_- |\chi_\beta\rangle \langle \chi_\beta| \Omega_-^\dagger
$$

因此探测概率是

$$
P_{\beta\leftarrow{\rm in}}
=
\langle \Psi_{\rm in} | Q_\beta^{\rm out} | \Psi_{\rm in} \rangle
$$

把 $|\Psi_{\rm in}\rangle = \Omega_+ |\Phi_{\rm in}\rangle$ 代入，可得

$$
P_{\beta\leftarrow{\rm in}}
=
\langle \Phi_{\rm in} |
\Omega_+^\dagger \Omega_-
|\chi_\beta\rangle
\langle \chi_\beta |
\Omega_-^\dagger \Omega_+
|\Phi_{\rm in}\rangle
$$

也就是

$$
P_{\beta\leftarrow{\rm in}}
=
\left|
\langle \chi_\beta | S | \Phi_{\rm in} \rangle
\right|^2
$$

同时，由

$$
\langle \chi_\beta | S | \Phi_{\rm in} \rangle
=
\langle \psi_\beta^{(-)} | \Psi_{\rm in} \rangle
$$

又得到

$$
P_{\beta\leftarrow{\rm in}}
=
\left|
\langle \psi_\beta^{(-)} | \Psi_{\rm in} \rangle
\right|^2
$$

这就是“为什么渐进态的内积给出概率”的严格原因。

不是因为渐进态是自由态，而是因为：

1. 探测器测量的是远未来的出射通道；
2. 这些出射通道在物理 Hilbert 空间里的正确投影是 out-projector；
3. out-projector 的本征态正是出态 $|\psi_\beta^{(-)}\rangle$；
4. 因此概率自然就是对这些出态的投影；
5. 只不过借助 $\Omega_-^\dagger$，这个投影可以等价地写成自由参考空间里的 `S` 矩阵元。

### 3.2 一整个末态窗口

若探测器接收的是一片末态区域 $\Delta$，则在自由参考空间中先定义

$$
\Pi_\Delta = \int_\Delta d\beta\, |\beta\rangle \langle \beta|
$$

对应的物理 out-projector 是

$$
Q_\Delta^{\rm out}
=
\Omega_- \Pi_\Delta \Omega_-^\dagger
$$

因此概率为

$$
P_\Delta
=
\langle \Psi_{\rm in} | Q_\Delta^{\rm out} | \Psi_{\rm in} \rangle
=
\langle \Phi_{\rm in} | S^\dagger \Pi_\Delta S | \Phi_{\rm in} \rangle
$$

这条式子比单个矩阵元更根本。它说明：

- Born 规则作用在物理 out-projector 上；
- `S^\dagger \Pi_\Delta S` 只是这个物理投影在自由参考空间中的表示。

## 4. 为什么有限时间下自由基底展开系数不是概率

现在看一个常见误区。

设在某个有限时刻 $t$，真实时变态写成

$$
|\Psi(t)\rangle = \int d\alpha\, c_t(\alpha)\, |\alpha\rangle
$$

这当然总能做到，因为 $|\alpha\rangle$ 是 $H_0$ 的一组基底。

但一般不能把 $|c_t(\alpha)|^2$ 解释成“系统以概率 $|c_t(\alpha)|^2$ 处于散射末态 $\alpha$”，原因有三条。

第一，这只是坐标展开。  
$|\alpha\rangle$ 是自由参考基底，不是物理 out-projector 的本征态。

第二，有限时间下入射、相互作用、出射尚未分离。  
这时系统仍可能处在相互作用区内，自由基底系数并不对应任何清晰的通道探测。

第三，单个平面波基矢通常是广义本征矢。  
它们不是归一化的物理态，直接取模平方会碰到 $\delta$ 函数平方。

所以：

- 任意自由基底展开系数没有直接概率意义；
- 真正的概率来自对物理渐近通道子空间的投影。

## 5. 定态散射 ket 与入出态

对固定自由参考基矢 $|\alpha\rangle$，Lippmann-Schwinger ket 定义为

$$
H |\psi_\alpha^{(+)}\rangle = E_\alpha |\psi_\alpha^{(+)}\rangle
$$

并满足

$$
|\psi_\alpha^{(+)}\rangle
=
|\alpha\rangle
+
G_0^{(+)}(E_\alpha)\, V |\psi_\alpha^{(+)}\rangle
$$

这里要再次强调：

- $|\alpha\rangle$ 是自由参考态；
- $|\psi_\alpha^{(+)}\rangle$ 才是完整哈密顿量的入态；
- 它不是自由态，只是带有由 $|\alpha\rangle$ 标记的入射边界条件。

同理，

$$
H |\psi_\beta^{(-)}\rangle = E_\beta |\psi_\beta^{(-)}\rangle
$$

是对应的出态。

于是

$$
\langle \beta | S | \alpha \rangle
=
\langle \psi_\beta^{(-)} | \psi_\alpha^{(+)} \rangle
$$

就成为两种语言的等价写法：

- 用自由参考态表示是 `S` 矩阵元；
- 用物理态表示是入态和出态的内积。

## 6. 从 S 到 T

on-shell 时，S 矩阵元写成

$$
\langle \beta | S | \alpha \rangle
=
\delta_{\beta\alpha}
- 2\pi i\, \delta(E_\beta-E_\alpha)\, T_{\beta\alpha}(E_\alpha)
$$

其中

$$
T_{\beta\alpha}(E)
=
\langle \beta | T(E) | \alpha \rangle
=
\langle \beta | V | \psi_\alpha^{(+)} \rangle
=
\langle \psi_\beta^{(-)} | V | \alpha \rangle
$$

所以 `T` 负责把真正的动力学跃迁部分从 `S` 中剥出来。

但要记住：

- `S` 是渐近通道的总映射；
- `T` 是去掉平凡单位项后的跃迁核；
- 真正的概率仍然要通过 out-projector 或入出态内积来定义。

## 7. 连续谱里为什么出现概率密度

若把 $|\alpha\rangle$、$|\beta\rangle$ 都理想化成严格单色平面波，则它们是 $\delta$ 归一化广义本征矢。此时

$$
\langle \beta | S | \alpha \rangle
$$

不是普通数，而是分布。

所以连续谱里更自然的可测量量不是“单个平面波末态的普通概率”，而是：

- 某个末态窗口中的概率；
- 或单位时间跃迁率；
- 或单位入射流归一化后的散射截面。

这就是为什么在实际计算中最后出现的是

$$
\frac{2\pi}{\hbar} |T_{\beta\alpha}|^2 \rho_\beta(E)
$$

这类态密度加权的表达式。

## 8. 散射截面为什么是流比值

实验上可直接统计的是某个末态窗口中的出射事件率，而不是抽象的振幅本身。

因此定义

$$
d\sigma = \frac{dW}{j_{\rm in}}
$$

其中：

- $dW$ 是单位时间内进入末态窗口的概率；
- $j_{\rm in}$ 是入射流强。

这一定义和前面的概率公式完全一致：

- `dW` 来自对 out-projector 的投影；
- 再除以入射流，就得到与束流强度无关的截面。

## 9. 两体弹性散射的微分截面

对两体短程势散射，入态波函数在远区满足

$$
\psi_{\mathbf k_i}^{(+)}(\mathbf r)
\xrightarrow{r\to\infty}
e^{i\mathbf k_i\cdot\mathbf r}
+
f(\hat{\mathbf r},\mathbf k_i)\,\frac{e^{ik_f r}}{r}
$$

这里

- 第一项是用来标记入射边界条件的参考平面波；
- 第二项是由真实入态在远未来产生的出射球面波尾。

对约化质量 $\mu$，入射流是

$$
j_{\rm in} = \frac{\hbar k_i}{\mu}
$$

出射球面波在立体角 $d\Omega$ 中携带的概率流为

$$
dW
=
\frac{\hbar k_f}{\mu}\,
|f(\hat{\mathbf r},\mathbf k_i)|^2\, d\Omega
$$

因此

$$
\frac{d\sigma}{d\Omega}
=
\frac{dW/d\Omega}{j_{\rm in}}
=
\frac{k_f}{k_i}\, |f(\hat{\mathbf r},\mathbf k_i)|^2
$$

对弹性散射 $k_f=k_i$，即

$$
\frac{d\sigma}{d\Omega}
=
|f(\hat{\mathbf r},\mathbf k_i)|^2
$$

这条公式为什么可测？因为它比较的是：

- 远未来出射通道中的概率流；
- 远过去入射通道中的参考流强。

两者都定义在渐近区，而不是定义在相互作用区内部。

## 10. 小结

把这篇文章压缩成一句最关键的话：

渐进态不是自由态；  
它之所以能给出概率，是因为探测器测量的正是远未来的物理 out-projector，而这些 out-projector 的本征态就是出态 `|\psi^{(-)}\rangle`。

在计算上，我们常写成

$$
\langle \beta | S | \alpha \rangle
$$

那只是因为波算符把这个物理投影拉回到了自由参考空间。真正的物理内容是

$$
\langle \psi_\beta^{(-)} | \psi_\alpha^{(+)} \rangle
$$

或者更一般的

$$
\langle \Psi_{\rm in} | Q_\Delta^{\rm out} | \Psi_{\rm in} \rangle
$$

其中 `Q_\Delta^{out}` 才是探测器对应的物理投影。

默认这里讨论的是短程相互作用。对 Coulomb 等长程势，自由参考传播和波算符的具体形式都需要修正；但“渐进态不是自由态，概率来自物理渐近投影”这一点并不改变。
