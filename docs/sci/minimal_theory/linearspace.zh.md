

# 线性空间、对偶空间与量子态



## 目录

1. 线性空间的定义与例子  
2. 对偶空间与配对  
3. 线性算符与对偶映射  
4. 希尔伯特空间与态矢  
5. 直和与张量积的区分  
6. 散射态与束缚态的希尔伯特空间结构  
7. Møller 算符与 S 算符  
8. 三种语言对照：形式化、指标、Dirac 记号

---

## 1. 线性空间（Vector Space）

### 定义

设 $F$ 为数域（通常为 $\mathbb{R}$ 或 $\mathbb{C}$）。  
线性空间（向量空间） $V$ 是带有加法 $+$ 与数乘 $\cdot$ 的集合，满足：

1. $V$ 对加法封闭；  
2. 数乘对加法、数的乘法满足分配律；  
3. 存在零向量和加法逆元；  
4. 单位元 $1\in F$ 满足 $1\cdot v = v$。

简言之：线性空间是可以“相加、缩放”的抽象空间。

### 例子

- $\mathbb{R}^n$：实数 $n$ 维向量。  
- 函数空间 $V=\{f:\mathbb{R}\to\mathbb{C}\}$。  
- 波函数空间 $L^2(\mathbb{R}^3)$（平方可积复函数）。

### 基底与坐标

若有基 $\{e_i\}_{i=1}^n$，则任意 $v\in V$ 可写作
$$
v = v^i e_i.
$$
分量 $v^i$ 为“逆变分量”，上标常用于表示它是向量在该基下的系数（爱因斯坦求和约定）。

---

## 2. 对偶空间（Dual Space）

### 定义

对偶空间 $V^*$ 是所有从 $V$ 到 $F$ 的线性泛函的集合：
$$
V^* = \{\alpha: V\to F \mid \alpha(a v + b w)=a\alpha(v)+b\alpha(w)\}.
$$

### 对偶基

若 $\{e_i\}$ 是 $V$ 的基，则存在唯一对偶基 $\{e^i\}\subset V^*$，满足
$$
e^i(e_j) = \delta^i_j.
$$
于是
$$
\alpha = \alpha_i e^i,\quad v=v^i e_i,\quad
\alpha(v)=\alpha_i v^i.
$$

记号约定：

- 向量分量 $v^i$：上标（反变）。  
- 对偶分量 $\alpha_i$：下标（协变）。

---

## 3. 线性算符与对偶映射

### 定义

线性算符 $A:V\to W$ 满足
$$
A(av+bw)=aA(v)+bA(w).
$$

### 对偶映射（伴随映射）

定义 $A^*:W^*\to V^*$，对任意 $\beta\in W^*$、$v\in V$，
$$
(A^*\beta)(v)=\beta(A v).
$$

### 矩阵形式

若 $A(e_i)=f_a\,A^a{}_{i}$（$ \{f_a\}$ 为 $W$ 基），则
$$
A^*(f^a) = e^i A^a{}_{i}.
$$
即 $A^*$ 的矩阵为 $A$ 的转置（对复数域通常取共轭转置）。

---

## 4. 希尔伯特空间（Hilbert Space）与态矢（State Vector）

### 定义

希尔伯特空间 $\mathcal H$ 是带有内积且完备的线性空间：
$$
\langle\phi|\psi\rangle \in \mathbb C,\qquad
\langle a\phi+b\chi|\psi\rangle = a^*\langle\phi|\psi\rangle + b^*\langle\chi|\psi\rangle.
$$

### Riesz 表示定理

在希尔伯特空间中，每个连续线性泛函 $\alpha$ 对应唯一向量 $|u\rangle$，使得：
$$
\alpha(|\psi\rangle) = \langle u|\psi\rangle.
$$
因此 $\mathcal H \cong \mathcal H^*$。

### 物理诠释

在量子力学中：

- ket $|\psi\rangle\in\mathcal H$：态矢；  
- bra $\langle\psi|\in\mathcal H^*$：其对偶；  
- 内积 $\langle\phi|\psi\rangle$：概率幅；  
- 算符 $A:\mathcal H\to\mathcal H$：物理可观测量的表示。

---

## 5. 直和与张量积

| 操作 | 符号 | 数学定义 | 物理意义 |
| ---: | :---: | :--- | :--- |
| 直和 | $\mathcal H_1\oplus\mathcal H_2$ | 元素为 $(v_1,v_2)$，内积为两个分量内积之和 | 系统只能处于 $\mathcal H_1$ 或 $\mathcal H_2$（如散射态 vs 束缚态） |
| 张量积 | $\mathcal H_1\otimes\mathcal H_2$ | 双线性生成空间 | 两个系统组合成一个复合系统 |

