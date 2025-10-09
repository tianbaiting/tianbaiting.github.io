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


## 临时保存

使用 `git stash`:
- `git stash push`: 保存当前修改。
- `git stash pop`: 恢复保存的修改。
- `git stash list`: 查看保存的修改。

## 附录


[Oh Shit, Git!?!](https://ohshitgit.com/zh): 一些常见问题及解决方法。
