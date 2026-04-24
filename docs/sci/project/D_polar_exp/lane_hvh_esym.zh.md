# Lane 关系、光学势、EST 展开与 HVH 推导对称能

> 本文串联氘核破裂反演对称能的一条上下游链路：
>
> 核子-核光学势（KD 2003） → Lane 能量依赖 → 分波相移（Woods-Saxon + Numerov） → EST 可分展开 → Lane 参数 → HVH 定理 → 对称能 $(S_{\mathrm{sym}},\,L)$。
>
> 参考素材：`D_nuclear_experiment/note/d_breakup/d_breakup.tex`，以及 `dpol/toy_DAbreak/docs/physics/04-06`（Lane observables、光学输入链、HVH 反演）。

## 1. 为什么需要这套链路

在 $(\vec d, pn)$ 破裂反应里，我们想从联合角分布（$d^2\sigma/d\Omega_p d\Omega_n$, $A_y$, $A_{yy}$）反演核物质对称能 $S_{\mathrm{sym}}(\rho)$ 与其斜率 $L$。但直接的观测量只接触到核子-核（NA）通道的复光学势；对称能是**核物质**的体性质。

桥梁分两段：

1. **NA 光学势 → Lane 能量依赖参数 $(V_1^{(0)}, \alpha_V, W_1^{(0)}, \alpha_W)$**：通过 Koning-Delaroche（KD 2003）全局参数化加一组 Lane-ED 四参数描述同位旋不对称项。
2. **Lane 参数 → $(S_{\mathrm{sym}}, L)$**：通过 Hugenholtz-Van Hove（HVH）定理，把费米面处的 Lane 实部值与斜率翻译成饱和密度处的对称能与斜率。

中间还有一道数值关卡：三体 Faddeev/AGS 求解要求**可分势**（分离势），于是引入 **EST（Ernst-Shakin-Thaler）rank-$N$ 展开**把 Woods-Saxon 的全复光学势投影到有限秩的可分形式 $(\lambda, \beta)$，再进入 AGS 的核。

整条流水线可以写成：

```
(V1_0, α_V, W1_0, α_W)
         │
         ▼
   KD 2003 + Lane-ED      —— 第 2、3 节
         │
         ▼
   WS + Numerov 分波相移    —— 第 4 节
         │
         ▼
   EST rank-N 可分势 (λ, β) —— 第 5 节
         │
         ▼
   AGS / Faddeev 三体求解   —— 观测量
         │
         ▼
   HVH 映射 → (S_sym, L)    —— 第 6 节
```

## 2. 核子-核光学势（KD 2003 骨架）

按 `d_breakup.tex` 末节的写法，**中心**光学势的实部 $V_\tau(E)$ 按能量多项式展开并带同位旋依赖：

$$
V_\tau(E,\delta) = V_0(E) + \tau_3\,V_{\mathrm{sym},1}(E)\,\delta + V_{\mathrm{sym},2}(E)\,\delta^2,
$$

其中 $\tau_3 = +1$ 对中子、$-1$ 对质子，$\delta = (N-Z)/A$ 是靶核同位旋不对称度。把等号右边三项分别称为：

- $V_0(E)$：**同位旋标量势**（iso-scalar）；
- $V_{\mathrm{sym},1}(E)$：**一阶对称势**（Lane 势，$\propto \delta$）；
- $V_{\mathrm{sym},2}(E)$：**二阶对称势**（$\propto \delta^2$）。

完整形式还包括虚部体、虚部面、自旋-轨道、库仑项：

$$
V(r,E) = -V_v f_v(r) - i W_v f_v(r) + i 4 a_s W_s \frac{d f_s(r)}{dr}
        + \frac{2\lambda_\pi^{-2}}{\pi}\!\left(V_{so}+i W_{so}\right)\frac{1}{r}\frac{df_{so}(r)}{dr}\,\mathbf{S}\!\cdot\!\mathbf{L}
        + V_C(r).
$$

KD 2003 对体实深的参数化为

