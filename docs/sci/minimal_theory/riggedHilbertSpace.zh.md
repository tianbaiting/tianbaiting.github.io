---
title: 装备希尔伯特空间与 Dirac 形式的严格化
tags:
    - 数学
    - 物理
    - 泛函分析
    - 量子力学
    - 装备希尔伯特空间
    - rigged Hilbert space
    - Gelfand triplet
    - 分布
---

# 装备希尔伯特空间与 Dirac 形式的严格化

Dirac 的 bra-ket 形式简洁优雅， 可它在希尔伯特空间 $\mathcal H$ 内并不自洽：连续谱的本征矢 $|p\rangle, |x\rangle$ 不是 $L^2$ 的元素， $\delta(x-x')$ 也不是真正的函数。 把 $\mathcal H$ 与分布理论合体， 得到的"装备希尔伯特空间" (rigged Hilbert space, RHS； 又名 Gelfand triplet) 才是 Dirac 形式的真正舞台。

本文沿用 de la Madrid 2005 (*Eur. J. Phys.* 26 287) 的一维矩形势垒例子， 把 RHS 的三个空间一一构造出来， 并解释每一个空间的物理含义。

参考资料： Ballentine, *Quantum Mechanics* (1990)； Bohm, Gadella, *Dirac Kets, Gamow Vectors and Gelfand Triplets* (1989)； 以及上述 de la Madrid 综述。

## 为什么希尔伯特空间不够

### 无界算符的定义域问题

位置算符 $Q f(x) = x f(x)$ 在 $L^2(\mathbb R)$ 上不处处有定义：
\[
\mathcal D(Q) = \{ f\in L^2 \mid x f \in L^2\} \subsetneq L^2.
\]
而 $g(x)=1/(x+\mathrm i)\in L^2$ 但 $Qg\notin L^2$，所以 $Q$ 是无界算符。 进一步， $Q^2$ 的定义域比 $\mathcal D(Q)$ 还小， $\mathcal D(Q)$ 不在 $Q$ 的作用下保持不变 ($Q\mathcal D(Q)\not\subset \mathcal D(Q)$)。

后果： 期望值 $(\varphi, Q\varphi)$、 不确定度 $\Delta_\varphi Q$、 对易关系 $[Q,P]=\mathrm i\hbar I$， 在 $L^2$ 上没有处处良定义。

### 连续谱本征矢不在 $L^2$ 中

$P$ 的本征方程 $-\mathrm i\hbar\, \mathrm d/\mathrm dx\,\langle x|p\rangle = p\,\langle x|p\rangle$ 给出平面波 $\langle x|p\rangle = \mathrm e^{\mathrm i p x/\hbar}/\sqrt{2\pi\hbar}$， 它不平方可积。 类似地 $\langle x|x'\rangle = \delta(x-x')$ 根本不是函数。 Dirac 形式中的"完备性"
\[
I = \int\mathrm dp\,|p\rangle\langle p|,\qquad \langle p|p'\rangle = \delta(p-p')
\]
在 $\mathcal H$ 内毫无意义。

### 思路： 一缩一放

要补救， 一方面要把 $\mathcal H$ 缩小到一个对所有 $Q,P,H$ 的任意次幂都不变的子空间 $\Phi$， 那里期望值、 不确定度、 对易关系都良定义； 另一方面要把 $\mathcal H$ 放大到包含本征 bra 和 ket 的更大空间 $\Phi^\times, \Phi'$。 这就是装备：
\[
\Phi \subset \mathcal H \subset \Phi^\times,\qquad \Phi \subset \mathcal H \subset \Phi'.
\]

## Gelfand 三元组

$\Phi$ 是 $\mathcal H$ 的稠密子空间， 其上有比 $\mathcal H$ 内积范数更强的拓扑 $\tau_\Phi$；

- $\Phi^\times$ ：$\Phi$ 上 $\tau_\Phi$-连续<strong>反线性</strong>泛函的空间， 称为 antidual， 装着 ket $|a\rangle$；
- $\Phi'$ ：$\Phi$ 上 $\tau_\Phi$-连续<strong>线性</strong>泛函的空间， 称为对偶 dual， 装着 bra $\langle a|$。

