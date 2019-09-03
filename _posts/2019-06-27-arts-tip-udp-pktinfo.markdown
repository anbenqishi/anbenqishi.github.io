---
layout: post
title: 【tip】udp源地址获取的问题
published: true
categories: ARTS UDP
tags: ARTS UDP
---

## 问题

两台机子使用可靠UDP来连接，结果发现接收方收到报文后没有任何反应，即没有反馈发回任何报文回来。

## 排查

1. 通过在接收端（服务端）log信息可以看到，他是在`recvmsg`时，提取控制信息为空，导致无法获取控制消息中的源地址，判断出错，退出连接。

2. 通过log中信息判断这是两个IPv6地址连接之间，同时进一步查看两个地址，可以发现这是两个地址实际上IPv4地址，包装成了一个IPv6地址。注意到这点很重要，先前已经注意到一个IPv6地址，当从控制信息提取目的地址时，如果是一个实际为v4的v6地址，需要使用`IP_PKTINFO`类型来判断获取，而不是使用`IPV6_PKTINFO`。这是处理v6信息的特殊之处。

3. 由于是因为接收端没有接收到控制信息，怀疑是发送端没有把数据送出来，注意到发送端套接字选项`IP_PKTINFO`的设置情况，怀疑是选项没有设置正确。后面调试log证实了这个猜想：由于这个地址实际是一个v4地址，实际要设置的是`IP_PKTINFO`，而不是`IPV6_PKTINFO`；如果设置当前是个0地址，由于不能确定这个地址实际是属于哪个地址族的，建议v4、v6的`pktinfo`都一起设置。套接字代码如下：

   ```c
   int on = 1;
   if (af == AF_INET) {
       return setsockopt(fd, IPPROTO_IP, IP_PKTINFO, (const void *)&on, sizeof(on));
   } 
   #ifdef IPV6_RECVPKTINFO
   return setsockopt(fd, IPPROTO_IPV6, IPV6_RECVPKTINFO, (const void *)&on, sizeof(on));
   #else
   
   #if defined(__APPLE__)
   return setsockopt(fd, IPPROTO_IPV6, IPV6_2292PKTINFO, (const void *)&on, sizeof(on));
   #else
   return setsockopt(fd, IPPROTO_IPV6, IPV6_PKTINFO, (const void *)&on, sizeof(on));
   #endif /* __APPLE__ */
   #endif/* IPV6_RECVPKTINFO */
   ```

4. 在修订完发送端并确认设置正常后测试，还是发现接收端收到的消息长度为0。此时从接收端的角度考虑，是否也正确设置了套接字选项？接收端监听时绑定的是0地址，由于设置的是IPv6地址族，所以绑定地址是`::`。发现设置socket选项时，之前判断了它是不是一个v4映射的v6地址，而没有判断它是不是一个0地址。导致此时还是设置了v6的`pktinfo`，设置错误会获取不到`pktinfo`信息。重新修订成0地址时，同时设置v4和v6的socket选项。至此终于正常接收到控制消息。

5. 此问题解决完，我打算重新查看一遍设置发送`pktinfo`的代码，结果竟然没有找到！没有设置，远端也能收到吗？难道内核会自动帮我们打包吗？看到[这篇文章](https://www.cnblogs.com/kissazi2/p/3158603.html)也是获取UDP包中控制消息，没有显式设置过控制消息（BTW，我们项目是获取**头标识目的地址**即`ipi_addr`作为`local_addr`），同时强调这种方法只能用于UDP传输中（[man page](http://man7.org/linux/man-pages/man7/ip.7.html)的原话是`only works for datagram oriented sockets`）。但[其他文章](https://blog.csdn.net/l1902090/article/details/37742297)有提到在发送数据包前需要设置这个控制信息，更让人不解了我们代码中并没有设置信息，只有选项。

6. [进一步查找获悉](https://stackoverflow.com/questions/3062205/setting-the-source-ip-for-a-udp-socket)，这个socket选项主要就是用于设置或获取控制信息使用的。如果不需要特别地变更某个具体内容，那么内核会帮你设置的，只要它看到你的fd设置了这个选项。[这个](https://groups.google.com/forum/#!original/comp.os.linux.development.system/7Eql8Xkef7o/4W9-jCecneAJ)是代码参考。[这个](http://www.potaroo.net/ispcol/2016-09/udp-server.c)是自己设置`IPV6_PKTINFO`的代码参考。

7. 收工。

## 参考

[docker 容器网络下 UDP 协议的一个问题](https://cizixs.com/2017/08/21/docker-udp-issue/)

