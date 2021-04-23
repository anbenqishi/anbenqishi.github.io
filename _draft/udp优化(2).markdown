---
layout: post
title: udp优化(2)
published: true
tags: Linux UDP 
categories: Linux UDP
---

## UDP系统参数

## UDP丢包

这里不是指UDP在网络传输中不知道丢哪里去的情况，而是从接收方来看UDP丢包的情况。丢包信息可以通过`cat /proc/net/udp`的`drops`看到。

1. 缓冲区满了：水满则溢。UDP缓冲区被数据塞满，后来的UDP包就被丢弃。应用层调度的时候，应该及时感知到socket的数据接收情况，及时read来缓解这种情况。单纯地增大缓冲区大小治标不治本，繁忙的应用也应该先把数据从内核中读取出来，后续再处理。
2. 缓冲区小了：接不了发送的一个大包，这个包立马就被丢掉了。涉及到socket缓冲区的配置如下：`/proc/sys/net/core/rmem_default`缺省值，`/proc/sys/net/core/rmem_max`最大值。要合理配置。
3. ARP缓存过期（这应该不仅限于UDP）：接收方没有对方MAC或是MAC缓存过期了，在获取到MAC地址之前，接收到的UDP包会先被缓存到`arp_queue`队列中，默认最多3个，多余则被丢弃。被丢弃的包的计数(?)可以在`/proc/net/stat/arp_cache`中的`unresolved_discards`看到。队列大小可以通过`/proc/sys/net/ipv4/neigh/eth0/unres_glen`来修改。

## UDP 发送与接收



## 参考文献

[告知你不为人知的UDP-疑难杂症和使用](https://zhuanlan.zhihu.com/p/25622691)