| 空间 | 物理意义 | 数学意义 |
| --- | --- | --- |
| $\Phi$ | 物理可制备的波函数 $\varphi$ | 测试函数空间 |
| $\mathcal H$ | 概率振幅的承载空间 | 希尔伯特空间 |
| $\Phi^\times$ | ket $|a\rangle$ 所在 | antidual， 反线性泛函 |
| $\Phi'$ | bra $\langle a|$ 所在 | dual， 线性泛函 |

记号 $\langle\varphi|F\rangle\equiv F(\varphi)$ 把分布作用在测试函数上的过程改写成内积外形， 这正是 Dirac 形式的源头。

## 例子： 一维矩形势垒

考虑一维无自旋粒子， 哈密顿量
\[
H = -\frac{\hbar^2}{2m}\frac{\mathrm d^2}{\mathrm dx^2} + V(x),\qquad
V(x) = \begin{cases} 0, & x<a\;\text{或}\;x>b \\ V_0, & a<x<b \end{cases}.
\]
谱 $\mathrm{Sp}(Q)=\mathrm{Sp}(P)=\mathbb R$， $\mathrm{Sp}(H)=[0,\infty)$， 全为连续谱， 无束缚态。 这是检验 RHS 的最干净场景。

### 构造测试函数空间 $\Phi$

要让 $Q,P,H$ 的任意多项式作用在 $\varphi$ 上仍是 $L^2$， 并且 $H$ 在势垒边界 $a,b$ 仍可反复求导， $\Phi$ 必须满足：

- 无穷次可微；
- 在 $x=a, b$ 各阶导数为零 (势的间断点)；
- $P^n Q^m H^l \varphi \in L^2$ 对一切 $n,m,l\geq 0$。

正式记
\[
\Phi \equiv \mathcal S(\mathbb R - \{a,b\})
= \{\varphi\in L^2\mid \varphi\in C^\infty(\mathbb R),\ \varphi^{(n)}(a)=\varphi^{(n)}(b)=0,\ \|\varphi\|_{n,m,l}<\infty\}
\]
其中范数族
\[
\|\varphi\|_{n,m,l} = \sqrt{\int|P^n Q^m H^l \varphi(x)|^2\,\mathrm dx},\qquad n,m,l=0,1,\dots
\]
诱导拓扑 $\tau_\Phi$。 $\Phi$ 几乎就是 Schwartz 空间 $\mathcal S(\mathbb R)$， 只多两个边界条件。 可以验证 $A\Phi\subset\Phi$ 对 $A=Q,P,H$ 都成立： 这就是不变性。

### 构造 ket 空间 $\Phi^\times$

给定本征函数 $f(x)$ (例如平面波 $\mathrm e^{\mathrm ipx/\hbar}/\sqrt{2\pi\hbar}$)， 用积分核生成<strong>反线性</strong>泛函
\[
F(\varphi) = \int\overline{\varphi(x)}\,f(x)\,\mathrm dx.
\]
Dirac 写法
\[
\langle\varphi|F\rangle = \int\mathrm dx\,\langle\varphi|x\rangle\langle x|F\rangle.
\]
按此模板， 三组本征 ket 依次定义：

- 动量 ket：
  \[
  \langle\varphi|p\rangle \equiv \int\mathrm dx\,\overline{\varphi(x)}\,\frac{1}{\sqrt{2\pi\hbar}}\,\mathrm e^{\mathrm ipx/\hbar}.
  \]
- 位置 ket：
  \[
  \langle\varphi|x\rangle \equiv \int\mathrm dx'\,\overline{\varphi(x')}\,\delta(x-x') = \overline{\varphi(x)}.
  \]
- 能量 ket $|E^\pm\rangle_{\mathrm l,r}$ ：以 $\langle x|E^\pm\rangle_{\mathrm l,r}$ 为核， 这些核是带边界条件的 Sturm-Liouville 本征函数 (透射/反射波)。 上标 $\pm$ 区分正向/反向时序， 下标 l/r 区分粒子从左/右入射。