$$
V_V(E) = V_1^{(n/p)}\!\left[1 - V_2\,\Delta E + V_3\,\Delta E^2 - V_4\,\Delta E^3\right],\qquad \Delta E = E - E_F,
$$

其中 Fermi 能

$$
E_F^{(n)} = -11.2814 + 0.02646\,A,\qquad
E_F^{(p)} = -8.4075  + 0.01378\,A,
$$

而同位旋依赖进入 $V_1$：

$$
V_1^{(n)} = 59.30 - 21.0\,\delta - 0.024\,A,\qquad
V_1^{(p)} = 59.30 + 21.0\,\delta - 0.024\,A.
$$

**符号相反**是 Lane 项在 KD 原始参数化中的直接体现。虚部体 $W_V(E)$、虚部面 $W_D(E)$、几何 $R_V, a_V, R_D, a_D, R_C$ 都有相应的解析形式（见 `toy_DAbreak` 讲义第 5.2 节的完整列表）。

## 3. Lane 关系

### 3.1 原始 Lane 形式

Lane 原始的等价中子/质子势写法：

$$
U_n = U_0 + 4\,U_1\,\frac{N-Z}{A},\qquad
U_p = U_0 - 4\,U_1\,\frac{N-Z}{A} + V_C,
$$

或紧凑地

$$
U_\tau = U_0 + \tau_3\,U_1\,\delta \quad (\tau_3 = \pm 1).
$$

这把 $(n, p)$ 的光学势差额归结到一个**同位旋矢量**分量 $U_1$。从物理上看，$U_1 > 0$ 时，中子在中子过剩核中比在对称核中感到更深的实势（中子"不想进来"，因为价中子已多），这与对称能表达式一致。

### 3.2 叠加能量依赖：Lane-ED 四参数

KD 2003 已经含一个**能量无关**的 Lane 不对称项（来自 $V_1^{(n/p)}$ 和 $D_1^{(n/p)}$）。在此之上，对称能反演所需的自由度来自对 $U_1$ 的**能量依赖**建模。`toy_DAbreak` 采用最小的四参数线性模型：

$$
V_1(E) = V_1^{(0)} + \alpha_V\,E,\qquad
W_1(E) = W_1^{(0)} + \alpha_W\,E.
$$

这四个参数 $(V_1^{(0)}, \alpha_V, W_1^{(0)}, \alpha_W)$ 就是闭环反演的自由量。

叠加到 WS 深度时，按通道符号：

$$
V_{\mathrm{tot}}(E, \tau) = V_V^{\mathrm{KD}}(E, \tau) + \mathrm{sign}(\tau)\,V_1(E),\qquad
\mathrm{sign}(n) = +1,\;\mathrm{sign}(p) = -1.
$$

于是中子 / 质子的 Lane 差等于

$$
V_n - V_p = 2\,V_1(E) = 2\bigl[V_1^{(0)} + \alpha_V\,E\bigr],
$$

这是 Lane 势在代码层面可观测的直接数值标志。

### 3.3 Lane 参数的物理边界

`toy_DAbreak` 的 `LaneEnergyDepBounds` 把物理合理范围作为 LM 拟合的硬约束：

| 参数 | 范围 | 直觉 |
|---|---|---|
| $V_1^{(0)}$ | $[-5, 20]$ MeV | 零能 Lane 实部 |
| $\alpha_V$  | $[-0.10, 0.05]$ | Lane 实部能斜率 |
| $W_1^{(0)}$ | $[0, 10]$ MeV | 零能 Lane 虚部 |
| $\alpha_W$  | $[-0.02, 0.05]$ | Lane 虚部能斜率 |

## 4. 从 $V(r, E)$ 到分波相移：Numerov

拿到能量依赖的 WS 深度 $V_{\mathrm{tot}}(E)+iW_{\mathrm{tot}}(E)$ 之后，在径向网格上解**径向 Schrödinger**（对每个 $l$，每种电荷，支撑能量集合 $E_i$）：

