---
layout: post
title: BGP性能问题
published: true
tags: BGP performance protocol network
---


这次修订BGP的性能问题，有必要总结记录下，之前做过的工作，都没有好好记录，结果现在都快四年了，感觉好像刚刚工作一样，没什么经验。

这次修订的起因，是一个比较重要的客户A提出来要在keepalive/holdtime较短的情况下，至少要建立N百个个邻居，容量是Nw普通路由/ECMP路由。之前的BGP还从没有达到过这个性能指标；而且实际测试时，N百个邻居目前都不能正常稳定地建立起来，遇到holdtime超时而造成各种邻居down，这样会恶性循环下去；本身当前实现的BGP标的就没有支持这么大容量的邻居/路由，因此需尽可能解决。

其实问题的本质是当前的zebos框架使用的是伪线程机制，即单线程机制，多核多CPU根本不能有效利用到。而在当前的单线程机制下，想要让整个协议顺畅运行起来，最有效的方式就是把之前的耗时线程拆分出来，放在多个伪线程里面执行，好让其他task能够及时得到调度，特别是像BGP协议这种具有保活报文机制的进程----一旦邻居没收到保活，认为你死了，立马就断开了邻居。

从本质上思考，邻居报文的接收/发送，不能与路由的计算分发放在一个线程里面执行。前者具有时间敏感性，后者只有计算收敛性要求，二者没有强关联性，把他们放在一起抢时间片不是一种有效的设计。但是目前还是需要从当前框架出发，短期内不可能对整体框架大动手脚。

先分析罗列出在满足当前场景下可以使用的性能调优方法，结合之前对代码的理解和分析：

1. 伪线程运行时间切片

    需要提取当前耗时较长，影响较大的伪线程事件进行拆分，拆分需要注意伪线程间的影响。

2. 链表---> hash

    之前的某些结构使用链表的方式组织，一是因为大部分行为都是遍历操作，二是要求组织是有序，三是之前可能没有考虑过大容量的情况。这对于查找来说是个灾难，每次都要进行O(n)的遍历也是够受的。因此考虑新增hash结构，专门针对查找做优化。

3. 一次执行 ---> 批量执行, 由此引发的异步逻辑影响考虑。

    这个其实就是上面说的伪线程拆分，这里是着重强调本来是一次行完成的事件，在分成多个伪线程之后，对于本来A->B的事件流，需要考虑A1->B->A2->B类似这种逻辑的影响。

4. 自己计算定时器时间：

    虽然伪线程也有做定时器的时间计算，但是都是在事件队列执行完成后才能执行这个计算，这样时间上可能已经来不及了，所以把定时器计算单独拎出来，在每个事件完成后都计算一次，这样保证时间能够及时计算出来，报文能够及时发送出去。当然这个只是缓解的方式，如果一个事件

    本身就花很长时间，那么定时器还是不能及时计算出来。需要配合其他的优化手段进行。

5. 尽量拆线程，评估影响:

    一个线程如果执行太多的处理，也会耗费较长时间，此时要考虑把一些事件处理挪到下一个线程去执行，这个与上述批量执行不同。即不要做成一个要处理很多事情的伪线程，不要一口吃成胖子，有些处理挪到下一个伪线程处理也是可以的。


