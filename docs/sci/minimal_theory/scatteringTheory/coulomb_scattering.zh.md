# Coulomb 散射的完整形式

本篇沿 Taylor《Scattering Theory》第 14 章的脉络，把 `S_matrix_and_cross_section.zh.md:540` 末尾留下的备注展开成一条完整的逻辑链：从 Møller 算符的失败、到 Dollard 修正传播子、再到径向 Coulomb 函数 $F_l, G_l$、Coulomb 相移 $\sigma_l$、Rutherford 振幅、$f = f_C + f_{SR}$ 分解，以及 Coulomb-distorted Born。每一节都把短程势的对应结论与 Coulomb 的修正并排列出，目的是看清"哪些代数结构原封不动地搬过去，哪些必须重写"。

## 目标

短程势框架（$|V(r)| < C/r^{1+\epsilon}$，$\epsilon > 0$）下，主线笔记给出的整套结论——渐近条件、Møller 算符强极限、$S = \Omega_-^\dagger \Omega_+$、Lippmann–Schwinger 方程、$d\sigma/d\Omega = |f|^2$、光学定理——都不假思索地依赖一件事：自由演化 $e^{-iH_0 t}$ 是合格的参考动力学。

Coulomb 势

$$
V_C(r) = \frac{Z_1 Z_2 e^2}{r} \tag{Vc}
$$

衰减恰好慢到把这件事破坏掉。它属于"长程势"（long-range potential），$V \sim 1/r$，不满足 $1/r^{1+\epsilon}$ 的条件。结果是：自由波包 $e^{-iH_0 t}|\phi\rangle$ 在远未来与真实波包 $e^{-iHt}|\psi\rangle$ 之间始终差一个发散的相位累积。Møller 算符的强极限不存在，下游一切都垮掉。

物理上的图像：经典 Coulomb 双曲轨道在 $r \to \infty$ 时仍偏离直线一个对数大小的量（轨迹相对于直线的偏角衰减为 $\ln r / r$ 而非 $1/r$）。量子层面，这表现为 $\psi^{(+)}$ 的渐近形式不再是 $e^{i\mathbf{k}\cdot\mathbf{r}} + f(\theta)\,e^{ikr}/r$，而要在两个项里都加上对数相位修正。

这一篇只处理弹性、自旋无关、单中心 Coulomb 势的"完整形式"。极化与 Coulomb 的耦合在姊妹篇 `polarization_formalism.zh.md:538` 留作 next-step。

## 长程势对 Møller 强极限的破坏

回顾短程势下的定义（`T_and_U_operators.zh.md:80`）

$$
\Omega_\pm = \operatorname*{s-lim}_{t \to \mp \infty} e^{iHt/\hbar} e^{-iH_0 t/\hbar} \tag{Mol}
$$

强极限存在的核心是渐近条件：对任何归一化 $|\phi\rangle$，

$$
\bigl\| e^{-iHt/\hbar} \Omega_+ |\phi\rangle - e^{-iH_0 t/\hbar}|\phi\rangle \bigr\| \xrightarrow{t \to -\infty} 0 \tag{AC-SR}
$$

证明依赖 Cook 引理：只要 $\int_{-\infty}^0 dt\, \|V e^{-iH_0 t}|\phi\rangle\|$ 有限，强极限就存在。对 $V \sim 1/r^{1+\epsilon}$，把 $|\phi\rangle$ 取成动量空间紧支撑波包，$e^{-iH_0 t}|\phi\rangle$ 在坐标空间中以 $|t|^{-3/2}$ 扩散，$\|V e^{-iH_0 t}\phi\|$ 衰减为 $|t|^{-(1+\epsilon)}$，时间积分收敛。

对 $V_C = Z_1Z_2 e^2/r$，同样的估计给

$$
\|V_C e^{-iH_0 t}\phi\| \sim |t|^{-1}
$$

时间积分发散为 $\ln |t|$。Cook 判据失效——强极限本身不存在。

更具体地，把 $\Omega_+$ 写成形式积分

$$
\Omega_+ = I + i \int_{-\infty}^0 dt\, e^{iHt/\hbar} V e^{-iH_0 t/\hbar}
\, \cdot \frac{1}{\hbar}
$$