$$
\!\left[\frac{d^2}{dr^2} + k^2 - \frac{l(l+1)}{r^2} - \frac{2\mu}{(\hbar c)^2}\bigl(V(r) + iW(r) + V_C(r)\bigr)\right]\!u_l(r) = 0.
$$

WS 形状与面形状：

$$
f_{\mathrm{WS}}(r; R, a) = \frac{1}{1 + e^{(r - R)/a}},\qquad
f_{\mathrm{surf}}(r; R, a) = \frac{4\,e^{(r-R)/a}}{\bigl(1 + e^{(r-R)/a}\bigr)^{2}}.
$$

库仑势（均匀带电球，仅质子）：

$$
V_C(r) =
\begin{cases}
\dfrac{Z\alpha\hbar c}{2R_C}\!\left(3 - \dfrac{r^2}{R_C^2}\right), & r < R_C,\\[6pt]
\dfrac{Z\alpha\hbar c}{r}, & r \ge R_C.
\end{cases}
$$

Numerov 从近原点 $u_l(r_0) = r_0^{l+1}$、$u_l(r_1) = r_1^{l+1}$ 出发迭代到 $r_{\mathrm{match}} = r_{\max}$，用球 Bessel 解匹配：

$$
\tan\delta_l = \frac{\beta\,j_l(k r) - k\,j_l'(k r)}{\beta\,y_l(k r) - k\,y_l'(k r)},\qquad
\beta = \frac{u_l'(r_{\mathrm{match}})}{u_l(r_{\mathrm{match}})}.
$$

输出为分波相移 $\delta_l^{(n/p)}(E)$ 和径向波函数 $\psi_l(r; E)$，喂给下一步 EST 展开。

## 5. EST Rank-$N$ 可分势展开

三体 AGS 积分方程对**两体 T-矩阵**要求**可分势**（separable）以保持核紧致、数值可解。Yamaguchi rank-1 形式是最简单的例子：

$$
V_{\mathrm{sep}}(k, k') = \lambda\,g(k)\,g(k'),\qquad g(k) = \frac{1}{k^2 + \beta^2}.
$$

EST（Ernst-Shakin-Thaler）给出一种把**全势** $V(r, E)$ 投影成 rank-$N$ 可分形式的系统程序，核心是选 $N$ 个支撑能量 $E_i$ 与对应的 on-shell 波函数 $\psi_i(r)$。

### 5.1 形状因子（form factor）

对每个 $l$ 和每个支撑能量 $E_i$，

$$
\phi_i^{(l)}(q) = \int_0^\infty dr\,r\,j_l\!\bigl(q r / \hbar c\bigr)\,V(r; E_i)\,\psi_l(r; E_i).
$$

这是**分波 t-matrix 的谱投影**：用 $\psi_l(r; E_i)$ 作为"优先再现"的态，保证 rank-$N$ 投影在支撑能量上严格等价于原始势。

### 5.2 Bateman 矩阵与 $\Lambda$

Bateman 矩阵定义为

$$
B_{ij}^{(\mathrm{LHS})} = \int dr\,\psi_i(r)\,V(r; E_j)\,\psi_j(r),
$$

对称化

$$
B_{ij} = \tfrac{1}{2}\bigl(B_{ij}^{(\mathrm{LHS})} + \overline{B_{ji}^{(\mathrm{RHS})}}\bigr),
$$

耦合强度矩阵

$$
\Lambda = B^{-1}.
$$

于是可分势写成

$$
V_{\mathrm{sep}}^{(l)}(q, q') = \sum_{i,j=1}^{N} \phi_i^{(l)}(q)\,\Lambda_{ij}\,\overline{\phi_j^{(l)}(q')}.
$$

`toy_DAbreak` 固定 $N = \mathrm{rank} = 3$，支撑能量取 $(25, 75, 150)$ MeV，分别覆盖低 / 中 / 高能区。对 $3\times 3$ 直接用 Cramer 展开求逆。

### 5.3 为什么 $N=3$、且支撑能量分散