例子：

- 自旋 + 轨道角动量：$\mathcal H = \mathcal H_L \otimes \mathcal H_S$。  
- 散射 + 束缚态：$\mathcal H = \mathcal H_{\mathrm{bound}} \oplus \mathcal H_{\mathrm{scatt}}$。

---

## 6. 散射态与束缚态的希尔伯特空间结构

### 哈密顿量与谱分解

给定 $H = H_0 + V$，其中 $H_0$ 是自由哈密顿量，$V$ 是势或相互作用。谱分解为：
$$
\mathcal H = \mathcal H_{\mathrm{bound}} \oplus \mathcal H_{\mathrm{scatt}}.
$$

- 束缚态（Bound state）：离散本征值 $E_n$，对应归一化本征态 $|\psi_n\rangle\in\mathcal H_{\mathrm{bound}}$，满足 $\langle\psi_n|\psi_m\rangle=\delta_{nm}$。  
- 散射态（Scattering state）：连续谱 $E>0$，形式归一化 $\langle \psi_E | \psi_{E'}\rangle = \delta(E-E')$。

### 渐进自由态（Asymptotic Free States）

在 $t\to\pm\infty$ 极限下，相互作用项 $V$ 的影响消失，系统表现如自由粒子。自由态生成的空间为：
$$
\mathcal H_{\mathrm{free}} = \operatorname{span}\{|\phi_p\rangle : H_0|\phi_p\rangle = E_p|\phi_p\rangle\}.
$$

---

## 7. Møller 算符与 S 算符

### 时间演化算符

$$
U(t,t_0)=e^{-\frac{i}{\hbar}H(t-t_0)}.
$$

### Møller 算符（Wave Operators）

$$
\Omega_\pm = \lim_{t\to\mp\infty} e^{iH_0 t} e^{-iHt},
$$

其中 $\Omega_\pm:\mathcal H_{\mathrm{free}}\to\mathcal H_{\mathrm{int}}$，将自由态映射为“渐进相互作用态”。

### S 算符（Scattering Operator）

$$
S = \Omega_+^\dagger \Omega_-.
$$

作用在自由空间上：
$$
|\psi_{\mathrm{out}}\rangle = S |\psi_{\mathrm{in}}\rangle.
$$

因此 $\mathcal H_{\mathrm{int}} \cong \mathcal H_{\mathrm{free}}$，同构映射由 $\Omega_\pm$ 给出。

---

## 8. 三种语言对照表

| 概念 | 形式化定义 | 指标形式 | Dirac 记号 |
| --- | --- | --- | --- |
| 向量 | $v=v^i e_i$ | $(v^i)$ | $\| v \rangle$ |
| 对偶向量 | $\alpha=\alpha_i e^i$ | $(\alpha_i)$ \| $\langle\alpha|$ |
| 配对 | $\alpha(v)=\alpha_i v^i$ | $\alpha_i v^i$ | $\langle\alpha\|v\rangle$ |
| 算符 | $A(e_i)=A^j{}_{i} e_j$ | $(A^j{}_{i})$ | $A\|\psi\rangle$ |
| 伴随算符 | $\langle Av,w\rangle=\langle v,A^\dagger w\rangle$ | $A^{\dagger i}{}_{j}=(A^j{}_{i})^*$ | $\langle v\|A^\dagger\|w\rangle$ |
| 张量积 | $v_1\otimes v_2$ | $v_1^i v_2^j$ | $\|v_1\rangle\otimes\|v_2\rangle$ |
| 直和 | $(v_1,v_2)$ | $(v_1^i,v_2^j)$ | $\|v_1\rangle\oplus\|v_2\rangle$ |
| 自由态 | $H_0$ 本征态 | $\phi_p$ | $\|\phi_p\rangle$（例如波函数 $\psi_p(x)=e^{ipx}$） |
| 相互作用态 | $H$ 本征态 | $\psi$ | $\|\psi\rangle$（波包或束缚波） |
| 渐进关系 | $\psi_{\mathrm{in/out}}=\Omega_{\mp}\phi$ | — | $\psi(x,t\to\pm\infty)\sim e^{ipx}+\dots$ |

---

## 小结

- 线性空间：抽象的“可叠加”的集合。  
- 对偶空间：作用在向量上的线性泛函。  
- 算符：向量空间上的线性映射。  
- 希尔伯特空间：具有内积与完备性的线性空间，是物理态空间。  
- 直和：表示系统状态空间的分块。  
- 张量积：表示复合系统。  
- 散射理论：$\mathcal H_{\mathrm{int}}$ 与 $\mathcal H_{\mathrm{free}}$ 通过 Møller 算符同构，S 算符描述输入输出映射。
