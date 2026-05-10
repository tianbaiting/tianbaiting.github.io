---
title: 散射理论与 Faddeev 方程
subtitle: 定义与推导备忘单
tags:
  - 科研
  - 散射理论
  - 三体问题
comments: true
---

约定：质心系，$\hbar=1$，相互作用势短程（衰减快于 $1/r$）。$+i\epsilon$ 默认为出射边界条件。

## 两体散射的基本量

Hamiltonian 与自由部分：

$$
H = H_0 + V,\qquad H_0 = \frac{\vec{p}^2}{2\mu},\qquad \mu = \frac{m_1 m_2}{m_1+m_2}.
$$

散射态渐近行为（出射边界条件）：

$$
\psi_{\vec{k}}^+(\vec{r}) \xrightarrow{r\to\infty} e^{i\vec{k}\cdot\vec{r}} + f_{\vec{k}}(\hat{r})\,\frac{e^{ikr}}{r}.
$$

微分截面：

$$
\frac{d\sigma}{d\Omega} = |f_{\vec{k}}(\hat{r})|^2.
$$

光学定理（粒子流守恒的直接推论）：

$$
\sigma_{\text{tot}}(k) = \frac{4\pi}{k}\,\mathrm{Im}\, f_{\vec{k}}(\hat{k}).
$$

## Green 算符与解析延拓

自由 / 完整 resolvent：

$$
G_0(z) = (z - H_0)^{-1},\qquad G(z) = (z - H)^{-1}.
$$

Resolvent 恒等式：

$$
G = G_0 + G_0\,V\,G = G_0 + G\,V\,G_0.
$$

带 $\pm i\epsilon$ 的边界值：

$$
G_0^\pm(E) = \lim_{\epsilon\to 0^+} (E - H_0 \pm i\epsilon)^{-1}.
$$

Sokhotski–Plemelj：

$$
\frac{1}{E - H_0 \pm i\epsilon} = \mathcal{P}\frac{1}{E-H_0} \mp i\pi\,\delta(E-H_0).
$$

## Lippmann–Schwinger 方程

波函数形式：

$$
|\psi_E^+\rangle = |\phi_E\rangle + G_0^+(E)\,V\,|\psi_E^+\rangle.
$$

T 算符形式（定义 $T|\phi\rangle \equiv V|\psi^+\rangle$）：

$$
T(E) = V + V\,G_0^+(E)\,T(E) = V + V\,G(E)\,V.
$$

散射振幅与 T 矩阵元：

$$
f_{fi} = -\frac{(2\pi)^2 \mu}{\hbar^2}\,\langle \phi_f | T(E) | \phi_i \rangle.
$$

## Møller 波算符与 S 矩阵

Møller 算符（intertwining）：

$$
\Omega_\pm = \lim_{t\to\mp\infty} e^{iHt} e^{-iH_0 t},\qquad H\,\Omega_\pm = \Omega_\pm\,H_0.
$$

S 算符：

$$
S = \Omega_-^\dagger\,\Omega_+,\qquad S = I - 2\pi i\,\delta(E_f-E_i)\,T_{fi}.
$$

幺正性 $S^\dagger S = I$ 与光学定理等价。

## 分波展开与相移

球面波分解：

$$
e^{i\vec{k}\cdot\vec{r}} = \sum_{l=0}^{\infty}(2l+1)\,i^l\,j_l(kr)\,P_l(\cos\theta).
$$

分波 S 矩阵 / 散射振幅：

$$
S_l(k) = e^{2i\delta_l(k)},\qquad f(\theta) = \frac{1}{k}\sum_l (2l+1)\,e^{i\delta_l}\sin\delta_l\,P_l(\cos\theta).
$$

## 有效力程展开与 Levinson 定理

低能展开（s 波）：

$$
k\cot\delta_0(k) = -\frac{1}{a} + \frac{1}{2}\,r_0\,k^2 + O(k^4).
$$

$a$ 为散射长度，$r_0$ 为有效力程。

Levinson 定理（$l$ 分波）：

$$
\delta_l(0) - \delta_l(\infty) = n_l\,\pi,
$$

$n_l$ 为该分波的束缚态数（s 波且存在零能共振时增加 $\pi/2$ 修正）。

## Jost 函数与 S 矩阵解析性

$l=0$ 的 Jost 解：

