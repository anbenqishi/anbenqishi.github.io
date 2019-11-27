---
layout: post
title: leetcode-9
published: true
categories: Algorithm leetcode
tags: algorithm leetcode ARTS
---

## problem

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

**Example 1:**

```
Input: 121
Output: true
```

**Example 2:**

```
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

**Example 3:**

```
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

**Follow up:**

Could you solve it without converting the integer to a string?

## analysis

1. 对不同的数字分析：个位数，肯定是回文的；有符号数，肯定不是回文的；其他情况，从头与尾同步向中间逼近来判断。
2. 目前`int`型数值最大可能达到$2^{64}-1$，有20个数字。可以申请`char num[20]`来把`x`分解成一个个数字存放在数组中，然后使用两头遍历数组的方式判断回文。按这个思路编写的算法，时间上ok，空间上占用估计beat不过其他人。version 1。
3. ok，换一种方式，回文数字的一个特点就是回文后的值与原值相同。那么其实我们完全可以在分解x的过程中创建这个数字，之后直接比较是否相等就行了。这样我们就不用申请什么数组保存数字了。version 2。
4. 上述想法固然好，不过要注意的一点是，反转后的数字超过了`int`能表示的最大数字，所以反转后的数字最好用无符号数来表示（**犯错的地方**）。不过...结果好像，与上述version1算法差距不明显（不过发现leetcode显示的时间与空间占用不是很靠谱啊，多跑几次竟然都不一样，只能当作参考啦）。

## algorithm 

```c++
/** 
* version 1
* Runtime: 8 ms, faster than 93.82% of C++ online submissions for Palindrome Number.
* Memory Usage: 8.1 MB, less than 58.78% of C++ online submissions for Palindrome Number.
*/
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0)
            return false;
        if (x < 10)
            return true;
        char num[20] = {'\0'};
        int i = 0;
        while(x) {
            num[i++] = x%10;
            x = x/10;
        }
        --i; /* locate last num. */
        for (int j = 0, k = i; j != k && j <= k; ++j, --k) {
            if (num[j] != num[k])
                return false;
        }
        return true;
    }
};
```

```c++
/**
* version 2
* Runtime: 12 ms, faster than 82.61% of C++ online submissions for Palindrome Number.
* Memory Usage: 8.2 MB, less than 34.33% of C++ online submissions for Palindrome Number.
*/
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0)
            return false;
        if (x < 10)
            return true;
        unsigned rx = 0;
        int tmp = x;
        while(tmp) {
            rx = rx * 10 + tmp%10;
            tmp = tmp/10;
        }
        if (rx == x)
            return true;
        return false;
    }
};
```



## epilogue

这个问题相对简单，思路比较顺。要求说不用转化，应该是说最好不要使用version1那种方式吧。

