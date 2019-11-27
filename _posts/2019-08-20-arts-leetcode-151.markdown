---
layout: post
title: leetcode-151
published: true
categories: Algorithm leetcode
tags: ARTS algorithm leetcode
---

## [problem](https://leetcode.com/problems/reverse-words-in-a-string/)

Given an input string, reverse the string word by word.

**Example 1:**

```
Input: "the sky is blue"
Output: "blue is sky the"
```

**Example 2:**

```
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```

**Example 3:**

```
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

**Note:**

- A word is defined as a sequence of non-space characters.
- Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
- You need to reduce multiple spaces between two words to a single space in the reversed string.

**Follow up:**

For C programmers, try to solve it *in-place* in *O*(1) extra space.

## analysis

1. 题目中只提到空格，没有提到换行符TAB等其他相关的空白字符，暂不做考虑；

​    2. 由于是一个个单词反转输出，先想到的是用stack，就是依次遍历，单词入栈。最后出栈输出。

​    3. 第二种方法想到的是反向遍历，碰到空格就把已经遍历到的单词输出暂放在result string中。

​    4. 这里试下这两种方法。

​    5. 至于题目中提到的O(1)原地反转操作，刚想到的思路是从后往前遍历，然后碰到一个单词就与前面的指针调换字符，遍历主要由后面进行，前面的指针只是负责往前进。最后遇到了就结束了。然后可以再从前往后遍历一把去掉可能多余的空格。大概如此吧 。

## algorithm

```c++
/**
 * Runtime: 4 ms, faster than 97.98% of C++ online submissions for Reverse Words in a String.
 * Memory Usage: 10.8 MB, less than 54.05% of C++ online submissions for Reverse Words in a String.
*/
class Solution {
public:
    string reverseWords(string s) {
        int len = s.length();
        int start = -1; 
        int end = 0;
        stack<string> reverse;
        for(int i = 0; i < len; ++i) {
            if (s[i] == ' ') {
                /* a word captured. */
                if (start >= 0 && end > start) {
                    reverse.push(s.substr(start, end - start)); 
                    start = -1;
                }
                continue; 
            }
            /* new start. */
            if (start >= 0) {
                ++end;
            } else {
                start = i;
                end = start + 1;
            }
        }

        if (start >= 0 && end > start) {
            reverse.push(s.substr(start, end - start)); 
        }

        string result = "";
        while(!reverse.empty()) {
            if (result != "")
                result += " ";
            result += reverse.top();
            reverse.pop();
        }
        return result;
    }
};
```

```c++
/**
 * Runtime: 4 ms, faster than 97.98% of C++ online submissions for Reverse Words in a String.
 * Memory Usage: 10.6 MB, less than 59.46% of C++ online submissions for Reverse Words in a String.
*/
class Solution {
public:
    string reverseWords(string s) {
        int len = s.length();
        int start = len; 
        int end = -1;

        string result = "";
        for(int i = len - 1; i >= 0; --i) {
            if (s[i] == ' ') {
                /* a word captured. */
                if (end >= 0 && start > end) {
                    if (result != "")
                        result += " ";
                    result += s.substr(end, start - end); 
                    end = -1;
                }
                continue; 
            }

            /* new start. */
            if (end >= 0) {
                --end;
            } else {
                start = i + 1;
                end = i;
            }
        }

        if (end >= 0 && start > end) {
            if (result != "")
                result += " ";
            result += s.substr(end, start - end); 
        }

        return result;
    }
};
```

## epilogue

易犯错的地方主要是偏移量的计算，以及空格的处理。一不小心就漏了。