被积函数模长以 $1/|t|$ 衰减，积分给出对数发散相位。物理上这就是经典 Coulomb 轨道在远过去仍在不断"被偏转"——相位累积不收敛。

## Dollard 处方与修正 Møller 算符

Dollard（1964, 1971）提出的解决方案：把参考动力学从纯自由演化改成一个加了对数相位修正的渐近传播子 $U_C(t)$，使新的强极限存在。

对 Coulomb 势，标准结果为

$$
U_C(t) = e^{-iH_0 t/\hbar}\, \exp\!\Bigl[-i\eta(p)\,\mathrm{sgn}(t)\,\ln\!\bigl|2 H_0 t/\hbar\bigr|\Bigr] \tag{UC}
$$

其中

$$
\eta(p) = \frac{Z_1 Z_2 e^2 m}{\hbar^2 |\mathbf{p}|/\hbar}
= \frac{Z_1 Z_2 e^2 \mu}{\hbar^2 k},
\qquad k = |\mathbf{p}|/\hbar \tag{eta}
$$

是 Sommerfeld 参数（动量算符的函数；这里 $\eta$ 与 $H_0$ 对易，故指数可写）。修正 Møller 算符定义为

$$
\Omega_\pm^C = \operatorname*{s-lim}_{t \to \mp \infty} e^{iHt/\hbar}\, U_C(t) \tag{Mol-C}
$$

散射算符 $S^C = (\Omega_-^C)^\dagger \Omega_+^C$。

self-derive 思路：对自由波包 $|\phi(t)\rangle = e^{-iH_0 t}|\phi\rangle$，用稳相点法求其在远区的坐标表示，$\phi(\mathbf r, t) \sim (m/it)^{3/2}\exp[i m r^2/(2\hbar t)]\,\tilde\phi(m\mathbf r/t)$。代入 $V_C$ 并对时间积分，主导项就是 $-\eta(p)\,\mathrm{sgn}(t)\,\ln|2 E_p t/\hbar|/\hbar$ 的相位，其中 $E_p = p^2/(2m)$。把这个相位"反加"到参考演化里，就得到 $\text{(UC)}$。

物理理解：去掉对数相位等价于在时间域抵消 $|t|^{i\eta\,\mathrm{sgn}(t)}$ 因子，这对应永远抵不消的库仑相位累积。短程势下这一项不出现是因为它恰好正比于 $\eta \propto 1/k$ 与势强度——Coulomb 让它有限非零。

注意三件事：

- $\Omega_\pm^C$ 与 $|\alpha\rangle$ 的乘积 $|\psi_\alpha^{(\pm)C}\rangle$ 仍是 $H = H_0 + V_C$ 的精确广义本征态，与 `T_and_U_operators.zh.md:120` 的"精确入出态"是同一个数学对象，只是"参考动力学"被改写。
- $U_C(t)$ 不是 unitary 群（它对 $t$ 的依赖含 $\mathrm{sgn}$ 与 $\ln|t|$），但它把在 $H_0$ 下散布的自由波包带到与 $e^{-iHt}$ 渐近匹配的位置。
- 短程极限 $V \to V_{SR}$ 时 $\eta \to 0$，$U_C \to e^{-iH_0 t}$，整套退化回 $\text{(Mol)}$。

## 径向 Coulomb 方程与 $F_l, G_l$

定态层面，规则化 Schrödinger 方程取无量纲化 $\hbar = 2m = 1$（与 `partial_wave_projection.zh.md` 一致），

$$
\Bigl[\frac{d^2}{dr^2} + k^2 - \frac{2k\eta}{r} - \frac{l(l+1)}{r^2}\Bigr] u_l(r) = 0 \tag{rad-C}
$$

记 $\rho = kr$，$u_l = u_l(\rho/k)$，方程化为

$$
\frac{d^2 u_l}{d\rho^2} + \Bigl[1 - \frac{2\eta}{\rho} - \frac{l(l+1)}{\rho^2}\Bigr] u_l = 0 \tag{rad-rho}
$$

这是合流超几何方程在变量替换下的标准形式。两组线性独立解为：

regular 解 $F_l(\eta, \rho)$，在原点

