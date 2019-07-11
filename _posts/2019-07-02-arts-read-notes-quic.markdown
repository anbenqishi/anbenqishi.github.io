---
layout: post
title: 【阅读】HTTP/3笔记
published: true
categories: ARTS QUIC   
tags: ARTS HTTP/3 QUIC 
---

## 原文

[Some notes about HTTP/3](https://blog.erratasec.com/2018/11/some-notes-about-http3.html#.XRlvc-gzbIV)

## 概述

1. 互联网领域与其他领域不同的一点是，关于标准的建立。在互联网上，往往是人们先实现了某种东西，好用的话，其他人会跟进使用。使用的人越多就会变成事实上的标准。而RFC仅仅是把这个“事实上的标准”以规范文档的形式记录下来。比如TCP/IP，比如SPDY等等。
2. HTTP/3标准进行中，而且几乎就是围绕QUIC来展开的。因为全球TOP2的两大网站[google.com](www.google.com)以及[youtube.com](www.youtube.com)都握在Google手里，所以Google已经是间接控制了未来Web协议的发展。比如SPDY，HTTP/2标准，其他浏览器以及主流Web服务器都已经跟进支持了。所以是时候好好看看QUIC了。
3. 其实QUIC更像是TCP的一种新版本，而不是HTTP的。因为针对HTTP来说，相比HTTP/2，几乎没有改变什么；更多的，QUIC影响的是传输层面的，接下来聚焦传输问题就好了。
4. 主要特性一：更快的连接建立，更少的延迟。TCP要来回握手建立连接，套上SSL，又要几个来回来加密，听上去都很慢。QUIC降低了RTT。
5. 主要特性二：带宽利用。连接之间因为拥塞的原因总是有带宽限制。传统HTTP在这方面利用率不高，一般与网站的交互会同时有多种数据的传输，浏览器会与web服务器建立多条连接。每条TCP连接会各自进行带宽估计，这样就无法进行整体的带宽估计。SPDY使用了多路技术来做统一的带宽计算。
6. QUIC扩展了上述的多路技术，使用上更简单，连接间不会互相阻塞，用户角度上看，交互会更平滑。
7. `user-mode stacks`。TCP连接是在内核进行处理的，但是我们的服务往往都是在用户模式下运行的。这必然有模式切换的性能开销。可以使用类似于DPDK的技术，用一个`usermode driver`来绕过内核，直接使用用户模式的自定义TCP栈。如果使用UDP来替代TCP则可以获得一样的性能而不必使用`usermode drivers`。通过调用`recvmmsg()`可以得到多个UDP包，虽然这里还有用户态/内核态的切换，但是均摊下来，相比于一个包切换一次，这里只需要100个包切换一次。
8. RSS(Receive Side Scaling)是一种能把接收的数据包分散到多个接收队列的网卡驱动技术。但多核情况下可能有竞争问题。硬件厂商跟进，RSS现具有给每个核独有的非共享队列。OS也支持UDP SO_REUSEPORT选项。QUIC集大成，使用了上述技术如有神助。
9. 主要特性三：移动支持。手机的特点是它可能在多个WIFI、网络下频繁切换，IP地址在变，当前基于socket四元组的连接也会被频繁地关闭、重建。但是QUIC看到了这个弊端，不使用传统的socket来标识一个连接，而是用一个64位的标识符来确定一条connection。任你IP改变，我自岿然不动。
10. 最后一点，使用QUIC/HTTP/3编程，相比于传输层的socket API，更加面向高层，比如在Go或者OpenResty的Lua里使用（这里大意就是我们更面向应用层编程，而不是传输层）。

## 自说自话

QUIC并不是说取代了TCP，应该看作是对TCP的一次升级，来适应现在的网络环境。TCP已经很厉害了，服役了这么多年，还历久弥新的姿态。作者提到这次HTTP/3其实更像是对传输层的一次UPGRADE，那么其实QUIC可以当作一种传输层协议剥离出来使用。估计大厂们都在做了。