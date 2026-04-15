# 从波算符到 T 算符，再到三体 AGS 的 U 算符

这篇只做一件事：把两体里的 $S$、$\Omega_\pm$、$T$，以及三体里的 $U_{\beta\alpha}$ 放到同一条推导链上，并且严格区分

- 自由参考态；
- 完整哈密顿量下的精确渐进态；
- 三体中的通道参考态。

全文固定在薛定谔表象。

## 0. 表象先固定：全文只用薛定谔表象

设两体系统

$$
H = H_0 + V
$$

三体系统

$$
H = H_0 + v_1 + v_2 + v_3
$$

在薛定谔表象里：

- 态随时间演化；
- 不显含时的算符本身不随时间演化；
- 真实动力学由完整哈密顿量 $H$ 生成；
- 参考传播由 $H_0$ 或通道哈密顿量 $H_\alpha$ 生成。

所以如果 $|\Psi(0)\rangle$ 是真实态，那么

$$
|\Psi(t)\rangle = e^{-iHt/\hbar} |\Psi(0)\rangle
$$

如果 $|\phi\rangle$ 是自由参考态，那么

$$
|\phi(t)\rangle = e^{-iH_0 t/\hbar} |\phi\rangle
$$

如果 $|\Phi_\alpha\rangle$ 是三体通道参考态，那么

$$
|\Phi_\alpha(t)\rangle = e^{-iH_\alpha t/\hbar} |\Phi_\alpha\rangle
$$

后面所有强极限、Lippmann-Schwinger 方程、以及 $S$、$T$、$U_{\beta\alpha}$ 的定义，都在这个表象下理解。这里没有切到海森伯格表象。

## 1. 两体里必须先分清哪几个态

### 1.1 自由参考态

自由哈密顿量的广义本征态记为

$$
H_0 |\alpha\rangle = E_\alpha |\alpha\rangle
$$

$|\alpha\rangle$ 的作用是：

- 标记通道量子数；
- 作为自由参考空间中的基矢；
- 给波算符、$S$ 矩阵、$T$ 矩阵提供表示。

它不是完整哈密顿量 $H$ 的散射态。

### 1.2 精确入态和出态

对应于同一个参考 ket $|\alpha\rangle$，精确入态和出态定义为

$$
|\psi_\alpha^{(+)}\rangle = \Omega_+ |\alpha\rangle,
\qquad
|\psi_\alpha^{(-)}\rangle = \Omega_- |\alpha\rangle
$$

其中波算符

$$
\Omega_+
=
\operatorname*{s-lim}_{t\to -\infty}
e^{iHt/\hbar} e^{-iH_0 t/\hbar}
$$

$$
\Omega_-
=
\operatorname*{s-lim}_{t\to +\infty}
e^{iHt/\hbar} e^{-iH_0 t/\hbar}
$$

这两个态满足时间域渐近条件

$$
\lim_{t\to -\infty}
\left\|
e^{-iHt/\hbar} |\psi_\alpha^{(+)}\rangle
-
e^{-iH_0 t/\hbar} |\alpha\rangle
\right\|
= 0
$$

$$
\lim_{t\to +\infty}
\left\|
e^{-iHt/\hbar} |\psi_\alpha^{(-)}\rangle
-
e^{-iH_0 t/\hbar} |\alpha\rangle
\right\|
= 0
$$

这里最重要的一句就是：

$|\psi_\alpha^{(\pm)}\rangle$ 不是自由态，而是完整哈密顿量 $H$ 的精确广义本征态；它们只是在远过去或远未来与某个自由参考传播相匹配。

### 1.3 有限时间内实验里真正演化的态

实验里真正准备和探测的是波包。它在有限时间内按照

$$
|\Psi(t)\rangle = e^{-iHt/\hbar} |\Psi(0)\rangle
$$

演化。这个波包一般既不是单个 $|\alpha\rangle$，也不是单个 $|\psi_\alpha^{(\pm)}\rangle$，而是许多通道的叠加。

