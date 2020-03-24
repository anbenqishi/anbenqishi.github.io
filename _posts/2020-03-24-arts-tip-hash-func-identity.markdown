---
layout: post
title: [TIPS]identity hash函数
published: true
categories: hash algorithm ARTS
tags: hash algorithm ARTS
---

如果需要被hash的数据比较少，可以使用数据本身（当作是一个整数）来作为hash值。这种方式，hash函数的开销为0.比较完美，因为它把所有的输入都映射到各不相同的hash值上去。

比如在Java中，hash值是32位的，那么Integer和Float的值都可以直接当作hash值；但是64位的Long和Double就无法用这种方法。像ASCII字符（8位），或者两个字母表示的国家代码（26^2 = 676个表项），也都可以采用这种方法。

identity function我们一般翻译为恒等函数，换句话说就是：$f(x) = x$.

## 参考文献

[wiki](https://en.wikipedia.org/wiki/Hash_function#Identity_hash_function)

