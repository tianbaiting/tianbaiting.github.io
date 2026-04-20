# S 矩阵与散射截面

本文沿 Taylor《Scattering Theory: Quantum Theory of Nonrelativistic Collisions》第 2–3 章的思路，在薛定谔表象下建立非相对论散射的核心框架：渐近条件 → Møller 算符 → 入出态与 S 算符 → T 矩阵 → 微分截面 → 光学定理。

## 原书参考（Taylor, Ch. 2–3）

关于态与散射截面的讲解，Taylor 这本书是我见过最清楚的。下面把相关页面直接附在开头。阅读本文时可随时对照——后文的符号和推导基本按 Taylor 的思路走。

### Chapter 2: The Scattering Operator for a Single Particle（pp. 21–37）

渐近条件、Møller 算符、散射算符的引入。

<details>
<summary>展开页面图片</summary>

![Taylor p.21](./assets/S_matrix_and_cross_section.zh/taylor-p21.png)
![Taylor p.22](./assets/S_matrix_and_cross_section.zh/taylor-p22.png)
![Taylor p.23](./assets/S_matrix_and_cross_section.zh/taylor-p23.png)
![Taylor p.24](./assets/S_matrix_and_cross_section.zh/taylor-p24.png)
![Taylor p.25](./assets/S_matrix_and_cross_section.zh/taylor-p25.png)
![Taylor p.26](./assets/S_matrix_and_cross_section.zh/taylor-p26.png)
![Taylor p.27](./assets/S_matrix_and_cross_section.zh/taylor-p27.png)
![Taylor p.28](./assets/S_matrix_and_cross_section.zh/taylor-p28.png)
![Taylor p.29](./assets/S_matrix_and_cross_section.zh/taylor-p29.png)
![Taylor p.30](./assets/S_matrix_and_cross_section.zh/taylor-p30.png)
![Taylor p.31](./assets/S_matrix_and_cross_section.zh/taylor-p31.png)
![Taylor p.32](./assets/S_matrix_and_cross_section.zh/taylor-p32.png)
![Taylor p.33](./assets/S_matrix_and_cross_section.zh/taylor-p33.png)
![Taylor p.34](./assets/S_matrix_and_cross_section.zh/taylor-p34.png)
![Taylor p.35](./assets/S_matrix_and_cross_section.zh/taylor-p35.png)
![Taylor p.36](./assets/S_matrix_and_cross_section.zh/taylor-p36.png)
![Taylor p.37](./assets/S_matrix_and_cross_section.zh/taylor-p37.png)

</details>

### Chapter 3: Cross Sections in Terms of the S Matrix（pp. 38–55）

能量守恒、壳上 T 矩阵、经典与量子截面、波包与碰撞参数、光学定理。

<details>
<summary>展开页面图片</summary>

![Taylor p.38](./assets/S_matrix_and_cross_section.zh/taylor-p38.png)
![Taylor p.39](./assets/S_matrix_and_cross_section.zh/taylor-p39.png)
![Taylor p.40](./assets/S_matrix_and_cross_section.zh/taylor-p40.png)
![Taylor p.41](./assets/S_matrix_and_cross_section.zh/taylor-p41.png)
![Taylor p.42](./assets/S_matrix_and_cross_section.zh/taylor-p42.png)
![Taylor p.43](./assets/S_matrix_and_cross_section.zh/taylor-p43.png)
![Taylor p.44](./assets/S_matrix_and_cross_section.zh/taylor-p44.png)
![Taylor p.45](./assets/S_matrix_and_cross_section.zh/taylor-p45.png)
![Taylor p.46](./assets/S_matrix_and_cross_section.zh/taylor-p46.png)
![Taylor p.47](./assets/S_matrix_and_cross_section.zh/taylor-p47.png)
![Taylor p.48](./assets/S_matrix_and_cross_section.zh/taylor-p48.png)
![Taylor p.49](./assets/S_matrix_and_cross_section.zh/taylor-p49.png)
![Taylor p.50](./assets/S_matrix_and_cross_section.zh/taylor-p50.png)
![Taylor p.51](./assets/S_matrix_and_cross_section.zh/taylor-p51.png)
![Taylor p.52](./assets/S_matrix_and_cross_section.zh/taylor-p52.png)
![Taylor p.53](./assets/S_matrix_and_cross_section.zh/taylor-p53.png)
![Taylor p.54](./assets/S_matrix_and_cross_section.zh/taylor-p54.png)
![Taylor p.55](./assets/S_matrix_and_cross_section.zh/taylor-p55.png)