$$
F_l(\eta, \rho) \xrightarrow{\rho \to 0} C_l(\eta)\, \rho^{l+1},
\qquad
C_l(\eta) = \frac{2^l\, e^{-\pi\eta/2}\,|\Gamma(l+1+i\eta)|}{(2l+1)!} \tag{Cl}
$$

irregular 解 $G_l(\eta, \rho)$，在原点 $\sim \rho^{-l}$ 发散。

它们与合流超几何函数的连接（self-derive 给出）：写 $u_l = e^{i\rho}\rho^{l+1} w(\rho)$ 代入 $\text{(rad-rho)}$，得

$$
\rho \frac{d^2 w}{d\rho^2} + (2l+2 - 2i\rho)\frac{dw}{d\rho} - 2i(l+1+i\eta)\, w = 0
$$

这是 Kummer 方程 $z w'' + (b-z) w' - a w = 0$，参数 $z = -2i\rho$，$a = l+1+i\eta$，$b = 2l+2$。两组解 $M(a,b,z)$（regular）与 $U(a,b,z)$（irregular）分别给出

$$
F_l(\eta, \rho) = C_l(\eta)\, \rho^{l+1}\, e^{-i\rho}\, M(l+1+i\eta,\, 2l+2,\, 2i\rho) \tag{F-M}
$$

$G_l$ 由 $U$ 给出（标准实数线性组合，使其在远区为 cosine）。

渐近行为 $\rho \to \infty$：

$$
F_l(\eta, \rho) \xrightarrow{\rho \to \infty} \sin\!\bigl[\rho - \tfrac{l\pi}{2} - \eta \ln(2\rho) + \sigma_l(\eta)\bigr] \tag{F-asy}
$$

$$
G_l(\eta, \rho) \xrightarrow{\rho \to \infty} \cos\!\bigl[\rho - \tfrac{l\pi}{2} - \eta \ln(2\rho) + \sigma_l(\eta)\bigr] \tag{G-asy}
$$

与短程势的渐近 $u_l(r) \to \sin(kr - l\pi/2 + \delta_l)$ 对比，差别有两条：

- 多了 $-\eta \ln(2kr)$，这是对数相位。它在 $r \to \infty$ 不消失，所以不能被吸收进相移；它来自 $V_C$ 的长程性。
- 多了 Coulomb 相移 $\sigma_l(\eta)$（下一节）。

数值角度：$F_l, G_l$ 由 GSL、`scipy.special.coulomb_phase`、`scipy.special.fdfdr_coulomb` 类例程提供；递推（在 $l$ 上稳定向上 / 向下）是实现细节，留给 `examples/11_coulomb_demo`。

## Coulomb 相移 $\sigma_l$

闭式

$$
\sigma_l(\eta) = \arg \Gamma(l+1+i\eta) \tag{sigma-l}
$$

证明思路：用 $\text{(F-M)}$，把 $M(a,b,2i\rho)$ 在 $|\rho|\to\infty$ 用 Kummer 大变量渐近展开为 $\Gamma(b)/\Gamma(b-a)\,(-2i\rho)^{-a} + \Gamma(b)/\Gamma(a)\,(2i\rho)^{a-b}\,e^{2i\rho}$，组合相位即得 $\sigma_l = \arg\Gamma(l+1+i\eta)$。

由 $\Gamma(l+1+i\eta) = (l+i\eta)\Gamma(l+i\eta)$ 立得递推

$$
\sigma_{l+1}(\eta) = \sigma_l(\eta) + \arctan\!\frac{\eta}{l+1} \tag{sigma-rec}
$$

self-derive：取 $\arg$，用 $\arg\Gamma(l+1+i\eta) = \arg(l + i\eta) + \arg\Gamma(l+i\eta) = \arctan(\eta/l) + \sigma_{l-1}$；移位下标即得 $\text{(sigma-rec)}$。

$\sigma_0(\eta)$ 的级数。从 Weierstrass 乘积 $1/\Gamma(z) = z e^{\gamma z}\prod_{n\ge 1}(1 + z/n) e^{-z/n}$，取 $z = 1+i\eta$，分离实虚部，对 $\arg$ 求和：

