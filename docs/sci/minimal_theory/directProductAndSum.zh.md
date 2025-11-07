# 直积 / 直和 / 张量积 辨析

简述：在数学与物理文献中，“直积”（Direct Product）、“直和”（Direct Sum）与“张量积”（Tensor Product）常被混用。最可靠的区分方法是看它们对维度的处理：是“相加”还是“相乘”。

来源链接：

https://www.changhai.org/forum/collection_article_load.php?aid=1186358149


直积有时候称为“完全直积”，以区别于“离散直积”（就是直和）。


另外还有个叫做笛卡尔积的，这是对集合的操作。 集合上是不是线性空间，有没有算符都无所谓。

## 问题核心
“直积”一词在不同上下文中含义模糊：有文献把它当作张量积的同义词（常见于某些 QM 教材），也有文献把它表示为集合上的笛卡尔积或因而导致的直和（常见于流形与几何场合）。

## 两类基本操作

1. 维度相加（直和，Direct Sum）
    - 符号：$V\oplus W$
    - 作用：把互斥或不重叠的子空间拼接为一个更大的空间。
    - 维度：$\dim(V\oplus W)=\dim V+\dim W$
    - 物理/示例：
      - Fock 空间：$\mathcal{F}=\mathcal{H}_0\oplus\mathcal{H}_1\oplus\mathcal{H}_2\oplus\cdots$
      - 流形乘积处的切空间为直和（如 $AdS_5\times S^5$ 是 $5+5=10$ 维，而不是 $25$ 维）

2. 维度相乘（张量积，Tensor Product）
    - 符号：$V\otimes W$
    - 作用：构造能同时描述两个系统并可发生纠缠的复合空间。
    - 维度：$\dim(V\otimes W)=\dim V\cdot\dim W$
    - 物理/示例：
      - 复合量子系统：$\mathcal{H}_{\text{total}}=\mathcal{H}_{\text{orb}}\otimes\mathcal{H}_{\text{spin}}$
      - 度规张量的基底由切空间基底的张量积生成：$\partial_\mu\otimes\partial_\nu$（$4\times4=16$ 个基）

## 物理中的命名约定
- 有些 QM 教材把“张量积”称作“直积”——这是命名约定，不改变数学结构。
- 在微分几何、广义相对论与 QFT 中，常严格使用“张量积”与“直和”的区分。

## 如何避免混淆（实用建议）
- 不要只看作者用词，立即检查上下文或计算维度变化：
  - 若结果是维度相加（或矩阵块对角），则为直和 $\oplus$。
  - 若结果是维度相乘（或使用 Kronecker/张量积矩阵形式），则为张量积 $\otimes$。

总结：关注运算对维度的影响比记住术语更可靠：相加→直和， 相乘→张量积。



张量积 ($\otimes$)：用于组合“共存”的、不同的系统 (AND)。

- 对态矢/空间: 组合两个同时存在的物理系统。

    - 例子: 两个粒子的系统 $\mathcal{H} = \mathcal{H}_1 \otimes \mathcal{H}_2$。

    - 例子: 一个粒子的轨道和自旋 $\mathcal{H} = \mathcal{H}_{orb} \otimes \mathcal{H}_{spin}$。总的态矢是 $\sum c_{ij} |\psi_i\rangle_1 \otimes |\phi_j\rangle_2$ 这样的线性组合（可能纠缠）。


- 对算符: 描述如何在一个复合系统上定义算符。

    - 例子: 只作用于第一个粒子的算符 $A$ 写作 $A \otimes \mathbf{1}$。

    - 例子: 描述两个粒子相互作用的哈密顿量，可能包含 $S_z^{(1)} \otimes S_z^{(2)}$ 这样的项。

直和 ($\oplus$)：用于组合“互斥”的、正交的子空间 (OR)。

- 对态矢/空间: 将一个大的希尔伯特空间分解为几个相互正交的子空间。

    - 例子: Fock 空间 $\mathcal{F} = \mathcal{H}_0 \oplus \mathcal{H}_1 \oplus \mathcal{H}_2 \oplus \dots$。一个态矢要么在0粒子空间 $\mathcal{H}_0$，要么在1粒子空间 $\mathcal{H}_1$，要么是它们的叠加。但一个1粒子态和一个2粒子态是天然正交的。

    - 例子: 由于对称性（如宇称），希尔伯特空间分解为偶宇称空间和奇宇称空间 $\mathcal{H} = \mathcal{H}_{even} \oplus \mathcal{H}_{odd}$。

