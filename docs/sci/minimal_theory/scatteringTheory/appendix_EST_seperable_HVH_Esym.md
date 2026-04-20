# Woods-Saxon 光学势的 EST Separable 化及其与对称能的联系

> 本文整理两部分内容：
> 1. 从 Woods-Saxon 光学势出发，通过 Ernst-Shakin-Thaler（EST）展开匹配 separable 势参数 $(\lambda, \beta)$ 的完整推导；
> 2. Isoscalar/Isovector 势的 Lane 分解、HVH 定理，以及 EST 构造如何透明地揭示对称能 $E_{\rm sym}$ 的双成分结构。

---

## 第一部分：EST Separable 化推导

### 1. Woods-Saxon 光学势的定义

核散射中的光学势描述入射核子与靶核的有效相互作用，同时具有实部（弹性散射）和虚部（吸收/非弹性道）：

$$
U(r) = -V_0\, f(r) - i\,W_0\, f_I(r)
$$

其中 Woods-Saxon 形状因子为：

$$
f(r) = \frac{1}{1 + \exp\!\left(\frac{r - R}{a}\right)}, \qquad R = r_0 A^{1/3}
$$

| 参数 | 含义 |
|------|------|
| $V_0$ | 实部阱深（约 40–60 MeV） |
| $W_0$ | 虚部阱深（吸收强度） |
| $R$ | 核半径，$r_0 \approx 1.25$ fm |
| $a$ | 扩散参数（约 0.65 fm） |
| $A$ | 靶核质量数 |

由于 $U(r)$ 为复数局域势，导出的相移 $\delta_l$ 也是复数：$\delta_l = \delta_l^R + i\,\delta_l^I$，S 矩阵元 $S_l = e^{2i\delta_l}$ 满足 $|S_l| \leq 1$（吸收）。

---

### 2. 相移的计算

#### 2.1 分波展开与径向 Schrödinger 方程

将全散射振幅按分波 $l$ 展开，每个分波满足径向方程（令 $\hbar=1,\, 2\mu=1$）：

$$
\left[-\frac{d^2}{dr^2} + \frac{l(l+1)}{r^2} + 2\mu\, U(r) - k^2\right] u_l(r;k) = 0
$$

其中 $k^2 = 2\mu E/\hbar^2$，边界条件：$u_l(0) = 0$。

#### 2.2 渐近匹配提取相移

在 $r \to \infty$（势消失区域），解渐近为：

$$
u_l(r;k) \xrightarrow{r\to\infty} A_l\left[h_l^{(-)}(kr) - S_l\,h_l^{(+)}(kr)\right]
$$

其中 $h_l^{(\pm)}$ 为第一/二类 Hankel 球函数，$S_l = e^{2i\delta_l}$ 为 S 矩阵。等价地：

$$
u_l(r;k) \sim \cos\delta_l \cdot j_l(kr) - \sin\delta_l \cdot n_l(kr) \quad (r\to\infty)
$$

#### 2.3 在壳 T 矩阵与相移的精确关系

在若干支撑能量 $\{E_1, E_2, \ldots, E_N\}$ 处数值积分（Numerov 法或 Runge-Kutta），于 $r_{\max}$ 处作渐近匹配，得复相移 $\delta_l(E_n)$，进而给出在壳 T 矩阵元：

$$
t_l(k_n) \equiv T_l(k_n, k_n; E_n) = -\frac{\hbar^2}{\pi\mu}\frac{e^{i\delta_l(k_n)}\sin\delta_l(k_n)}{k_n}
$$

---

### 3. T 矩阵理论

#### 3.1 Lippmann-Schwinger 方程

$$
T(z) = V + V\,G_0(z)\,T(z), \qquad G_0(z) = (z - H_0)^{-1}
$$

#### 3.2 分波 T 矩阵的动量空间表示

