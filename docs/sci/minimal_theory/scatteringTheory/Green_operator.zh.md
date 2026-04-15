# 格林算符与格林函数

格林函数最初来自含源线性方程的求解问题。它的核心作用不是“再发明一种解法”，而是把“求解微分方程”改写成“研究一个逆算符或其核的结构”。到了量子力学里，这个逆算符正是哈密顿量的 resolvent，因此格林函数同时承担了传播子、谱信息载体、以及散射边界条件编码器这三个角色。

严格地说，在散射理论里最好先区分两个对象：

$$
G(z) = (z - H)^{-1}
$$

它是定义在 Hilbert 空间上的格林算符，也就是 resolvent。

$$
G(x, x'; z) = \langle x | G(z) | x' \rangle
$$

它是格林算符在某个表象下的矩阵元，通常才被称为格林函数。坐标表象里它是传播核，动量表象里它则直接控制能量分母与极点结构。

因此，很多物理书里“格林函数”和“格林算符”会混着说；但一旦要讨论边界条件、谱分解或散射振幅，先把这两个层次分开会清楚得多。

## 1. 从含源方程出发

考虑一个线性算符 $L$ 与源项 $f$。我们要求解

$$
L u(x) = f(x)
$$

若 $L^{-1}$ 存在，那么解可以形式化地写成

$$
u = L^{-1} f
$$

在坐标表象下，把 $L^{-1}$ 的核记为 $G(x, x')$，即

$$
G(x, x') = \langle x | L^{-1} | x' \rangle
$$

便得到熟悉的格林函数方程

$$
L G(x, x') = \delta(x - x')
$$

以及积分形式的解

$$
u(x) = \int dx'\, G(x, x') f(x')
$$

这里有一个经常被忽略但在散射理论里极其关键的事实：同一个微分方程往往不只对应一个格林函数，因为逆算符并不只由微分算子本身决定，还由边界条件决定。对时间问题，可以有 retarded 和 advanced 两种选择；对空间散射问题，可以有 outgoing 和 incoming 两种选择。真正决定物理内容的，正是这些边界条件。

## 2. 薛定谔方程中的格林算符

设哈密顿量分解为

$$
H = H_0 + V
$$

其中 $H_0$ 是自由部分，$V$ 是相互作用。定态薛定谔方程为

$$
H |\psi_E\rangle = E |\psi_E\rangle
$$

也就是

$$
(E - H) |\psi_E\rangle = 0
$$

如果 $E$ 正好落在谱上，那么 $E - H$ 并不能按普通有界逆算符来处理，所以必须先把能量提升到复平面，定义

$$
G(z) = \frac{1}{z - H},
\qquad
G_0(z) = \frac{1}{z - H_0},
\qquad z \notin \sigma(H),\sigma(H_0)
$$

这就是全格林算符与自由格林算符。等到最后再从复平面逼近实轴，才得到散射理论真正使用的边界值

$$
G^{(\pm)}(E) = \lim_{\epsilon \to 0^+} \frac{1}{E - H \pm i\epsilon},
\qquad
G_0^{(\pm)}(E) = \lim_{\epsilon \to 0^+} \frac{1}{E - H_0 \pm i\epsilon}
$$

这里的 $+i0$ 和 $-i0$ 不是装饰项，而是两种不同的物理解。它们告诉你奇点应该从实轴哪一侧绕开，也就决定了最后得到的是出射波还是入射波。

## 3. Dyson 形式与两种“源”的理解

由

$$
(z - H) G(z) = I,
\qquad
(z - H_0) G_0(z) = I
$$

以及 $H = H_0 + V$，可以立刻得到 resolvent identity  (证明 恒等式 $A^{-1} - B^{-1} = A^{-1}(B - A)B^{-1}$ 即可)

$$
G(z) = G_0(z) + G_0(z) V G(z)
$$

同理也可以写成

$$
G(z) = G_0(z) + G(z) V G_0(z)
$$

这就是散射理论里最常见的 Dyson 形式。继续迭代便得到 Born 级数

$$
G = G_0 + G_0 V G_0 + G_0 V G_0 V G_0 + \cdots
$$

这个公式本身已经说明了格林算符的物理意义：自由传播、相互作用、再次自由传播，如此反复，直到把所有多次散射过程都加起来。

接下来再看定态本征方程。设 $|\phi_E\rangle$ 为自由哈密顿量的本征态，

$$
H_0 |\phi_E\rangle = E |\phi_E\rangle
$$

这里必须先把对象区分开：

- $|\phi_E\rangle$ 只是自由参考 ket，用来标记通道和边界条件；
- 真正的入态、出态是 $|\psi_E^{(\pm)}\rangle = \Omega_\pm |\phi_E\rangle$；
- $|\psi_E^{(\pm)}\rangle$ 是完整哈密顿量 $H$ 的精确广义本征态，不等于 $|\phi_E\rangle$。

那么对这个精确入态或出态 $|\psi_E^{(\pm)}\rangle$ 有

$$
(E - H_0) |\psi_E^{(\pm)}\rangle = V |\psi_E^{(\pm)}\rangle
$$

这给出第一种“源”的理解：把 $V |\psi_E^{(\pm)}\rangle$ 看成源，那么自由格林算符负责把这个源传播出去，于是得到

$$
|\psi_E^{(\pm)}\rangle
=
|\phi_E\rangle
+
G_0^{(\pm)}(E) V |\psi_E^{(\pm)}\rangle
$$

这就是 Lippmann-Schwinger 方程。

同一个方程还可以换一个角度来看。因为

$$
(E - H) |\phi_E\rangle = - V |\phi_E\rangle
$$

所以

$$
(E - H)\bigl(|\psi_E^{(\pm)}\rangle - |\phi_E\rangle\bigr)
=
V |\phi_E\rangle
$$

于是得到第二种“源”的理解：把自由参考 ket 经相互作用产生的 $V |\phi_E\rangle$ 当成源，然后由全格林算符传播，

$$
|\psi_E^{(\pm)}\rangle
=
|\phi_E\rangle
+
G^{(\pm)}(E) V |\phi_E\rangle
$$

这两个写法完全等价，差别只在于你选择把哪一部分吸收到传播子里。一个用自由 Green 算符加上“未知的精确散射态”作为源，另一个用全 Green 算符加上“已知的自由参考 ket”作为源。它们之间正是由 Dyson 方程连接起来的。

## 4. 从时间演化看格林算符

这一节最容易混淆的地方，是 $U(t)$、时域 Green 算符、以及能量域 Green 算符并不是同一个对象。

时间依赖薛定谔方程的齐次解由时间演化算符给出：

$$
|\psi(t)\rangle = U(t) |\psi(0)\rangle,
\qquad
U(t) = e^{-iHt/\hbar}
$$

但 Green 算符本来是用来求解含源方程的。若写成

$$
\left(i\hbar \frac{\partial}{\partial t} - H\right) |\psi(t)\rangle = |s(t)\rangle
$$

那么 retarded Green 算符 $G^R(t-t')$ 满足

$$
\left(i\hbar \frac{\partial}{\partial t} - H\right) G^R(t-t') = \delta(t-t')\, I
$$

并且要求 $t < t'$ 时传播为零，也就是因果性。对时间无关哈密顿量，这个方程的解正是

$$
G^R(t) = - \frac{i}{\hbar}\, \theta(t)\, U(t)
=
- \frac{i}{\hbar}\, \theta(t)\, e^{-iHt/\hbar}
$$

advanced Green 算符则是

$$
G^A(t) = \frac{i}{\hbar}\, \theta(-t)\, U(t)
=
\frac{i}{\hbar}\, \theta(-t)\, e^{-iHt/\hbar}
$$

所以，严格地说，时域 Green 算符不是单独的 $U(t)$，而是“带因果投影的 $U(t)$”。$\theta(t)$ 或 $\theta(-t)$ 决定了你只保留哪个时间方向的传播。

接着对时间变量做 Fourier 变换，就得到能量域 Green 算符。对 retarded 情形，

$$
G^{(+)}(E)
=
\int_{-\infty}^{\infty} dt\, e^{iEt/\hbar} G^R(t)
=
- \frac{i}{\hbar} \int_0^\infty dt\, e^{iEt/\hbar} U(t)
$$

把 $U(t)=e^{-iHt/\hbar}$ 代回去，

$$
G^{(+)}(E)
=
- \frac{i}{\hbar} \int_0^\infty dt\, e^{i(E-H)t/\hbar}
$$

为了让积分收敛，必须加入因果规定的收敛因子：

$$
G^{(+)}(E)
=
\lim_{\epsilon \to 0^+}
\left(
- \frac{i}{\hbar}
\int_0^\infty dt\,
e^{i(E-H+i\epsilon)t/\hbar}
\right)
=
\frac{1}{E - H + i0}
$$

也就是说，能量域的 retarded Green 算符确实就是 $U(t)$ 的单边 Fourier-Laplace 变换。

同理，

$$
G^{(-)}(E)
=
\int_{-\infty}^{\infty} dt\, e^{iEt/\hbar} G^A(t)
=
\frac{i}{\hbar} \int_{-\infty}^0 dt\, e^{iEt/\hbar} U(t)
$$

于是

$$
G^{(-)}(E)
=
\lim_{\epsilon \to 0^+}
\left(
\frac{i}{\hbar}
\int_{-\infty}^0 dt\,
e^{i(E-H-i\epsilon)t/\hbar}
\right)
=
\frac{1}{E - H - i0}
$$

这里要特别强调一个细节：如果你把整条时间轴上的 $U(t)$ 直接做普通 Fourier 变换，

$$
\int_{-\infty}^{\infty} dt\, e^{iEt/\hbar} U(t)
=
\int_{-\infty}^{\infty} dt\, e^{i(E-H)t/\hbar}
=
2\pi \hbar\, \delta(E-H)
$$

得到的是谱投影算符，而不是 resolvent。真正给出

$$
G^{(\pm)}(E) = \frac{1}{E-H\pm i0}
$$

的是带有 $\theta(\pm t)$ 的因果传播，或者等价地说，是带收敛因子的单边 Fourier-Laplace 变换。

因此，从时间观点看，$\pm i0$ 的本质就是因果规定在能量表象中的遗迹：在时间域里它对应 $\theta(\pm t)$，在复能量平面里它对应极点绕开的方向。

最后，由定义立刻可得

$$
(E - H \pm i0)\, G^{(\pm)}(E) = I
$$

这正是格林算符在能量表象里作为逆算符的含义。

## 5. 坐标表象中的传播意义

一旦进入坐标表象，

$$
G^{(\pm)}(\mathbf r, \mathbf r'; E)
=
\langle \mathbf r | G^{(\pm)}(E) | \mathbf r' \rangle
$$

它就能被直观理解为：一个振幅从源点 $\mathbf r'$ 传播到观察点 $\mathbf r$ 的能量固定传播核。

对自由粒子，

$$
H_0 = - \frac{\hbar^2}{2m} \nabla^2
$$

因此自由格林函数满足

$$
\left(
E + \frac{\hbar^2}{2m}\nabla^2
\right)
G_0^{(\pm)}(\mathbf r, \mathbf r'; E)
=
\delta^{(3)}(\mathbf r - \mathbf r')
$$

当 $E = \hbar^2 k^2 / 2m$ 且 $k > 0$ 时，其三维解为

$$
G_0^{(\pm)}(\mathbf r, \mathbf r'; E)
=
- \frac{m}{2\pi \hbar^2}
\frac{e^{\pm i k |\mathbf r - \mathbf r'|}}{|\mathbf r - \mathbf r'|}
$$

这里已经把边界条件写进去了：

- $G_0^{(+)}$ 含有 $e^{+ikR}/R$，表示向外传播的出射球面波。
- $G_0^{(-)}$ 含有 $e^{-ikR}/R$，表示向内汇聚的入射球面波。

于是 Lippmann-Schwinger 方程在坐标表象下变成

$$
\psi^{(+)}(\mathbf r)
=
\phi(\mathbf r)
+
\int d^3 r'\,
G_0^{(+)}(\mathbf r, \mathbf r'; E)\,
V(\mathbf r')\,
\psi^{(+)}(\mathbf r')
$$

如果入射态是平面波 $\phi(\mathbf r) = e^{i\mathbf k \cdot \mathbf r}$，并且考察远区 $r \to \infty$，则有近似

$$
|\mathbf r - \mathbf r'|
\approx
r - \hat{\mathbf r}\cdot \mathbf r'
$$

从而

$$
G_0^{(+)}(\mathbf r, \mathbf r'; E)
\sim
- \frac{m}{2\pi \hbar^2}
\frac{e^{ikr}}{r}\,
e^{-ik \hat{\mathbf r}\cdot \mathbf r'}
$$

代回后便得到标准远区形式

$$
\psi^{(+)}(\mathbf r)
\sim
e^{i\mathbf k \cdot \mathbf r}
+
f(\hat{\mathbf r}, \mathbf k)\, \frac{e^{ikr}}{r}
$$

其中散射振幅为

$$
f(\hat{\mathbf r}, \mathbf k)
=
- \frac{m}{2\pi \hbar^2}
\int d^3 r'\,
e^{-ik \hat{\mathbf r}\cdot \mathbf r'}\,
V(\mathbf r')\,
\psi^{(+)}(\mathbf r')
$$

 $G_0^{(+)}$ 的远区渐近已经自动替你选中了出射波边界条件，于是散射振幅会自己从积分核里冒出来。

## 6. 解析结构、极点与连续谱

若形式上把谱分解写出来，格林算符可表示为

$$
G(z)
=
\sum_n \frac{|n\rangle \langle n|}{z - E_n}
+
\int dE'\, \frac{|E'\rangle \langle E'|}{z - E'}
$$

这里离散部分对应束缚态，连续积分部分对应散射态。这个表达式马上揭示了两个事实。

第一，若系统存在束缚态能级 $E_n$，那么 $G(z)$ 在 $z = E_n$ 处有极点，其留数正是投影算符

$$
\operatorname*{Res}_{z = E_n} G(z) = |n\rangle \langle n|
$$

因此极点位置给出本征值，极点留数给出本征态的信息。

第二，连续谱不会表现成孤立极点，而会在实轴上表现为边界值的不连续。用分布恒等式

$$
\frac{1}{E - E' \pm i0}
=
\mathcal P \frac{1}{E - E'}
\mp
i\pi \delta(E - E')
$$

可得

$$
G(E + i0) - G(E - i0) = - 2\pi i\, \delta(E - H)
$$

这说明格林算符跨越实轴的“跳跃”直接就是谱测度。换句话说，连续谱虽然不对应单个极点，却完整地编码在 $G(E \pm i0)$ 的虚部和不连续性里。

常见的谱函数定义为

$$
A(E) = i \bigl[G(E + i0) - G(E - i0)\bigr]
=
2\pi \delta(E - H)
$$

若再取迹，就得到态密度与 Green 算符虚部之间的关系

$$
\rho(E)
=
\operatorname{Tr}\,\delta(E - H)
=
- \frac{1}{\pi}\, \operatorname{Im}\, \operatorname{Tr} G(E + i0)
$$

## 7. 共振为什么也会表现成极点

对自伴哈密顿量来说，物理谱本身位于实轴上；但如果把 $G(z)$ 穿过连续谱支割做解析延拓，就可能在第二张 Riemann 面上遇到复极点

$$
z_R = E_R - \frac{i}{2}\Gamma_R
$$

这类极点不再对应可归一化的束缚态，而对应寿命有限的共振态。它们的实部给出共振位置，虚部给出衰变宽度。散射截面里的 Breit-Wigner 形状，本质上正是这个复极点在实轴附近留下的痕迹。

因此，从格林算符的角度看：

- 束缚态是物理面上的实极点。
- 连续谱是实轴边界值的跳跃。
- 共振是解析延拓后第二张面上的复极点。

这三类现象虽然在波函数语言里看上去很不一样，但在 resolvent 语言里都只是同一个复变函数的不同奇性。

## 8. 小结

格林算符之所以在散射理论里特别有力，是因为它把几件原本分散的事情统一了起来：

- 作为逆算符，它把含源方程变成积分方程。
- 作为时间传播子的 Fourier 变换，它把因果性写成 $\pm i0$。
- 作为坐标核，它把出射波或入射波边界条件直接写进空间传播。
- 作为 resolvent，它把束缚态、连续谱和共振全部编码进复平面的解析结构。

所以在散射理论里，真正需要记住的不是一句“格林函数用来解微分方程”，而是下面这条逻辑链：

$$
\text{边界条件}
\Longrightarrow
G^{(\pm)}(E)
\Longrightarrow
\text{Lippmann-Schwinger 方程}
\Longrightarrow
\text{散射振幅与谱结构}
$$

之后自然会接到 $T$ 矩阵、$S$ 矩阵，以及具体模型中的自能与共振极点分析。
