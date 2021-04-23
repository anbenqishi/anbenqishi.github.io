---
layout: post
title: 【TIPS】git操作若干
published: true
categories: ARTS git
tags: ARTS git
---

### 打patch

```bash
# 从某一个commit提交至今的记录打patch，可能生成多个patch
git format-patch [commit hash]
# 当前未commit的修订，可以直接生成patch
git patch > a.patch
# 应用patch前先check一遍是否可以正常打上
git apply --check a.patch
# 应用patch
git apply a.patch
```

同事遇到的问题，已经add了，但是还没有commit，此时想要做patch给其他同事评审，[stackoverflow](https://stackoverflow.com/questions/9810752/how-to-create-a-patch-without-commit-in-git)感觉比较靠谱的方案是：

```bash
# 先commit，反正本地不怕
git commit -a -m "specific message"
# 生成patch
git format-patch -s -n -1 HEAD
# 重置本地commit
git reset --soft HEAD~1
# 删除commit
git reset --hard HEAD~1
```

可以通过应用patch重新恢复自己的commit。这期间就不要push/pull骚操作了。

`git diff`貌似不靠谱，我试了，没生成一个有效的patch出来，哪里操作不当？

### 合并提交记录

场景：本地做了好几次commit，这时候想要push上去，先要pull最新记录，仓库上难免有更新，此时有两个要求：一是自己的commit记录应该当前master分支的最前面（我应该是最近一个push上去的），二是自己的commit记录综合成一条，否则太零散。

解决办法：如果当前的修订还未commit，这时候建议用stash：

```bash
git stash
# 等到pull完，再pop出来，此时可能有冲突，解决一下就好
git stash pop
```

第一个要求([参考1](https://juejin.im/post/5dcd457b518825109012c23b))：

```bash
# 如果本地已commit，但是尚未pull的情况
git pull --rebase
# 上述命令拆出来就是如下的命令的结合：
git fetch
git rebase FETCH_HEAD
# 如果有冲突，rebase会暂停，需要去解决冲突
git status # 查看Unmerged paths冲突部分
git add XXX # 冲突解决完添加进去
git rebase --continue # 继续rebase的过程
git rebase --abort # 如果冲突搞不定，中指回滚回去
```

如果本地已经commit，也已经pull了，这个自己的commit log会是在中间，即“远端log + 本地log + 旧的log”。这个时候想要把本地log提前有办法吗？@todo

第二个要求（[参考2](http://jartto.wang/2018/12/11/git-rebase/)）：

```bash
# 只能操作本地的commit，而不是远端
# 合并最近4次提交记录
git rebase -i HEAD~4
```

### 查看当前仓库的git配置

```bash
git config --list
```

### 改已经push上去的邮箱

同事碰到的问题，邮箱忘记改成公司邮箱，结果push上去的是私人邮箱，如何修改？

网上看到都是commit的修改，没有看到已经push上去后再修改的情况。根据[此UP主的说法](https://blog.sjfkai.com/2019/03/01/Git-修改-Commit-的用户名与邮箱/)：

> 修改 Commit 的用户名或邮箱会生成一个新的 commit 来替换之前的 commit 。如果在修改之前已经 push 到了远端，修改后再次 push 会出现冲突。 只能使用 `push -f`。 如果其他人已经拉取（ pull ）了旧 commit 会出现很多麻烦。

所以我们最后还是没改，不敢在主干代码上动手动脚，你都不知道哪个同事在此期间又提了代码，造成不必要的误操作。