$$
T_l(p,p';z) = V_l(p,p') + \int_0^\infty \frac{q^2\,dq}{2\pi^2} \frac{V_l(p,q)\,T_l(q,p';z)}{z - q^2/2\mu}
$$

在壳条件：$p = p' = k,\; z = E = k^2/2\mu + i\varepsilon$。

对于复光学势，$\delta_l$ 是复数，T 矩阵元也是复数，匹配时需同时处理实部和虚部。

---

### 4. Separable 势及其解析 T 矩阵

#### 4.1 秩-N Separable 势

Separable 势在动量空间可分离，秩-$N$ 形式为：

$$
V_l^{\rm sep}(p,p') = \sum_{i,j=1}^N g_i(p)\,\lambda_{ij}\, g_j(p')
$$

#### 4.2 T 矩阵的精确闭合解析形式

将 $V^{\rm sep}$ 代入 Lippmann-Schwinger 方程，精确求解得：

$$
T_l^{\rm sep}(p,p';z) = \sum_{i,j=1}^N g_i(p)\,\left[D(z)^{-1}\right]_{ij}\, g_j(p')
$$

其中矩阵 $D(z)$ 定义为：

$$
D_{ij}(z) = \lambda_{ij}^{-1} - \tau_{ij}(z), \qquad \tau_{ij}(z) = \frac{2}{\pi}\int_0^\infty \frac{q^2\,dq\;g_i(q)g_j(q)}{z - q^2/2\mu}
$$

这是 Separable 势的最大优势：T 矩阵有解析形式，无需再求解积分方程，在多体理论（Faddeev 等）中极为关键。

---

### 5. EST 展开原理

#### 5.1 核心思想（Ernst-Shakin-Thaler 1973）

选取 $N$ 个支撑能量 $\{E_1,\ldots,E_N\}$，要求 separable 势的 T 矩阵在这些点上在壳精确再现原势的 T 矩阵。

#### 5.2 形状因子的 EST 最优选择

EST 的关键：选取形状因子为原势在支撑能量处的精确散射波函数：

$$
|g_n\rangle = T(E_n)|k_n\rangle \quad \Leftrightarrow \quad g_n(r) = u_l(r;k_n) \ \text{（正则化后）}
$$

在动量空间：

$$
g_n(p) = V_l(p,k_n) + \frac{2}{\pi}\int_0^\infty \frac{q^2\,dq\;V_l(p,q)\,T_l(q,k_n;E_n)}{E_n - q^2/2\mu + i\varepsilon}
$$

#### 5.3 $\lambda$ 矩阵的确定

由在壳匹配条件 $T_l^{\rm sep}(k_m,k_m;E_m) = T_l^{\rm phys}(k_m,k_m;E_m)$，对 $m=1,\ldots,N$，可以证明：

$$
\left[\lambda^{-1}\right]_{mn} = \frac{\delta_{mn}}{t_l^{\rm phys}(k_n)} - \left[\tau(E_n)\right]_{mn} + \left[\tau(E_m)\right]_{mn}^*
$$

---

### 6. 实用方案：高斯形状因子 + 秩-1

最简单的实践做法：取高斯形状因子，秩-1 展开：

$$
g_l(p) = e^{-\beta p^2}, \quad V_l^{\rm sep}(p,p') = \lambda\, e^{-\beta p^2} e^{-\beta p'^2}
$$

#### 6.1 传播子积分 $\tau_l(E)$

$$
\tau_l(E + i\varepsilon) = \frac{2}{\pi}\int_0^\infty \frac{q^2\, e^{-2\beta q^2}}{E + i\varepsilon - q^2/2\mu}\,dq
= \frac{2}{\pi}\,{\rm P}\!\!\int_0^\infty \frac{q^2\, e^{-2\beta q^2}}{E - q^2/2\mu}\,dq - i\mu k\, e^{-2\beta k^2}
$$

主值积分可表示为实解析函数（涉及误差函数 $\mathrm{erfi}$）。

#### 6.2 在壳匹配方程

$$
\frac{\lambda\, e^{-2\beta k_1^2}}{1 - \lambda\,\tau_l(E_1)} = -\frac{\hbar^2}{\pi\mu}\frac{e^{i\delta_l(k_1)}\sin\delta_l(k_1)}{k_1} \equiv t_l^{\rm phys}(k_1)
$$

#### 6.3 求解 $\lambda$（$\beta$ 给定时）

$$
\boxed{\lambda = \frac{t_l^{\rm phys}(k_1)}{e^{-2\beta k_1^2} + t_l^{\rm phys}(k_1)\cdot\tau_l(E_1)}}
$$

这是关于 $\lambda$ 的线性方程，直接求解。$\beta$ 控制形状因子的范围——$\beta$ 越大，$g(p)$ 在高动量处衰减越快，等价于坐标空间的势越软。

#### 6.4 秩-N 推广

取 $N$ 个支撑能量 $\{E_1,\ldots,E_N\}$，形状因子 $g_n(p) = e^{-\beta_n p^2}$，则 $\lambda$ 变为 $N\times N$ 复矩阵，由 $N$ 组匹配方程联立确定。$\beta_n$ 可按能量间隔等比/等差分配，或优化拟合相移曲线。

#### 6.5 完整流程

```
选定 β（范围参数）
    ↓
数值积分 WS 势的径向 Schrödinger 方程
    ↓
渐近匹配 → 复相移 δ_l(E_n) → t_l^phys(k_n)
    ↓
计算传播子积分 τ_l(E_n)（数值或解析）
    ↓
代入匹配方程，线性求解 λ（复数）
    ↓
调节 β 或增加秩 N → 拓宽有效能量范围
```

---

## 第二部分：与对称能的联系（HVH 定理）

### 7. Lane 分解：同位旋标量势与同位旋矢量势

核子在非对称核物质（$\delta = (\rho_n-\rho_p)/\rho \neq 0$）中感受到的光学势，按 Lane（1962）分解为：

$$
U_{n/p}(k,\rho,\delta) = U_0(k,\rho) \pm U_{\rm sym}(k,\rho)\,\delta
$$

式中 $+$ 对中子，$-$ 对质子。

| 分量 | 物理意义 | 与 WS 参数的对应 |
|------|----------|------------------|
| $U_0$（同位旋标量） | 中子和质子相同，控制有效质量 $m^*$ | WS 势的 $V_0, W_0$ |
| $U_{\rm sym}$（同位旋矢量） | 中子/质子符号相反，直接联系对称能 | WS 势的 $V_1, W_1$（同位旋依赖部分） |

在 WS 势框架下，$U_{\rm sym}$ 来自势深对同位旋的线性依赖：$V_0 \to V_0 + V_1\tau_3\delta$。

EST separable 化的关键认识：$U_0$ 和 $U_{\rm sym}$ 各自对应一组独立的 separable 参数，从而将同位旋物理与 separable 势的结构完全分离。

---

### 8. Hugenholtz–Van Hove（HVH）定理

在饱和点 $\rho_0$（满足 $\partial(E/A)/\partial\rho\big|_{\rho_0}=0$），HVH 定理断言：

$$
\varepsilon_q(k_{F,q}) = \mu_q, \quad q = n,\, p
$$

其中准粒子能量 $\varepsilon_q(k) = k^2/2m + U_q(k,\rho,\delta)$，$\mu_q$ 为化学势。

#### 8.1 化学势差与对称能

能量密度按 $\delta$ 展开：$E/A = E_0/A + E_{\rm sym}\delta^2 + O(\delta^4)$，由此：

$$
\mu_n - \mu_p = 4\delta\, E_{\rm sym}(\rho_0) + O(\delta^3)
$$

#### 8.2 费米动量的同位旋劈裂

由 $\rho_{n/p} = k_{F,n/p}^3/3\pi^2$，展开到 $O(\delta)$：

$$
k_{F,n} \approx k_F\!\left(1+\frac{\delta}{3}\right), \qquad k_{F,p} \approx k_F\!\left(1-\frac{\delta}{3}\right)
$$

其中 $k_F=(3\pi^2\rho_0/2)^{1/3}$ 为对称核物质费米动量。

#### 8.3 代入 HVH，展开到 $O(\delta)$

$$
\mu_n-\mu_p = \frac{k_{F,n}^2-k_{F,p}^2}{2m} + U_n(k_{F,n})-U_p(k_{F,p})
$$

$$
\approx \frac{4\delta k_F^2}{6m} + 2U_{\rm sym}(k_F)\delta + \frac{2k_F\delta}{3}\frac{\partial U_0}{\partial k}\bigg|_{k_F}
$$

$$
= 4\delta\left[\frac{k_F^2}{6m} + \frac{U_{\rm sym}(k_F)}{2} + \frac{k_F}{6}\frac{\partial U_0}{\partial k}\bigg|_{k_F}\right]
$$

---

### 9. 对称能的双成分结构

#### 9.1 有效质量吸收第三项

从准粒子速度定义有效质量（E-mass）：

$$
\frac{\hbar^2 k_F}{m^*} \equiv \frac{\partial\varepsilon}{\partial k}\bigg|_{k_F} = \frac{\hbar^2 k_F}{m} + \frac{\partial U_0}{\partial k}\bigg|_{k_F}
$$

因此 $\dfrac{\partial U_0}{\partial k}\big|_{k_F} = \hbar^2 k_F\!\left(\dfrac{1}{m^*}-\dfrac{1}{m}\right)$，代入得：

$$
\frac{k_F^2}{6m} + \frac{k_F}{6}\cdot\hbar^2 k_F\!\left(\frac{1}{m^*}-\frac{1}{m}\right) = \frac{\hbar^2 k_F^2}{6m^*}
$$

#### 9.2 HVH 核心结果

$$
\boxed{E_{\rm sym}(\rho_0) = \underbrace{\frac{\hbar^2 k_F^2}{6m^*}}_{\text{动能项（同位旋标量控制）}} + \underbrace{\frac{U_{\rm sym}(k_F,\rho_0)}{2}}_{\text{势能项（同位旋矢量控制）}}}
$$

- 动能项：受 $m^*$ 调制的费米气体贡献，$m^* < m$ 时大于自由气结果 $k_F^2/6m$，由 $U_0(k)$ 的动量梯度决定。
- 势能项：费米面上的同位旋矢量势，完全由 $U_{\rm sym}(k_F)$ 决定，与动量梯度无关。

自由 Fermi 气（$U=0$, $m^*=m$）：$E_{\rm sym}^{FG}=k_F^2/6m\approx 12\,{\rm MeV}$。实验值约 $30\sim 35\,{\rm MeV}$，势能项贡献约一半至三分之二。

---

### 10. EST 构造的透明性

#### 10.1 Gauss Separable 势在核物质中的解析自能

取各分波 $(\tau,l)$ 的 Gauss 形状因子 $g(k)=e^{-\beta k^2}$，HF 级别自能（以 S 波示意）：

$$
U_0(k,\rho) = \lambda_0\, e^{-\beta_0 k^2} \cdot \rho_0\, I(\beta_0, k_F)
$$

$$
U_{\rm sym}(k,\rho) = \lambda_1\, e^{-\beta_1 k^2} \cdot \rho_0\, I(\beta_1, k_F)
$$

密度积分有精确解析形式（误差函数）：

$$
I(\beta, k_F) = \frac{1}{2\pi^2}\int_0^{k_F} p^2 e^{-\beta p^2}dp = \frac{1}{2\pi^2}\left[\frac{\sqrt{\pi}}{4\beta^{3/2}}{\rm erf}(\sqrt{\beta}k_F) - \frac{k_F}{2\beta}e^{-\beta k_F^2}\right]
$$

#### 10.2 有效质量的解析表达

$$
\frac{\partial U_0}{\partial k}\bigg|_{k_F} = -2\lambda_0\beta_0 k_F e^{-\beta_0 k_F^2}\cdot\rho_0 I(\beta_0,k_F)
$$

$$
\therefore\quad \frac{1}{m^*} = \frac{1}{m} - 2\lambda_0\beta_0 e^{-\beta_0 k_F^2}\rho_0 I(\beta_0,k_F)
$$

#### 10.3 对称能的完全解析形式（EST 结果）

$$
\boxed{E_{\rm sym}(\rho_0) = \frac{\hbar^2 k_F^2}{6}\cdot\frac{1}{\dfrac{1}{m}-2\lambda_0\beta_0 e^{-\beta_0 k_F^2}\rho_0 I_0} + \frac{\lambda_1 e^{-\beta_1 k_F^2}\rho_0 I_1}{2}}
$$

---

### 11. 总结：参数的物理解耦

EST separable 构造将两套参数的物理角色完全分离：

| 参数组 | 控制的物理量 | 对 $E_{\rm sym}$ 的贡献 |
|--------|-------------|------------------------|
| $(\lambda_0, \beta_0)$ | 同位旋标量势 $U_0(k)$，有效质量 $m^*$ | 动能项 $\hbar^2 k_F^2 / 6m^*$ |
| $(\lambda_1, \beta_1)$ | 同位旋矢量势 $U_{\rm sym}(k)$ | 势能项 $U_{\rm sym}(k_F)/2$ |

两组参数解耦：可分别从弹性散射相移匹配（通过 EST 流程），再直接映射到 $E_{\rm sym}$ 的两个物理成分，无需额外数值过程。

这正是 EST 方法在核结构和重离子碰撞研究中被广泛采用的根本原因：它在 NN 散射信息（通过相移 → separable 参数）与核物质性质（$E_{\rm sym}$、$m^*$、压缩系数 $K$）之间建立了完全解析的桥梁，并将中低能核子-核散射与中子星物态方程（由 $E_{\rm sym}(\rho)$ 主导）联系起来。
