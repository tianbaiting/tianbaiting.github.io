
这是关于 S.B.S. Miller 在其博士论文和 PRC 2022 工作中，为求解三核子（NNN）Faddeev 方程所采用的计算基（computational basis）的技术说明，目标是提供足够的信息以便复现其计算框架。

## 概览：两阶段基选择策略

为便于数值求解，采用两阶段基选择策略：

1. 理论基（连续）
    - 目标：在理论上严格定义 NNN 系统的希尔伯特空间。
    - 选择：三核子偏波基（Three-Nucleon Partial-Wave Basis），以雅可比动量 $p$ 与 $q$ 为连续变量。

2. 计算基（离散）
    - 目标：将连续理论基离散化，得到有限维矩阵问题。
    - 选择：波包连续区离散化（Wave-Packet Continuum Discretization, WPCD）。

下面按步骤详细说明两部分与数值实现要点。

---

## 第一部分：理论基 — 偏波基（Partial-Wave Basis）

在计算之前需定义系统的量子态，采用 (Jj) 耦合方案，偏波基向量记为 $|p,q;\alpha\rangle$，其中 $\alpha$ 由以下量子数定义：

- 对（由 $\vec p$ 描述）：
  - $L$：轨道角动量
  - $S$：两体自旋（$0$ 或 $1$）
  - $J$：两体总角动量 $\vec J=\vec L+\vec S$
  - $T$：两体同位旋（$0$ 或 $1$）

- 旁观者（由 $\vec q$ 描述）：
  - $l$：轨道角动量
  - $s$：自旋（$1/2$）
  - $j$：旁观者总角动量 $\vec j=\vec l+\vec s$
  - $t$：同位旋（$1/2$）

- 总和：
  - $\mathcal J=\vec J+\vec j$：总角动量
  - $\mathcal T=\vec T+\vec t$：总同位旋
  - $\mathcal T_z$：总同位旋 z 分量

总结：
$$
|p,q;\alpha\rangle \equiv |p,q;(LS)J,(ls)j,(Jj)\mathcal J,(Tt)\mathcal T,\mathcal T_z\rangle
$$

在数值计算中需截断角动量空间（例如工作中使用 $\mathcal J \le 17/2$ 和 $J \le 3$）。

---

## 第二部分：计算基 — WPCD 离散化

目标是把连续基 $|p,q;\alpha\rangle$ 离散化，使 AGS（Faddeev）方程
$$
\hat U = \hat P \hat v + \hat P \hat v \hat G_1(E) \hat U
$$
可转化为有限维矩阵方程。

WPCD 的核心思想是用波包（wave packet）将动量轴分箱并构建两类基：

### 步骤 1：定义输入基 — 自由波包（FWP）

- 一维 FWP $|x_i\rangle_p$ 表示动量区间（箱）$\mathcal D_i=[k_i,k_{i+1}]$ 上所有平面波的归一化积累：
  $$
  |x_i\rangle_p = \frac{1}{N_i}\int_{\mathcal D_i} f(p)\,|p\rangle\,p\,dp
  $$
  其中 $f(p)$ 与归一化因子 $N_i$ 依具体选择而定。

- 三核子 FWP 基为张量积：
  $$
  |X_{ij}^\alpha\rangle = |x_i\rangle_p \otimes |\overline{x}_j\rangle_q \otimes |\alpha\rangle.
  $$

- 网格选择（可复现要点）：
  - 使用广义切比雪夫网格（generalized Chebyshev grid）。
  - 网格点生成公式：
     $$
     p_i = \alpha \cdot \tan^{t}\!\left(\frac{2i-1}{4N_{WP}}\pi\right),\quad i=1,\dots,N_{WP}.
     $$
  - 常用参数示例：$N_{WP}=50,75,100,\dots$；$\alpha=200\ \text{MeV}$；$t=1$。
  - 在 $p$ 和 $q$ 自由度上通常使用相同的 $N_{WP}$ 和网格参数。

### 步骤 2：定义求解基 — 散射波包（SWP）

- 通道哈密顿量：
  $$
  \hat H_1 = \hat h_{NN} + \hat h_{\text{spec}} = (\hat h_0^{(p)} + \hat v_{23}) + \hat h_0^{(q)}.
  $$
  通道格林函数 $\hat G_1(E)=(E-\hat H_1+i\epsilon)^{-1}$ 在 FWP 基上通常是非对角的。

- 思路：在使 $\hat G_1$ 对角的本征基上求解。由于 $\hat h_{NN}$ 与 $\hat h_{\text{spec}}$ 可对易，本征基为各自本征基的张量积：
  - $\hat h_{\text{spec}}$ 的本征基：FWP $|\overline{x}_j\rangle_q$（旁观者自由）。
  - $\hat h_{NN}$ 的本征基：两体相互作用系统的本征态，即散射波包（SWP） $|z_i^\alpha\rangle_p$。

