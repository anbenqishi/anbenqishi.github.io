---
layout: post
title: P4学习（二）
published: true
categories: P4 netowrk
tags: P4 network
---

这里所指的P4都是指P4_16，即2016年版本的P4，鉴于P4_14版本有渐渐被取代之势，目前工作中也建议只维护16版本。如果部分描述，需要参考14版本更好理解，会提出来。

目前最新的P4_16版本是1.2.0，2019年10月23日出，可以从[官网](https://p4.org/p4-spec/docs/P4-16-v1.2.0.pdf)上下载得到。	

## 专有名词

架构Architecture：P4可编程组件的集合，以及他们之间的数据面接口。

控制面Control plane：一个算法类，有相应的输入和输出，针对数据面的部署和配置。

数据面data plane：一个算法类，描述了packet处理系统对packets的转换。

元数据metadata：P4程序执行过程中产生的中间数据。

数据包packet：一个网络包，是由包交换网络携带的格式化的数据单元。

包头packet header：在一个packet的起始位置，经过格式化的数据。对于一个给定的packet，可能包含一系列的包头，分别表示不同的网络协议。

包负载packet payload：包头之后的包数据。

包处理系统packet-processing system：一个数据处理系统，专门设计处理网络包。通常来说，都实现了控制面和数据面的算法。

目标target：可以执行P4程序的包处理系统。

***

以上名词之后都会涉及到。

## 语言的核心抽象思想

1. 包头类型（header types）定义了一个packet的header格式（字段集合以及大小）。
2. 解析器（Parsers）描述了当接收到一个包时，允许的headers序列，以及如何识别这些序列和从packet抽取出来的headers和fields。
3. 表（Tables）拥有用户自定义的key和action。P4 tables比传统的交换表更强大，可以用来实现路由表，ACL，以及其他用户自定义的表格，包括一些复杂的多变量决策等。
4. 动作（Actions）是一些代码片段，用来描述packet的header域和metadata是如何处理的。Actions包括数据，这些数据可以再运行时又控制面提供。
5. 匹配-动作单元（Match-Action Units, MAU）主要执行以下操作：
   1. 从packet的字段或或者metadata中构建用于查找的keys；
   2. 使用构建的key进行表的查找，选择一个action来执行，并最终执行这个action。
6. 控制流（control flow）是一个命令式的程序，描述在一个target上packet的处理过程。包括MAU的调用，Deparsing也可以在控制流中执行。
7. Extern的对象，是依赖于architecture的，可以通过APIs被P4程序所使用。但是其行为是内嵌的，并不是P4可编程的。
8. 用户自定义的metadata，是伴随每一个packet的数据结构（类似于通用编程语言中的临时变量用来传递数据的）。
9. 内置的metadata（intrinsic metadata），是由architecture提供的metadata，如每个packet进来时候的输入端口信息。

![image-20200309225754321](/Users/willpower/Documents/GitHub/anbenqishi.github.io/images/posts/P4/image-20200309225754321.png)

上图即是P4的开发工作流。P4是一门DSL语言，用于可编程的网络设备上。编译P4程序后会产生2个输出，一个是数据面配置，即由P4定义的转发逻辑；一个是API，控制面可以通过API来操作数据面对象状态。这里特别指出的是，如何debug P4程序呢？语言本身可没有提供什么打印、log机制，毕竟是转发面语言，所以一般是由定义architecture的产商提供软件模型来辅助P4的开发和debug。

P4语言目前有两个版本，P4_14和P4_16，最新的是16版本，对14做了大量的简化，只保留语言的核心。趋势是16替代14。目前P4_16的最新版本是1.2.0.注意到上图中的“extern objects”，extern关键字相当于用来引入库（类似于通用语言中的库概念）----一些额外的功能或由芯片产商提供的功能。一些14的功能被删除，在16中就是以库的形式体现的，如couters，meter等。原则上，你用P4语言书写的代码是可以跑在任意支持P4芯片上，而且行为不会有差异。但是如果你有基于某一特定architecture的代码，就很难一次编写到处运行，或者在不同architecture间是不可移植的。也就是标准库缺失。从目前的实践上看，如果没有architecture产商提供额外的功能，P4做的事还是即为有限。迫切有个功能强大的标准库（个人愚见哈哈），当前看，只有一个`core.p4`的核心库。

spec中提到标准architecture的问题，不过说这不是spec的范围。不过也没看到哪里有标准architecture的介绍。无非就两个吧，数据面的统一接口，还有extern的对象和函数。

