---
layout: post
title: leetcode-8
categories: Algorithm leetcode
tags: algorithm leetcode ARTS
---

## [problem](https://leetcode.com/problems/string-to-integer-atoi/)

Implement `atoi` which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

**Note:**

- Only the space character `' '` is considered as whitespace character.
- Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [$−2^{31}$,  $2^{31}$ − 1]. If the numerical value is out of the range of representable values, INT_MAX ($2^{31}$ − 1) or INT_MIN ($−2^{31}$) is returned.

**Example 1:**

```
Input: "42"
Output: 42
```

**Example 2:**

```
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
```

**Example 3:**

```
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
```

**Example 4:**

```
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
```

**Example 5:**

```
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN is returned.
```

## Analysis

1. 题目比较长，是好事，说明他把很多情况都跟我们讲明白了。简单总结下：a. 前置空格需过滤掉，不算异常；b. 有前置符号位，除此之外其他非数字前置符号都算异常；c. 数字的非数字字符不再解析，取已解析数字为结果；d. 若解析的数字超过类型所能表示的最大（小）值，按当前类型的最大（小）值给出结果。
2. 这里面唯一要注意的点是溢出判断，其他逻辑较为直白；溢出需要预判，即再将要溢出的时候提前获知其是否需要溢出，否则溢出判断将会出错。这里我是使用了判断正数是否溢出的方式，负数作为特殊情况处理。
3. 判断溢出的方式是看`INT_MAX/10`的值，与我们当前解析出来的结果`result`比较，是否已经出现`result`比较大，或是相等但`INT/MAX%10`比接下来的一个解析数字小的情况。这两种情况即是溢出。
4. 从绝对值来看，`|INT_MAX| + 1 = |INT_MIN|`。所以正数判断溢出时，负数可能还没有溢出，但是这种情况只出现在要解析字符串值是`INT_MIN`的时候。这时我们判断它溢出，对于负数来说返回的还是`INT_MIN`，所以我们不需要做特殊处理，统一看成是正数是合理的。

## algorithm

```c++
/**
 * Runtime: 4 ms, faster than 88.96% of C++ online submissions for String to Integer (atoi).
 * Memory Usage: 8.3 MB, less than 86.26% of C++ online submissions for String to Integer (atoi).
 */
class Solution {
public:
    int myAtoi(string str) {
        int overflowed = 0;
        unsigned int result = 0;
        int sign = 0;
        int len = str.length();
        
        if (len == 0)
            return 0;
        
        /* skip white space */
        int index;
        for (index = 0; index < len; ++index) {
            if (str[index] != ' ')
                break;
        }
        
        /* all space. */
        if (index == len) 
            return 0;
        
        /* not start with valid symbol. */
        if (str[index] != '-' && str[index] != '+' 
            &&  (str[index] < '0' || str[index] > '9'))
            return 0;
        
        if (str[index] == '-') {
            sign = 1;
            ++index;
        } else if (str[index] == '+') {
            ++index;
        }
        
        int tmp = INT_MAX / 10;
        while(index < len) {
            /* stop at non-valid number. */
            if (str[index] < '0' || str[index] > '9')
                break;

            /* check overflow at last position. */
            if (tmp < result || (tmp == result && INT_MAX % 10 < (str[index] - '0'))) {
                overflowed = 1;
                break;
            }

            result = result * 10 + (str[index] - '0');
            ++index;
        }

        if (sign) {
            if (overflowed)
                return INT_MIN;
            return -result;
        }

        if (overflowed)
            return INT_MAX;
        return result;
    }
};
```



## epilogue

1. 没有去看其他人的实现，自己的实现感觉已经比较直白，非常好理解了，完全就是按部就班。
2. 去掉了一个不必要的负数溢出判断`result > (unsigned)abs(INT_MIN)`，由前面可以看出，显然多余，这是一个不会成立的条件。