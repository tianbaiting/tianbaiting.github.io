# todo

## 散射理论 / 教学轨：可解模型系列

地点：`docs/sci/minimal_theory/scatteringTheory/examples/`

每篇统一模板：目标 → 势的定义 → 解析推导 → 渐近与极点 → 数值与图 → 与主线笔记的对账 → next-step 留白。
每篇配同名 `.py`，依赖只用 numpy / scipy / matplotlib。

- [x] 1. 一维 delta 势 (`1d_delta`)：S 矩阵基本结构、单极点束缚态、最干净的 $T(E)$ 解析延拓
- [x] 2. 三维方阱 s 波 (`square_well_3d`)：散射长度、有效力程、Levinson、束缚态出现判据
- [x] 3. delta-壳层势 (`delta_shell`)：从无共振到 Breit-Wigner，对应 Friedrichs 笔记中的极点结构
- [x] 4. Yukawa 势 (`yukawa`)：Born 振幅闭式、Born 级数何时崩、屏蔽 Coulomb 极限
- [x] 5. Separable rank-1 (`separable_rank1`)：T 矩阵闭合解、off-shell 行为，给 EST 附录补最小完整范例
- [x] 6. 数值实验 (`numerical_pipeline`)：Numerov + Gauss 求积，把前 5 篇势作为 sanity-check 标准

## 散射理论 / 教学轨：共振态例子

延续可解模型系列，覆盖三种典型共振机制。

- [ ] 7. 一维势阱+势垒 (`well_barrier_1d`)：α 衰变图像、长寿命极限、Numerov 透射率 vs WKB 障壁穿透
- [ ] 8. 离心障壁共振 (`centrifugal_barrier`)：3D 吸引方阱 + $l(l+1)/r^2$，d 波准束缚态、复 $k$ 极点轨迹随 $V_0$
- [ ] 9. 双通道 Feshbach (`feshbach_two_channel`)：矩阵 Numerov、闭合通道泄漏、$\Gamma \propto g^2$、与 Friedrichs 笔记 $\Sigma(z)$ 对账

设计约束沿用前 6 篇：
- 单 `.py` < 150 行
- markdown 贴关键代码段，整文件可执行
- 图保存到 `examples/assets/<篇名>/*.png`
- CSS 自动编号、noun-phrase 标题、中文不用 bold