所以三件事必须分开：

- $|\alpha\rangle$ 是自由参考 ket；
- $|\psi_\alpha^{(\pm)}\rangle$ 是精确入态 / 出态；
- $|\Psi(t)\rangle$ 是有限时间中的真实波包。

## 2. 波算符和 S 算符各做什么

### 2.1 真正把参考态变成精确散射态的是波算符

由定义立刻有

$$
|\psi_\alpha^{(+)}\rangle = \Omega_+ |\alpha\rangle
$$

这才是“从参考入射描述到真实入态”的严格公式。

因此：

- $\Omega_+$ 的输入是自由参考态 $|\alpha\rangle$；
- $\Omega_+$ 的输出是精确入态 $|\psi_\alpha^{(+)}\rangle$；
- 真正把参考态 dress 成完整散射态的是 $\Omega_+$，不是 $S$，也不是 $T$。

### 2.2 S 算符作用在参考空间上

$S$ 算符定义为

$$
S = \Omega_-^\dagger \Omega_+
$$

它的矩阵元满足

$$
\langle \beta | S | \alpha \rangle
=
\langle \psi_\beta^{(-)} | \psi_\alpha^{(+)} \rangle
$$

所以：

- 左边是在自由参考空间中的表示；
- 右边是两个精确渐进态的内积；
- $S$ 不是把 $|\alpha\rangle$ 直接“变成”精确态的算符；
- $S$ 连接的是同一个物理散射过程在过去和未来的参考描述。

这点非常关键。若说“$S$ 作用在自由态上”，那只是说它在参考空间里有一个矩阵表示；不能据此把 $|\alpha\rangle$ 误认为精确渐进态本身。

## 3. 两体里的 T 算符是怎么来的

### 3.1 从 Lippmann-Schwinger 方程开始

取一个固定参考 ket $|\alpha\rangle$，满足

$$
H_0 |\alpha\rangle = E_\alpha |\alpha\rangle
$$

对应的精确入态满足

$$
H |\psi_\alpha^{(+)}\rangle = E_\alpha |\psi_\alpha^{(+)}\rangle
$$

并 obey 出射边界条件。Lippmann-Schwinger 方程为

$$
|\psi_\alpha^{(+)}\rangle
=
|\alpha\rangle
+
G_0^{(+)}(E_\alpha)\, V |\psi_\alpha^{(+)}\rangle
$$

其中

$$
G_0^{(+)}(E) = \frac{1}{E - H_0 + i0}
$$

### 3.2 T 的第一种定义

现在定义

$$
T(E_\alpha) |\alpha\rangle
\equiv
V |\psi_\alpha^{(+)}\rangle
$$

这个定义本身已经说明了 $T$ 的角色：

- $T(E_\alpha)|\alpha\rangle$ 不是完整散射态；
- 它是相互作用从参考入射 ket 中抽出来的散射源项；
- 真正的精确入态仍然是 $|\psi_\alpha^{(+)}\rangle$。

把这个定义代回 Lippmann-Schwinger 方程，得到

$$
|\psi_\alpha^{(+)}\rangle
=
|\alpha\rangle
+
G_0^{(+)}(E_\alpha)\, T(E_\alpha) |\alpha\rangle
$$

因此

$$
\Omega_+ |\alpha\rangle
=
\left[
1 + G_0^{(+)}(E_\alpha)\, T(E_\alpha)
\right]
|\alpha\rangle
$$

这条式子可以直接读成：

- $\Omega_+$ 把参考 ket 变成精确入态；
- 在固定能量壳上，这个 dressing 可写成 $1 + G_0^{(+)} T$；
- 其中 $T$ 负责产生源项，$G_0^{(+)}$ 负责把源传播成散射部分。

所以如果问“哪个算符把 $|\alpha\rangle$ 变成精确入态”，答案是 $\Omega_+$；
如果问“相互作用部分在这个 dressing 里由谁编码”，答案才是 $T$。

