# 本地论文 RAG

科研工作者面对的论文越来越多，用浏览器 50 个 tab 打开、 Mendeley 里堆成几千条、Zotero collection 互相重复——这些都不解决"我读过的某篇论文里到底是怎么定义 ε 的"或者"我代码里这个公式和原文一致吗"这类实际工作中真正卡住的问题。这篇笔记记录我目前用的本地 RAG 方案：用 [paperpipe](https://github.com/hummat/paperpipe) 管论文、用 [LEANN](https://github.com/yichuan-w/LEANN) 做本地语义检索，整套不依赖任何云端 API，集成进 Claude Code / Codex / Gemini CLI 的 skill 系统。

文章先讲什么是 embedding 和 RAG（如果你已经懂可以跳过），再讲我推荐的工具栈和落地配置，最后讨论"知识应该怎么组织"——其中包含一些反直觉的判断，比如不要给所有论文都写 Markdown 总结。

---

## 概念

### 文本 embedding

一段文字（比如一句话、一个段落）经过 embedding 模型后，会变成一个高维向量（典型是 384、768 或 1536 维）。这个向量的几何性质有用：

- 语义接近的两段文本，向量的 cosine 相似度高
- 语义无关的两段文本，向量近似正交

举个具体例子：

```
"deuteron polarization"   →  [0.21, -0.04, ..., 0.18]   (768 维)
"polarized deuterium"     →  [0.19, -0.03, ..., 0.17]   ← 几乎一样
"banana"                  →  [-0.40, 0.31, ..., -0.05]  ← 完全不同
```

embedding 模型通常是一个 transformer，被训练到"语义相同的句子向量靠近"。常见的开源选项：

| 模型 | 维度 | 大小 | 多语言 | 何时用 |
|---|---|---|---|---|
| `sentence-transformers/all-MiniLM-L6-v2` | 384 | 90MB | 英文为主 | 默认入门 |
| `BAAI/bge-m3` | 1024 | 2.3GB | 是（中英日韩等） | 中文/多语种文献 |
| `voyage-3-lite` | 512 | 云端 | 是 | 需要顶级质量、能联网 |
| `text-embedding-3-small` (OpenAI) | 1536 | 云端 | 是 | 已有 OpenAI key |

纯本地运行只能用前两个。维度高一般质量好但慢；中文文献优先选 `bge-m3`。

### RAG

RAG 的全套流程：

```
                  ┌────────────┐
查询 query ─────► │ embedding  │ ─► query 向量
                  └────────────┘
                                      ▼
                            ┌──────────────────┐
                            │ 向量索引（数据库） │  ← 提前把每篇论文切片、
                            └──────────────────┘    做 embedding 存进来
                                      │
                                      ▼
                          top-k 最相似的文本片段
                                      │
                                      ▼
                  ┌────────────┐
                  │   LLM      │ ─► 合成最终回答（含引用）
                  └────────────┘
```

关键点：

1. 检索（retrieval）解决"哪些段落和我的问题相关"。靠的是向量相似度，不是关键词匹配。
2. 生成（generation）解决"基于这些相关段落，把答案组织出来"。靠的是 LLM 阅读理解。
3. 引用（grounding）是 RAG 区别于普通 chatbot 的关键——回答里每个 claim 都要能追溯到某段原文，否则 LLM 会幻觉。

### 何时不需要 RAG

如果你的语料是 grep 友好的纯文本（Markdown 笔记、代码、LaTeX 源码），ripgrep 比向量检索更准——专业术语（"Hamiltonian"、"²P doublet"、"Faddeev"）的精确匹配天然吊打 cosine 相似度。RAG 真正发力是在 PDF / 长论文 / 跨语义表述这种场景。

所以我的实践分两层：

| 语料 | 工具 | 原因 |
|---|---|---|
| 我自己的 Markdown 笔记 + 项目 docs | `ripgrep` + `Read` | 量小（~30MB），术语精确 |
| 论文 PDF / arXiv | paperpipe + LEANN | PDF 不能直接 grep；跨论文综合需要语义 |

---

## 工具

### paperpipe

paperpipe 不是又一个 Zotero 替代品。它的定位是 "给 coding agent 提供论文上下文"：每篇论文加进库时，会自动产出 `paper.pdf` / `source.tex` / `equations.md` / `summary.md` / `tldr.md` / `notes.md` / `meta.json`。结构化产物可以直接进 LEANN 索引、可以被 Claude Code / Codex / Gemini CLI 的 skill 触发，也可以让你手写实现笔记。

```
~/.paperpipe/
├── index.json
├── .leann/                    # LEANN 索引缓存
└── papers/
    └── lora/
        ├── paper.pdf
        ├── source.tex         # arXiv 上有的话自动拉
        ├── equations.md       # 提取的方程 + 上下文
        ├── summary.md         # 面向编码的摘要
        ├── tldr.md            # 一段话 TL;DR
        ├── meta.json
        ├── notes.md           # 你的实现笔记（手写）
        └── figures/
            └── figure1.png
```

对比 Zotero/Mendeley，paperpipe 的特点：

- 没有图形界面（命令行 + agent skill）
- 没有"协作 / 引文样式"功能
- 但有 "论文 ↔ 我的代码"对照核验这个 niche 卖点（`papi-verify` / `papi-ground`）

适用人群：用 LLM 辅助写代码 / 实现论文方法的人。如果你只是阅读、不实现，Zotero 更合适。

### LEANN

LEANN 是斯坦福 SkyLab 的开源项目，主要卖点：

- 本地优先——索引存在你自己机器上，不需要任何远程服务
- 图索引（HNSW / DiskANN）——查询快，比 brute force 强一个数量级
- 支持 sentence-transformers / Ollama / OpenAI / Anthropic 等多种 embedding 后端- 有交互式终端 UI（`leann ask --interactive`）

paperpipe 把 LEANN 包装成 `papi index --backend leann` 一行命令，连模型下载也代办了。

### 安装

paperpipe 推荐用 [`uv`](https://github.com/astral-sh/uv) 装。先确保 uv 在 PATH 里：

```bash
# 装 uv（user-local，无需 sudo）
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"   # 写进 ~/.zshrc 或 ~/.bashrc
```

然后装 paperpipe + LEANN 后端：

```bash
# 注意 LEANN 目前没有 Python 3.14 wheel，强制用 3.13
uv tool install --python 3.13 --with 'paperpipe[leann]' \
    git+https://github.com/hummat/paperpipe

papi --version    # 1.9.0 或更新
papi path         # /home/<you>/.paperpipe
```

uv 会自动给 paperpipe 单独建一个 venv，不污染系统 Python。装完会拉 ~5GB（torch + transformers + LEANN backends）。

### 接入 Claude Code

paperpipe 自带 skill 安装命令：

```bash
papi install skill --claude
# claude: linked 7 skill(s) to /home/<you>/.claude/skills
```

这条命令在 `~/.claude/skills/` 下建 7 个 symlink（`papi`、`papi-ask`、`papi-ground`、`papi-verify`、`papi-init`、`papi-curate`、`papi-compare`），指向 paperpipe 包里的 SKILL.md。重启 Claude Code 后，对话里说"对照 LoRA 论文检查我的实现"会自动触发 `papi-verify`，按"未支持的 claim 必须说 Not supported"的规则给你回答。

Codex CLI 用 `--codex`，Gemini CLI 用 `--gemini`，参数互通。

---

## 使用

### 添加论文

```bash
# arXiv ID 直接拉
papi add 2303.08813

# 多个一起
papi add 2303.08813 1706.03762 "Attention Is All You Need"

# 已有本地 PDF
papi add --pdf ~/Downloads/glockle1996.pdf \
         --title "The three-nucleon continuum" \
         --authors "Glöckle, Witała, Hüber, Kamada, Golak" \
         --year 1996 --venue "Phys. Rep." \
         -t faddeev,3N,review
```

`-t/--tags` 是浏览用的（`papi list -t faddeev`），不影响检索权重，但养成习惯随手打——日后翻阅会感谢自己。

### 建索引

```bash
# 默认用 sentence-transformers/all-MiniLM-L6-v2（90MB，英文）
papi index --backend leann

# 中文文献多，换 bge-m3（2.3GB，多语言）
papi index --backend leann \
    --leann-embedding-mode sentence-transformers \
    --leann-embedding-model BAAI/bge-m3
```

首次会下载 embedding 模型，之后增量更新。索引存在 `~/.paperpipe/.leann/indexes/papers/`。

### 查询

模式 A：纯本地，零 API（推荐起步）
```bash
papi ask "How do Faddeev equations decompose the 3N continuum?" \
    --backend leann --leann-provider simulated
```

`--leann-provider simulated` 意味着只检索、不合成——返回最相关的 chunks 给你。如果是在 Claude Code 对话里，Claude Code 自己会负责合成答案，因此不需要本地或云端 LLM。这是最便宜、最干净的路线。

模式 B：本地 LLM 合成（要先跑 ollama）
```bash
ollama serve &
ollama pull llama3.1:8b

papi ask "..." --backend leann \
    --leann-provider ollama --leann-model llama3.1:8b
```

适合不在 Claude Code 里、纯命令行用户。

模式 C：在 Claude Code 里直接说自然语言
```
你：对照 arXiv 2303.08813 检查我的 lora_adapter.py 实现是否正确
```

`papi-verify` skill 自动触发，调 `papi show lora --level eq` 取方程，按 grounding 规则给出符号映射表 + 不一致清单 + 修补方案。这是日常最高频的入口。

### 命令速查

```bash
papi list                    # 列所有论文
papi list -t faddeev         # 按 tag 过滤
papi show lora -l eq         # 看某篇的方程
papi show lora -l tex        # 看 LaTeX 源码定义
papi show lora -l summary    # 看摘要
papi notes lora              # 打开/编辑 notes.md（你的实现笔记）
papi remove lora             # 删除
papi list --json > backup.json   # 备份元数据
papi add --from-file backup.json # 从备份恢复
```

---

## 知识组织

这部分是我踩过坑后的判断，可能和你看到的 LLM 时代"知识管理"教程相反。

### PDF 位置

让 paperpipe 管，不要再分散到别处。
- ✅ `~/.paperpipe/papers/<name>/paper.pdf` 是唯一源
- ❌ 不要再在 `~/Documents/papers/` 或项目仓库 `dpol/papers/` 放副本——双源永远 drift
- ❌ 论文不要 commit 进 git——文件大、PDF 二进制、版权复杂
- ✅ 想跨机器同步：把 `~/.paperpipe/` 整体 symlink 到 Dropbox/syncthing 同步盘
- ✅ 想阅读：直接 `open ~/.paperpipe/papers/lora/paper.pdf`，paperpipe 不锁文件

### 全局还是项目隔离

我的判断：按"研究领域"分，不按"代码仓库"分。

- 你的 DPOL 实验下面有 Tic-tac、smsimulator、polarimeter 多个子项目，但它们共享 80% 文献——分项目反而要 add 多次
- 用 git worktree 做并行开发时，`.paperpipe/` 在仓库里就跟着 worktree 切，反而碎了
- 跨论文的语义检索是 RAG 卖点，强行隔离把卖点废了

主流做法（Zotero / Obsidian / Mendeley 用户的共识）也是一个大库。所以我用单一的 `~/.paperpipe/`，所有论文进去；如果哪天我开一个完全无关的项目（比如玩量子计算），那时再考虑独立 DB。

如果你确实想隔离，paperpipe 走 `PAPER_DB_PATH` 环境变量：

```bash
# 进项目自动激活——用 direnv 或 .claude/settings.json
export PAPER_DB_PATH="$PWD/.paperpipe"
```

### 两种总结

这个问题真正的答案是：取决于你是按"论文"还是按"概念"组织笔记。这是两件容易被混在一起、但完全不同的工作。

#### 按论文索引：不写

我刚开始也想"读一篇就在 Obsidian 写 3000 字解读、互相 wiki 链接"。试了三个月，结论是——这是低性价比劳动：

- 每篇至少 30 分钟，深的 2 小时
- 你读 50 篇真用上的就 5 篇，剩下 45 篇的总结永远不会被翻
- paperpipe 的 `summary.md` + `equations.md` + `tldr.md` 已经是结构化的、按论文索引的 KB，并且进了 LEANN 就能语义检索——完全覆盖了"我之前在某篇论文看过 X"这类需求
- 手写"按论文索引"的 KB 三个月不维护就成噪音

#### 按概念索引：必写

这一层是 paperpipe 不能也不该替代的，必须自己写。原因：

- 论文之间不一致——同一个量，A 用 $\phi$、B 用 $\psi$，符号约定、归一化、近似层级各不相同。RAG 检索回来的是某一篇的原话，不是统一视角下的解释
- 你的研究方向需要一个固定坐标系——给 ε(jJ) 一个你自己版本的定义，所有论文的差异都映射到这一坐标系上
- 概念笔记是写论文/答辩/教学的真正素材，而不是临时检索来的零散段落
- 写概念笔记的过程本身就是理解（Feynman Technique）

我自己的 `minimal_theory/` 就是这一层。打开 [resolvent.zh.md](../minimal_theory/resolvent.zh.md) 你能看到典型结构：

```
# resolvent
## 预解式算符的定义与谱理论基础
   定义 1.1 (预解集) ...   [1]
   定义 1.2 (谱) ...        [1, 6]
   ...
## 谱的精细结构
   定义 1.3 (点谱) ...      [5]
   ...
参考文献
[1] <book/paper>
[2] ...
```

特点：

- 按物理概念编号（不是按论文）
- 统一的符号、约定——你的标准
- 每个 claim 有引用到原文，但只是 anchor，不是逐篇照搬
- 跨多个文献综合——同一个定义可能出现在 Reed-Simon、Glöckle、Kato 三本书里，你写一遍

paperpipe 里的论文是这一层的引用基础。当你在 `minimal_theory/` 写 `[1] Glöckle 1996` 时，那篇论文就在 `~/.paperpipe/papers/glockle1996/`，能 grep 它的 `equations.md`，能用 `papi-verify` 对照你的代码。两层互相引用：概念笔记按物理概念组织、用你自己的符号，paperpipe 按论文索引、保留原文 grounding。

#### 两类补充笔记

(a) `papi notes <paper>`——实现某篇论文时的具体决定
```bash
papi notes faddeev_glockle96
```

写 5–15 行论文 ↔ 你代码的桥接：

```markdown
- 用在 `Tic-tac/src/core/faddeev_solver/ags_solver.cpp:42`
- partial-wave decomposition 我去掉了 P-wave 以上耦合（论文 §3.4）
- 关键 figure 是 Fig. 4（不是摘要里那张）
- 我的 Np=30 收敛对齐它的 Np=20，注意 grid spacing 不同
```

这是论文级实现笔记——不可被自动总结替代，但也不试图替代概念层。

(b) 写论文/答辩时再做主题综述
不预先建 KB，而是当你要写 PRC/PRL 或准备 talk 时，触发综述工具（比如 `systematic-literature-review` skill），它临时检索→评分→分组→综述，用完即焚。比预先建论文级综述 KB 更合时宜。

#### 分工对照

| 层级 | 索引方式 | 谁写 | 何时写 | 例子 |
|---|---|---|---|---|
| 概念抽象层 | 物理概念 | 你 | 系统读完一个主题后 | `minimal_theory/resolvent.zh.md` |
| 论文-代码桥 | 论文 cite key | 你 | 实现/引用某篇时 | `~/.paperpipe/papers/glockle96/notes.md` |
| 论文摘要层 | 论文 cite key | paperpipe 自动 | `papi add` 时 | `~/.paperpipe/papers/<name>/{summary,equations,tldr}.md` |
| 临时综述 | 主题 query | LLM 临时 | 写 paper/talk 时 | `systematic-literature-review` skill 一次性输出 |

反对的只有"按论文写 3000 字解读"这一类——它既被 paperpipe 自动覆盖，又没起到抽象层的作用。其他三层都该写，且角色不同。

### tag 习惯

这是真正提高效率的小习惯：

```bash
papi add 2303.08813 -t faddeev,3N,benchmark,190MeV
```

tag 不影响 LEANN 检索，但 `papi list -t 190MeV` 浏览时极有用，几个月后回头找"我之前 190 MeV 看过的论文都有哪些"会感谢自己。

我个人的 tag 体系（仅供参考）：

- 物理领域：`faddeev`, `nuclear-reaction`, `polarization`, `breakup`, `optical-model`
- 数值方法：`wpcd`, `swp`, `r-matrix`, `cdcc`
- 实验：`samurai`, `ribf`, `dpol-2026`
- 用途：`benchmark`（标定基准）, `cite`（写文章时要引）, `implement`（在我代码里实现了）

---

## 笔记分工

我的三层知识架构：

- `tianbaiting.github.io/docs/sci/minimal_theory/`：概念抽象层，按物理概念组织，统一你自己的符号
- `tianbaiting.github.io/docs/sci/minimal_code/`：工具与方法 how-to（本文也属于此）
- `<项目>/docs/`：项目内算法说明与验证报告，跟代码同 git
- `~/.paperpipe/papers/<name>/`：论文层，按 cite key 索引。`paper.pdf` / `source.tex` / `equations.md` / `summary.md` / `tldr.md` 由 paperpipe 自动维护，`notes.md` 你写实现笔记

分工原则：

| 内容类型 | 存哪里 | 索引方式 | 为什么 |
|---|---|---|---|
| 概念骨架（散射理论 / Faddeev / 谱分解） | 博客 `minimal_theory/` | 按物理概念 | 跨论文综合，统一你自己的符号；paperpipe 给不了 |
| 通用方法、speed run 教程 | 博客 `minimal_code/` | 按主题 | 给未来的自己 + 学生 + 招我的人看 |
| 项目内算法说明、验证报告 | `<项目>/docs/*.md` 或 `*.tex` | 按代码模块 | 跟代码同 git，PR 一起 review |
| 某篇论文的实现细节 | `papi notes <paper>` | 按论文 cite key | 紧贴论文+代码 |
| 论文摘要/方程/tldr | `~/.paperpipe/papers/<name>/` | 按论文 cite key | paperpipe 自动维护 |
| 临时想法、跨论文比较 | 让 LLM 在对话里临时检索综合 | 按 query | 别预先存，存了就过期 |

### 检索优先级

1. 个人事项 / lifestyle 问题 → 触发 `local-notes-search`，grep 我的博客
2. 项目算法 / 验证 / 物理实现 → grep 当前 `<项目>/docs/`
3. 论文级问题（"那篇论文怎么定义 X"） → 触发 `papi-ask` / `papi-ground`，走 LEANN
4. 代码 ↔ 论文一致性 → 触发 `papi-verify`
5. 以上都没命中 → LLM 一般知识 + 明确标注"非笔记内容"

这个流程靠 skill 系统自动选择，我大多数时候只是用自然语言提问。

---

## 工作流

### 角色

JabRef 是文献全集，paperpipe 是其中精选子集。所有论文先进 JabRef，确认要用作 grounding 或代码核验时再 `papi add`。`minimal_theory/` 是跨论文的概念抽象层，paperpipe 不替代它。

### 入库判断

每读一篇新论文按下列三步处理：

1. JabRef 加入条目，填好 keywords 和 file 字段。
2. 判断这篇是否会被引用、被实现、或作为基准。是则 `papi add -n <citekey> -t <tags>`，否则保留在 JabRef 不再处理。
3. 判断是否带来新概念。是则在 `minimal_theory/` 新建或扩充对应文件，统一你自己的符号，文末参考列表加入这篇 cite key。

数量级目标：每读 10 篇，进 paperpipe 约 2 到 3 篇，触发概念笔记改动约 1 篇。

### 触发表

下表是日常工作里最高频的输入与对应 skill。大多数时候只用自然语言提问，skill 系统自动选择。

| 输入 | 触发的 skill | 内部动作 |
|---|---|---|
| 项目 docs 里 X 是怎么实现的 | local-notes-search | grep 当前项目 docs |
| 我博客里写过 X 吗 | local-notes-search | grep `tianbaiting.github.io/docs` |
| 某论文如何定义 X | papi-ask | LEANN 检索带引用 |
| 对照论文检查我的实现 | papi-verify | 符号映射加不一致清单 |
| 把这一段引用到原文位置 | papi-ground | 强制 paper:section 引用 |
| 起草论文章节 | paper-write-sci | 调用概念层加引用补全 |
| 主题综述 | systematic-literature-review | 检索加分组加综述 |

### 维护节奏

读论文当下立即处理 JabRef 入库与 `papi add` 决定，不要先攒一周——切换成本高于增量处理成本。每月跑一次 `papi index --backend leann` 让新加论文进入索引。某个题目读到第五篇以上时，开始写或扩充对应的 `minimal_theory/` 文件。项目里程碑时同步更新 `<项目>/docs/`。

### 例子

读到一篇 3N continuum 综述。先在 JabRef 加入条目，cite key `Glockle1996three`，keywords 写 `faddeev,3N,review`。判断这是经典综述会被引用，所以执行：

```bash
papi add --pdf <path-to-pdf> -n Glockle1996three \
    --title "..." --authors "..." --year 1996 \
    --venue "Phys. Rep." -t faddeev,3N,review
```

打开 `minimal_theory/scatering_theory.zh.md`，加一节关于 3N continuum 的 partial-wave 分解。把这篇里的 ε(jJ) 翻译成你自己坐标系下的形式，文末参考列表加 `[N] Glöckle et al., Phys. Rep. 274 (1996)`。

后续在 Tic-tac 里实现这套框架时，在 Claude Code 对话里说"对照 Glockle1996three 检查 `ags_solver.cpp`"，papi-verify 给出符号映射和不一致清单。实现完成后 `papi notes Glockle1996three` 写 5 到 15 行实现笔记，记录代码位置、近似选择、与原文的偏差。

这样这篇论文留下四个痕迹：JabRef 元数据、paperpipe 论文条目、概念笔记的一节、`papi notes` 的实现决定。每个痕迹各司其职，没有重复劳动。

## 局限

paperpipe + LEANN 不是银弹，目前还有这些问题：

- OCR：扫描版 PDF 检索效果差。paperpipe 有 `[figures]` extra 走 docling，但精度有限。期刊新版 PDF 没问题
- 公式检索：embedding 对 LaTeX 数学符号不敏感，"什么是 ⟨φ|G₀|ψ⟩"这种问题不如直接 grep `equations.md` 里的 `\langle \phi |`
- 多语言：bge-m3 解决了中英混合，但德文/日文老论文还是会差
- 跨论文综合：LEANN 的 `papi ask` 走 simulated provider 不会真的"综合"，只是返回 top-k chunks。综合得靠 Claude Code 在对话里完成

如果哪天上面这些成为瓶颈，可以考虑加 PaperQA2（`paperpipe[paperqa]`，需要 LLM API key），它的 multi-step retrieval 在跨论文综合上更强，代价是每次 query 0.01–0.05 USD。

---

## 快速上手

如果你看完想立刻试：

```bash
# 1. 安装
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
uv tool install --python 3.13 --with 'paperpipe[leann]' \
    git+https://github.com/hummat/paperpipe
papi install skill --claude

# 2. 加你想读的论文（举例：经典 Faddeev review）
papi add nucl-th/9407006 -t faddeev,review

# 3. 建索引
papi index --backend leann

# 4. 用
papi ask "how is the AGS equation reduced to one variable?" \
    --backend leann --leann-provider simulated
```

或者重启 Claude Code 后直接说自然语言，让 skill 帮你调命令。

---

## 参考

- [paperpipe - hummat/paperpipe](https://github.com/hummat/paperpipe)
- [LEANN - yichuan-w/LEANN](https://github.com/yichuan-w/LEANN)
- [PaperQA2 - Future-House/paper-qa](https://github.com/Future-House/paper-qa)
- [sentence-transformers](https://www.sbert.net/)
- [BGE-M3 (BAAI multilingual embedding)](https://huggingface.co/BAAI/bge-m3)
- [Anthropic skill system - Claude Code docs](https://docs.claude.com/)