每一分波 $l$ 的 EST 展开通过"在 $E_i$ 处严格再现"来吸收能量依赖：rank = 3 让 $s, p, d$ 波分别偏重低、中、高能的势形，保证**Lane 能量斜率** $\alpha_V$ 有独立的投影信号——否则四参数 $(V_1^{(0)}, \alpha_V, W_1^{(0)}, \alpha_W)$ 会在单一能量处被压成两个标量（实 + 虚），秩亏，反演不可辨识。

### 5.4 Born 匹配：回到 $(\lambda, \beta)$

为了把 rank-$N$ 结果最终"压"回 AGS 基矩阵实际使用的 rank-1 形式（出于计算代价与相位保留的折衷），做一步 **Born K-matrix 匹配**：

$$
B_l(k) = \int_0^\infty dr\,r^2\,j_l(k r)^2\,V_{\mathrm{WS}}(r).
$$

对两个支撑能量 $E_1, E_2$，假设 rank-1 形式因子 $g_l(k) = 1/(k^2 + \beta^2)$，由比值

$$
\frac{|B(k_1)|}{|B(k_2)|} = \!\left(\frac{k_2^2 + \beta^2}{k_1^2 + \beta^2}\right)^{\!2}
$$

得到 $\beta^2$ 的封闭解：

$$
\sqrt{R} \equiv \sqrt{\frac{|B_1|}{|B_2|}},\qquad
\beta^2 = \frac{k_2^2 - \sqrt{R}\,k_1^2}{\sqrt{R} - 1}.
$$

$\lambda$ 的比值（**复数**，保留相位）：

$$
\frac{\lambda_{pA}}{\lambda_{nA}}
= \frac{B^{(pA)}(k_1)\bigl(p_1^{(pA)\,2} + \beta_{pA}^2\bigr)^{2}}
       {B^{(nA)}(k_1)\bigl(p_1^{(nA)\,2} + \beta_{nA}^2\bigr)^{2}}.
$$

中子通道：$B^{(nA)} = B^{(\mathrm{iso})} + B^{(\mathrm{iv})}$；质子通道：$B^{(pA)} = B^{(\mathrm{iso})} - B^{(\mathrm{iv})}$——与 Lane 符号约定一致。

至此，给定 Lane 四参数，便能唯一确定 NA 通道在 AGS 中使用的 $(\lambda, \beta)$。

## 6. HVH 定义推导对称能

### 6.1 核物质能密度与每核子能

令核子密度 $\rho = \rho_n + \rho_p$，不对称度 $\delta = (\rho_n - \rho_p)/\rho$。

- 能密度 $\xi(\rho, \delta) = \rho\,E(\rho, \delta)$；
- 每核子能 $E(\rho, \delta)$；
- 单粒子势 $U_\tau(\rho, \delta, k)$，中子/质子分别记 $\tau = n, p$。

对称能按 $\delta$ 的 Taylor 展开：

$$
E(\rho, \delta) = E(\rho, 0) + E_{\mathrm{sym},2}(\rho)\,\delta^2 + E_{\mathrm{sym},4}(\rho)\,\delta^4 + \cdots
$$

通常只保留二阶项，$S_{\mathrm{sym}}(\rho) \equiv E_{\mathrm{sym},2}(\rho)$。

### 6.2 Hugenholtz-Van Hove 定理

**HVH 定理**给出无穷自束缚费米系统在零温的普适关系：

$$
E_F = \frac{d\xi}{d\rho} = E + \rho\,\frac{dE}{d\rho} = E + \frac{P}{\rho}.
$$

即**费米面处的单粒子能等于每核子能加压强份额**。对中子/质子分开：

$$
t(k_F^n) + U_n(\rho, \delta, k_F^n) = \frac{\partial\xi}{\partial\rho_n},\qquad
t(k_F^p) + U_p(\rho, \delta, k_F^p) = \frac{\partial\xi}{\partial\rho_p},
$$

其中 $t(k) = k^2/(2m)$，$k_F^\tau = k_F\,(1 + \tau\delta)^{1/3}$，$k_F = (3\pi^2\rho/2)^{1/3}$ 为对称核物质的费米动量。HVH 定理对任何相互作用的自束缚无限费米系统都严格成立，是"微观单粒子势"与"宏观状态方程"之间的普适桥梁。