$$
f^\pm(k,r) \xrightarrow{r\to\infty} e^{\pm ikr}.
$$

Jost 函数 $\mathcal{F}(k) = f^+(k,0)$，则

$$
S_0(k) = \frac{\mathcal{F}(-k)}{\mathcal{F}(k)}.
$$

性质：$\mathcal{F}(k)$ 在上半 $k$ 平面解析，$\mathcal{F}(i\kappa_n)=0$ 对应束缚态 $E_n=-\kappa_n^2/(2\mu)$；$S$ 极点在物理片对应共振或束缚态。

## 时间反演与细致平衡

时间反演 $\Theta$ 反线性、$\Theta\,\vec{p}\,\Theta^{-1}=-\vec{p}$，$\Theta\,\vec{S}\,\Theta^{-1}=-\vec{S}$。若 $[H,\Theta]=0$：

$$
\langle \vec{k}_f, m_f | T | \vec{k}_i, m_i \rangle = (-1)^{\Delta m}\,\langle -\vec{k}_i, -m_i | T | -\vec{k}_f, -m_f \rangle.
$$

对截面给出细致平衡：

$$
k_i^2\,(2s_a+1)(2s_b+1)\,\sigma_{a+b\to c+d} = k_f^2\,(2s_c+1)(2s_d+1)\,\sigma_{c+d\to a+b}.
$$

## Coulomb 修正

纯 Coulomb 渐近：

$$
\psi_{\vec{k}}^{(C)+}(\vec{r}) \xrightarrow{r\to\infty} \exp\!\big[i\vec{k}\!\cdot\!\vec{r} + i\eta\ln(kr-\vec{k}\!\cdot\!\vec{r})\big] + f_C(\theta)\,\frac{e^{i(kr-\eta\ln 2kr)}}{r},
$$

Sommerfeld 参数 $\eta = Z_1 Z_2 \alpha\,\mu/k$。Coulomb 振幅与相移：

$$
f_C(\theta) = -\frac{\eta}{2k\sin^2(\theta/2)}\,\exp\!\big[-i\eta\ln\sin^2(\theta/2) + 2i\sigma_0\big],\quad \sigma_l = \arg\Gamma(l+1+i\eta).
$$

## 双势公式与 DWBA

将 $V = U + W$，$\chi^\pm$ 为 $H_0+U$ 的失真波，则

$$
T_{fi} = \langle \phi_f | U | \chi_i^+ \rangle + \langle \chi_f^- | W | \psi_i^+ \rangle.
$$

DWBA：上式右端用 $\chi_i^+$ 取代 $\psi_i^+$（一阶近似）：

$$
T_{fi}^{\text{DWBA}} = \langle \phi_f | U | \chi_i^+ \rangle + \langle \chi_f^- | W | \chi_i^+ \rangle.
$$

## 三体 Jacobi 坐标

第 $k$ 套（$k$ 为旁观者）：

$$
\vec{\rho}_k = \vec{r}_i - \vec{r}_j,\qquad \vec{\lambda}_k = \frac{m_i\vec{r}_i + m_j\vec{r}_j}{m_i+m_j} - \vec{r}_k,
$$

约化质量 $\mu_{ij} = m_i m_j/(m_i+m_j)$，$\nu_k = (m_i+m_j)m_k/M$。质心系自由 Hamiltonian：

$$
H_0 = \frac{\vec{p}_{\rho_k}^2}{2\mu_{ij}} + \frac{\vec{p}_{\lambda_k}^2}{2\nu_k}.
$$

三套坐标通过线性正交变换互换；变换矩阵中的角度即标准化的“Raynal–Revai 旋转”。

## 三体 LS 方程的病态

总 T 算符的 LS 方程

$$
T = V + V G_0 T,\qquad V = V_1 + V_2 + V_3
$$

