# 历史：前进、后退与分叉

> 历史是一组状态，加上从一个状态走到另一个状态的规则。

## 一、先分清三种历史

- **导航历史**：去过哪里？——浏览器页面、终端目录、编辑器光标位置。
- **修改历史**：做过什么？——编辑器 Undo/Redo。
- **版本历史**：哪些状态被保留下来？——Vim undo tree、Git commits。

三者能共存，但得分清。**返回旧位置不等于撤销修改。**

## 二、所有分叉，只有三种基本处置

起初 `A → B → C → D`；后退到 `B`，再进入 `E`：

```text
原历史： A ─ B ─ C ─ D
             ↑
          回到 B

① 截断： A ─ B ─ E          （C、D 失去前进入口）

② 保留： A ─ B ┬─ C ─ D    （旧分支仍可选择）
                └─ E

③ 重排： [E, B, D, C, A]     （只记目录集合的次序）
```

**截断、保留、重排**，对应不同的数据结构与用户预期。

## 三、数据结构就是行为

| 机制 | 内部模型 | 后退后产生新动作 | 典型实例 |
|---|---|---|---|
| 目录栈 | 栈／旋转列表 | 旧项保留，位置重排 | Zsh `cd -N`（需相应选项） |
| 导航历史 | 数组 + 游标 | 通常截断未来 | 浏览器、Oh My Zsh `dirhistory` |
| 常规撤销 | Undo 栈 + Redo 栈 | 清空 Redo | 许多编辑器的 Undo/Redo |
| 撤销树 | 带父子关系的修改节点 | 旧分支保留 | Vim / Neovim undo tree |
| 版本图 | 提交节点 + 父指针（DAG） | 显式分支，允许合并 | Git |

### 线性历史：游标走，数据不动

```text
history = [A, B, C, D]
index   = 3

back():    index = max(0, index - 1)
forward(): index = min(len(history)-1, index + 1)

visit(E):
    history = history[:index+1] + [E]
    index += 1
```

两次 `back()` 后，`index = 1`（B）；`visit(E)` 得到 `[A, B, E]`。**前进只是移动指针；新访问才截断未来。**

### 常规 Undo/Redo：两个栈

一次编辑是一个**可撤销事务**（一次插入、粘贴或一组连续输入），不是单个字符。

```text
edit(op):  执行 op；记录其逆操作／前后状态；清空 redo
undo():    撤销最近事务，并把它移入 redo
redo():    重做 redo 中最近撤销的事务
```

实现可保存**快照**，也可保存**增量／逆操作**；事务合并、容量限制和落盘策略决定内存开销与持久性。

### 撤销树：过去会分叉

撤销到 B 再修改为 E，树保留两路：

```text
A ─ B ┬─ C ─ D
      └─ E   ← 当前
```

普通 `undo/redo` 不会自动跳到另一条分支，要找回旧分支得手动导航。Vim 用 `:undolist` 查看分支叶子，`:undo {N}` 按修改编号跳转，`g-` / `g+` 按修改时间穿行。**Redo 只认当前分支。**

Git 更进一步：提交保存父提交引用；分支名是可移动的引用；合并提交可有多个父节点，因而形成**有向无环图**，不再只是树。

## 四、编辑器至少有两本账

| 要问的问题 | Vim / Neovim |
|---|---|
| “我刚才改了什么？” | `u` / `Ctrl-R`：撤销／重做内容 |
| “我曾经改到哪里？” | `g;` / `g,`：修改位置列表（changelist） |
| “我刚才跳到哪里？” | `Ctrl-O` / `Ctrl-I`：跳转位置列表（jumplist） |
| “撤销后另改的旧版本在哪？” | `:undolist`、`:undo {N}`、`g-` / `g+` |

**位置历史 ≠ 内容历史。** Vim 的 jumplist 默认会追加新的跳转；设置 `jumpoptions=stack` 时，才按类似浏览器的方式丢弃当前位置后的跳转项。它与 undo tree 是两套独立机制。

## 五、一句设计原则

- 只要“返回上一步”——**栈**。
- 要有“后退／前进”——**线性历史 + 游标**，或**双栈**。
- 要让“撤销后另改”的两个未来都存在——**树**。
- 要让分支重新汇合——**DAG**。

**分叉很正常：它就是线性历史选择不保存的那部分。**

---

*参阅：[Zsh Directory Stacks](https://zsh.sourceforge.io/Intro/intro_6.html) · [MDN History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API/Working_with_the_History_API) · [Vim Undo](https://vimhelp.org/undo.txt.html) · [Vim Jumps](https://vimhelp.org/motion.txt.html) · [Git User Manual](https://www.kernel.org/pub/software/scm/git/docs/user-manual.html)*
