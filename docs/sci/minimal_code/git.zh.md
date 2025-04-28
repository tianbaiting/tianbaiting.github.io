# git




## git 工作流


[十分钟学会正确的github工作流，和开源作者们使用同一套流程](https://www.bilibili.com/video/BV19e4y1q7JJ/?share_source=copy_web&vd_source=727ffe1727e24c229169af42b43aa2e0)


### rebase 方法

1. git clone // 到本地
2. git checkout -b xxx 切换至新分支xxx
（相当于复制了remote的仓库到本地的xxx分支上
4. git diff 查看自己对代码做出的改变
5. git add 上传更新后的代码至暂存区
6. git commit 可以将暂存区里更新后的代码更新到本地git
7. git push origin xxx 将本地的xxxgit分支上传至github上的git
-----------------------------------------------------------
（如果在写自己的代码过程中发现远端GitHub上代码出现改变）
1. git checkout main 切换回main分支
2. git pull origin master(main) 将远端修改过的代码再更新到本地
3. git checkout xxx 回到xxx分支
4. git rebase main 我在xxx分支上，先把main移过来，然后根据我的commit来修改成新的内容
（中途可能会出现，rebase conflict -----》手动选择保留哪段代码）
5. git push -f origin xxx 把rebase后并且更新过的代码再push到远端github上
（-f 强行）
1. 原项目主人采用pull request 中的 squash and merge 合并所有不同的commit

### merge 方法

1. git clone // 到本地
2. git checkout -b xxx 切换至新分支 xxx
3. 在 xxx 分支上进行代码修改
4. git add 将修改的代码添加到暂存区
5. git commit 提交修改到本地仓库
6. git push origin xxx 将本地 xxx 分支推送到远程仓库
-----------------------------------------------------------
（如果在写自己的代码过程中发现远端 GitHub 上代码出现改变）
1. git checkout main 切换回 main 分支
2. git pull origin main 将远端修改过的代码更新到本地
3. git checkout xxx 回到 xxx 分支
4. git merge main 将 main 分支的最新代码合并到 xxx 分支
（如果出现 merge conflict -----》手动解决冲突并保存）
5. git push origin xxx 将合并后的代码推送到远程仓库
6. 提交 Pull Request，等待项目维护者审核并合并