迭代后含 $G_0 V_i G_0 V_i$ 这类“旁观者从未参与”的链；动量表象下 $V_i$ 矩阵元含 $\delta(\vec{q}'-\vec{q})$（旁观者动量守恒）。结果：积分核 $K=G_0 V$ 非紧致（non-compact），Fredholm 唯一性失效。

## Faddeev 分解

T 矩阵分量（以 $V_i$ 为“末次作用”）：

$$
T^{(i)} \equiv V_i + V_i\,G_0\,T,\qquad T = T^{(1)} + T^{(2)} + T^{(3)}.
$$

波函数分量：

$$
|\Psi^{(i)}\rangle = G_0\,V_i\,|\Psi\rangle,\qquad |\Psi\rangle = |\Phi\rangle + \sum_i |\Psi^{(i)}\rangle.
$$

## Faddeev / AGS 方程

利用两体 t 矩阵 $t_i = V_i + V_i G_0 t_i$，把 $T^{(i)}$ 化为耦合方程：

$$
\boxed{\;T^{(i)} = t_i + t_i\,G_0\sum_{j\neq i} T^{(j)}\;}
$$

矩阵形式 $\mathbf{X} = \mathbf{Y} + \mathbf{K}\mathbf{X}$，

$$
\mathbf{K} = \begin{pmatrix} 0 & t_1 G_0 & t_1 G_0 \\ t_2 G_0 & 0 & t_2 G_0 \\ t_3 G_0 & t_3 G_0 & 0 \end{pmatrix}.
$$

对角元为零禁止 $t_i G_0 T^{(i)}$ 出现，去掉了非连通图。$\mathbf{K}^2$ 的所有分量形如 $t_i G_0 t_j$（$i\neq j$）：紧致；Fredholm 唯一性恢复。

## 置换算符与角动量重耦合

置换 $P_{ki}$ 把 $k$ 套基矢映射到 $i$ 套，矩阵元分解为

$$
\langle i;\alpha',m' | P_{ki} | k;\alpha,m \rangle = (\text{几何积分}) \times (\text{重耦合系数}).
$$

重耦合系数由 Wigner 6-j 与 9-j 符号组合而成；几何因子是变换后 $g_n(p)$ 在新基上的投影积分。

带置换的 Faddeev 形式（识别粒子全同时合并）：

$$
T = (1+P)\,t\,G_0\,(1+P)\,T + (1+P)\,t.
$$

## 分波与离散化

径向归一化（含 Jacobian $p^2 dp$）：

$$
\int_0^\infty p^2\,dp\;g_m(p)\,g_n(p) = \delta_{mn}.
$$

三体分波基矢复合指标：

$$
|p,q;\,((l_p,S_{ij})j_{ij},(l_q,s_k)j_k)\,J,M\rangle.
$$

WP-CD 基矢：解广义本征值问题 $\mathbf{H}\mathbf{c} = E\,\mathbf{B}\mathbf{c}$，正本征值给出离散化连续谱基。

## 求解流程速查

1. 选 $(J,\Pi)$ 通道，列出所有 $\alpha$。
2. 在分波径向基上算两体 $t$ 矩阵 $t^{(j,s)}_{l'l}(E_{\text{sub}})$。
3. 预算 $P_{ki}$ 矩阵（6-j、9-j 与几何积分）。
4. 装配 $\mathbf{K}$、驱动项 $\mathbf{Y}$。
5. 用 GMRES 等 Krylov 解 $(\mathbf{I}-\mathbf{K})\mathbf{X}=\mathbf{Y}$。
6. 投影到入/出态得到 $T^J_{fi}$，相干叠加到自旋空间散射振幅 $f_{m_f m_i}(\theta,\phi)$，给出截面与极化观测量。

## 相关条目

- 详细推导：[scatteringTheory/T_and_U_operators.zh](../minimal_theory/scatteringTheory/04_T_and_U_operators.zh.md)、[scatteringTheory/Green_operator.zh](../minimal_theory/scatteringTheory/02_Green_operator.zh.md)、[scatteringTheory/jost_analyticity.zh](../minimal_theory/scatteringTheory/10_jost_analyticity.zh.md)、[scatteringTheory/effective_range_levinson.zh](../minimal_theory/scatteringTheory/11_effective_range_levinson.zh.md)、[scatteringTheory/coulomb_scattering.zh](../minimal_theory/scatteringTheory/07_coulomb_scattering.zh.md)、[scatteringTheory/dwba.zh](../minimal_theory/scatteringTheory/08_dwba.zh.md)、[scatteringTheory/time_reversal_detailed_balance.zh](../minimal_theory/scatteringTheory/09_time_reversal_detailed_balance.zh.md)。
- Faddeev 实现：[project/faddeev/faddeev_WavePacket.zh](../project/faddeev/faddeev_WavePacket.zh.md)、[project/faddeev/construct_basis.zh](../project/faddeev/construct_basis.zh.md)。