$$
\sigma_0(\eta) = -\gamma \eta + \sum_{n=1}^{\infty}\Bigl[\frac{\eta}{n} - \arctan\!\frac{\eta}{n}\Bigr] \tag{sigma-0-ser}
$$

其中 $\gamma$ 是 Euler–Mascheroni 常数。这条级数在 $|\eta|$ 不太大时收敛，每一项 $\sim \eta^3/(3 n^3)$。极限 $\eta \to 0$：每一项消失，$\sigma_0 \to 0$；递推给 $\sigma_l \to 0$。这与短程势退化情形一致。

物理意义：纯 Coulomb 散射（无短程势）的总分波相移由 $\sigma_l$ 完全给出，与势的短程细节无关。这是 "$1/r$ 势是积分得动" 的特殊性体现——所有依赖能量的相移都装进一个 Gamma 函数。

## Rutherford 振幅与发散总截面

把 $\text{(F-asy)}$ 代回三维定态，并把入射方向取 $\hat z$，纯 Coulomb 散射波函数的渐近形式为

$$
\psi_C^{(+)}(\mathbf r) \xrightarrow{r\to\infty}
e^{i[\mathbf k \cdot \mathbf r + \eta \ln(kr - \mathbf k \cdot \mathbf r)]}
+ f_C(\theta)\,\frac{e^{i[kr - \eta \ln(2kr)]}}{r} \tag{psi-C}
$$

注意"入射"项不再是 $e^{i\mathbf k\cdot \mathbf r}$，而是带对数畸变 $\eta\ln(kr - \mathbf k\cdot\mathbf r) = \eta\ln[kr(1-\cos\theta)]$ 的扭曲平面波；"出射"项的球面波相位也带 $-\eta\ln(2kr)$。两个对数项都不能丢——它们是长程势的渐近残留。

$f_C(\theta)$ 的闭式（self-derive 来源）：把 $\psi_C^{(+)}$ 用 parabolic 坐标 $\xi = r-z, \eta_p = r+z$ 求解，得 $\psi_C^{(+)} = e^{-\pi\eta/2}\Gamma(1+i\eta)\,e^{i\mathbf k\cdot\mathbf r}\,M(-i\eta, 1, ik\xi)$；对 $M$ 在 $k\xi \to \infty$ 用大变量渐近 $M(a,1,z) \sim \Gamma(1)/\Gamma(1-a)(-z)^{-a} + \Gamma(1)/\Gamma(a) z^{a-1}e^z$，把第一项对应到入射、第二项对应到散射，比对球面波系数即得

$$
f_C(\theta) = -\frac{\eta}{2k\sin^2(\theta/2)}\,
\exp\!\bigl[-i\eta \ln\sin^2(\theta/2) + 2i\sigma_0(\eta)\bigr] \tag{fC}
$$

复相位的来源拆开看：

- $-i\eta\ln\sin^2(\theta/2)$ 来自 $M(-i\eta,1,ik\xi)$ 渐近中 $(-z)^{-a} = (-ik\xi)^{i\eta}$，其中 $\xi = r(1-\cos\theta) = 2r\sin^2(\theta/2)$，对数项的 $r$ 部分被并入"扭曲入射波"的 $\eta\ln(kr - kz)$；剩下的 $\eta\ln\sin^2(\theta/2)$ 留在散射振幅里。
- $2i\sigma_0(\eta) = 2\arg\Gamma(1+i\eta)$ 来自前面 prefactor $\Gamma(1+i\eta)$ 与 $1/\Gamma(1+i\eta)^*$ 的商（在 $\Gamma(1-a)$ 中 $a = -i\eta$）。

模平方给 Rutherford 微分截面

$$
\frac{d\sigma_C}{d\Omega} = |f_C(\theta)|^2 = \frac{\eta^2}{4 k^2 \sin^4(\theta/2)}
= \Bigl(\frac{Z_1 Z_2 e^2}{4 E}\Bigr)^2 \frac{1}{\sin^4(\theta/2)} \tag{Ruth}
$$

其中 $E = \hbar^2 k^2/(2\mu)$。这与经典 Rutherford 公式逐字相同——量子-经典对应在这里"玄妙"的原因是 $V \sim 1/r$ 恰好是经典 Kepler 问题的可积情形，所有量子修正都凝聚在 $f_C$ 的相位里，不进入 $|f_C|^2$。