</details>

---

##  记号约定与核心区分

令 $H = H_0 + V$，$H_0 = p^2/2m$ 是自由粒子哈密顿量，$V$ 是短程势。整个问题有**三类不同**的对象，它们在文献里常被同一批符号混用，因此先把身份讲清楚：

| 对象 | 记号 | 方程 | 可归一？ | 角色 |
|:--|:--|:--|:--|:--|
| 自由基矢 | $\|\mathbf{p}\rangle$，$\|\alpha\rangle$ | $H_0\|\alpha\rangle = E_\alpha\|\alpha\rangle$ | 否（$\delta$-归一） | **坐标轴** |
| 自由波包 | $\|\phi\rangle = \int g(\alpha)\|\alpha\rangle\,d\alpha$ | 自由演化 $e^{-iH_0 t}\|\phi\rangle$ | 是 | 渐近**参考** |
| 入出态 | $\|\psi_\alpha^{\pm}\rangle = \Omega_\pm\|\alpha\rangle$ | $H\|\psi_\alpha^{\pm}\rangle = E_\alpha\|\psi_\alpha^{\pm}\rangle$ | 否（$\delta$-归一） | **物理态**的坐标 |
| 散射态 | $\|\Psi(t)\rangle = e^{-iHt}\|\Psi(0)\rangle$ | 完整 $H$ 下演化 | 是 | 实验对象 |

需要反复提醒自己的两件事：

1. **基矢不是物理态**。$|\alpha\rangle$ 和 $|\psi_\alpha^\pm\rangle$ 都是 $\delta$-归一的广义本征矢，都不直接出现在概率公式里。它们的作用是为可归一的波包提供展开基底。
2. **入出态不是自由态**。$|\psi_\alpha^{\pm}\rangle$ 是 $H$（不是 $H_0$）的广义本征矢。它之所以带上自由标签 $\alpha$，仅仅是因为它在 $t\to\mp\infty$ 时的渐近行为与自由态 $|\alpha\rangle$ 匹配；在有限距离、有限时间内它与自由态完全不同。

##  渐近条件

短程势下，对于任何一个散射态 $|\Psi\rangle$（$H$ 的正能子空间里的矢量），存在两个归一化的**自由**波包 $|\phi_\text{in}\rangle$、$|\phi_\text{out}\rangle$，使得

$$
\lim_{t\to-\infty}\bigl\|\,e^{-iHt}|\Psi\rangle - e^{-iH_0 t}|\phi_\text{in}\rangle\,\bigr\| = 0,
\qquad
\lim_{t\to+\infty}\bigl\|\,e^{-iHt}|\Psi\rangle - e^{-iH_0 t}|\phi_\text{out}\rangle\,\bigr\| = 0.
$$

三点注记：

- 左边的 $e^{-iHt}|\Psi\rangle$ 一直是**完整**动力学，没有把 $V$ 关掉；只是在远时极限下，真实演化在范数意义下与某个自由演化不可区分。
- 渐近条件是关于**波包**（可归一态）的陈述，范数差 $\|\cdot\|$ 才有意义。对 $\delta$-归一的广义态，这个极限没有直接含义。
- 束缚态不满足渐近条件——它们永远不会跑到远处，没有自由波包与之对应。渐近条件只定义**散射子空间** $\mathcal{H}_\text{scatt}\subset\mathcal{H}$。

##  Møller 算符

###  定义

对渐近条件的第一式两边左乘 $e^{iHt}$ 并取极限，得到

$$
|\Psi\rangle = \lim_{t\to-\infty} e^{iHt}e^{-iH_0 t}|\phi_\text{in}\rangle.
$$