- 对算符: 当一个算符（如哈密顿量 $H$）保持这些子空间不变时（即 $H$ 不会把一个偶宇称态变成奇宇称态），这个算符就是块对角化的。

    - 例子: 这样的 $H$ 可以写作 $H = H_{even} \oplus H_{odd}$。在矩阵形式上，它看起来像：$$  H = \begin{pmatrix}
    H_{even} & 0 \\
    0 & H_{odd}
    \end{pmatrix}$$


| 类型                       | 符号                                  | 意义                            | 常见场景                   |
| ------------------------ | ----------------------------------- | ----------------------------- | ---------------------- |
| **直和 (direct sum)**      | $\mathcal{ H_1} \oplus \mathcal{H_2}$ | 描述“系统只能处于H1或H2之一”的情形（离散可分子空间） | 自旋空间的不同分量、散射态与束缚态的并合空间 |
| **张量积 (tensor product)** | $\mathcal {H_1} \otimes \mathcal{ H_2}$ | 描述“两个系统组成一个复合系统”              | 两粒子系统、角动量耦合、量子纠缠       |



## 在物理中的具体写法


包括三个部分：
（A）形式化（纯线性代数）写法，
（B）指标记号写法，
（C）量子力学中的 braket 记法。
并且我会区分“直和”（direct sum）、“张量积”（tensor product）和“直乘”（direct product／有时也称直积，但在线性空间背景需澄清）三者。再分别用一个量子力学例子和一个广义相对论例子来说明。

---


假设我们所用的域为 $F$（例如 $\mathbb{R}$ 或 $\mathbb{C}$）。

## 1. 向量空间、对偶空间、矢量与对偶矢量

### 1.1 形式化写法

* 设 $V$ 是一个 $F$ 上的向量空间。  
* 定义其对偶空间（dual space）：

    $$
    V^*=\{\,f:V\to F\mid f\ \text{为线性映射}\,\}.
    $$

* 若 $\{e_i\}_{i=1}^n$ 是 $V$ 的基底，则定义对偶基底 $\{e^i\}_{i=1}^n\subset V^*$ 满足

    $$
    e^i(e_j)=\delta^i_j.
    $$

* 任取矢量 $v\in V$，可写为

    $$
    v=v^i e_i,\qquad v^i\in F.
    $$
* 任取对偶矢量 $\alpha\in V^*$，可写为

    $$
    \alpha=\alpha_j e^j,\qquad \alpha_j\in F.
    $$
* 它们的自然配对（evaluation）为

    $$
    \alpha(v)=\alpha_j v^i e^j(e_i)=\alpha_j v^i \delta^j_i=\alpha_i v^i.
    $$

### 1.2 指标写法

* 矢量分量写作 $v^i$（上标，反变）。  
* 对偶矢量分量写作 $\alpha_i$（下标，协变）。  
* 配对写作 $\alpha_i v^i$（重复指标求和）。  
* 基底变换时，矢量分量“反变”：

    $$
    v'^i={M^i}_j v^j,
    $$

    对偶矢量分量“协变”：

    $$
    \alpha'_i=\alpha_j {(M^{-1})^j}_i,
    $$

    其中 $M$ 为基变换矩阵。

### 1.3 braket 记法（量子力学版）

* 在量子力学中我们通常使用希尔伯特空间 $\mathcal H$，态向量写作 $|\psi\rangle\in\mathcal H$。  
* 对偶矢量对应的是 $\langle\phi|\in\mathcal H^*$（狄拉克 bra）。  
* 配对写作 $\langle\phi|\psi\rangle$，这是一个标量。  
* 若 $|\psi\rangle=v^i|e_i\rangle$，则 $\langle\phi|=\overline{\alpha_i}\langle e^i|$，那么

    $$
    \langle\phi|\psi\rangle=\overline{\alpha_i}\,v^i.
    $$

---

## 2. 直和（Direct Sum）、直乘（Direct Product）与张量积（Tensor Product）

这里常见混淆在于“直乘”一词在不同文献里有不同用法。为避免混淆，先说明各自定义。

### 2.1 形式化写法

#### 2.1.1 直和

设 $V_1$ 和 $V_2$ 是 $F$-向量空间。定义

$$
V_1\oplus V_2=\{(v_1,v_2)\mid v_1\in V_1,\ v_2\in V_2\},
$$

其加法与数乘按分量定义：

$$
(v_1,v_2)+(v'_1,v'_2)=(v_1+v'_1,\ v_2+v'_2),\qquad
a\cdot(v_1,v_2)=(a v_1,\ a v_2).
$$
若为有限维，$\dim(V_1\oplus V_2)=\dim V_1+\dim V_2$。