## 4. T 算符的各种等价定义

### 4.1 向量定义

最直接的定义就是

$$
T(E_\alpha) |\alpha\rangle
=
V |\psi_\alpha^{(+)}\rangle
$$

### 4.2 T 自己的 Lippmann-Schwinger 方程

由

$$
|\psi_\alpha^{(+)}\rangle
=
|\alpha\rangle
+
G_0^{(+)}(E_\alpha)\, T(E_\alpha) |\alpha\rangle
$$

左乘 $V$，得到

$$
T(E_\alpha)|\alpha\rangle
=
V|\alpha\rangle
+
V G_0^{(+)}(E_\alpha)\, T(E_\alpha)|\alpha\rangle
$$

于是算符形式为

$$
T(E) = V + V G_0^{(+)}(E)\, T(E)
$$

这就是最常见的两体 $T$ 方程。

### 4.3 右作用形式

同理由 resolvent identity 也可得到

$$
T(E) = V + T(E)\, G_0^{(+)}(E)\, V
$$

这是与上式等价的右作用形式。

### 4.4 用完整 resolvent 表示

记

$$
G^{(+)}(E) = \frac{1}{E - H + i0}
$$

由

$$
|\psi_\alpha^{(+)}\rangle
=
|\alpha\rangle
+
G^{(+)}(E_\alpha)\, V |\alpha\rangle
$$

再代入 $T(E_\alpha)|\alpha\rangle = V |\psi_\alpha^{(+)}\rangle$，得到

$$
T(E) = V + V G^{(+)}(E) V
$$

这给出了 $T$ 与完整 Green 算符的关系。

### 4.5 形式逆算符写法

若形式逆存在，则还可写成

$$
T(E) = \bigl[1 - V G_0^{(+)}(E)\bigr]^{-1} V
$$

或

$$
T(E) = V \bigl[1 - G_0^{(+)}(E) V\bigr]^{-1}
$$

这两条只是把 Lippmann-Schwinger 方程做了代数重排。

### 4.6 与 resolvent 的等价关系

把 Dyson 方程和 $T$ 方程结合起来，可得

$$
G^{(+)}(E)
=
G_0^{(+)}(E)
+
G_0^{(+)}(E)\, T(E)\, G_0^{(+)}(E)
$$

这条式子很有用，因为它说明：

- resolvent 的散射部分正是由 $T$ 插在两个自由传播子之间形成的；
- 两体里“相互作用核”与“传播”之间的分工，在这里写得最清楚。

### 4.7 与 S 矩阵的 on-shell 关系

在自由参考基底里，on-shell 的 $T$ 矩阵元给出

$$
\langle \beta | S | \alpha \rangle
=
\delta_{\beta\alpha}
-
2\pi i\, \delta(E_\beta - E_\alpha)\,
\langle \beta | T(E_\alpha) | \alpha \rangle
$$

这里必须注意两件事：

- $\langle \beta | T(E_\alpha) | \alpha \rangle$ 是参考空间中的矩阵元；
- 它之所以有物理意义，是因为它等价地编码了精确渐进态之间的重叠和跃迁振幅。

## 5. 三体里首先出现的是通道参考态，不是完整渐进态

### 5.1 通道哈密顿量

三体总哈密顿量写成

$$
H = H_0 + v_1 + v_2 + v_3
$$

其中

- $v_1 \equiv v_{23}$；
- $v_2 \equiv v_{31}$；
- $v_3 \equiv v_{12}$。

对每个通道 $\alpha$，定义通道哈密顿量

$$
H_\alpha = H_0 + v_\alpha
$$

以及剩余耦合

$$
\bar V_\alpha = H - H_\alpha = \sum_{\gamma \neq \alpha} v_\gamma
$$

### 5.2 通道参考态的定义

若对偶粒子对 $\alpha$ 存在束缚态 $|\phi_\alpha\rangle$，满足