由此定义

$$
\Omega_+ = \operatorname*{s\text{-}lim}_{t\to-\infty} e^{iHt}e^{-iH_0 t},
\qquad
\Omega_- = \operatorname*{s\text{-}lim}_{t\to+\infty} e^{iHt}e^{-iH_0 t},
$$

其中 s-lim 指**强**算符极限：对每个归一化 $|\phi\rangle$，$\Omega_\pm|\phi\rangle$ 作为 Hilbert 空间矢量收敛。渐近条件可以紧凑地写成

$$
|\Psi\rangle = \Omega_+|\phi_\text{in}\rangle = \Omega_-|\phi_\text{out}\rangle.
$$

一句话：$\Omega_+$ 把"粒子在远过去看起来像 $|\phi_\text{in}\rangle$"翻译成"它实际上就是散射态 $|\Psi\rangle$"。$\Omega_-$ 类似，只是参考时刻在远未来。

### 等距性与值域

直接从定义可以验证

$$
\Omega_\pm^\dagger \Omega_\pm = \mathbf{1},
$$

即 $\Omega_\pm$ 保持内积。但一般地 $\Omega_\pm\Omega_\pm^\dagger \neq \mathbf{1}$：$\Omega_\pm$ 的值域恰是散射子空间 $\mathcal{H}_\text{scatt}$，束缚态不在里面。

**渐近完备性**：若 $\text{Range}(\Omega_+) = \text{Range}(\Omega_-) = \mathcal{H}_\text{scatt}$，则系统渐近完备——远过去看起来自由的态，远未来也看起来自由。短程势下这成立。

### 交缠关系

从 $H = H_0 + V$ 与极限定义出发，考察 $e^{iH\tau}\Omega_\pm$：

$$
\begin{aligned}
e^{iH\tau}\Omega_\pm
&= \lim_{t\to\mp\infty} e^{iH(t+\tau)} e^{-iH_0(t+\tau)}\,e^{iH_0\tau} \\
&= \Omega_\pm\, e^{iH_0\tau}.
\end{aligned}
$$

对 $\tau$ 求导并令 $\tau\to 0$：

$$
\boxed{\,H\Omega_\pm = \Omega_\pm H_0\,}
$$

这是整个理论最重要的代数关系。直接推论：若 $H_0|\alpha\rangle = E_\alpha|\alpha\rangle$，则

$$
H\,\Omega_\pm|\alpha\rangle = E_\alpha\,\Omega_\pm|\alpha\rangle.
$$

因此

$$
|\psi_\alpha^{\pm}\rangle \equiv \Omega_\pm|\alpha\rangle
$$

是 $H$ 的广义本征矢，与 $|\alpha\rangle$ **能量相同**但**态不同**。再重申一遍：$|\alpha\rangle$ 是标签（$H_0$ 本征），$|\psi_\alpha^{\pm}\rangle$ 是物理态（$H$ 本征）。

由等距性 $\Omega_\pm^\dagger\Omega_\pm = \mathbf{1}$ 和交缠关系还可得到

$$
\Omega_\pm^\dagger H\,\Omega_\pm = H_0,
$$

即 Møller 算符把完整哈密顿量限制在散射子空间上与自由哈密顿量酉等价。

##  S 算符

###  定义

同一个散射态 $|\Psi\rangle$ 对应两个自由波包：

$$
\Omega_+|\phi_\text{in}\rangle = \Omega_-|\phi_\text{out}\rangle.
$$

用 $\Omega_-^\dagger$ 作用左边，利用 $\Omega_-^\dagger\Omega_- = \mathbf{1}$：

$$
|\phi_\text{out}\rangle = \Omega_-^\dagger\Omega_+\,|\phi_\text{in}\rangle \;\equiv\; S\,|\phi_\text{in}\rangle.
$$

所以

$$
S = \Omega_-^\dagger\Omega_+.
$$

$S$ 定义在**自由空间**上：输入和输出都是自由波包。真实动力学由 $H$ 生成；$S$ 只是这个动力学投影到自由参考空间中的表示。