#### 2.1.2 直乘（笛卡尔积/物理语境说明）

“直乘”在不同语境下含义不同。若指集合意义上的笛卡尔积 $V_1\times V_2$，并在其上赋予向量空间结构，它与 $V_1\oplus V_2$ 本质等价（作为向量空间）。但在物理文献中，有时说 “direct product” 实际上意指张量积。为避免歧义，本文中把“直乘”专指笛卡尔积/直和的集合并列结构（非张量耦合）。

#### 2.1.3 张量积

设 $V$ 和 $W$ 是 $F$-向量空间。张量积 $V\otimes W$ 具有泛性质：存在双线性映射

$$
\otimes:V\times W\to V\otimes W,\qquad (v,w)\mapsto v\otimes w,
$$

使得对任意线性空间 $X$ 与任意双线性映射 $b:V\times W\to X$，存在唯一线性映射 $\tilde b:V\otimes W\to X$ 满足

$$
b(v,w)=\tilde b(v\otimes w).
$$

若 $\{v_i\}$ 是 $V$ 的基，$\{w_j\}$ 是 $W$ 的基，则 $\{v_i\otimes w_j\}_{i,j}$ 是 $V\otimes W$ 的基，故（有限维）

$$
\dim(V\otimes W)=\dim V\cdot\dim W.
$$

一般元素可写为有限线性组合 $\sum_{i,j} c_{ij}\, (v_i\otimes w_j)$。

### 2.2 指标写法

设 $\dim V=m,\ \dim W=n$，基分别为 $\{e_i\}_{i=1}^m,\ \{f_j\}_{j=1}^n$。

* 在 $V\oplus W$ 中，一个元素可以写为 $(v^i e_i,\ w^j f_j)$.  
* 在 $V\otimes W$ 中，一个纯张量写为
    $$
    (v^i e_i)\otimes(w^j f_j)=v^i w^j\,(e_i\otimes f_j),
    $$
    更一般的元素为 $\sum_{i,j}T^{ij}\,(e_i\otimes f_j)$.  
* 若引入对偶空间，则类型为 $(r,s)$ 的张量可写为
    $$
    T^{i_1\ldots i_r}{}_{j_1\ldots j_s}\, (e_{i_1}\otimes\cdots\otimes e_{i_r}\otimes e^{j_1}\otimes\cdots\otimes e^{j_s}),

    $$
    其中上标为“矢量方向”（逆变指数），下标为“对偶矢量方向”（协变指数）。

### 2.3 braket 记法（量子力学）

* 若系统 A、B 的希尔伯特空间为 $\mathcal H_A,\mathcal H_B$，合成系统的态空间为 $\mathcal H_A\otimes\mathcal H_B$（不是直和）。  
* 直和通常表示“系统 A 或 系统 B”的选择性合并；张量积表示两个系统“同时”存在并可纠缠。  
* 若 $|\psi_A\rangle\in\mathcal H_A,\ |\phi_B\rangle\in\mathcal H_B$，合态可写为

    $$
    |\psi_A\rangle\otimes|\phi_B\rangle\equiv|\psi_A,\phi_B\rangle.
    $$

* 合态的一般表示为 $\sum_{i,j}c_{ij}\,|e_i\rangle_A\otimes|f_j\rangle_B$，不总能写成单一纯张量（即存在纠缠态）。

### 2.4 直和 vs 张量积 vs “直乘”的关键区别

* 直和 $V_1\oplus V_2$：并列合并，维度相加，元素形如 $(v_1,v_2)$.  
* 笛卡尔积/“直乘” $V_1\times V_2$：集合意义上的有序对；若赋予向量空间结构则等同于直和，但与张量积不同。  
* 张量积 $V\otimes W$：表示两个空间同时参与的耦合结构，维度相乘，元素可为一般线性组合 $\sum_{i,j}T^{ij}(e_i\otimes f_j)$；许多元素不是纯张量 $v\otimes w$，因此可表征纠缠等耦合现象。  
* 公式区别：

    $$
    \dim(V_1\oplus V_2)=\dim V_1+\dim V_2,\qquad
    \dim(V\otimes W)=\dim V\cdot\dim W.
    $$

---

## 3. 举例：量子力学 & 广义相对论

### 3.1 量子力学例子：两个自旋-1/2 粒子系统