$$
h_\alpha |\phi_\alpha\rangle = \epsilon_\alpha |\phi_\alpha\rangle,
\qquad
\epsilon_\alpha < 0
$$

再设旁观者与该束缚簇之间的相对动量 ket 为 $|q_\alpha\rangle$。那么通道参考态定义为

$$
|\Phi_\alpha(q_\alpha)\rangle
=
|\phi_\alpha\rangle \otimes |q_\alpha\rangle
$$

并满足

$$
H_\alpha |\Phi_\alpha(q_\alpha)\rangle
=
E |\Phi_\alpha(q_\alpha)\rangle,
\qquad
E = \epsilon_\alpha + \frac{q_\alpha^2}{2\mu_\alpha}
$$

这里最容易混淆的点必须单独说清楚：

- $|\Phi_\alpha\rangle$ 不是完全自由态，因为其中的 $|\phi_\alpha\rangle$ 是簇内的精确束缚态；
- $|\Phi_\alpha\rangle$ 也不是完整三体哈密顿量 $H$ 的精确渐进态，因为它只对 $H_\alpha$ 是本征态；
- $|\Phi_\alpha\rangle$ 的正确名字是通道参考态。

换句话说，三体里的参考对象已经不是两体散射中的 $H_0$ 本征态，而是“一个真实束缚簇 + 一个旁观者相对运动”的通道态。

### 5.3 真正的三体精确渐进态

对应的波算符不再是相对于 $H_0$ 定义，而是相对于 $H_\alpha$ 定义：

$$
\Omega_\alpha^{(+)}
=
\operatorname*{s-lim}_{t\to -\infty}
e^{iHt/\hbar} e^{-iH_\alpha t/\hbar}
$$

于是精确的入射三体渐进态定义为

$$
|\Psi_\alpha^{(+)}\rangle
=
\Omega_\alpha^{(+)} |\Phi_\alpha\rangle
$$

这个态才是完整三体哈密顿量 $H$ 的精确入态。

因此三体里要分清三层对象：

- 自由三体运动的参考空间由 $H_0$ 描述；
- 某个具体簇化通道的参考态由 $H_\alpha$ 描述；
- 真正的三体精确渐进态由 $H$ 描述。

## 6. 从通道 Lippmann-Schwinger 方程定义 U_{\beta\alpha}

### 6.1 通道形式的 Lippmann-Schwinger 方程

因为

$$
H = H_\alpha + \bar V_\alpha
$$

所以精确入态满足

$$
|\Psi_\alpha^{(+)}\rangle
=
|\Phi_\alpha\rangle
+
G_\alpha^{(+)}(E)\, \bar V_\alpha |\Psi_\alpha^{(+)}\rangle
$$

其中

$$
G_\alpha^{(+)}(E) = \frac{1}{E - H_\alpha + i0}
$$

这与两体公式

$$
|\psi_\alpha^{(+)}\rangle
=
|\alpha\rangle
+
G_0^{(+)}(E_\alpha)\, V |\psi_\alpha^{(+)}\rangle
$$

完全平行，只是参考哈密顿量从 $H_0$ 换成了 $H_\alpha$。

### 6.2 U_{\beta\alpha} 的定义

现在固定一个观察通道 $\beta$，定义 AGS 跃迁算符

$$
U_{\beta\alpha}(E)\, |\Phi_\alpha\rangle
\equiv
\bar V_\beta |\Psi_\alpha^{(+)}\rangle
$$

这一定义与两体里的

$$
T(E_\alpha)|\alpha\rangle = V |\psi_\alpha^{(+)}\rangle
$$

是完全对应的。

所以 $U_{\beta\alpha}$ 的角色就是：

- 输入是入射通道参考态 $|\Phi_\alpha\rangle$；
- 输出不是完整散射态，而是“喂入通道 $\beta$ 的源项”；
- 再经过 $G_\beta^{(+)}$ 传播，才得到在通道 $\beta$ 中显现出来的散射部分。