总截面

$$
\sigma_C^\text{tot} = \int |f_C|^2 d\Omega \propto \int_0^\pi \frac{\sin\theta\, d\theta}{\sin^4(\theta/2)}
\xrightarrow{\theta\to 0} \infty \tag{sigtot-C}
$$

前向 $\theta \to 0$ 处奇异，物理上是因为任意大 impact parameter 的入射粒子都被偏转（$1/r$ 势的力学到处都不为零）——这正对应 Cook 判据的失败。

光学定理在纯 Coulomb 中要小心：$\mathrm{Im}\, f_C(0) = +\infty$，与 $\sigma_C^\text{tot} = \infty$ 在"两个无穷"的意义下匹配，但定理的有限版本（`S_matrix_and_cross_section.zh.md:451`）需要把 $f_C$ 减掉得到正则化的 $f_{SR}$ 后才能用——这是下一节的事。

## 分波展开 Coulomb 振幅

形式上，

$$
f_C(\theta) = \frac{1}{2ik}\sum_{l=0}^{\infty}(2l+1)\bigl[e^{2i\sigma_l(\eta)} - 1\bigr] P_l(\cos\theta) \tag{fC-pw}
$$

形式 $\text{(fC-pw)}$ 与短程势分波展开（`partial_wave_projection.zh.md:355`-369）

$$
f_{SR}(\theta) = \frac{1}{2ik}\sum_l (2l+1)\bigl[e^{2i\delta_l} - 1\bigr] P_l(\cos\theta)
$$

形式上一模一样——只把短程相移 $\delta_l$ 换成 Coulomb 相移 $\sigma_l$。

但有两条关键区别：

第一，这个级数实际上不收敛（在普通函数意义下）。原因：$\sigma_l \to \eta\,\ln l - \eta(\ln \eta - 1) + \pi/4 + O(1/l)$ 在大 $l$ 渐近为对数发散，$e^{2i\sigma_l} - 1$ 不衰减。$P_l(\cos\theta)$ 在 $\theta = 0$ 处取 $1$，整数级数发散，反映的就是 $f_C$ 的前向奇异 $1/\sin^4(\theta/2) \to \infty$。

第二，$\text{(fC-pw)}$ 与闭式 $\text{(fC)}$ 的等价仅在 distributional 意义下成立。具体地，对任何 $0 < \theta < \pi$ 有平均收敛：用 Abel 求和或 Cesàro 求和能恢复 $\text{(fC)}$；但逐项级数本身不行。数值实践中要么用闭式 $\text{(fC)}$，要么对级数做正则化（如先减去 Born 近似的 $-\eta/(k(1-\cos\theta))$ 主导奇异部分再求和）。

这是 Coulomb 直接套分波 LS 方程（`partial_wave_projection.zh.md:340`）失败的另一个症状：$V_l(k', k) = (2/\pi)\int dr\, r^2\, j_l(k'r) V_C(r) j_l(kr)$ 在 $r \to \infty$ 处对数发散，分波势矩阵元本身不是良定义函数。

## Coulomb 加短程势的分解

现实情形：核物理、原子物理几乎所有过程都是

$$
V = V_C + V_{SR}, \qquad V_{SR}(r) \in O(r^{-1-\epsilon}) \tag{V-tot}
$$

例如 pp 散射（Coulomb 加核力）、$\alpha$ + 重核（Coulomb 加 optical potential）。直接用短程势主线笔记的工具不行（$V$ 含 $V_C$）；纯 Coulomb 工具也不行（缺 $V_{SR}$）。正确做法是把 Coulomb 部分作为"已解掉的参考动力学"，对 $V_{SR}$ 做扰动。

技术上：把 $\text{(Mol-C)}$ 改成 $H = H_C + V_{SR}$ 的两步定义。$H_C = H_0 + V_C$ 已经"用 Dollard 处方驯服"，相对 $H_C$ 再做一次普通短程 Møller 极限：

$$
\Omega_\pm^\text{full} = \operatorname*{s-lim}_{t\to\mp\infty} e^{iHt/\hbar}\, e^{-iH_C t/\hbar} \cdot \Omega_\pm^C(\text{from } H_C \text{ to } H_0\text{ + Dollard})
$$