* 单粒子状态空间 $\mathcal H_1\cong\mathbb{C}^2$，基为 $\{|+\rangle,|-\rangle\}$.  
* 两粒子系统状态空间为 $\mathcal H=\mathcal H_1\otimes\mathcal H_2\cong\mathbb{C}^4$。若误用直和 $\mathcal H_1\oplus\mathcal H_2$，则表示“一个粒子在系统1 或 系统2”，而非“两个粒子同时存在且可能纠缠”。  
* 未纠缠态：

    $$
    |\Psi\rangle=|+\rangle_1\otimes|-\rangle_2\equiv|+,-\rangle.
    $$
* 纠缠态示例（Bell 态）：

    $$
    |\Phi^+\rangle=\frac{1}{\sqrt2}\big(|+\rangle_1\otimes|+\rangle_2+|-\rangle_1\otimes|-\rangle_2\big),
    $$
    不能分解为單一的 $|v\rangle_1\otimes|w\rangle_2$。  
* 指标记法：若系统1基为 $e_i$，系统2基为 $f_j$，则

    $$
    |\Psi\rangle=v^i w^j\,(e_i\otimes f_j).
    $$

### 3.2 广义相对论例子：应力-能量张量与矢量、对偶矢量

* 在广义相对论中，切空间 $T_p(M)$ 是一个四维实向量空间。矢量写作 $v^a$，对偶矢量写作 $w_b$。  
* “直和”将两个切空间并列 $T_p(M)\oplus T_p(M)$ 在物理上不常用；常见的是张量结构。  
* 应力-能量张量 $T^{ab}$（类型 $(2,0)$）或 ${T^a}_b$（类型 $(1,1)$）属于

    $$
    T^{ab}\in V\otimes V,\qquad {T^a}_b\in V\otimes V^*.
    $$

* 指标表示（示例）：

    $$
    T^{ab}=\rho\,u^a u^b + p\,(g^{ab}+u^a u^b),
    $$

    其中 $u^a$ 为 4-速度，$\rho$ 为密度，$p$ 为压强，$g^{ab}$ 为度规张量。  
* 自然配对（标量）为 $w_b v^b$。虽然 braket 在 GR 中不常用，但形式上可类比为 $\langle w|v\rangle=w_b v^b$。

---

## 4. 总结与提示

1. 矢量与对偶矢量是不同对象，务必区分上标／下标。  
2. 直和（或笛卡尔合并）与张量积本质不同：前者为“或／并列”合并，后者为“同时／耦合”合并，维度与元素形式均不同。  
3. “直乘”一词需看语境：在物理文献中有时指张量积，建议明确使用 $\oplus$ 或 $\otimes$。  
4. 熟练在三种写法间转换：形式化（基与坐标）、指标（$v^i,\ \alpha_j,\ T^{ij}{}_{k\ell}$）、braket（$|\psi\rangle,\ \langle\phi|,\ |\psi,\phi\rangle$）。  
5. 例子表明：量子系统耦合用张量积；广义相对论中的张量多由张量积构成；直和用于状态选择型合并较多。

---



参考链接：
- https://en.wikipedia.org/wiki/Tensor_product "Tensor product"  
- https://cns.gatech.edu/~predrag/courses/PHYS-6124-12/StGoChap10.pdf "Vectors and Tensors (chapter)"  
- https://quantum-abc.de/Tensor_products.pdf "Tensor products (intro)"




### 一、集合论层面：笛卡尔积的定义

设 A, B 是两个集合，则它们的**笛卡尔积**定义为：

$$
A \times B = \{(a,b)\mid a\in A,\; b\in B\}.
$$

它的元素是**有序对 (a,b)**，表示“一个来自 A，一个来自 B”的组合。


性质：

- 是一个 **集合**；
- 没有加法、乘法等代数运算；
- 若 A 有 m 个元素，B 有 n 个元素，则

  $$ |A\times B| = mn; $$

- 常见于“定义函数域”或“关系”的场景，例如 \(f: A\times B\to C\)。



例子：

$$\mathbb{R} \times \mathbb{R} = \{(x,y)\mid x,y\in\mathbb{R}\} = \mathbb{R}^2.$$

这是一个平面上的点集（但此时还**只是集合**，尚未有向量结构）。



### 二、代数结构层面：直积（direct product）

当 A、B 各自拥有**代数结构**（如群、环、线性空间）时，我们可以在它们的笛卡尔积上**定义代数运算**。  
这样得到的结构叫作**直积**。

 群的直积

设 \((G_1,\cdot)\) 和 \((G_2,\cdot)\) 是群，则它们的**直积群**定义为：

$$
G_1 \times G_2 = \{(g_1,g_2)\mid g_i\in G_i\},
$$

配上分量定义的群运算：

$$
(g_1,g_2)\cdot(h_1,h_2) = (g_1 h_1,\; g_2 h_2).
$$

 性质：

