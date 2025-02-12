---
layout: post
title: 【TIPS】C++函数模板实例化问题
published: true
categories: C++ ARTS
tags: C++ ARTS
---

### 问题

库里面定义了一个函数模板，项目中使用这个模板函数，结果编译不过，提示找不到定义。仔细看了库代码，有显式实例化部分函数。而刚好我使用的是另一个未显式实例化的模板类型。直接在文件中显式声明即可顺利编过。

问题是：既然已经提供模板了，我干嘛还要显式实例化一次，我又没有特定的，有别于模板的实现。

### 原因

在一个[知乎](https://www.zhihu.com/question/25312471)的问答中找到原因：

> 这样的话是编译不通过的，在a.cpp编译时不会有实例函数生成，而main.cpp也不会有实例函数生成，执行时会出现链接错，
> 这样就必须在a.cpp中显式实例化，所以C++中模板函数（类）的调用与定义分离时，需要使用显式实例化

我自己要去实验了一下这个简单的例子，确实如此。在这种情况下，需要显式实例化。

补充：https://stackoverflow.com/questions/2351148/explicit-template-instantiation-when-is-it-used

参考：https://docs.microsoft.com/en-us/cpp/cpp/explicit-instantiation
