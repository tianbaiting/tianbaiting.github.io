# `ctags` 使用教程（C/C++）

本文给出一套可落地的 `ctags` 用法，适合中大型 C/C++ 项目；最后附录补充 `clangd` 的最小可用配置。

## 1. `ctags` 是什么

`ctags` 会扫描源码并生成一个符号索引文件（通常叫 `tags` 或 `.tags`）。
编辑器根据这个索引实现“按符号跳转到定义”。

核心特点：

- 快：生成和查询都很快。
- 轻：不依赖完整编译。
- 限制：不是完整语义分析，复杂宏/模板场景精度不如 `clangd`。

推荐策略：

- `clangd` 负责语义（诊断、补全、精确跳转）。
- `ctags` 负责快速兜底导航。

## 2. 安装

### Debian/Ubuntu

```bash
sudo apt update
sudo apt install -y universal-ctags
```

校验：

```bash
ctags --version
readtags --help | head -n 3
```

### Micromamba（可选）

```bash
micromamba install -n <env-name> -c conda-forge universal-ctags
micromamba activate <env-name>
```

## 3. 在项目中生成标签

在项目根目录执行：

```bash
ctags -R --languages=C,C++ --fields=+iaS --extras=+q \
  --exclude=.git --exclude=build --exclude=bin --exclude=.cache \
  -f .tags
```

说明：

- `-R`：递归扫描。
- `--languages=C,C++`：只处理 C/C++。
- `--fields=+iaS`：附加更多可用信息（继承、访问属性、签名等）。
- `--extras=+q`：增强查询能力。
- `-f .tags`：把索引写到项目根目录的 `.tags`。

验证：

```bash
ls -lh .tags
wc -l .tags
```

## 4. 查询符号

使用 `readtags` 直接查：

```bash
readtags -t .tags -e -n EventProcessor
readtags -t .tags -e -n SimDataManager
```

常用参数：

- `-t .tags`：指定标签文件。
- `-e`：显示扩展字段。
- `-n`：显示行号。

## 5. 在 Neovim/Vim 中使用

在配置中加入：

```vim
set tags=./.tags;,./tags;,tags;
```

常用命令：

```vim
:tag SymbolName
:tnext
:tprev
```

快捷键：

- `Ctrl-]`：跳到符号定义。
- `Ctrl-t`：返回。

## 6. 在 VSCode 中使用 `ctags`

VSCode 本身不原生依赖 `ctags`，通常通过扩展使用。
可在扩展市场安装 `ctags` 类插件（如 `vscode-ctags`）。

最实用做法：

1. 把 `.tags` 放在项目根目录。
2. 修改代码后重新生成 `.tags`。
3. 把跳转主路径交给 `clangd`，`ctags` 作为兜底。

## 7. 自动刷新建议

可以在项目里放一个脚本，例如 `scripts/dev/update_tags.sh`：

```bash
#!/usr/bin/env bash
set -euo pipefail

ctags -R --languages=C,C++ --fields=+iaS --extras=+q \
  --exclude=.git --exclude=build --exclude=bin --exclude=.cache \
  -f .tags

echo "updated .tags"
```

然后：

```bash
chmod +x scripts/dev/update_tags.sh
./scripts/dev/update_tags.sh
```

## 8. 常见问题

### Q1: 为什么跳转不准？

`ctags` 是基于文本解析，不是完整语义分析。复杂宏、模板特化、条件编译下，结果可能偏差。

### Q2: 为什么找不到某些符号？

通常是这些原因：

- 标签文件过期。
- 扫描范围被 `--exclude` 排除了。
- 符号在未被扫描的生成目录或外部依赖中。

---

## 附录 A：`clangd` 最小使用说明

`clangd` 是 C/C++ 语言服务器，依赖 `compile_commands.json` 提供精确语义。

### A.1 安装

```bash
sudo apt install -y clangd
# 或
micromamba install -n <env-name> -c conda-forge clang-tools
```

校验：

```bash
clangd --version
```

### A.2 生成编译数据库

以 CMake 为例：

```bash
mkdir -p build
cd build
cmake .. -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
```

会生成 `build/compile_commands.json`。

### A.3 `.clangd` 示例

如果你把数据库放在 `clangd_db/compile_commands.json`，项目根目录可放：

```yaml
CompileFlags:
  CompilationDatabase: clangd_db
```

### A.4 VSCode 使用 `clangd`

`settings.json` 示例：

```json
{
  "clangd.path": "/usr/bin/clangd",
  "clangd.arguments": [
    "--compile-commands-dir=clangd_db",
    "--background-index"
  ],
  "C_Cpp.intelliSenseEngine": "Disabled"
}
```

说明：

- 若同时启用 `cpptools` 的 IntelliSense 与 `clangd`，可能出现重复诊断。
- 建议保留一个语义引擎（通常选 `clangd`）。

### A.5 Neovim 使用 `clangd`

`lspconfig` 最小示例：

```lua
local lspconfig = require("lspconfig")
local util = require("lspconfig.util")

lspconfig.clangd.setup({
  cmd = {
    "clangd",
    "--background-index",
    "--compile-commands-dir=clangd_db",
  },
  root_dir = util.root_pattern(".clangd", "compile_commands.json", ".git"),
})
```

### A.6 `clangd` 与 `ctags` 关系

两者不冲突，推荐并用：

- 主导航/诊断：`clangd`
- 快速兜底跳转：`ctags`