数学上严格化要点是：$V_{SR}$ 相对 $H_C$ 仍是短程的（$e^{-iH_C t}$ 让波包扩散与自由情形同阶），所以这一步重新满足 Cook 判据。

最终散射振幅可分解：

$$
f(\theta) = f_C(\theta) + f_{SR}(\theta) \tag{f-decomp}
$$

其中 $f_{SR}$ 的分波形式（self-derive）：径向 Coulomb-distorted Schrödinger 方程

$$
\Bigl[\frac{d^2}{dr^2} + k^2 - \frac{2k\eta}{r} - \frac{l(l+1)}{r^2} - U_{SR}(r)\Bigr] u_l(r) = 0 \tag{rad-CS}
$$

（$U_{SR} = 2\mu V_{SR}/\hbar^2$）的物理解 $u_l$，渐近形式为

$$
u_l(r) \xrightarrow{r\to\infty} F_l(\eta, kr)\cos\delta_l^{SR}(k) + G_l(\eta, kr)\sin\delta_l^{SR}(k) \tag{ul-asy}
$$

与短程势 $u_l \to \sin(kr - l\pi/2 + \delta_l)$ 的形式一一对应，只是把自由 Riccati–Bessel $\hat j_l = \sin(kr - l\pi/2)$ 换成 Coulomb $F_l$、把 $\hat n_l$ 换成 $G_l$。$\delta_l^{SR}$ 是 Coulomb-distorted 短程相移；它定义在 Coulomb 波这一组畸变波基底上，与 $V_{SR}$ 的具体形状有关。

把 $\text{(ul-asy)}$ 与平面波 + 球面波拼装回三维（用 Coulomb 部分的展开）：

$$
f_{SR}(\theta) = \frac{1}{2ik}\sum_l (2l+1)\, e^{2i\sigma_l(\eta)}\,\bigl[e^{2i\delta_l^{SR}} - 1\bigr]\, P_l(\cos\theta) \tag{fSR-pw}
$$

每一分波振幅前都多一个 Coulomb 因子 $e^{2i\sigma_l}$。这与纯短程的 $\text{(fC-pw)}$ 不一样，那里是 $e^{2i\delta_l} - 1$ 整体。$f_{SR}$ 的分波级数收敛（$\delta_l^{SR}$ 对大 $l$ 衰减，$V_{SR}$ 短程让有限 $l$ 起作用）。

全相移记号：

$$
\delta_l^\text{tot} = \sigma_l + \delta_l^{SR} \tag{delta-tot}
$$

这是"分相移加和"——但只在 Coulomb-distorted 框架下成立，而且 $\delta_l^{SR}$ 本身依赖于 Coulomb 波作畸变波（不是用 $V_{SR}$ 单独定义的相移；那个会得到不同的数）。

实验观测量：

$$
\frac{d\sigma}{d\Omega} = |f|^2 = |f_C|^2 + 2\,\mathrm{Re}\bigl[f_C^*(\theta) f_{SR}(\theta)\bigr] + |f_{SR}|^2 \tag{dsig-CS}
$$

中间的 Coulomb–nuclear 干涉项 $2\mathrm{Re}(f_C^* f_{SR})$ 是 pp、$pd$、$p\alpha$ 等弹性散射在小角度（前向以外）最敏感的观测量。$|f_{SR}|^2$ 在大角度主导（$f_C$ 衰减为 $1/\sin^4(\theta/2)$，$f_{SR}$ 的角分布由短程势决定）。

## Coulomb-distorted Born 近似

把 $V_{SR}$ 当扰动，零阶用 Coulomb 波$\psi_C^{(\pm)}$ 替换主线 Born 近似（`S_matrix_and_cross_section.zh.md:506`-510）里的平面波：

$$
f_{SR}^\text{CB}(\mathbf k_f \leftarrow \mathbf k_i)
= -\frac{\mu}{2\pi\hbar^2}\int d^3 r\, \bigl[\psi_C^{(-)}(\mathbf k_f, \mathbf r)\bigr]^*\, V_{SR}(\mathbf r)\,\psi_C^{(+)}(\mathbf k_i, \mathbf r) \tag{fSR-CB}
$$