### 6.3 通道分解公式

由

$$
(E - H_\beta)|\Psi_\alpha^{(+)}\rangle
=
\bar V_\beta |\Psi_\alpha^{(+)}\rangle
$$

以及当 $\beta=\alpha$ 时

$$
(E - H_\alpha)|\Phi_\alpha\rangle = 0
$$

可得统一写法

$$
|\Psi_\alpha^{(+)}\rangle
=
\delta_{\beta\alpha} |\Phi_\alpha\rangle
+
G_\beta^{(+)}(E)\, U_{\beta\alpha}(E)\, |\Phi_\alpha\rangle
$$

这条式子就是三体里最核心的结构式。

它的物理意义非常直接：

- 若 $\beta=\alpha$，有一个显式的入射通道参考项，再加上弹性散射修正；
- 若 $\beta\neq\alpha$，没有直入项，整个通道 $\beta$ 的出现都来自 $G_\beta^{(+)} U_{\beta\alpha}$；
- 因而 $U_{\beta\alpha}$ 就是“把入射通道 $\alpha$ 的过程重新组织成最终在通道 $\beta$ 中出现的跃迁源”。

## 7. U_{\beta\alpha} 的标准 AGS 方程

定义两体对子系统的嵌入式 $T$ 算符

$$
T_\gamma(E) = v_\gamma + v_\gamma G_0(E) T_\gamma(E)
$$

其中

$$
G_0(E) = \frac{1}{E - H_0 + i0}
$$

再记

$$
\bar\delta_{\beta\alpha} = 1 - \delta_{\beta\alpha}
$$

则 AGS 方程写成

$$
U_{\beta\alpha}(E)
=
\bar\delta_{\beta\alpha}\, G_0^{-1}(E)
+
\sum_{\gamma=1}^3
\bar\delta_{\beta\gamma}\,
T_\gamma(E)\, G_0(E)\, U_{\gamma\alpha}(E)
$$

它告诉你：

- 通道跃迁最终还是由各对子系统的两体 $T_\gamma$ 叠加出来；
- 三体问题之所以复杂，是因为不同对子散射不断在不同通道之间来回耦合；
- AGS 的 $U_{\beta\alpha}$ 是“通道到通道”的有效跃迁算符，而不是单个对子势的简单替代。

## 8. 特别看 U_{21}：它到底怎样作用到通道 2

这正是三体重排散射里最重要的例子。

### 8.1 通道 1 与通道 2 的参考态

设

$$
|\Phi_1\rangle = |\phi_1\rangle \otimes |q_1\rangle
=
|\phi_{23}\rangle \otimes |q_1\rangle
$$

表示 $(23)$ 已经形成束缚簇，粒子 1 是旁观者。

再设

$$
|\Phi_2\rangle = |\phi_2\rangle \otimes |q_2\rangle
=
|\phi_{31}\rangle \otimes |q_2\rangle
$$

表示 $(31)$ 已经形成束缚簇，粒子 2 是旁观者。

这两个态都不是完整三体的精确渐进态，但它们都是各自通道哈密顿量的参考态。

### 8.2 真正的入射态是 |\Psi_1^{(+)}\rangle

物理上真正入射的精确态是

$$
|\Psi_1^{(+)}\rangle = \Omega_1^{(+)} |\Phi_1\rangle
$$

它描述的是：

- 远过去看起来像“束缚簇 $(23)$ 加旁观者 1 的通道参考传播”；
- 但在整个时间演化中，它始终是完整三体哈密顿量 $H$ 的精确态。

因此不能把 $|\Phi_1\rangle$ 当成真正的物理入态；$|\Phi_1\rangle$ 只是它在入射通道上的参考代表。

### 8.3 在通道 2 上看同一个精确态

对同一个精确态 $|\Psi_1^{(+)}\rangle$，取 $\beta=2$ 的通道分解：

