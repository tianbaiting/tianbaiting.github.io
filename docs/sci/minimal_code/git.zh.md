# Git

## Git 的核心思想

git 的命令很脏，但是它内部的思想非常干净。

所以不能死记硬背命令。


Git 是一个内容寻址的文件系统，其上层是一个由 Commit 对象构成的有向无环图（DAG），而我们日常使用的“分支”等概念，只不过是操作这个图的便捷指针。 可以想象成每个分支都是一个指向某个提交的指针，而这个提交又可以追溯到更早的提交，形成一条历史链。提交其实也是一个指针，指向一个树对象（Tree），而树对象则指向具体的文件（Blob）。 这种设计使得 Git 能够高效地存储和管理代码的历史版本，同时也支持强大的分支和合并操作。

### Git 的核心对象

在 Git 的世界里，一切皆对象。主要有三种核心对象类型，它们是构成历史图谱的基本节点：

1. **Blob (Binary Large Object)**: 存储文件内容的快照，不包含文件名等元数据。
2. **Tree**: 类似于文件夹，存储文件名、类型（文件或子目录）及其对应的 Blob 或子 Tree 的引用。Tree 对象构建了文件系统的层次结构。
3. **Commit**: 代表一次提交，包含指向一个 Tree 对象的引用（表示该提交时的文件状态）、作者信息、提交信息以及指向父 Commit 的引用（支持多父以实现合并）。

### Git 的指针

1. **分支 (Branch)**: 可移动的指针，指向图中的某个 Commit 节点。当你创建一个新的 Commit 时，你所在分支的指针会自动向前移动到这个新的 Commit 上。这就是为什么创建和切换分支如此之快的原因——Git 只是在修改一个指向40位哈希值的小文件。
2. **标签 (Tag)**: 基本不可移动的指针，通常用于标记重要里程碑。，如版本发布（v1.0）。
3. **HEAD**:  一个特殊的指针的指针。它通常指向你当前所在的分支。例如，当你在 main 分支上工作时，HEAD 会指向 main，且 main 再指向最新的 commit。HEAD 决定下一次提交的父节点，也决定工作目录应处于哪个快照状态。

## Git 命令的本质（图的操作）

理解了上述模型后，我们就可以用“图操作”的视角来重新解读那些令人困惑的命令了。

### 创建新节点

**`git commit`**: 在历史图谱中创建一个新的 Commit 节点。  
流程：
- 根据暂存区创建 Tree 对象。
- 创建 Commit 对象，指向 Tree，并将父指针指向当前 HEAD。
- 将 HEAD 所指向的分支指针移动到新 Commit。

### 移动与修改指针

1. **`git reset <commit>`**: 强制移动当前分支（如 main）的指针。这是最纯粹的指针操作命令。

   - `--soft`: 只移动 main 分支的指针到指定的 <commit>，工作目录和暂存区保持不变。
   - `--mixed`（默认）:移动指针，并用该 <commit> 的内容重置暂存区，工作目录保持不变。
   - `--hard`: 三位一体的重置，移动指针，并用该 <commit> 的内容同时覆盖暂存区和工作目录；这是一个危险操作，可能会丢失工作目录的修改。

<commit> 可以是分支名（如 main）、标签名（如 v1.0）、HEAD~n（表示当前 HEAD 的第 n 个祖先），hash值

2. **`git revert <commit>`**: 创建一个反向操作的新 Commit，而不是移动指针。

3. **`git checkout` / `git switch`**: 本质: 移动 HEAD 指针。
   - `git switch <branch>`: 将 HEAD 指针从指向当前分支，改为指向另一个分支。
   - `git checkout <commit>`: 让 HEAD 直接指向一个具体的 Commit 节点，而不是一个分支。这会使你进入 "detached HEAD"（分离头指针）状态。
  

git branch -f <branch> <commit>: 强制将某个分支指针移动到指定的 Commit。

git checkout <commit>


### 重写历史

**`git rebase`**: 复制一系列节点并嫁接到另一个位置。  
注意：会改变历史，谨慎在共享分支上使用。



## Reflog: 终极安全网

Reflog 记录了 HEAD 指针的移动轨迹。即使节点从分支上“消失”，也可以通过 Reflog 找回。



## Git 工作流

### Rebase 方法

1. `git clone` 克隆仓库。
2. `git checkout -b your-branch` 创建并切换到新分支。
3. 修改代码并使用 `git add` 和 `git commit` 提交。
4. `git push origin your-branch` 推送到远程分支。

**处理远程更新**:
1. 切换到 `main` 分支并 `git pull` 更新。
2. 切换回工作分支并 `git rebase main`。
3. 解决冲突后 `git push -f origin your-branch`。

### Merge 方法

1. `git clone` 克隆仓库。
2. `git checkout -b xxx` 创建并切换到新分支。
3. 修改代码并提交。
4. `git push origin xxx` 推送到远程分支。

**处理远程更新**:
1. 切换到 `main` 分支并 `git pull` 更新。
2. 切换回工作分支并 `git merge main`。
3. 解决冲突后 `git push origin xxx`。


```shell
git push origin main:main
# git push <远程仓库别名> <本地分支名>:<远程分支名>
```
当远程和本地分支同名时，可以简写为 `git push origin main`。


什么是 Remote？ 它只是你本地 Git 仓库的另一个“副本”的别名（比如 origin）。


“日常侦察”：git diff
你的笔记里讲了如何“回滚”和“暂存”，但没有讲如何“查看”你到底改了什么。

git diff：查看变更

git diff：

比较对象：工作区 vs 暂存区 (Index)。