### 6.3 $\partial\xi/\partial\rho_\tau$ 的 $\delta$ 分解

对 $\xi(\rho, \delta) = \rho\,E(\rho, \delta)$ 按链式法则：

$$
\frac{\partial\xi}{\partial\rho_n}
= \frac{\partial\xi}{\partial\rho}\,\frac{\partial\rho}{\partial\rho_n}
+ \frac{\partial\xi}{\partial\delta}\,\frac{\partial\delta}{\partial\rho_n}
= \frac{\partial\xi}{\partial\rho} + \frac{1}{\rho}\frac{\partial\xi}{\partial\delta} - \frac{\delta}{\rho}\frac{\partial\xi}{\partial\delta},
$$

$$
\frac{\partial\xi}{\partial\rho_p}
= \frac{\partial\xi}{\partial\rho} - \frac{1}{\rho}\frac{\partial\xi}{\partial\delta} - \frac{\delta}{\rho}\frac{\partial\xi}{\partial\delta}.
$$

两式相减：

$$
\frac{\partial\xi}{\partial\rho_n} - \frac{\partial\xi}{\partial\rho_p}
= \frac{2}{\rho}\frac{\partial\xi}{\partial\delta}
= 2\,\frac{\partial E(\rho, \delta)}{\partial\delta}.
$$

两式相加：

$$
\frac{\partial\xi}{\partial\rho_n} + \frac{\partial\xi}{\partial\rho_p}
= 2E(\rho, \delta) + 2\rho\,\frac{\partial E}{\partial\rho} - 2\delta\,\frac{\partial E}{\partial\delta}.
$$

### 6.4 二阶对称能与 Lane 实部的关系

把 HVH 的两式相减结合 $U_\tau$ 的 $\delta$ 展开

$$
U_\tau(\rho, \delta, k) = U_0(\rho, k) + \tau_3\,U_{\mathrm{sym},1}(\rho, k)\,\delta + U_{\mathrm{sym},2}(\rho, k)\,\delta^2 + \cdots
$$

在 $\delta \to 0$ 附近展开 $\partial E/\partial\delta$，最终可推得（标准推导见申庆彪《核反应极化理论》或 Li 的综述）：

$$
\boxed{\;
E_{\mathrm{sym},2}(\rho)
= \frac{1}{6}\!\left.\frac{\partial[t(k) + U_0(\rho, k)]}{\partial k}\right|_{k_F}\!\! k_F
+ \tfrac{1}{2}\,U_{\mathrm{sym},1}(\rho, k_F)
\;}
$$

或展开动能项：

$$
E_{\mathrm{sym},2}(\rho)
= \frac{1}{3}\,t(k_F)
+ \frac{1}{6}\!\left.\frac{\partial U_0}{\partial k}\right|_{k_F}\!\! k_F
+ \tfrac{1}{2}\,U_{\mathrm{sym},1}(\rho, k_F).
$$

三项的物理含义：

1. $\tfrac{1}{3}\,t(k_F)$：**自由费米动能**的同位旋贡献；
2. $\tfrac{1}{6}(\partial U_0/\partial k)\,k_F$：**同位旋标量势的动量依赖**（有效质量）贡献；
3. $\tfrac{1}{2}\,U_{\mathrm{sym},1}(\rho, k_F)$：**Lane 实部在费米面上的值**。

### 6.5 引入有效质量 $m^*/m$

把同位旋标量势的动量依赖吸收进有效质量：

$$
\frac{1}{m^*} = \frac{1}{m} + \frac{1}{\hbar^2 k_F}\!\left.\frac{\partial U_0}{\partial k}\right|_{k_F},
$$

则第一、二项合并为

$$
\frac{1}{3}\,t(k_F) + \frac{1}{6}\!\left.\frac{\partial U_0}{\partial k}\right|_{k_F}\! k_F = \frac{1}{3}\cdot\frac{T_F}{m^*/m},\qquad T_F = \frac{(\hbar c)^2 k_F^2}{2m}.
$$