- 混合求解基：
  $$
  |Z_{ij}^\alpha\rangle = |z_i^\alpha\rangle_p \otimes |\overline{x}_j\rangle_q,
  $$
  在此基上 $\hat G_1(E)$ 为对角矩阵，其对角元可通过 SWP 本征能量与旁观者能量解析得到。

### 步骤 3：构建转换矩阵 C（FWP ↔ SWP）

- 在一维 FWP 基 $|x_i\rangle_p$ 上构建两体哈密顿量矩阵：
  $$
  (\mathbf H_{NN})_{ik} = \langle x_i|\hat h_{NN}|x_k\rangle = \langle x_i| \hat h_0^{(p)} + \hat v |x_k\rangle.
  $$
  这是一个 $N_{WP}\times N_{WP}$ 的实对称矩阵。

- 对角化 $\mathbf H_{NN}$（例如用 LAPACK 的 `dsyev` 等例程）：
  $$
  \mathbf H_{NN} = \mathbf C \mathbf D \mathbf C^T.
  $$
  返回的本征向量矩阵 $\mathbf C$ 的列即 SWP 在 FWP 基上的表示，元素 $C_{ki}=\langle x_k|z_i\rangle$。对角矩阵 $\mathbf D$ 给出 SWP 的本征能量 $\epsilon_i^\alpha$。

### 最终矩阵方程

在 SWP 基中，AGS 方程变为有限维矩阵方程：
$$
\mathbf U = \mathbf A + \mathbf A\,\mathbf G(E)\,\mathbf U,
$$
其中：
- $\mathbf U = \langle Z|\hat U|Z\rangle$（待求矩阵）。
- $\mathbf G(E) = \langle Z|\hat G_1(E)|Z\rangle$，为对角矩阵，其对角元可写为 $\displaystyle \frac{1}{E-\epsilon_i-E_j^q}$（$\epsilon_i$ 为 SWP 本征能，$E_j^q$ 为旁观者能量）。
- $\mathbf A = \langle Z|\hat P\hat v|Z\rangle$，为在 SWP 基中的非对角核矩阵。

由于 $\hat P$ 与 $\hat v$ 通常在 FWP 基中构建（记为 $\mathbf P_{FWP}$ 与 $\mathbf V_{FWP}$），$\mathbf A$ 通过基变换得到：
$$
\mathbf A = \mathbf C^T \big(\mathbf P_{FWP}\,\mathbf V_{FWP}\big) \mathbf C,
$$
其中 $\mathbf C$ 作用于 $p$ 自由度，$q$ 自由度保留单位阵。

---

## 复现要点与步骤清单

1. 理论层面
    - 采用 (Jj) 耦合方案定义 $\alpha$。
    - 截断角动量（示例：$\mathcal J \le 17/2$, $J \le 3$）。

2. 数值层面（FWP 基）
    - 选择 $N_{WP}$（例如从 50 起）。
    - 用切比雪夫公式生成 $N_{WP}$ 个动量点，示例参数 $\alpha=200\ \text{MeV}$，$t=1$。
    - 构建 $p$ 与 $q$ 的 FWP 基，形成三体 FWP 基 $|X_{ij}^\alpha\rangle$。
    - 在该基上构建稀疏置换矩阵 $\mathbf P$ 和块对角势能矩阵 $\mathbf V$。

3. 数值层面（SWP 基）
    - 在每个 $\alpha$ 通道的二体 FWP 基上构建 $\mathbf H_{NN}$。
    - 对 $\mathbf H_{NN}$ 对角化，获得 $\mathbf C$ 與本征能 $\epsilon_i$。
    - 存储并使用 $\mathbf C$ 将算符从 FWP 基变换到 SWP 基。

4. 方程求解
    - 构建 $\mathbf A = \mathbf C^T(\mathbf P_{FWP}\mathbf V_{FWP})\mathbf C$。
    - 构建对角 $\mathbf G(E)$（用 $\epsilon_i$ 和旁观者能量）。
    - 求解线性系统 $\mathbf U = \mathbf A + \mathbf A\mathbf G(E)\mathbf U$（可用迭代方法并结合 Padé 近似以加速收敛）。

---

## 实现建议与注意事项

- 网格质量对结果至关重要，建议对 $N_{WP}$ 与网格参数进行收敛测试。
- 对每个角动量通道独立构建并对角化二体哈密顿量以获得 SWP，便于并行化。
- 利用数值库（LAPACK/BLAS）处理对角化与线性代数，注意数值稳定性与内存管理。
- 将 $p$ 与 $q$ 自由度的张量结构、对称性和稀疏性充分利用，以降低计算资源需求。

