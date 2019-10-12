---
layout: post
title: P4学习（一）
published: true
categories: P4 netowrk
tags: P4 network
---

## P4是什么

P4是数据面编程语言（data-plane programming language），面向网络芯片，是一种DSL(Domain Specific Language)语言。所以它与我们熟知的，在CPU上运行的，通用目的编程语言如C/C++不同。它的出现更像是一种顺势而为——因为有了SDN----面与数据面相分离的提出，有了openflow，即控制面的可编程性----然目前看，协议本身还没能让人满意，不能适应新协议----于是自然延伸到了数据面的可编程性问题上，P4由此应运而生。

openflow是使能SDN的关键协议，提供了一种与网络系统标准化的交互方式。它是一种平台无关的南向协议，但它其实还是依赖于协议的，即不是协议无关的，如果有新增协议的话，旧openflow就无法支持，你只能去寻找使用支持新协议的新版本openflow，局限性太大，对于只支持旧openflow的交换机来说是个困扰。

吸取了这一教训，P4提出来就是协议无关的，它主要想实现的是协议无关的数据面编程。也被称为openflow2.0，被认为是SDN的未来（P4也提出了类似于openflow的南向协议，我还没有去了解）。其实可编程芯片已经存在蛮久的，不过之前都是各自为战，难以统一阵线，所以P4的出世被普遍看好。不过最终结果如何，还得看各方博弈与发展，这个不表，咱还是学会P4。以后即使有P5、P6等其他语言，也会很快能过渡过去。

扯了这么多，啥是P4？P4是Programming Protocol-Independent Packet Processors的缩写，即4个P。

## P4使用与语法

作为一门DSL语言，P4有其特有的使用方式与规范，最详细的当然是看官方的spec，最新的是P4_16。其中16指的是2016年起草的版本，目前规范都是以年份命名的。先前一份标准是2014年定稿的，称为P4_14。初步看，14与16的语言差异还是蛮大的，这个后续可以对比看看。

P4是面向数据面的，用于处理网络数据包。数据包在各种不同的转发设备中处理大体上差不多。

### P4编程模型

我们以P4 github库提到的V1Model体系结构为例，主要包括五部分(从左至右)：

1. Parser：解析器，主要是解析报文的头部。

2. Ingress：入口处理，主要一堆match-action单元处理。

3. TM: traffic manager，报文队列，流量控制等，调度相关。这部分是目前不可编程的（是的，P4也不能为所欲为，后续看是否会支持编程）。

4. Engress：出口处理，也是一堆match-action处理，Ingress/Engress即是pipeline，流水线处理（类比工厂流水线）。

5. Deparser：反解析器，如其名，这里是把报文再重新组合起来（因为前面被parse了），用于后续处理（转发啊丢弃等等）。

   ![V1Model](../images/posts/P4/v1Model.png)

Barefoot公司推出的Tofino芯片的体系结构与上述模型大同小异。可以看出，这与我们的通用编程语言差距较大，毕竟它是有自己专属的应用环境。所以当你进入P4的世界，就要抛开CPU语言那一套东东了。

不过P4还有一个特点，那就是“一次编写，到处编译”，达到适配不同设备的目的。这与C语言相像（不过其实不同设备可能有其特有的约束条件等因素影响，比如architecture，P4代码可能还是得做微调）。

### 语法

P4语法类C，所以有C语言基础的话，还是比较容易看懂的。P4_16语言主要代码结构如下：

```p4
/*include头文件*/

/*数据格式定义部分*/
header ethernet_t{
    bit<48> dst_addr;  //根据各个字段的长度等信息，定义各种数据包头。
    bit<48> src_addr;
    bit<16> ether_type;
}
//.....其他包头格式和 metadata格式定义
 
/*Parser部分*/
parser MyParser(packet_in packet,
                out headers hdr) {
	/* */
}
 
/*Ingress 处理*/
control MyIngress(inout headers hdr) {
/* 定义match-action */
}
 
/*与Ingress处理过程类似*/
control MyEgress(inout headers hdr) {
    apply {  }
}

/*Deparser 数据包重组*/
control MyDeparser(packet_out packet, in headers hdr) {
    apply {
        packet.emit(hdr.ethernet);
        packet.emit(hdr.ipv4);
        // other emit
    }
}
 
/*将上述代码中定义的各个模块组装起来，有点像C/C++中的main函数*/
V1Switch(
MyParser(),
MyIngress(),
MyEgress(),
MyDeparser()
) main;

```

可以看到，语法、逻辑都还是比较清晰；而且如果理解了其编程模型，那么其语义也是相对简单的。主要是根据前面提到的体系结构来写。

## P4版本与使用环境

上面有提到，P4语言现在有两个版本，语法上还是有蛮多差异的。由于一开始我学习了16版本，结果后续项目上说要使用14的版本，所以之后可能两个版本都会提及。

由于我目前不是在开源的P4环境上做开发，所以也没有其安装使用经验，可以参考[这篇文章](https://takeshi.tw/架設-p4-模擬開發環境/)来搭建环境，看上去还是比较简单的。

后续想要记录复习下自己学习的P4内容，主要还是以官方spec来展开。

## 参考文献

1. [P4_tutorial](https://docs.google.com/presentation/d/1zliBqsS8IOD4nQUboRRmF_19poeLLDLadD5zLzrTkVc/edit#slide=id.g37fca2850e_6_155)
2. [P4编程理论与实践——理论篇](https://www.sdnlab.com/22466.html)
3. [P4编程理论与实践（2）—快速上手](https://www.sdnlab.com/22512.html)
4. [P4-16-v1.1.0-spec.pdf](https://p4.org/p4-spec/docs/P4-16-v1.1.0-spec.pdf)

