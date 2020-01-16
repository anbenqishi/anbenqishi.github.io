---
layout: post
title: python源码学习（一）--环境搭建
published: true
categories: python
tags: python
---

主要是是对《Python源码剖析》这本书的学习，之前学了一半，耽搁放下了，这次重拾起来希望督促自己学完。

## 环境

windows 7 professional 64bit

python2.5源码（按书上的）

编译环境：VS2005（可以在win7上安装，需要安装相应的补丁；vs2003貌似不行了）

## 问题

### 编译问题

1. config.obj : error LNK2001: 无法解析的外部符号 _init_types

   找不到符号定义，搜索这个符号，没找到；去掉前置的“_”再次搜索，找到了相关的函数定义，但是它是定义为static的本地函数。去掉static即可（奇怪，原来的源码竟然编译不过？？）。

2. LINK : fatal error LNK1104: 无法打开文件“python25_d.lib”

   搜索了下，在编译的目录下，生成的是`python25_d.dll`动态库，而提示是想要静态库，所以需要修改一下。看了一下，主要修改pythoncore项目为生成静态库即可（原为动态库）。如下图所示：

   ![1571279372753](python%E6%BA%90%E7%A0%81%E5%AD%A6%E4%B9%A0%EF%BC%88%E4%B8%80%EF%BC%89.assets/1571279372753.png)

ok，编译过，生成了`python.exe`并正常运行（但其实这个运行应该是链接了`python.dll`的缘故，前面已经生成，只是后面再编译了一次`python.lib`而已，lib只是定义了符号而已，真正的实现都在dll中）。

再试验了下，其实应该是先编译`pythoncore`（会生成lib和dll），再编译`python`就能正常编译链接通过了，不需要我去改项目属性的。整个solution的启动项可以指定为`pythoncore`即可。`python`只是简单生成一个exe文件而已。后续的修改源码动作基本都在`pythoncore`中进行。

