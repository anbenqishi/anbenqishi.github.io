---
layout: post
title: leetcode-6
published: true
categories: Algorithm leetcode
tags: ARTS algorithm leetcode
---

## [problem](https://leetcode.com/problems/zigzag-conversion/)

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```

**Example 1:**

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

**Example 2:**

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
```

## analysis

1. 看题目，从上到下，从左到右，是按`N`字形来排列，关键是找出每行字符出现的规律；

2. 我们把`N`字形拆成两部分，左右`|`杠部分，以及中间斜杠的部分。其中`|`杠部分可以总结出规律：如果`numRows=n`，那么每一行上的下标是按$2(n-1)$的步幅来递增的。举例来说，如果numRows=4，那么有如下所示图：2(n-1)=6，所以每一行都是以6的步幅来递增。

   ```
   0     6      12
   1   5 7   11 13
   2 4   8 10   14
   3     9      15
   ```

3. 注意到除头尾行外，中间行都是有包括斜杠部分的下标。这部分下标有什么规律吗？以上述例子为例，注意到0到6是+6；1到5是+4,7到11也是+4；2到4是+2,8到10也是+2。到+6到+4到+2，是以-2的步幅递减的。可以得到中间行的下标规律：在初始步幅（即上述的2(n-1)）的基础上，从上到下，斜杠中下标是通过增加2(n-1) - 2 * Row步幅来计算得到的。如n=4情况下，第二行的下标步幅为2(4-1)-2*1=4，则第一个斜杠下标为1+4=5；之后先增加`|`下标，得到7，再继续计算斜杠下标7+4=11；如此交替进行，可以顺序输出完整的一行（第三行类推，是+2）。再次注意头尾是没有斜杠部分的。
4. 根据上述思想来实现。实现过程中注意到先增加`|`杠步幅，再往左看一眼斜杠的方式实现更简洁一点。只是计算方式从之前的+4，变成了-2而已（以上述例子为例，第三行类推，原本是+2，这里就是-4了）。

## algorithm

```c++
/*
 * Runtime: 12 ms, faster than 82.91% of C++ online submissions for ZigZag Conversion.
 * Memory Usage: 10.2 MB, less than 74.49% of C++ online submissions for ZigZag Conversion.
 */
class Solution {
public:
    string convert(string s, int numRows) {
        int len = s.length();
        if (len == 0 || numRows == 1 || len <= numRows)
            return s;
        
        /* 看规律，算出步长 */
        int hop = (numRows - 1) << 1;
        string result;
        /* according to rows. */
        for (int i = 0; i < numRows; ++i) {
            int tmp = i;
            while (tmp < len) {
                /* put in result. */
                result += s[tmp];
                /* 步长递增 */
                tmp += hop;      
                /* 中间特殊处理 */
                if (i > 0 && i + 1 < numRows) {
                    int zig = tmp - (i << 1);
                    if (zig < len)
                        result += s[zig];
                }
            }
        }
        return result;
    }
};
```



## epilogue

犯的错误：

1. 触发了leetcode的`AddressSanitizer: stack-buffer-overflow`检测错误，可能是string的下标使用不当造成的，改成用`+`来拼接字符就没有报错了。
2. 粗心大意了，漏写了一个步长的操作，就是输出`Zigzag`斜杠那段漏了写，估计是刚才处理上述报错问题漏了