- 单位元为 \((e_1,e_2)\)；
- 逆元为 \((g_1^{-1}, g_2^{-1})\)。

### 2️ 向量空间的直积（或直和）

设 \(V, W\) 是定义在同一域 \(\mathbb{F}\) 上的向量空间。定义：

$$
V \times W = \{(v,w)\mid v\in V,\; w\in W\},
$$

并规定：

$$
(v_1,w_1) + (v_2,w_2) = (v_1+v_2,\; w_1+w_2),\qquad
a(v,w) = (av,\; aw).
$$

于是 \(V\times W\) 成为一个**新的向量空间**。有时也记作 \(V\oplus W\)，若维度有限时两者等价（即同构）。


### 张量积

虽然 \(V\times W\) 是一个线性空间，但它的线性结构是：
$$
c\,(v,w) = (cv, cw),
$$
这意味着两个分量受到**同一个标量**作用。

而双线性需要的是：一个标量作用在 $v$，另一个标量作用在 $w$，并且二者乘积 $ab$ 出现在结果中。

具体对比：

| 性质   | 直积的标量作用               | 双线性的标量作用 |
|--------|-----------------------------|------------------|
| 描述   | $c(v,w)=(cv,\,cw)$      | $B(av,bw)=ab\,B(v,w)$ |
| 要求   | 单一标量同时作用两分量       | 两个标量各自作用并相乘 |

因此：

 
在 $V \times W$的结构中，标量只出现**一次**，  
而在双线性结构中，标量出现**两次（相乘）**。

这就是为什么“直积”不能表示双线性结构。

张量积如何修正这个问题
--------------------

张量积 \(V\otimes W\) 是通过“强制”实现双线性关系而得的空间。我们定义等价关系：

$$
( a v_1 + b v_2, w ) \sim a(v_1,w) + b(v_2,w),
$$

$$
( v, a w_1 + b w_2 ) \sim a(v,w_1) + b(v,w_2).
$$

这一步把直积空间“线性化”到双线性世界。

于是：

$$
(v,w) \mapsto v\otimes w
$$

就是**把单一标量线性**扩展为**双标量线性**的过程。


张量积 实现双线性结构的方法。

为什么要用张量积？ 

因为我们希望研究双线性映射$B: V\times W\to X$ .  

    一个双线性映射是由两个向量空间上的元素，生成第三个向量空间上一个元素之函数，并且该函数对每个参数都是线性的

所以实现了一个新的线性空间 $v \otimes w$，使得这个空间 $v \otimes w$ 存在到X的线性映射。

比较数学化的语言：

张量积 $V\otimes W$ 是一个向量空间，配有一个双线性映射：

$$\otimes: V\times W \to V\otimes W,\quad (v,w)\mapsto v\otimes w,$$

满足以下 **“泛性质” (universal property)**：

> 对任意向量空间 $X$ 和任意双线性映射 $B: V\times W\to X$，  
> 存在唯一的线性映射 $\tilde{B}: V\otimes W \to X$，使得
>
> $$
> B(v,w) = \tilde{B}(v\otimes w)\quad \forall v,w.
> $$

这一性质使得我们可以把双线性映射「线性化」。


 构造方法（从直积到商空间）

- 从直积空间出发

    我们从自由向量空间 $F(V\times W)$ 开始，即以 $V\times W$ 为基的所有有限线性组合：

    $$\sum_i a_i (v_i, w_i).$$

- 加上线性关系（生成等价关系）

    为了让 $(v,w)\mapsto v\otimes w$ 成为**双线性映射**，我们必须在这个自由空间中“强制”以下等式成立：

    $$
    \begin{aligned}
    (v_1+v_2, w) &\sim (v_1,w) + (v_2,w),\\
    (v, w_1+w_2) &\sim (v,w_1) + (v,w_2),\\
    (a v, w) &\sim a(v,w),\\
    (v, b w) &\sim b(v,w).
    \end{aligned}
    $$

- 取商空间

    定义：

    $$V\otimes W = F(V\times W) / R,$$

    其中 $R$ 是由上述所有关系生成的子空间。

    在这个商空间中，我们记等价类为 $v\otimes w = [(v,w)]$。


    (物理的群论里常见错误， 讲述群的直积的时候就和张量积的符号混用， 在群表示论的时候，默认选取了矩阵的Kronecker product， 却没有意识到这是一个很强的条件。 导致学物理的一直以为群的直积就是张量积.  其实直和才和群的直积几乎是一个概念，没有加入另外的条件只需要保群的乘法。  而张量积有双线性的要求)