self-derive：从 Lippmann–Schwinger 在 $V = V_C + V_{SR}$ 下分裂为 $V_{SR}$ 围绕 Coulomb Green 函数 $G_C^{(+)} = (E - H_C + i0)^{-1}$，

$$
\psi^{(+)} = \psi_C^{(+)} + G_C^{(+)} V_{SR} \psi^{(+)}
$$

迭代一次（第一阶 Born），

$$
\psi^{(+)} \approx \psi_C^{(+)} + G_C^{(+)} V_{SR} \psi_C^{(+)}
$$

把其远场行为提出来即得 $\text{(fSR-CB)}$。$\psi_C^{(-)}(\mathbf k_f, \mathbf r) = [\psi_C^{(+)}(-\mathbf k_f, \mathbf r)]^*$ 用时间反演关系。

与短程纯 Born $f^B = -(\mu/2\pi\hbar^2)\int e^{-i\mathbf q\cdot\mathbf r} V_{SR}\,d^3r$ 对照（$\mathbf q = \mathbf k_f - \mathbf k_i$），区别只在内外两个波函数：

| | 自由 Born | Coulomb-distorted Born |
|:--|:--|:--|
| 出射方向波 | $e^{-i\mathbf k_f\cdot\mathbf r}$ | $\psi_C^{(-)}(\mathbf k_f, \mathbf r)$ |
| 入射方向波 | $e^{i\mathbf k_i \cdot \mathbf r}$ | $\psi_C^{(+)}(\mathbf k_i, \mathbf r)$ |
| 系数 | $-\mu/(2\pi\hbar^2)$ | 同 |
| 适用场景 | 弱短程势、无 Coulomb | 弱短程势 + 强 Coulomb |

分波形式：把两个 Coulomb 波函数都展开（Rayleigh-类公式 + 加法定理），$V_{SR}$ 取中心势 $V_{SR}(r)$，得

$$
f_{SR}^\text{CB}(\theta) = -\frac{2\mu}{k\hbar^2}\sum_l(2l+1)\, e^{2i\sigma_l}\, P_l(\cos\theta)\, \int_0^\infty dr\, F_l(\eta, kr)^2\, V_{SR}(r) \tag{fSR-CB-pw}
$$

注意径向积分核是 $F_l^2$（不是自由 Born 的 $j_l^2$），且每分波有 Coulomb 相位因子 $e^{2i\sigma_l}$。比较 $\text{(fSR-pw)}$ 的精确分波

$$
e^{2i\sigma_l}(e^{2i\delta_l^{SR}} - 1) \approx e^{2i\sigma_l} \cdot 2i\delta_l^{SR}\quad (\delta_l^{SR}\ll 1)
$$

可读出 Coulomb-distorted Born 近似下的 $\delta_l^{SR}$：

$$
\delta_l^{SR,\text{CB}}(k) \approx -\frac{2\mu}{\hbar^2 k}\int_0^\infty dr\, F_l(\eta, kr)^2\, V_{SR}(r) \tag{delta-CB}
$$

这是数值上常用的快速估计，等价于 distorted-wave Born 近似（DWBA）的 onshell elastic 特例。完整 DWBA（含通道耦合）留给研究轨 C 篇。

极限 $\eta \to 0$：$F_l(\eta, kr) \to (kr) j_l(kr)$（精确），$\sigma_l \to 0$，$\text{(delta-CB)}$ 退化为短程纯 Born 相移

$$
\delta_l^{B}(k) \to -\frac{2\mu k}{\hbar^2}\int_0^\infty dr\, r^2\, j_l(kr)^2\, V_{SR}(r)
$$

这与教科书结果一致。

## 与主线笔记的对账

每一条都可用 `grep -n` 在源文件中校验。