每一个都属于 $\mathcal S^\times(\mathbb R-\{a,b\})$。

### 算符在 $\Phi^\times$ 上的延拓

希尔伯特空间内 $A$ 自伴等价于 $(f, Ag)=(Af, g)$。 把它推广到 ket：
\[
\langle\varphi|A|F\rangle \equiv \langle A\varphi|F\rangle,\qquad \forall\varphi\in\Phi.
\]
"$|F\rangle$ 是 $A$ 的本征 ket， 本征值 $a$" 严格地表述为
\[
\langle\varphi|A|a\rangle = \langle A\varphi|a\rangle = a\langle\varphi|a\rangle,\qquad \forall\varphi\in\Phi.
\]
省略左侧 $\varphi$ 即得熟悉的 Dirac 写法 $A|a\rangle = a|a\rangle$。 由此可证
\[
P|p\rangle = p|p\rangle,\quad Q|x\rangle = x|x\rangle,\quad H|E^\pm\rangle_{\mathrm l,r} = E|E^\pm\rangle_{\mathrm l,r}.
\]

### 构造 bra 空间 $\Phi'$

把核改成"先复共轭再积分"， 得到<strong>线性</strong>泛函：
\[
\tilde F(\varphi) = \int\varphi(x)\,\overline{f(x)}\,\mathrm dx,\qquad
\langle F|\varphi\rangle = \int\mathrm dx\,\langle F|x\rangle\,\langle x|\varphi\rangle.
\]
于是
\[
\langle p|\varphi\rangle = \int\mathrm dx\,\varphi(x)\,\frac{1}{\sqrt{2\pi\hbar}}\,\mathrm e^{-\mathrm ipx/\hbar}
=\overline{\langle\varphi|p\rangle},
\]
\[
\langle x|\varphi\rangle = \varphi(x),\qquad \langle x|x'\rangle = \delta(x-x').
\]
bra 在算符左侧的延拓
\[
\langle F|A|\varphi\rangle \equiv \langle F|A\varphi\rangle
\]
给出 $\langle p|P = p\langle p|$， $\langle x|Q = x\langle x|$， $_{\mathrm{l,r}}\langle{}^{\pm}E|H = E\;_{\mathrm{l,r}}\langle{}^{\pm}E|$。

bra 与 ket 一一对应， $\langle p|\in\Phi'$， $|p\rangle\in\Phi^\times$。

## Dirac 基展开

完备性
\[
\int\mathrm dp\,|p\rangle\langle p| = I,\qquad \int\mathrm dx\,|x\rangle\langle x| = I,
\]
\[
\int_0^\infty\mathrm dE\,|E^\pm\rangle_{\mathrm l\,\mathrm l}\langle{}^\pm E| + \int_0^\infty\mathrm dE\,|E^\pm\rangle_{\mathrm r\,\mathrm r}\langle{}^\pm E| = I
\]
都是<strong>形式</strong>等式， 必须夹在 $\varphi,\psi\in\Phi$ 之间才有意义：
\[
\langle x|\varphi\rangle = \int\mathrm dp\,\langle x|p\rangle\langle p|\varphi\rangle
\quad(\text{即 Fourier 反演}),
\]
\[
\langle x|\varphi\rangle = \int_0^\infty\mathrm dE\,\langle x|E^\pm\rangle_{\mathrm l\,\mathrm l}\langle{}^\pm E|\varphi\rangle
+ \int_0^\infty\mathrm dE\,\langle x|E^\pm\rangle_{\mathrm r\,\mathrm r}\langle{}^\pm E|\varphi\rangle.
\]
这些等式只对 $\varphi\in\Phi$ 严格成立， 对一般 $L^2$ 元素只能取极限。

