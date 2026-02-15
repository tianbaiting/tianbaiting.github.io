---
title: jupytext 工作流（Git 追踪 .py，而不是 .ipynb）
tag:
  - jupytext
  - jupyter
  - git
  - notebook
---

# jupytext 工作流（完整版）

本文是可直接迁移到任意仓库的实战教程，目标是：

1. Git 不再追踪 `.ipynb`，只追踪 notebook 对应的 `.py`（`py:percent` 格式）。
2. `.ipynb <-> .py` 自动双向同步。
3. 新下载的 `.py` 能快速生成 `.ipynb`。
4. 在 `commit`、`pull`、`checkout` 后自动同步，减少冲突和无意义 diff。

## 1. 为什么要这样做

Jupyter Notebook 的 JSON 文件天然不适合代码评审：

1. diff 噪声大（尤其是输出单元和执行计数）。
2. 多人协作冲突频繁。
3. 很难把 notebook 当作“普通代码”纳入 CI 与代码规范。

使用 `jupytext` 后，团队可以：

1. 继续用 notebook 交互式开发。
2. 让 Git 只看可读、可审查的 `.py` 文本。
3. 在不牺牲体验的前提下，把 notebook 纳入工程化流程。

## 2. 适用场景与不适用场景

### 2.1 适用场景

1. 数据分析、科研计算、可视化报告类仓库。
2. 团队成员同时使用 JupyterLab/VSCode Notebook。
3. 需要 PR review、CI 检查、代码归档。

### 2.2 不适用场景

1. notebook 中大量依赖“输出快照”作为审查对象（图像输出必须保留版本化时）。
2. 团队不接受任何本地 hook 机制。

## 3. 前置条件

### 3.1 工具要求

建议最低版本：

1. Python 3.9+
2. Git 2.30+
3. jupytext 1.16+

安装：

```bash
python3 -m pip install jupytext
```

代码解释：

1. `python3 -m pip`：使用当前 Python 环境中的 `pip`，避免装到错误解释器。
2. `install jupytext`：安装 jupytext 主程序，后续 `jupytext --sync` 依赖它。

如果项目使用 `requirements.txt` 或 `pyproject.toml`，请把 `jupytext` 作为开发依赖写入。

### 3.2 仓库目录约定（推荐）

```text
repo/
├── notebooks/
│   └── ...
├── tools/
│   └── jupytext_sync.py
├── .githooks/
│   ├── pre-commit
│   ├── post-merge
│   ├── post-checkout
│   └── post-rewrite
└── .jupytext.toml
```

代码解释：

1. `notebooks/`：存放 notebook 及其配对 `.py`。
2. `tools/jupytext_sync.py`：统一同步入口，避免每个人手写命令。
3. `.githooks/`：仓库内共享 hooks，便于团队一致行为。
4. `.jupytext.toml`：定义全仓库 notebook 配对策略。

## 4. 核心配置

### 4.1 新建 `.jupytext.toml`

```toml
formats = "ipynb,py:percent"
notebook_metadata_filter = "kernelspec,language_info,jupytext"
cell_metadata_filter = "-all"
```

代码解释：

1. `formats = "ipynb,py:percent"`：同一份 notebook 维护两种表示，前端编辑 `.ipynb`，版本管理看 `.py`。
2. `notebook_metadata_filter`：只保留内核和语言等必要元信息，减少 merge 冲突。
3. `cell_metadata_filter = "-all"`：去除 cell 级元数据，减少无效变更。

### 4.2 `.gitignore` 建议

推荐加入：

```gitignore
*.ipynb
```

代码解释：

1. 防止未来新增或同步出来的 `.ipynb` 被误提交。
2. 该规则只影响“未追踪文件”，不会自动取消已追踪 `.ipynb`。

注意：迁移时仍需 `git rm --cached` 取消旧追踪。

## 5. 同步脚本（可复用）

新建 `tools/jupytext_sync.py`：

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_ROOT = REPO_ROOT / "notebooks"