| 主线知识点 | 对账位置 | 本篇对应位置 |
|:--|:--|:--|
| 短程 Møller 算符强极限定义 $\Omega_\pm = \mathrm{s\text{-}lim}\,e^{iHt}e^{-iH_0 t}$ | `T_and_U_operators.zh.md:80` | 长程破坏分析 + 修正定义 $\text{(Mol-C)}$ |
| 渐近条件 $\|e^{-iHt}\Omega_+\phi - e^{-iH_0 t}\phi\|\to 0$ | `S_matrix_and_cross_section.zh.md:129` | Cook 判据失败一节 |
| 自由 $G_0^{(+)}$ 出射球面波远场 $e^{ikR}/R$ | `Green_operator.zh.md:350` | Coulomb 渐近多了 $-\eta\ln(2kr)$ 对数项 $\text{(F-asy)}$ |
| 散射振幅 $f$ 的远场系数定义 | `S_matrix_and_cross_section.zh.md:280` | $f_C$ 的扭曲入射 + 扭曲出射 $\text{(psi-C)}$ |
| 短程 Born 近似 $f^B = -(m/2\pi)\int e^{-i\mathbf q\cdot\mathbf r}V$ | `S_matrix_and_cross_section.zh.md:506` | Coulomb-distorted Born $\text{(fSR-CB)}$ |
| 分波 Lippmann–Schwinger 方程 $\text{(LS-pw)}$ | `partial_wave_projection.zh.md:340` | $V_C$ 致 $V_l$ 对数发散，方程不成立 |
| 短程 on-shell 相移定义 $\delta_l$、$f_l = e^{i\delta_l}\sin\delta_l/k$ | `partial_wave_projection.zh.md:355` | $\delta_l \to \sigma_l$ 形式不变，但意义改变 $\text{(fC-pw)}$ |
| 长程势备注（缺口） | `S_matrix_and_cross_section.zh.md:540` | 整篇填补 |

## next-step

- 数值 Coulomb 波计算（指向 `examples/11_coulomb_demo`）：用 `scipy.special` 算 $F_l, G_l, \sigma_l$，在 pp 弹性散射 $E_\text{lab} = 1\text{–}10$ MeV 下绘 $|f_C|^2, |f_C+f_{SR}|^2$ 与干涉项；展示 Coulomb-nuclear 干涉极小点。验证 Rutherford 极限与小相移 Born $\text{(delta-CB)}$。
- Coulomb-distorted DWBA 完整形式（研究轨 C）：从 $\text{(fSR-CB)}$ 推广到通道耦合 $\langle \beta | T | \alpha\rangle = \langle \chi_\beta^{(-)}| V_{SR}|\chi_\alpha^{(+)}\rangle$，含 transfer reaction 与 inelastic 通道；与 AGS 框架（`T_and_U_operators.zh.md:454`）的 $V_C$ 处理对接。
- 极化 + Coulomb：把 `polarization_formalism.zh.md:538` 提到的"含 Coulomb 长程势的修正"展开。M 矩阵在 Coulomb-distorted 基下的分解 $M = M_C + M_{SR}$，自旋-轨道耦合下 Coulomb 不影响 spin-flip（因为 $V_C$ 是中心、自旋无关），但 distorted-wave 基会改变 Wolfenstein 振幅的提取流程。
- 重核库仑散射的相对论修正（Mott 散射）：电子-核 elastic 中 Dirac 方程 + Coulomb 给出 $d\sigma_M/d\Omega = (Z\alpha/2 k\sin^2(\theta/2))^2[1 - \beta^2\sin^2(\theta/2)]$；结构上是把 Schrödinger Coulomb 替换为 Dirac Coulomb，$\sigma_l$ 用 Dirac $\Gamma$ 函数组合代替。
- 屏蔽 Coulomb 与重整化：物理的 Coulomb 在原子物理中实际被电子云屏蔽 $V \to e^{-r/a}/r$（短程化），$\eta_\text{eff}(k, a)$ 形式给出有限总截面；屏蔽极限 $a\to\infty$ 重新得到 Rutherford 但途径合法（满足 Cook）。这是 Coulomb 长程势困难的"物理正则化"路径。
- $1/r^2$ 与对数势等其它长程势的 Møller 修正：$1/r^2$ 处于阈值，需要不同的对数指数；van der Waals 类 $1/r^6$ 短程，无修正；$\ln r$ 势（受限色禁闭模型）需要更强的 Dollard 类处方。这些都在 Reed–Simon III、Derezinski–Gérard 中系统展开。