类似地， 算符的"矩阵元"
\[
\langle x|Q|x'\rangle = x'\delta(x-x'),\quad
\langle x|P|x'\rangle = -\mathrm i\hbar\,\frac{\mathrm d}{\mathrm dx}\delta(x-x'),
\]
\[
\langle x|H|x'\rangle = \left(-\frac{\hbar^2}{2m}\frac{\mathrm d^2}{\mathrm dx^2}+V(x)\right)\delta(x-x')
\]
都是分布意义下的等式， 是有限维基底中 $A_{ij}=\langle a_i|A|a_j\rangle = a_i\delta_{ij}$ 的连续推广。

## $\delta$ 归一化的真意

\[
\langle p|p'\rangle = \delta(p-p'),\qquad \langle x|x'\rangle = \delta(x-x')
\]
本身是形式记号， 真正的内容是
\[
\int\mathrm dp\,\varphi(p)\langle p'|p\rangle = \varphi(p')
\]
对一切 $\varphi\in\Phi$ 成立： 即 $\langle p'|p\rangle$ 是分布 $\delta(p-p')$。

\[
\frac{1}{2\pi\hbar}\int\mathrm dx\,\mathrm e^{\mathrm i(p-p')x/\hbar} = \delta(p-p')
\]
也只是这套 sandwich 解释的一例。

## 物理读法： bra/ket 是概率振幅的核

连续谱本征矢不可归一化， 几率诠释要换一种说法。 离散谱的 $f_n(x)=\langle x|a_n\rangle$ 平方可积， 直接是几率振幅； 连续谱的 $f_a(x)=\langle x|a\rangle$ 是几率振幅的"积分核"：
\[
\langle\varphi|a\rangle = \int\mathrm dx\,\langle\varphi|x\rangle\langle x|a\rangle.
\]
$\varphi$ 才是物理上可制备的波包。 当 $\varphi(p)$ 在 $p_0$ 处尖峰时， 其 $\varphi(x)\sim\mathrm e^{\mathrm ip_0x/\hbar}/\sqrt{2\pi\hbar}$ 才是有效近似。

平面波之于光波包， 正如 $|p\rangle$ 之于 $\varphi$： 单频不可制备， 却是分解物理脉冲的好工具。 这就是 Dirac 形式的 Fourier 隐喻。

## $|E^+\rangle$ 与 $|E^-\rangle$ 的差别， 以及谱测度

希尔伯特空间的谱定理给出 $A=\int a\,\mathrm dE_a$， 对应分解
\[
\mathrm dE_p = |p\rangle\langle p|\,\mathrm dp,\quad
\mathrm dE_x = |x\rangle\langle x|\,\mathrm dx,
\]
\[
\mathrm dE_E = |E^\pm\rangle_{\mathrm l\,\mathrm l}\langle{}^\pm E|\,\mathrm dE
+ |E^\pm\rangle_{\mathrm r\,\mathrm r}\langle{}^\pm E|\,\mathrm dE.
\]
$\mathrm dE_a$ 在 $\mathcal H$ 内是唯一的， 但其分解并不唯一： $|E^+\rangle$ 对应入射初条件 (出射波在 $\pm\infty$)， $|E^-\rangle$ 对应出射末条件 (入射波在 $\pm\infty$)。 希尔伯特空间的谱测度看不出二者差别， RHS 看得出。 在散射理论里这就是 in/out 基的来源。

## 结语

- 装备 (equipped) 比"延拓 extension"或"诠释 interpretation"更准。 RHS 不是替代希尔伯特空间， 而是把它和分布理论装在一起。
- 一缩 ($\Phi$) 一放 ($\Phi^\times,\Phi'$)， 缩出可以良定义算符代数和期望值的子空间， 放出可以容纳 bra/ket 的对偶空间。
- Dirac 公式始终带一个隐藏的"夹在 $\varphi\in\Phi$ 中间"。 一旦补回这层 sandwich， 所有形式操作都是合法的。
- 本文只讲了纯连续谱的最简例子。 含束缚态、 共振态、 多体或非循环可观测量的 RHS 构造更难， 但思路一致： 找一个对相关算符代数封闭的核测试函数空间。
