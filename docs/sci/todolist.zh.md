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

设计约束：
- 单 `.py` < 100 行
- markdown 中贴关键代码段，整文件可执行
- 图保存到 `examples/assets/<篇名>/*.png`
- 第 6 篇在前 5 篇完成后再写

