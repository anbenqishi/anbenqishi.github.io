---
layout: post
title: 最近工作的一点思考
published: true
tags: 随笔 总结
---

最近一周处理了一个ios-http代理引流方面的问题，从上周写完一点代码后，结果这周几乎都在联调测试改bug，好像一下子回到几年前刚开始工作有点懵懂打杂的状态了。突然有了危机感，好歹也工作好几年了，感觉是不是陷入了一种“工作一年，copy N年”的状态中了。反省一下：

1. 这个问题本身不是很难。一来代码我也是上周刚刚接触修订（相关代码之前有看过一点，但是移动端的还是有些许不同），对于整个流程逻辑总的说没有完全摸透，也没有人能指导，自己边看边改。这样造成了一个问题，在同事讨论中发现还有有些许逻辑流程遗漏的地方后来又补充进去了，其实有点耗费工时了。只能说前期工作没有完全做好，急着写完，结果还是返工了一丢丢。

2. 编码上。在后面的联调过程中，发现自己虽然有自我审查了一遍代码，但还是有些许地方考虑不周全，犯了一些低级的编码失误，比如内存释放，比如本应放在if/else逻辑之外的代码被我放进去了，造成严重的逻辑缺陷。造成这种情况的原因，是在写代码的过程中时不时添加、删除东西，没有及时照顾到整体的情况，有偏差；后面立马审查也会陷入一种思维定势中去。

3. 实现上。这次的引流方案其实跟原本我们自己的逻辑其实有很大不同，原本应该仔细推敲下造成的逻辑影响，而不是看上去觉得很简单的方案就着急上手了，结果就是联调时出了好多问题，同事因为嵌入式编译运行都不是很方便，浪费很多时间，实在是不应该。直接造成这一个周自己的效率非常低下，惶恐了。

4. 方案上。原本是实现方案的人，方案在会议他们讨论了，我也听了，都挺靠谱的样子（应用层上的一些实现我不是很熟悉），也说在别的项目上有验证过了。等到实现https引流发现一直不通，中间抓包，log分析后认为不是自己这边的问题，然后找应用层的人确认，他因为也刚接手不久，也是不能确定。最后只能找以前接触的人探讨，才发现之前他们定方案时，应该是部分细节没有核对清楚，造成偏差......导致的后果是这一天感觉是白白浪费掉（干扰我排查的一个原因是，接口人跟我说，只要不通过我这个NDK平台，连接就没有问题，直接让我一直怀疑是自己的代码有问题，后面其实是他的理解也出现偏差）。其实关于https代理引流的理论知识，后面我一搜就一目了然，根本不需要这么折腾。这么说，自己的上下层知识储备还是很重要的，关键时候不必被人牵着走。

在这里入职快满一年，当回过头来发现，这一年的成长实在有限（虽然生活上的人生大事算是办了），没有特别突出的或者可以引以为豪的东西出来，无论是产品、技术亦或是人与人之间的交流。将满一年的今天，要鞭策。

