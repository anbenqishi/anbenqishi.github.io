---
layout: post
title: [TIPS]CRC hash函数
published: true
categories: hash algorithm ARTS
tags: hash algorithm ARTS
---

### 概念

CRC：Cyclic Redundancy Check，循环冗余校验，是这样一种hash函数，它根据网络packet或电脑file等数据产生简短的固定位数的校验码。一般是用来检测或校验数据传输或保存是否出现错误。不过毕竟它算hash的，所以算hash的场景都可以使用。

### 基本原理

把原始数据（消息）当作被除数，定义一个“生成器多项式（generator polynomial）”作为除数。最后的商被丢弃，余数作为最后的结果。注意，除数，即多项式，其系数是有约束的----这会扯到数学方面去，不熟----当前计算机使用最广的就是0或1。

一个CRC值是n-bit的，是指其是n-bit长度的。不同的多项式，结果当然会有不同。一般来说，多项式的最高项是n，也就是其有n+1项，或者长度是n+1。CRC与其多项式一般命名为CRC-n-xxx的形式。

例如，CRC-1，其多项式是$x+1$(1即是x的0次幂)。就是我们通常看到的奇偶校验。结果是一个bit长的。

### 例子

计算一个n-bit的二进制CRC。

有个14bit的消息`11010011101100`，多项式为$x^3+x+1$ (这里有4项哦，系数可以写成`1011`)，所以结果是3-bit的。

我们有了被除数和除数，可以做运算了。但是这里注意，我们做的是二进制的[模2除法](https://en.wikipedia.org/wiki/Computation_of_cyclic_redundancy_checks)。与普通二进制除法的不同点在于，不做借位的操作。

模2加法运算为：

```python
# 无进位，也无借位
1+1=0
0+1=1
0+0=0
```

模2减法运算为（其实就是异或操作，这就是除法所作的事儿）：

```python
# 也无进位，无借位
1-1=0
0-1=1
1-0=1
0-0=0
```

同时，被除数需要左移n位。除法运算的余数即是最后的结果。

## 参考文献

[如何计算CRC校验码（循环冗余检验码）](https://blog.csdn.net/Kj1501120706/article/details/73330526)

[wiki](https://en.wikipedia.org/wiki/Cyclic_redundancy_check)