$$
|\Psi_1^{(+)}\rangle
=
G_2^{(+)}(E)\, U_{21}(E)\, |\Phi_1\rangle
$$

这里没有 $\delta_{21} |\Phi_1\rangle$ 项，因为 $\delta_{21}=0$。

这条公式一定要按下面的顺序理解：

1. 输入的是通道 1 的参考态 $|\Phi_1\rangle$；
2. $U_{21}(E)$ 把它变成“喂入通道 2 的源项”；
3. $G_2^{(+)}(E)$ 再按通道 2 的动力学把这个源传播出去；
4. 最后在远未来的通道 2 区域里，你看到的是“束缚簇 $(31)$ 加旁观者 2”的重排散射成分。

所以 $U_{21}$ 的作用并不是“把一个完全自由态直接变成束缚态”，而是：

- 以入射通道 1 的参考态为输入；
- 从完整三体相互作用中抽出指向通道 2 的跃迁源；
- 这个源再由 $G_2^{(+)}$ 组织成通道 2 的渐近传播。

### 8.4 为什么通道 2 里会同时有束缚态和相对运动态

因为通道 2 的参考哈密顿量本来就是

$$
H_2 = H_0 + v_2
$$

它已经把对子 $(31)$ 的相互作用完整保留在里面了。于是：

- $|\phi_2\rangle$ 是 $(31)$ 的真实束缚态；
- $|q_2\rangle$ 是粒子 2 相对该束缚簇的运动标签；
- 二者张量积出来的 $|\Phi_2\rangle$ 是通道 2 的参考态。

因此通道态里“有真实束缚态”并不奇怪；真正需要避免的误解是把它误叫成“完全自由态”。

更精确地说：

- 通道参考态不是自由三体态；
- 通道参考态也不是完整三体的精确渐进态；
- 精确渐进态是 $\Omega_\alpha^{(+)} |\Phi_\alpha\rangle$；
- $U_{\beta\alpha}$ 负责在不同通道参考描述之间提取跃迁核。

### 8.5 U_{21} 的物理矩阵元

最终真正出现在重排散射振幅里的，是 on-shell 矩阵元

$$
\langle \Phi_2 | U_{21}(E) | \Phi_1 \rangle
$$

它的意义是：

- 初态参考标签是“簇 $(23)$ 加旁观者 1”；
- 末态参考标签是“簇 $(31)$ 加旁观者 2”；
- 这个矩阵元编码了完整三体动力学把一个通道重排到另一个通道的振幅。

再结合适当归一化、能量守恒和入射流因子，就得到对应的三体重排截面。

## 9. 结构总结

把整条链压缩成最短的公式，就是：

两体里

$$
|\psi_\alpha^{(+)}\rangle
=
\Omega_+ |\alpha\rangle
=
\left[1 + G_0^{(+)}(E_\alpha)\, T(E_\alpha)\right] |\alpha\rangle
$$

其中

$$
T(E_\alpha)|\alpha\rangle = V |\psi_\alpha^{(+)}\rangle
$$

三体里

$$
|\Psi_\alpha^{(+)}\rangle
=
\Omega_\alpha^{(+)} |\Phi_\alpha\rangle
=
\delta_{\beta\alpha} |\Phi_\alpha\rangle
+
G_\beta^{(+)}(E)\, U_{\beta\alpha}(E)\, |\Phi_\alpha\rangle
$$

其中

$$
U_{\beta\alpha}(E)\, |\Phi_\alpha\rangle
=
\bar V_\beta |\Psi_\alpha^{(+)}\rangle
$$

所以最后必须记住：

- 真正把参考态变成精确散射态的是波算符；
- $S$ 作用在参考空间里，表示精确入态与精确出态之间的关系；
- $T$ 是两体里对相互作用源的编码；
- $U_{\beta\alpha}$ 是三体里对“从通道 $\alpha$ 喂入通道 $\beta$ 的跃迁源”的编码；
- 三体通道态既不是完全自由态，也不等于完整三体的精确渐进态。
