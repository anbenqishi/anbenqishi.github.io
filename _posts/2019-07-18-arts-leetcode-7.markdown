---
layout: post
title: leetcode-7
published: true
categories: Algorithm leetcode
tags: ARTS algorithm leetcode
---

## [problem](https://leetcode.com/problems/reverse-integer/)

Given a 32-bit signed integer, reverse digits of an integer.

**Example 1:**

```
Input: 123
Output: 321
```

**Example 2:**

```
Input: -123
Output: -321
```

**Example 3:**

```
Input: 120
Output: 21
```

**Note:**
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [$−2^{31}$,  $2^{31} − 1$]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

## analysis

1. 因为反转可能出现溢出的情况，即超过32bit `int`所能表示的最大（小）值，所以我习惯上先统一使用`unsigned int`来表示反转后的值，再去考虑溢出的情况；
2. leetcode-7与leetcode-8都有判断整数溢出的情况，俺使用了同一种判断溢出的方式，即在要添加最后一个数字之前判断其是否会超出当前`int`所能表示的最大值。
3. 代码本身还是比较直白的，直接看代码吧，这种题主要还是细节。

## algorithm

```c++
/**
 * Runtime: 4 ms, faster than 77.74% of C++ online submissions for Reverse Integer.
 * Memory Usage: 8.1 MB, less than 77.50% of C++ online submissions for Reverse Integer.
 */
class Solution {
public:
    int reverse(int x) { 
        /* convert to positive number */
        unsigned tmp_x = x;
        char flag = 0;
        if (x < 0) {
            flag = 1;
            tmp_x = x == INT_MIN ? (unsigned)x : -x;
        }

        unsigned result = 0;
        while (tmp_x) {
            result = result * 10 + tmp_x % 10;
            tmp_x /= 10;
            /* check overflow */
            if (tmp_x < 10 && tmp_x && result > UINT_MAX / 10) {
                return 0;
            } 
        }
        
        if (flag) {
            if (result > (unsigned)INT_MIN)
                return 0;
            return -result;
        }
        
        if (result > INT_MAX)
            return 0;
        return (int)result;
    }
};
```

## epilogue

连续两题整数题，解法类似，都还好，没那么多弯弯绕绕。