---
layout: post
title:【TIPS】git操作若干
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