于是得到 `toy_DAbreak` `compute_hvh` 使用的紧凑形式：

$$
\boxed{\;
S_{\mathrm{sym}}(\rho_0)
= \frac{1}{3}\,\frac{T_F}{m^*/m}
+ \tfrac{1}{2}\,U_1(T_F)
\;}
$$

其中把 $U_{\mathrm{sym},1}$ 与 Lane 实部 $U_1$ 在费米能处等同（假设两者在 OMP → HVH 映射下以 $T = T_F$ 等价）。

### 6.6 对称能斜率 $L$

斜率 $L = 3\rho_0\,(\partial S_{\mathrm{sym}}/\partial\rho)|_{\rho_0}$，在本模型下由三项给出：

$$
L = 2\,S_{\mathrm{sym}} + 3\gamma\,U_1(T_F) + 3 k_F\,\left.\frac{dU_1}{dk}\right|_{k_F},
$$

其中

- $\gamma$ 是 $U_0$ 的**密度依赖指数**（$U_0 \propto \rho^\gamma$），toy 模型取 $\gamma = 0.30$；
- $dU_1/dk$ 通过链式法则由 $\alpha_V$ 给出：

$$
\left.\frac{dU_1}{dk}\right|_{k_F}
= \frac{(\hbar c)^2\,k_F}{m^*}\,\alpha_V,
$$

因为 $U_1(E) = V_1^{(0)} + \alpha_V E$ 且 $E = (\hbar c)^2 k^2 / (2 m^*)$（在有效质量框架里）。

### 6.7 从光学势（$V$）到核物质单粒子势（$U$）

注意**光学势 $V_\tau(E, \delta)$** 与**单粒子势 $U_\tau(\rho, k, \delta)$** 形式相似却定义不同：前者随**入射动能 $E$**，后者随**费米面内动量 $k$**。两者通过 $T(E)$ 转换：

$$
E = T + \mathrm{Re}\,U_0(T) + \mathrm{Re}\,U_1(T),
$$

以及

$$
T(E) = T_0(E) - \tau_3\,U_{\mathrm{sym},1}(T)\,\mu(T)\,\delta,\qquad
\mu = \left(1 + \frac{dU_0}{dT}\right)^{-1}.
$$

于是光学势展开系数 $V_{\mathrm{sym},k}(E)$ 与单粒子势展开系数 $U_{\mathrm{sym},k}(T)$ 的关系为：

$$
\begin{aligned}
U_0(T(E)) &= V_0(E),\\
U_{\mathrm{sym},1}(T(E)) &= V_{\mathrm{sym},1}\,\mu,\\
U_{\mathrm{sym},2}(T(E)) &= V_{\mathrm{sym},2}\,\mu + \zeta\,V_{\mathrm{sym},1}\,\mu^2 + \vartheta\,V_{\mathrm{sym},1}^{2}\,\mu,
\end{aligned}
$$

其中

$$
\mu = 1 - \frac{\partial V_0}{\partial E},\qquad
\zeta = \frac{\partial V_{\mathrm{sym},1}}{\partial E},\qquad
\vartheta = \frac{\partial^{2} V_0}{\partial E^{2}}.
$$

`toy_DAbreak` 的实现直接用 $V_1(T_F)$ 代 $U_1(T_F)$、并以 `m_star_ratio = 0.70` 固定 $\mu \leftrightarrow m^*/m$，省掉 $E\to T$ 的自洽迭代。这是一种**刚性 HVH 映射**，足够作为闭环反演的自洽代价函数，但不是实验级定量模型。

### 6.8 数值标定（默认背景参数）

令 $\rho_0 = 0.16\,\mathrm{fm}^{-3}$，$m^*/m = 0.70$，$\gamma = 0.30$：

- $k_F \approx 1.33\,\mathrm{fm}^{-1}$，$T_F \approx 36.8\,\mathrm{MeV}$；
- 对 truth 点 $P_{\mathrm{mid}}$（$V_1^{(0)} = 8,\,\alpha_V = -0.030$）：

