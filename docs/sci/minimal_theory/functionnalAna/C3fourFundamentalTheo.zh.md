# 泛函四大基石定理

![alt text](assets/C3fourFundamentalTheo.zh/sida.JPG)

## hahn-banach 定理


设 $X$ 是实线性空间，$p$ 是 $X$ 上的次线性泛函。若 $f$ 是定义在子空间 $Z \subset X$ 上的线性泛函，且满足 $|f(x)| \le p(x)$ , $\forall x \in Z$ ，则在整个空间 $X$ 上存在线性泛函 $F$，使得：

$F|_Z = f$ （延拓性）

$|F(x)| \le p(x)$  $ \forall x \in X$ 成立（保号/保范性）


物理直观： 它保证了对偶空间 $X^*$ 足够大。在量子力学中，这意味着对于任何态向量，我们都能找到足够的观测物理量（线性泛函）来描述它。

## 一致有界原理(Uniform Boundedness Principle / Banach-Steinhaus Theorem) 共鸣定理

def： 设 $X$ 是 Banach 空间，$Y$ 是赋范线性空间。若算子族 $\mathcal{T} \subset \mathcal{B}(X, Y)$ 是逐点有界的，即对于每个 $x \in X$，有 $\sup_{T \in \mathcal{T}} \|Tx\| < \infty$，则该算子族是一致有界的，即：$\sup_{T \in \mathcal{T}} \|T\| < \infty$

保证了在点态下的有界性可以推广到整个空间的有界性。

## 开映像定理

def： 设 $X, Y$ 是 Banach 空间。若 $T: X \to Y$ 是连续线性算子且是满射（Surjective），则 $T$ 是一个开映射（即 $T$ 将 $X$ 中的开集映射为 $Y$ 中的开集）。


保证了线性算子在满射情况下的“良好行为”，即它们不会将开集压缩成非开集。 保证了逆算子的存在性和连续性。

## 闭图像定理

 def:设 $X, Y$ 是 Banach 空间，$T: X \to Y$ 是线性算子。若 $T$ 的图像 $G(T) = \{(x, Tx) : x \in X\}$ 在 $X \times Y$ 中是闭集，则 $T$ 是连续的（有界的）。

保证了线性算子的连续性与其图像闭合性的等价性。这在分析线性算子的性质时非常有用。

## 逼近论的应用

对闭区间套的抽象.

布劳威尔不动点定理的推广.

### banach不动点定理

设 $(X, d)$ 是一个非空的完备度量空间。若映射 $T: X \to X$ 是一个压缩映射，即存在常数 $0 \le k < 1$，使得对于所有 $x, y \in X$：$d(Tx, Ty) \le k \cdot d(x, y)$则 $T$ 在 $X$ 中有且仅有一个不动点 $x^*$（即 $Tx^* = x^*$）。

应用： 这是微分方程和积分方程解的存在唯一性证明的核心，比如在计算散射振幅的 Lippmann-Schwinger 方程 迭代求解时，其本质就是寻找不动点。


### 强收敛弱收敛 弱星收敛


对于赋范空间,

序列$\{x_n\}$ 强收敛到 $x$，如果 $\lim_{n \to \infty} \|x_n - x\| = 0$。

序列$\{x_n\}$ 弱收敛到 $x$，如果对于每个 $f^* \in X^*$，$\lim_{n \to \infty} f^*(x_n) = f^*(x)$。


对于算子序列$\{T_n\}$，

$\forall x \in X$，$\lim_{n \to \infty} \|T_n x - Tx\| = 0$，则称 $\{T_n\}$ 强收敛到 $T$。

 $\forall x \in X$ 和每个 $f^* \in Y^*$，$\lim_{n \to \infty} f^*(T_n x) = f^*(Tx)$，则称 $\{T_n\}$ 弱收敛到 $T$。


对于泛函序列$\{f_n\}$，

$\forall x \in X$，$\lim_{n \to \infty} |f_n(x) - f(x)| = 0$，则称 $\{f_n\}$ 强收敛到 $f$。

$\forall x \in X$，$\lim_{n \to \infty} f_n(x) = f(x)$，则称 $\{f_n\}$ 弱星收敛到 $f$。