###  酉性与能量守恒

渐近完备性下 $S^\dagger S = SS^\dagger = \mathbf{1}$。

由交缠关系 $H\Omega_\pm = \Omega_\pm H_0$：

$$
[S, H_0] = \Omega_-^\dagger\Omega_+ H_0 - H_0\Omega_-^\dagger\Omega_+
= \Omega_-^\dagger H\Omega_+ - \Omega_-^\dagger H\Omega_+ = 0.
$$

因此 $S$ 与 $H_0$ 对易：S 算符在**自由能量**壳层上对角化——**能量守恒**在连续谱中的体现。

### S 矩阵元

在自由基底 $\{|\alpha\rangle\}$ 上展开：

$$
S_{\beta\alpha} \equiv \langle\beta|S|\alpha\rangle
= \langle\beta|\Omega_-^\dagger\Omega_+|\alpha\rangle
= \langle\psi_\beta^{-}|\psi_\alpha^{+}\rangle.
$$

两种写法各有含义：

- 左边 $\langle\beta|S|\alpha\rangle$：S 算符在**自由基底**中的矩阵元，纯粹的坐标表示。
- 右边 $\langle\psi_\beta^{-}|\psi_\alpha^{+}\rangle$：**入态与出态**的物理内积。

二者相等正是 $\Omega_\pm$ 等距性的直接推论。真正的物理重叠发生在 $H$ 的广义本征态之间；自由基底 $|\alpha\rangle$、$|\beta\rangle$ 只提供展开时用的坐标轴。

### 概率的来源

**为什么是入出态的内积给出概率，而不是自由基底的展开系数？**

实验准备入态 $|\Psi_\text{in}\rangle = \Omega_+|\phi_\text{in}\rangle$。探测器放在远未来的渐近区，工作在某个出射通道 $|\chi_\beta\rangle$（归一化自由波包）上。"探测到出射通道 $\chi_\beta$" 这件事，对应的**物理**投影算符不是自由基底上的投影，而是

$$
Q_\beta^\text{out} = \Omega_-|\chi_\beta\rangle\langle\chi_\beta|\Omega_-^\dagger,
$$

因为探测器实际测到的本征态是 $|\psi_{\chi_\beta}^{-}\rangle = \Omega_-|\chi_\beta\rangle$，而非 $|\chi_\beta\rangle$ 本身。由 Born 规则：

$$
P_{\chi_\beta\leftarrow\phi_\text{in}}
= \bigl|\langle\psi_{\chi_\beta}^{-}|\Psi_\text{in}\rangle\bigr|^2
= \bigl|\langle\chi_\beta|\Omega_-^\dagger\Omega_+|\phi_\text{in}\rangle\bigr|^2
= \bigl|\langle\chi_\beta|S|\phi_\text{in}\rangle\bigr|^2.
$$

由 Møller 等距性，这个概率等价地可以写成自由空间中的 S 矩阵元：这正是 S 矩阵与概率之间联系的根源。$|S|\phi_\text{in}\rangle$ 之所以出现，是因为物理的 out-projector 被 $\Omega_-$ 共轭到了自由空间。

相应的有限时间下，把真实态在自由基底上展开得到的系数 $c_t(\alpha) = \langle\alpha|\Psi(t)\rangle$，一般**不**是通道探测概率——粒子可能还没有离开相互作用区，通道尚未分离。

##  动量表象、T 矩阵与散射振幅

接下来把 $|\alpha\rangle$ 具体取为动量本征态 $|\mathbf{p}\rangle$：

$$
H_0|\mathbf{p}\rangle = \frac{\mathbf{p}^2}{2m}|\mathbf{p}\rangle,
\qquad
\langle\mathbf{p}'|\mathbf{p}\rangle = \delta_3(\mathbf{p}'-\mathbf{p}).
$$

由 $[S,H_0] = 0$，S 矩阵元在动量空间必然挂一个能量 $\delta$ 函数。把 $S = \mathbf{1} + R$ 拆开（$R$ 是非平凡跃迁部分），定义 **T 矩阵元**

