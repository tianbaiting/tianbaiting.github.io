# 本地 RAG：用 paperpipe + LEANN 给科研论文做向量检索

科研工作者面对的论文越来越多，用浏览器 50 个 tab 打开、 Mendeley 里堆成几千条、Zotero collection 互相重复——这些都不解决"我读过的某篇论文里到底是怎么定义 ε 的"或者"我代码里这个公式和原文一致吗"这类**实际工作中真正卡住的问题**。这篇笔记记录我目前用的本地 RAG 方案：用 [paperpipe](https://github.com/hummat/paperpipe) 管论文、用 [LEANN](https://github.com/yichuan-w/LEANN) 做本地语义检索，整套不依赖任何云端 API，集成进 Claude Code / Codex / Gemini CLI 的 skill 系统。

文章先讲什么是 embedding 和 RAG（如果你已经懂可以跳过），再讲我推荐的工具栈和落地配置，最后讨论"知识应该怎么组织"——其中包含一些反直觉的判断，比如**不要给所有论文都写 Markdown 总结**。

---

## 一、概念：embedding 和 RAG 到底在做什么

### 1.1 文本 embedding：把语义压成一个向量

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

**纯本地运行**只能用前两个。维度高一般质量好但慢；中文文献优先选 `bge-m3`。

### 1.2 RAG（Retrieval-Augmented Generation）

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

1. **检索**（retrieval）解决"哪些段落和我的问题相关"。靠的是向量相似度，不是关键词匹配。
2. **生成**（generation）解决"基于这些相关段落，把答案组织出来"。靠的是 LLM 阅读理解。
3. **引用**（grounding）是 RAG 区别于普通 chatbot 的关键——回答里每个 claim 都要能追溯到某段原文，否则 LLM 会幻觉。

### 1.3 什么时候不需要 RAG

如果你的语料是 grep 友好的纯文本（Markdown 笔记、代码、LaTeX 源码），**ripgrep 比向量检索更准**——专业术语（"Hamiltonian"、"²P doublet"、"Faddeev"）的精确匹配天然吊打 cosine 相似度。RAG 真正发力是在 PDF / 长论文 / 跨语义表述这种场景。

所以我的实践分两层：

| 语料 | 工具 | 原因 |
|---|---|---|
| 我自己的 Markdown 笔记 + 项目 docs | `ripgrep` + `Read` | 量小（~30MB），术语精确 |
| 论文 PDF / arXiv | paperpipe + LEANN | PDF 不能直接 grep；跨论文综合需要语义 |

---

## 二、工具栈：paperpipe + LEANN

### 2.1 为什么是 paperpipe

paperpipe 不是又一个 Zotero 替代品。它的定位是 **"给 coding agent 提供论文上下文"**：每篇论文加进库时，会自动产出 `paper.pdf` / `source.tex` / `equations.md` / `summary.md` / `tldr.md` / `notes.md` / `meta.json`。结构化产物可以直接进 LEANN 索引、可以被 Claude Code / Codex / Gemini CLI 的 skill 触发，也可以让你手写实现笔记。

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
- 但有 **"论文 ↔ 我的代码"对照核验**这个 niche 卖点（`papi-verify` / `papi-ground`）

适用人群：用 LLM 辅助写代码 / 实现论文方法的人。如果你只是阅读、不实现，Zotero 更合适。

### 2.2 为什么是 LEANN（不是 Chroma / FAISS / Qdrant）

LEANN 是斯坦福 SkyLab 的开源项目，主要卖点：

- **本地优先**——索引存在你自己机器上，不需要任何远程服务
- **图索引（HNSW / DiskANN）**——查询快，比 brute force 强一个数量级
- **支持 sentence-transformers / Ollama / OpenAI / Anthropic 等多种 embedding 后端**
- **有交互式终端 UI**（`leann ask --interactive`）

paperpipe 把 LEANN 包装成 `papi index --backend leann` 一行命令，连模型下载也代办了。

### 2.3 安装

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

### 2.4 把 skill 链到 Claude Code

paperpipe 自带 skill 安装命令：

```bash
papi install skill --claude
# claude: linked 7 skill(s) to /home/<you>/.claude/skills
```

这条命令在 `~/.claude/skills/` 下建 7 个 symlink（`papi`、`papi-ask`、`papi-ground`、`papi-verify`、`papi-init`、`papi-curate`、`papi-compare`），指向 paperpipe 包里的 SKILL.md。重启 Claude Code 后，对话里说"对照 LoRA 论文检查我的实现"会自动触发 `papi-verify`，按"未支持的 claim 必须说 Not supported"的规则给你回答。

Codex CLI 用 `--codex`，Gemini CLI 用 `--gemini`，参数互通。

---

## 三、日常使用流程

### 3.1 添加论文

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

`-t/--tags` 是浏览用的（`papi list -t faddeev`），不影响检索权重，但**养成习惯随手打**——日后翻阅会感谢自己。

### 3.2 建索引

```bash
# 默认用 sentence-transformers/all-MiniLM-L6-v2（90MB，英文）
papi index --backend leann

# 中文文献多，换 bge-m3（2.3GB，多语言）
papi index --backend leann \
    --leann-embedding-mode sentence-transformers \
    --leann-embedding-model BAAI/bge-m3
```

首次会下载 embedding 模型，之后增量更新。索引存在 `~/.paperpipe/.leann/indexes/papers/`。

### 3.3 三种查询模式

**模式 A：纯本地，零 API（推荐起步）**

```bash
papi ask "How do Faddeev equations decompose the 3N continuum?" \
    --backend leann --leann-provider simulated
```

`--leann-provider simulated` 意味着只检索、不合成——返回最相关的 chunks 给你。如果是在 Claude Code 对话里，**Claude Code 自己会负责合成答案**，因此不需要本地或云端 LLM。这是最便宜、最干净的路线。

**模式 B：本地 LLM 合成（要先跑 ollama）**

```bash
ollama serve &
ollama pull llama3.1:8b

papi ask "..." --backend leann \
    --leann-provider ollama --leann-model llama3.1:8b
```

适合不在 Claude Code 里、纯命令行用户。

**模式 C：在 Claude Code 里直接说自然语言**

```
你：对照 arXiv 2303.08813 检查我的 lora_adapter.py 实现是否正确
```

`papi-verify` skill 自动触发，调 `papi show lora --level eq` 取方程，按 grounding 规则给出符号映射表 + 不一致清单 + 修补方案。这是日常最高频的入口。

### 3.4 实用命令速查

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

## 四、知识组织：什么该写，什么不该写

这部分是我踩过坑后的判断，可能和你看到的 LLM 时代"知识管理"教程相反。

### 4.1 论文 PDF 放在哪里

**让 paperpipe 管，不要再分散到别处。**

- ✅ `~/.paperpipe/papers/<name>/paper.pdf` 是唯一源
- ❌ 不要再在 `~/Documents/papers/` 或项目仓库 `dpol/papers/` 放副本——双源永远 drift
- ❌ 论文不要 commit 进 git——文件大、PDF 二进制、版权复杂
- ✅ 想跨机器同步：把 `~/.paperpipe/` 整体 symlink 到 Dropbox/syncthing 同步盘
- ✅ 想阅读：直接 `open ~/.paperpipe/papers/lora/paper.pdf`，paperpipe 不锁文件

### 4.2 一个全局 DB 还是每个项目一个

我的判断：**按"研究领域"分，不按"代码仓库"分**。

- 你的 DPOL 实验下面有 Tic-tac、smsimulator、polarimeter 多个子项目，但它们共享 80% 文献——分项目反而要 add 多次
- 用 git worktree 做并行开发时，`.paperpipe/` 在仓库里就跟着 worktree 切，反而碎了
- 跨论文的语义检索是 RAG 卖点，强行隔离把卖点废了

主流做法（Zotero / Obsidian / Mendeley 用户的共识）也是**一个大库**。所以我用单一的 `~/.paperpipe/`，所有论文进去；如果哪天我开一个完全无关的项目（比如玩量子计算），那时再考虑独立 DB。

如果你确实想隔离，paperpipe 走 `PAPER_DB_PATH` 环境变量：

```bash
# 进项目自动激活——用 direnv 或 .claude/settings.json
export PAPER_DB_PATH="$PWD/.paperpipe"
```

### 4.3 要不要给每篇论文写 Markdown 总结

**反直觉的答案：不要。**

我刚开始也想"读一篇就在 Obsidian 写 3000 字解读、互相 wiki 链接"。试了三个月，结论是——这是低性价比劳动：

- 每篇至少 30 分钟，深的 2 小时
- 你读 50 篇真用上的就 5 篇，剩下 45 篇的总结永远不会被翻
- paperpipe 的 `summary.md` + `equations.md` + `tldr.md` 已经是结构化 KB，进了 LEANN 就能检索
- 手写 KB 三个月不维护就成噪音，比没有还差

**该写的是另外两类轻量笔记：**

**(a) `papi notes <paper>`——只在你实际实现/引用时写**

```bash
papi notes faddeev_glockle96
```

打开 `~/.paperpipe/papers/faddeev_glockle96/notes.md`，写 5–15 行：

```markdown
# 实现笔记

- 用在 `Tic-tac/src/core/faddeev_solver/ags_solver.cpp:42`
- 它的 partial-wave decomposition 在 ε(jJ) 那一步我做了简化：去掉了 P-wave 以上耦合
- 关键 figure 是 Fig. 4（不是摘要里画的，作者隐瞒了）
- 我的 Np=30 收敛是和它的 Np=20 对齐的，注意他们 grid spacing 不同
```

这种笔记**不可被自动总结替代**——它是论文与你具体代码、具体决定的桥接。

**(b) 写论文/答辩时再做主题综述**

不预先建 KB，而是当你要写 PRC/PRL 或准备 talk 时，触发综述工具（比如 `systematic-literature-review` skill），它临时检索→评分→分组→综述，**用完即焚**。比预先建静态 KB 更合时宜，也不会过期。

### 4.4 `papi add` 时立刻打 tag

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

## 五、和"自己的 Markdown 笔记"如何分工

我的两层知识架构：

```
~/workspace/tianbaiting.github.io/docs/         ← 个人博客 + 长期笔记
├── sci/                                         （这就是你正在读的目录）
│   ├── minimal_code/    ← 工具/代码 how-to（包括这篇）
│   ├── minimal_theory/  ← 物理理论笔记
│   ├── cheatshet/       ← 速查
│   └── project/         ← 项目相关
├── life/
└── ...

~/workspace/<某项目>/docs/                       ← 项目内文档（算法、验证）

~/.paperpipe/                                    ← 论文 + 论文级笔记
└── papers/<name>/notes.md                       ← 实现某篇论文时的具体决定
```

分工原则：

| 内容类型 | 存哪里 | 为什么 |
|---|---|---|
| 通用方法、speed run 教程 | 博客 `minimal_code/` 或 `minimal_theory/` | 给未来的自己 + 学生 + 招我的人看 |
| 项目内算法说明、验证报告 | `<项目>/docs/*.md` 或 `*.tex` | 跟代码同 git，PR 一起 review |
| 某篇论文的实现细节 | `papi notes <paper>`（即 `~/.paperpipe/papers/<name>/notes.md`） | 紧贴论文+代码，不需要项目级 git |
| 临时想法、跨论文比较 | 让 LLM 在对话里临时检索综合 | 别预先存，存了就过期 |

### 检索时的优先级（我的 Claude Code skill 流程）

1. **个人事项 / lifestyle 问题** → 触发 `local-notes-search`，grep 我的博客
2. **项目算法 / 验证 / 物理实现** → grep 当前 `<项目>/docs/`
3. **论文级问题（"那篇论文怎么定义 X"）** → 触发 `papi-ask` / `papi-ground`，走 LEANN
4. **代码 ↔ 论文一致性** → 触发 `papi-verify`
5. **以上都没命中** → LLM 一般知识 + 明确标注"非笔记内容"

这个流程靠 skill 系统自动选择，我大多数时候只是用自然语言提问。

---

## 六、Roadmap & 局限

paperpipe + LEANN 不是银弹，目前还有这些问题：

- **OCR**：扫描版 PDF 检索效果差。paperpipe 有 `[figures]` extra 走 docling，但精度有限。期刊新版 PDF 没问题
- **公式检索**：embedding 对 LaTeX 数学符号不敏感，"什么是 ⟨φ|G₀|ψ⟩"这种问题不如直接 grep `equations.md` 里的 `\langle \phi |`
- **多语言**：bge-m3 解决了中英混合，但德文/日文老论文还是会差
- **跨论文综合**：LEANN 的 `papi ask` 走 simulated provider 不会真的"综合"，只是返回 top-k chunks。综合得靠 Claude Code 在对话里完成

如果哪天上面这些成为瓶颈，可以考虑加 PaperQA2（`paperpipe[paperqa]`，需要 LLM API key），它的 multi-step retrieval 在跨论文综合上更强，代价是每次 query 0.01–0.05 USD。

---

## 七、一行命令快速上手

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