def run(cmd: list[str], cwd: Path | None = None) -> str:
    p = subprocess.run(
        cmd,
        cwd=cwd or REPO_ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return p.stdout


def rel(p: Path) -> str:
    return str(p.relative_to(REPO_ROOT))


def is_notebook_py(p: Path) -> bool:
    try:
        with p.open("r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                if i > 120:
                    break
                if "jupytext:" in line or line.startswith("# %%"):
                    return True
    except OSError:
        return False
    return False


def staged_files() -> list[Path]:
    out = run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"]).strip()
    if not out:
        return []

    paths = []
    for s in out.splitlines():
        p = (REPO_ROOT / s).resolve()
        if p.exists():
            paths.append(p)
    return paths


def all_targets() -> list[Path]:
    items = []
    if NOTEBOOK_ROOT.exists():
        items.extend(NOTEBOOK_ROOT.rglob("*.ipynb"))
        for p in NOTEBOOK_ROOT.rglob("*.py"):
            if is_notebook_py(p):
                items.append(p)
    return [p.resolve() for p in items]


def normalize_targets(paths: list[Path]) -> list[Path]:
    uniq: dict[str, Path] = {}
    for p in paths:
        p = p.resolve()
        if not p.exists():
            continue

        try:
            p.relative_to(NOTEBOOK_ROOT)
        except ValueError:
            continue

        if p.suffix not in {".ipynb", ".py"}:
            continue

        if p.suffix == ".py" and not (is_notebook_py(p) or p.with_suffix(".ipynb").exists()):
            continue

        uniq[str(p)] = p

    return list(uniq.values())


def sync_one(p: Path) -> Path | None:
    subprocess.run(["jupytext", "--set-formats", "ipynb,py:percent", rel(p)], cwd=REPO_ROOT, check=True)
    subprocess.run(["jupytext", "--sync", rel(p)], cwd=REPO_ROOT, check=True)

    py = p.with_suffix(".py") if p.suffix == ".ipynb" else p
    return py if py.exists() else None


def stage(paths: list[Path]) -> None:
    files = sorted({rel(p) for p in paths if p.exists()})
    if files:
        subprocess.run(["git", "add", *files], cwd=REPO_ROOT, check=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--staged", action="store_true")
    ap.add_argument("--stage-updated", action="store_true")
    args = ap.parse_args()

    inputs: list[Path] = []
    if args.staged:
        inputs.extend(staged_files())
    if args.all:
        inputs.extend(all_targets())
    if args.paths:
        inputs.extend([(REPO_ROOT / p).resolve() for p in args.paths])

    targets = normalize_targets(inputs)
    if not targets:
        return 0

    updated_py = []
    for t in sorted(targets):
        try:
            p = sync_one(t)
            if p is not None:
                updated_py.append(p)
        except subprocess.CalledProcessError as e:
            sys.stderr.write((e.stderr or "") + "\n")
            return e.returncode

    if args.stage_updated:
        stage(updated_py)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

代码解释（按功能块）：

1. `REPO_ROOT` 和 `NOTEBOOK_ROOT`：统一路径基准，保证脚本在任意目录调用都稳定。
2. `run()`：封装子进程执行，统一 `check=True`，出错时及时失败。
3. `is_notebook_py()`：判断 `.py` 是否为 notebook 脚本（通过 `# %%` 或 jupytext 头信息）。
4. `staged_files()`：读取当前暂存区文件，用于增量同步模式（`--staged`）。
5. `all_targets()`：扫描 `notebooks/` 下所有可能要同步的 `.ipynb/.py`。
6. `normalize_targets()`：过滤无效路径、去重、限制目录范围，避免误处理非 notebook 代码。
7. `sync_one()`：核心同步逻辑。先 `--set-formats` 再 `--sync`，确保配对关系正确。
8. `stage()`：把同步更新后的 `.py` 自动 `git add`，防止提交遗漏。
9. `main()`：解析参数并调度三种工作模式：`--all`、`--staged`、指定路径。
10. 异常处理：捕获 `CalledProcessError` 并返回非 0，方便在 hooks/CI 中失败即中断。

给执行权限：

```bash
chmod +x tools/jupytext_sync.py
```

代码解释：

1. 给脚本添加可执行位，后续可直接被 hook 调用。
2. 不加可执行位时，部分环境会报 `Permission denied`。

## 6. Git hooks 自动同步

### 6.1 新建 `.githooks/pre-commit`

```bash
#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

python3 tools/jupytext_sync.py --all --stage-updated
```

代码解释：

1. `set -euo pipefail`：脚本严格模式，任何错误立即中止提交。
2. `git rev-parse --show-toplevel`：确保在仓库根目录执行。
3. `--all --stage-updated`：提交前全量同步，并把更新后的 `.py` 自动加入暂存区。

### 6.2 新建 `.githooks/post-merge`

```bash
#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

python3 tools/jupytext_sync.py --all >/dev/null 2>&1 || true
```

代码解释：

1. `post-merge` 在 `git pull` 后触发，保证拉取后 notebook 配对即时更新。
2. `>/dev/null 2>&1`：隐藏噪声输出，避免干扰日常 pull。
3. `|| true`：即使同步失败也不阻断 merge 完成（避免仓库状态被 hook 卡死）。

### 6.3 新建 `.githooks/post-checkout`

```bash
#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

python3 tools/jupytext_sync.py --all >/dev/null 2>&1 || true
```

代码解释：

1. 切换分支后自动同步，避免“分支 A/B 的 notebook 配对状态不一致”。
2. 其余逻辑与 `post-merge` 相同：静默执行且不阻断 checkout。

### 6.4 新建 `.githooks/post-rewrite`

```bash
#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

python3 tools/jupytext_sync.py --all >/dev/null 2>&1 || true
```

代码解释：

1. `post-rewrite` 覆盖 `rebase`、`commit --amend` 等历史重写场景。
2. 历史重写后立即同步可避免“旧 `.py` 与新 `.ipynb` 错位”。

### 6.5 启用 hooks

```bash
chmod +x .githooks/pre-commit .githooks/post-merge .githooks/post-checkout .githooks/post-rewrite
git config core.hooksPath .githooks
```

代码解释：

1. 第一行给所有 hook 增加执行权限。
2. 第二行告诉 Git 使用仓库内 `.githooks`，而不是默认 `.git/hooks`。

校验是否生效：

```bash
git config --get core.hooksPath
```

代码解释：

1. 该命令读取当前仓库 hook 目录配置。
2. 如果输出不是 `.githooks`，说明 hooks 尚未启用。

输出应为：

```text
.githooks
```

代码解释：

1. 这是预期值，表示后续 commit/pull/checkout 会触发你定义的脚本。

## 7. 迁移已有仓库（重点）

假设你的仓库中已有大量 `.ipynb` 被追踪。

### 7.1 先为已有 notebook 生成 `.py`

```bash
python3 tools/jupytext_sync.py --all
```

代码解释：

1. 扫描 `notebooks/` 下所有目标并生成或更新配对 `.py`。
2. 这是迁移第一步，保证后续取消追踪 `.ipynb` 时不会丢可读源码。

### 7.2 取消 Git 对 `.ipynb` 的追踪（保留本地文件）

```bash
git ls-files '*.ipynb' | xargs -r git rm --cached
```

代码解释：

1. `git ls-files '*.ipynb'`：列出当前“已追踪”的 notebook。
2. `git rm --cached`：仅从索引删除，不删除工作区文件。
3. `xargs -r`：当列表为空时不执行命令，避免空参数报错。

### 7.3 添加新文件并提交

```bash
git add .jupytext.toml .githooks tools/jupytext_sync.py
git add notebooks/**/*.py
git commit -m "migrate notebooks to jupytext py tracking"
```

代码解释：

1. 第一行提交配置与自动化脚本。
2. 第二行提交 notebook 对应 `.py`，作为后续唯一追踪对象。
3. 第三行形成迁移基线提交，便于回溯与团队同步。

## 8. 日常工作流

### 8.1 普通开发

1. 你可以继续用 JupyterLab 编辑 `.ipynb`。
2. 也可以直接编辑 `.py`（更利于重构和 review）。
3. `git commit` 前，hook 会自动同步并把更新后的 `.py` 重新入暂存区。

### 8.2 从远端更新后

1. `git pull`、`git checkout` 后会触发同步。
2. 如果你仍看到不同步，手动运行：

```bash
python3 tools/jupytext_sync.py --all
```

代码解释：

1. 这是“手动兜底”的全量同步命令。
2. 适合在 hook 未启用、CI 复现、或怀疑本地状态脏时执行。

## 9. 新下载 `.py` 如何生成 `.ipynb`

### 9.1 单文件生成

```bash
python3 tools/jupytext_sync.py notebooks/xxx/downloaded.py
```

代码解释：

1. 传入单个 `.py` 路径时，脚本只处理该文件。
2. 如果该文件符合 notebook 识别规则，会自动生成配对 `.ipynb`。

### 9.2 推荐写法

下载或新建的 `.py` 建议使用 `# %%` 分块，例如：

```python
# %%
import numpy as np

# %%
x = np.linspace(0, 1, 100)
```

代码解释：

1. `# %%` 是 jupytext/jupyter 常用 cell 分隔标记。
2. 转回 notebook 后，每个 `# %%` 会成为独立代码单元。

这样转回 notebook 后，单元结构清晰。

## 10. 团队协作与 CI 建议

### 10.1 团队要求（每位开发者一次性执行）

```bash
git config core.hooksPath .githooks
```

代码解释：

1. 这是“每位成员本地初始化”的关键步骤。
2. 不执行这条命令，仓库内 hooks 文件不会被 Git 自动使用。

### 10.2 CI 一致性检查

在 CI 中加入：

```bash
python3 tools/jupytext_sync.py --all
git diff --exit-code
```

代码解释：

1. 第一行强制在 CI 环境做一次全量同步。
2. 第二行检查同步后是否有未提交改动。
3. 若有改动，返回非 0，让 CI 失败，提醒开发者提交同步结果。

### 10.3 大仓库性能优化

如果 notebook 很多、提交较慢，可把 `pre-commit` 从：

```bash
python3 tools/jupytext_sync.py --all --stage-updated
```

改为：

```bash
python3 tools/jupytext_sync.py --staged --stage-updated
```

代码解释：

1. `--all`：全仓扫描，稳定但慢。
2. `--staged`：只处理当前暂存相关文件，提交速度更快。
3. 适合 notebook 数量多、单次 commit 变更范围小的项目。

## 11. 常见问题（FAQ）

### 11.1 `.py` 没被识别为 notebook 脚本

排查：

1. 文件是否在 `NOTEBOOK_ROOT` 指定目录下。
2. 文件中是否包含 `# %%` 或 jupytext 头信息。
3. 是否存在同名 `.ipynb`。

### 11.2 commit 后 `.py` 又变化了

这是预期行为：pre-commit 在同步后把 `.py` 规范化。再次执行 `git commit` 即可。

### 11.3 为什么不是直接删除 `.ipynb`

1. `.ipynb` 仍是 notebook 前端的主要编辑载体。
2. 我们做的是“不追踪”而不是“不存在”。
3. 本地仍保留 `.ipynb`，只是 Git 历史中只存 `.py`。

## 12. 一键初始化（可复制）

下面是一组最小命令（假设你已创建配置文件、脚本、hooks）：

```bash
python3 -m pip install jupytext
chmod +x tools/jupytext_sync.py
chmod +x .githooks/pre-commit .githooks/post-merge .githooks/post-checkout .githooks/post-rewrite
git config core.hooksPath .githooks
python3 tools/jupytext_sync.py --all
git ls-files '*.ipynb' | xargs -r git rm --cached
git add .jupytext.toml .githooks tools/jupytext_sync.py notebooks/**/*.py
git commit -m "migrate notebooks to jupytext py tracking"
```

代码解释：

1. 前三行完成安装与可执行权限。
2. `core.hooksPath` 让 Git 使用仓库内 hooks。
3. `--all` 同步历史 notebook。
4. `git rm --cached` 取消 `.ipynb` 追踪但不删本地文件。
5. 最后 `git add + commit` 固化迁移结果。

## 13. 迁移后的验收清单

提交前建议检查：

1. `git ls-files '*.ipynb'` 输出为空。
2. notebook 对应 `.py` 已纳入版本管理。
3. `git config --get core.hooksPath` 为 `.githooks`。
4. 手动执行 `python3 tools/jupytext_sync.py --all` 后 `git diff` 为空。

可直接执行：

```bash
git ls-files '*.ipynb'
git config --get core.hooksPath
python3 tools/jupytext_sync.py --all
git diff --name-only
```

代码解释：

1. 第 1 行验证是否仍有 `.ipynb` 被追踪。
2. 第 2 行验证 hooks 配置是否正确。
3. 第 3 行做一次全量同步自检。
4. 第 4 行确认同步后是否仍有未预期改动。

完成以上检查，说明这套工作流已稳定可用。