$$
\langle\mathbf{p}'|R|\mathbf{p}\rangle = -2\pi i\,\delta(E_{p'} - E_p)\,t(\mathbf{p}'\leftarrow\mathbf{p}),
$$

即

$$
\langle\mathbf{p}'|S|\mathbf{p}\rangle
= \delta_3(\mathbf{p}'-\mathbf{p})
- 2\pi i\,\delta(E_{p'}-E_p)\,t(\mathbf{p}'\leftarrow\mathbf{p}).
$$

能量 $\delta$ 函数确保 $t$ 只在能量壳上 $|\mathbf{p}'| = |\mathbf{p}|$ 取值——壳上 T 矩阵。**散射振幅**定义为

$$
f(\mathbf{p}'\leftarrow\mathbf{p}) \equiv -(2\pi)^2\,m\,t(\mathbf{p}'\leftarrow\mathbf{p}),
$$

于是

$$
\boxed{\;
\langle\mathbf{p}'|S|\mathbf{p}\rangle
= \delta_3(\mathbf{p}'-\mathbf{p})
- \frac{i}{2\pi m}\,\delta(E_{p'}-E_p)\,f(\mathbf{p}'\leftarrow\mathbf{p}).
\;}
$$

这个形式把所有壳上的物理信息浓缩到一个只含两个方向变量（和一个能量）的复函数 $f$ 上。

##  散射截面——Taylor 的推导

###  经典图像

先回忆经典定义。一束均匀入射粒子，已知入射动量 $\mathbf{p}_0$，但无法测量碰撞参数 $\boldsymbol\rho$（$\mathbf\rho \perp \mathbf{p}_0$）。每单位面积入射 $n_\text{inc}$ 个粒子，若散射到立体角 $d\Omega$ 内的总粒子数为 $N_\text{sc}(d\Omega)$，则

$$
\frac{d\sigma}{d\Omega}\,d\Omega = \frac{N_\text{sc}(d\Omega)}{n_\text{inc}}.
$$

直观上，$\sigma$ 是靶子在垂直于 $\mathbf{p}_0$ 方向的"有效横截面"。

关键是：散射截面需要对**随机均匀的碰撞参数**平均。如果所有粒子都恰好撞同一处，定义出的就不是 $\sigma$。

### 量子版本：波包加碰撞参数平均

量子力学里，实验制备的入射态是某个波包 $|\phi\rangle$（动量分布集中在 $\mathbf{p}_0$ 附近）。碰撞参数 $\boldsymbol\rho$ 对应在 $\mathbf\rho\perp\mathbf{p}_0$ 方向的**空间平移**：

$$
|\phi_{\boldsymbol\rho}\rangle = e^{-i\mathbf{p}\cdot\boldsymbol\rho}|\phi\rangle,
\qquad
\phi_{\boldsymbol\rho}(\mathbf{p}) = e^{-i\mathbf{p}\cdot\boldsymbol\rho}\phi(\mathbf{p}).
$$

对给定碰撞参数 $\boldsymbol\rho$，远未来探测到粒子在立体角 $d\Omega$（不含入射方向）内的概率是

$$
w(d\Omega\leftarrow\phi_{\boldsymbol\rho})
= d\Omega\int_0^\infty p^2\,dp\;\bigl|\psi_\text{out}^{\boldsymbol\rho}(\mathbf{p})\bigr|^2,
$$

其中 $\psi_\text{out}^{\boldsymbol\rho} = S\phi_{\boldsymbol\rho}$。把所有随机碰撞参数累加（对 $\boldsymbol\rho$ 在垂直平面上的均匀分布积分），**截面**就定义为

$$
\boxed{\;
\sigma(d\Omega\leftarrow\phi) = \int d^2\rho\;w(d\Omega\leftarrow\phi_{\boldsymbol\rho}).
\;}
$$

这是 Taylor 对量子散射截面的定义：入射波包形状、加上对碰撞参数的平均。经典截面定义里"每单位面积 $n_\text{inc}$ 粒子"的作用正是这个 $\int d^2\rho$。

### 用 S 矩阵计算

$\psi_\text{out}(\mathbf{p}) = \int d^3p'\,\langle\mathbf{p}|S|\mathbf{p}'\rangle\,\phi_{\boldsymbol\rho}(\mathbf{p}')$。代入 §4 的结构：

$$
\psi_\text{out}(\mathbf{p}) = \phi_{\boldsymbol\rho}(\mathbf{p})
- \frac{i}{2\pi m}\int d^3p'\,\delta(E_p-E_{p'})\,f(\mathbf{p}\leftarrow\mathbf{p}')\,\phi_{\boldsymbol\rho}(\mathbf{p}').
$$

对 $\mathbf{p}$ 不在入射方向 $\mathbf{p}_0$ 的小邻域里，第一项 $\phi_{\boldsymbol\rho}(\mathbf{p}) = 0$，只剩跃迁部分。代入 $\phi_{\boldsymbol\rho}(\mathbf{p}') = e^{-i\mathbf{p}'\cdot\boldsymbol\rho}\phi(\mathbf{p}')$ 并取模平方：

$$
|\psi_\text{out}(\mathbf{p})|^2
= \frac{1}{(2\pi m)^2}
\int d^3p'\,d^3p''\;
\delta(E_p-E_{p'})\,\delta(E_p-E_{p''})\,
f^*(\mathbf{p}\!\leftarrow\!\mathbf{p}')\,f(\mathbf{p}\!\leftarrow\!\mathbf{p}'')\,
\phi^*(\mathbf{p}')\phi(\mathbf{p}'')\,
e^{i(\mathbf{p}'-\mathbf{p}'')\cdot\boldsymbol\rho}.
$$

代入截面定义并对 $\boldsymbol\rho$ 积分。关键是

$$
\int d^2\rho\; e^{i(\mathbf{p}'-\mathbf{p}'')\cdot\boldsymbol\rho}
= (2\pi)^2\,\delta_2\!\bigl(\mathbf{p}'_\perp - \mathbf{p}''_\perp\bigr),
$$

这把 $\mathbf{p}'$、$\mathbf{p}''$ 的垂直分量锁在一起。再配合两个能量 $\delta$：固定 $\mathbf{p}'_\perp = \mathbf{p}''_\perp$ 以及 $E_{p'} = E_{p''}$，只剩纵向分量的一维自由度，而

$$
\delta(E_{p'}-E_{p''}) = \frac{m}{p'_\|}\,\delta\!\bigl(p'_\|-p''_\|\bigr).
$$

合在一起得到 $\delta_3(\mathbf{p}'-\mathbf{p}'')$。因此

$$
\sigma(d\Omega\leftarrow\phi)
= \frac{d\Omega}{m}\int_0^\infty p^2\,dp
\int d^3p'\;\frac{p'}{p'_\|}\,
\delta(E_p-E_{p'})\,\bigl|f(\mathbf{p}\leftarrow\mathbf{p}')\bigr|^2\,
|\phi(\mathbf{p}')|^2.
$$

现在利用波包**集中**这个假设：若 $\phi(\mathbf{p}')$ 集中在 $\mathbf{p}'\approx\mathbf{p}_0$ 附近（$\mathbf{p}_0$ 沿轴向，故 $p'_\|\approx p'$），且 $f$ 在这一邻域内近似常数，可以把 $f$ 和 $p'/p'_\|=1$ 提到积分外，并用 $\delta(E_p-E_{p'})$ 把 $p$ 积掉：

$$
\sigma(d\Omega\leftarrow\phi) \approx d\Omega\,|f(\mathbf{p}\leftarrow\mathbf{p}_0)|^2
\int d^3p'\,|\phi(\mathbf{p}')|^2
= d\Omega\,|f(\mathbf{p}\leftarrow\mathbf{p}_0)|^2.
$$

也就是

$$
\boxed{\;
\frac{d\sigma}{d\Omega}(\mathbf{p}\leftarrow\mathbf{p}_0)
= \bigl|f(\mathbf{p}\leftarrow\mathbf{p}_0)\bigr|^2.
\;}
$$

这就是课本里熟悉的公式。注意这里的推导**没有**出现 $[\delta(E)]^2$ 之类的病态量：能量的一个 $\delta$ 被碰撞参数积分 $\int d^2\rho$ 通过傅里叶分解吃掉了，另一个被波包 $|\phi|^2$ 的积分吃掉。

### 推导过程对波包的要求与散射方向的限制

- **$\phi(\mathbf{p})$ 必须足够集中**：集中在 $\mathbf{p}_0$ 的一个小邻域内，且 $f(\mathbf{p}\leftarrow\mathbf{p}')$ 在这一邻域里变化缓慢（即势 $V$ 不能太尖），才能把它提到积分外。这两个条件互相制约：波包越窄，位置展开越宽，但只要大于势的作用范围即可。
- **散射方向 $\mathbf{p}\neq\mathbf{p}_0$**：推导从一开始就扔掉了 $\phi_{\boldsymbol\rho}(\mathbf{p})$ 项——它只在前向方向有贡献。**前向散射的微分截面本来就没有清晰定义**：前向出射与"没散射直接穿过"的粒子无法区分。
- **只依赖 $|f|^2$，与相位无关**：这也解释了为什么 $f$ 的整体相位（在远场波函数的定义中是约定）不影响观测量。

## 光学定理

把 $S = \mathbf{1} + R$ 代入酉性 $S^\dagger S = \mathbf{1}$：

$$
R + R^\dagger + R^\dagger R = 0.
$$

取动量矩阵元 $\langle\mathbf{p}|\cdot|\mathbf{p}\rangle$（同一个态，前向方向）：

$$
\langle\mathbf{p}|R|\mathbf{p}\rangle + \langle\mathbf{p}|R|\mathbf{p}\rangle^*
= -\int d^3p''\,|\langle\mathbf{p}''|R|\mathbf{p}\rangle|^2.
$$

用 $\langle\mathbf{p}'|R|\mathbf{p}\rangle = -(i/2\pi m)\delta(E_{p'}-E_p)f(\mathbf{p}'\leftarrow\mathbf{p})$ 代入。左边两项相加给出 $2\operatorname{Im}f(\mathbf{p}\leftarrow\mathbf{p})/(\pi m)$ 乘以一个能量 $\delta$；右边的 $\delta^2$ 中有一个被能量积分吃掉，剩下的归一化因子配合立体角积分给出总截面。最后得到

$$
\boxed{\;
\operatorname{Im}f(\mathbf{p}\leftarrow\mathbf{p}) = \frac{p}{4\pi}\,\sigma_\text{tot}(\mathbf{p}),
\;}
\qquad
\sigma_\text{tot}(\mathbf{p}) = \int d\Omega_{\mathbf{p}'}\,|f(\mathbf{p}'\leftarrow\mathbf{p})|^2.
$$

两点含义：

1. 前向散射振幅的虚部由总散射截面决定。微分截面只测到 $|f|^2$，但光学定理把 $\operatorname{Im}f$ 和 $\sigma$ 联系起来，于是（配合色散关系）可以恢复 $\operatorname{Re}f$。
2. 推导只用到 $S$ 的酉性，这一结论在非弹性散射、相对论散射中都成立。

## Lippmann–Schwinger 方程

至此的一切都是时域的（通过 $t\to\pm\infty$ 极限定义算符）。若要一个不显含时间的定态散射方程，从交缠关系 $H\Omega_+ = \Omega_+H_0$ 出发直接得到：$|\psi_\alpha^+\rangle = \Omega_+|\alpha\rangle$ 满足

$$
(E_\alpha - H_0)|\psi_\alpha^+\rangle = V|\psi_\alpha^+\rangle.
$$

$E_\alpha$ 在 $H_0$ 的连续谱上，直接反演 $(E_\alpha - H_0)^{-1}$ 病态，加 $i\epsilon$ 选定远过去渐近条件（输入为自由平面波、输出为外行球面波）：

$$
|\psi_\alpha^+\rangle = |\alpha\rangle + G_0^+(E_\alpha)\,V\,|\psi_\alpha^+\rangle,
\qquad
G_0^+(E) = \frac{1}{E - H_0 + i\epsilon}.
$$

出态满足同样形式的方程，只是 $i\epsilon\to -i\epsilon$。

取 $|\alpha\rangle = |\mathbf{k}\rangle$ 并在坐标空间中写开，$G_0^+$ 的核是

$$
G_0^+(\mathbf{r},\mathbf{r}';E_k) = -\frac{m}{2\pi}\,\frac{e^{ik|\mathbf{r}-\mathbf{r}'|}}{|\mathbf{r}-\mathbf{r}'|}
\quad(\hbar=1).
$$

远场 $r\to\infty$，用 $|\mathbf{r}-\mathbf{r}'|\approx r - \hat{\mathbf{r}}\cdot\mathbf{r}'$：

$$
\psi_\mathbf{k}^{+}(\mathbf{r})
\;\xrightarrow{r\to\infty}\;
e^{i\mathbf{k}\cdot\mathbf{r}}
+ f(\hat{\mathbf{r}}\leftarrow\mathbf{k})\,\frac{e^{ikr}}{r},
$$

其中

$$
f(\hat{\mathbf{r}}\leftarrow\mathbf{k})
= -\frac{m}{2\pi}\int d^3r'\;e^{-i\mathbf{k}_f\cdot\mathbf{r}'}\,V(\mathbf{r}')\,\psi_\mathbf{k}^+(\mathbf{r}'),
\qquad \mathbf{k}_f = k\hat{\mathbf{r}}.
$$

这正是 §4 里定义的散射振幅（$\mathbf{p}'\leftarrow\mathbf{p}$ 的记号换成 $\hat{\mathbf{r}}\leftarrow\mathbf{k}$）。注意远场中那个 $e^{i\mathbf{k}\cdot\mathbf{r}}$ **不是**波函数"的自由部分"——$\psi_\mathbf{k}^{+}$ 通篇是 $H$ 的精确广义本征函数。平面波项只是渐近匹配条件给出的一种结构性写法。

**Born 近似**的含义至此也清楚了：把 $\psi_\mathbf{k}^+$ 用自由态 $|\mathbf{k}\rangle$ 近似替代，

$$
f^\text{Born}(\mathbf{k}_f\leftarrow\mathbf{k})
= -\frac{m}{2\pi}\int d^3r\,e^{-i(\mathbf{k}_f-\mathbf{k})\cdot\mathbf{r}}\,V(\mathbf{r}).
$$

它可以和 $V$ 足够弱（或耦合足够小）有关。**这正是自由态与入态不同的量化**：如果二者相等，就不存在散射。

##  逻辑链概览

$$
\boxed{\;
\text{渐近条件}
\;\longrightarrow\;
\Omega_\pm
\;\longrightarrow\;
S,\;|\psi_\alpha^{\pm}\rangle
\;\longrightarrow\;
t,\;f
\;\longrightarrow\;
d\sigma/d\Omega
\;\longrightarrow\;
\text{光学定理}
\;}
$$

| | 自由基矢 $\|\alpha\rangle$ | 入出态 $\|\psi_\alpha^{\pm}\rangle$ |
|:--|:--|:--|
| 方程 | $H_0\|\alpha\rangle = E_\alpha\|\alpha\rangle$ | $H\|\psi_\alpha^{\pm}\rangle = E_\alpha\|\psi_\alpha^{\pm}\rangle$ |
| 身份 | 坐标轴 / 标签 | 物理散射态（$\delta$-归一广义本征） |
| 含相互作用 | 否 | 是 |
| 在 $S$ 矩阵里的角色 | 提供展开基底 | 提供物理内积 |

最后一点：整篇都假设 $V$ 是短程势（快于 $1/r$ 衰减）。对 Coulomb 等长程势，自由传播本身就不对，需要把参考动力学改成包含对数相位修正的 Coulomb 波；但上面所有的代数结构都可以平行地搬过去。