$$
U_1(T_F) \approx 8 - 0.030\times 36.8 \approx 6.9\ \mathrm{MeV},
$$

$$
S_{\mathrm{sym}} \approx 17.5 + 3.4 \approx 20.9\ \mathrm{MeV}.
$$

（低于实验值 $\sim 32$ MeV，因为 toy 模型的 $m^*/m$、$\gamma$ 是固定占位，不做自洽拟合。）

## 7. 闭环反演与链路一致性审计

有了上述链路，四参数 $(V_1^{(0)}, \alpha_V, W_1^{(0)}, \alpha_W)$ 成为 LM 拟合的唯一自由量。`run_closed_loop` 流程：

1. 用 truth Lane 正演生成伪观测 $d^2\sigma_{\mathrm{truth}}[\mathrm{bin}]$；
2. 从 bounds 中点出发做 LM 拟合（目标是相对残差），每次评估都要**重跑一次完整 AGS**；
3. 对 fit 与 truth 分别 `compute_hvh`；
4. 分级审计：参数 5%、$S_{\mathrm{sym}}$ 10%、$L$ 20%。

$L$ 的容差最宽，是因为它依赖 $k_F \cdot dU_1/dk$，对 $\alpha_V$ 的放大比显著，$\alpha_V$ 的拟合不确定度在 HVH 映射里按 $k_F \approx 1.33\,\mathrm{fm}^{-1}$ 近似翻 2–3 倍到 $L$ 上。

## 8. 链路速查表

| 符号 | 定义 | 所在节 |
|---|---|---|
| $V_\tau(E, \delta)$ | 光学势能量依赖 + 同位旋展开 | §2 |
| $V_{\mathrm{sym},1},\,V_{\mathrm{sym},2}$ | 光学势一阶/二阶对称势 | §2, §6.7 |
| $U_1(\rho, k)$ | 核物质一阶对称势（Lane 实部） | §3, §6.4 |
| $V_1^{(0)}, \alpha_V, W_1^{(0)}, \alpha_W$ | Lane-ED 四参数 | §3.2 |
| $(\lambda, \beta)$ | rank-1 可分势强度 / 形状 | §5 |
| $\phi_i^{(l)}(q),\,\Lambda_{ij}$ | EST rank-N 形状因子 / 耦合矩阵 | §5.1–5.2 |
| $E_F,\,k_F,\,T_F$ | 费米能 / 费米动量 / 费米动能 | §6.2, §6.5 |
| $m^*/m,\,\gamma$ | 有效质量比 / 密度依赖指数 | §6.5–6.6 |
| $S_{\mathrm{sym}}(\rho),\,L$ | 饱和密度对称能 / 斜率 | §6.5–6.6 |

## 参考

- 申庆彪，《核反应极化理论》（第三章氘核 CDCC、§13.3.8 核势分解、光学势与单粒子势转换）。
- A. J. Koning, J. P. Delaroche, *Local and global nucleon optical models from 1 keV to 200 MeV*, Nucl. Phys. A 713, 231 (2003).
- D. J. Ernst, C. M. Shakin, R. M. Thaler, *Separable representations of two-body interactions*, Phys. Rev. C 8, 46 (1973)。
- N. M. Hugenholtz, L. Van Hove, Physica 24, 363 (1958)（HVH 定理原文）。
- B.-A. Li et al., *Nucleon effective mass splitting and symmetry energy*, 综述见 Phys. Rep. 464 (2008) 113。
- 本地素材：
  - `D_nuclear_experiment/note/d_breakup/d_breakup.tex`（§HVH、光学势、$E_{\mathrm{sym},2}$ 推导片段）；
  - `dpol/toy_DAbreak/docs/physics/04_lane_observables.zh.md`；
  - `dpol/toy_DAbreak/docs/physics/05_optical_input_chain.zh.md`；
  - `dpol/toy_DAbreak/docs/physics/06_symmetry_energy_inference.zh.md`。