回答的问题：“我修改了哪些内容，但还未 git add？”

git diff --staged (或 --cached)：

比较对象：暂存区 (Index) vs HEAD (最后一次 Commit)。

回答的问题：“我 git add 了哪些内容，即将被提交？”

git diff HEAD：

比较对象：工作区 vs HEAD。

回答的问题：“我本地的所有修改（包括已 add 和未 add 的）和最后一次提交相比，有什么不同？”

git diff <commit1> <commit2>：

比较对象：两个任意 Commit 节点。

回答的问题：“从 commit1 到 commit2 之间，到底发生了什么变化？”

git diff main origin/main：

比较对象：本地 main 指针 vs origin/main 指针。

回答的问题：“我本地的 main 分支比远程 main 多了/少了哪些代码？”


### 平行开发

两条branch

特性分支 想要更新主分支的功能

git rebase master topic


merge


三条分支：

```
o---o---o---o master                             
    \
    o---o---o---o next           
                \
                0---o topic
```

git rebase --onto master next topic

```
o---o---o---o master                             
    |        \
    |           o'--o'--o' topic
    |
    o---o---o---o next           
            
```

cherry-pick 后面在讲。

git cherry-pick <commit-hash>：

本质：从一个分支上“复制”一个 Commit 节点（的变更内容），然后在你当前 HEAD 指向的分支上创建一个新的 Commit。

图操作：它会计算 <commit-hash> 相比其父节点引入了哪些变更（Diff），然后把这个变更应用到你当前的分支，并创建一个全新的 Commit 节点（会有新的 Hash 值）。

何时使用：

从 hotfix 分支拉取一个紧急修复到 main 分支，但又不想合并 hotfix 上的其他所有内容。

从一个已经废弃的特性分支上抢救一两个有用的 commit。


## 本地查看或还原到某个 commit

### 查看某个 commit 中的单个文件
```bash
git show <commit>:<file_path>
```
- 显示指定提交中某个文件的内容（不修改工作区）。

### 将本地所有文件回到某个 commit 的状态
```bash
git checkout <commit>
```
它会：
1. 移动 HEAD：HEAD 指向你指定的 <commit>（进入 detached HEAD 状态）。
2. 更新暂存区和工作区：使其内容与该 <commit> 一致（若与未提交修改冲突会报错以防丢失）。

注意：
- detached HEAD：你不在任何分支上，若在此基础上创建新 commit，除非创建分支，否则这些 commit 可能难以找回。
- 对工作区的影响：Git 会尽量保留与当前未提交修改不冲突的内容，冲突则阻止切换。
- 提交历史不会被修改；分支指针保持原位。

如何返回：
```bash
git checkout main   # 或 git checkout <your-branch>
```

提示：仅为“回顾历史”时，不建议使用 git reset（reset 会修改分支指针）。

---

## 临时保存：git stash

常用命令：
```bash
git stash push -m "message"   # 保存当前修改（推荐）
git stash list                # 列出所有 stash
git stash apply <stash@{n}>   # 应用某个 stash（不删除）
git stash pop                 # 应用最近的 stash 并从堆栈中删除
git stash drop <stash@{n}>    # 删除某个 stash
git stash clear               # 清空所有 stash
```

工作流示例：
1. 在当前分支保存未完成的修改：
   ```bash
   git stash push -m "WIP: 说明"
   ```
2. 切换到 main 修复 bug、提交：
   ```bash
   git checkout main
   # 修复并 commit
   ```
3. 回到原分支并恢复修改：
   ```bash
   git checkout feature-A
   git stash pop
   ```

说明：
- stash 会把已跟踪文件的修改（工作区 + 暂存区）打包到一个堆栈里，恢复后可继续开发。
- 使用 `apply` 可以先试用并保留堆栈项；`pop` 会在应用后删除该项。
- stash 只保存已跟踪文件的修改，未跟踪（untracked）和忽略（ignored）文件需额外参数保存（如 `--include-untracked`）。
- 若遇冲突，按常规冲突流程解决并提交。  
- 若需要把 stash 恢复为一个新分支：`git stash branch <new-branch> <stash@{n}>`。
- 
## 标记里程碑：git tag 的用法

简要说明：Tag 用于给某个 Commit 打上不会随开发移动的“里程碑”。

### 轻量标签（Lightweight Tag）
- 命令：
   ```bash
   git tag v1.0.0
   ```
- 本质：仅是指向某个 Commit 的不可移动指针（相当于某个 commit 的别名），不包含额外元数据。

### 附注标签（Annotated Tag，推荐）
- 命令：
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   ```
- 本质：完整的 Git 对象，包含作者、日期、说明信息，并指向一个 Commit，适合标记发布里程碑。
- 查看：`git show v1.0.0`

git tag -a v1.0 -m "Release version 1.0" a867b41

对指定 commit 提交打tag.


 常用操作

- 列出所有标签：
   ```bash
   git tag
   ```
- 推送单个标签到远程：
   ```bash
   git push origin v1.0.0
   ```
- 推送所有本地标签到远程：
   ```bash
   git push origin --tags
   ```
- 删除本地标签：
   ```bash
   git tag -d v1.0.0
   ```
- 删除远程标签：
   ```bash
   git push --delete origin v1.0.0
   ```

说明：Git 默认不会随 `git push` 推送本地标签，需显式推送。

## 附录


[Oh Shit, Git!?!](https://ohshitgit.com/zh): 一些常见问题及解决方法。

推荐 在线小游戏： [learn git branching](https://learngitbranching.js.org/?locale=zh_CN)
这个里面可以学到怎么把修改随意调整 分支如何随意调整。
