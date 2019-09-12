---
title: 什么是MOM
---

要接手一个项目使用了MOM机制，了解一下。



### 关于Redis与MOM

Redis是一个快速的内存数据结构服务器，可以实现一个队列系统。但其实它不是一个[真正的MOM](https://stackoverflow.com/questions/19537841/redis-queue-vs-msmq)。一般是作为一个[轻量级的队列服务]([http://archwang.top/2018/07/03/%E6%B6%88%E6%81%AF%E4%B8%AD%E9%97%B4%E4%BB%B6%E5%AF%B9%E6%AF%94/](http://archwang.top/2018/07/03/消息中间件对比/))来使用。redis的Pub/Sub消息模式用于实时性较高的消息推送，不保证可靠（如何可靠?）。不支持事务的ACID属性，（Redis MULTI/EXEC/DISCARD）顶多算是一个[批量的序列化执行器](https://nosql.mypopescu.com/post/9871479844/redis-based-mom-redis-for-processing-payments)。

