---
layout: post
title: 【TIPS】一个关于C的小问题
published: true
categories: C algorithm ARTS
tags: C algorithm ARTS
---

### 问题

```c
#include <stdio.h>
void check_endian() {
	int num = 0x12345678;
	char *q = (char *)&num;
	if (*q = 0x78) {
		printf("little endian\n");
	} else {
		printf("big endian\n");
	}
	return;
}

int main(int argc, char *argv[]) {
	check_endian();

	int i = 0;
	int arr[3] = {0};
	printf("i = %p, arr[3] = %p\n", &i, &arr[3]);
	for(; i <= 3; i++) {
		arr[i] = 0;
		printf(" %p hello world!\n", &arr[i]);
	}
	return 0;
}
```

群里一个小伙伴刚学的编程问的，他说看的书里是说这个程序会无限循环，问为什么。

### 验证

群里的原因也有分析，就是数组越界跑到i的地址上去了，造成无限循环。但我的第一反应是，明显这是一个undefined的行为，发生什么都有可能，不能这么断定啊，谁跟你说内存就是这么布局的呢。然后吐槽了一句，被大佬教育了"这是从结果分析可能的原因，也是程序员需要的能力"。好尴尬，大佬说的是对的，我没转过弯来，以后不敢说我干了几年程序员。

于是我想要去跑出无限循环的情况。原来是windows10中招了。

#### UBUNTU18.04.4

```bash
little endian
i = 0x7ffd9092bee8, arr[3] = 0x7ffd9092bef8
 0x7ffd9092beec hello world!
 0x7ffd9092bef0 hello world!
 0x7ffd9092bef4 hello world!
 0x7ffd9092bef8 hello world!
*** stack smashing detected ***: <unknown> terminated
```

挂了，可以看到，`i`是低地址的，数组从下标0地址开始是增高的。所以踩不中i。

#### WINDOWS10

```bash
little endian
i = 000000000066FE1C, arr[3] = 000000000066FE1C
 000000000066FE10 hello world!
 000000000066FE14 hello world!
 000000000066FE18 hello world!
 000000000066FE10 hello world!
 000000000066FE14 hello world!
 000000000066FE18 hello world!
 000000000066FE10 hello world!
 000000000066FE14 hello world!
 000000000066FE18 hello world!
 ...
```

无限循环了。

### 结论

目前的运行结果（都在同一个CPU上跑的，x86_64）只能显示一个：`arr`的地址总是向上增长的。

这就是涉及到一个栈的分配增长方向问题，之前我依稀记得Linux的栈是从高地址往低地址方向增长的。以上面的例子为例，应是`i`在高地址，`arr`的地址比`i`低，在这个[知乎问答](https://www.zhihu.com/question/36103513)中有个回答提到"a0和a1这两个分配在栈帧里的数组到底哪个在高地址哪个在低地址，其实并不反映栈的增长方向，而只反映了编译器自己的决定。C与C++语言的数组元素要分配在连续递增的地址上，也不反映栈的增长方向。"

所以说跟编译器有关？Linux下的编译器是`gcc (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0`；Windows10下的编译器是`realgcc.exe (Rev1, Built by MSYS2 project) 7.2.0`。现在祭出那张经典的Linux内存布局也没啥用了。

其实从上面来看，栈上的空间分配，除了数组遵循连续，由低到高外，其实对于变量的分配顺序，与其初始化的顺序，并没有本质必然的联系【待商榷？】。

【感觉需要再补一下CSAPP的内容了。】

## 参考文献

[C/C++:堆栈面面观](https://zhuanlan.zhihu.com/p/56929325)

[The Function Stack](https://www.tenouk.com/Bufferoverflowc/Bufferoverflow2a.html)