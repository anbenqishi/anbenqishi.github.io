---
layout: post
title: leetcode-20
categories: Algorithm leetcode
tags: algorithm leetcode ARTS
---

## [problem](https://leetcode.com/problems/valid-parentheses/)

Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

**Example 1:**

```
Input: "()"
Output: true
```

**Example 2:**

```
Input: "()[]{}"
Output: true
```

**Example 3:**

```
Input: "(]"
Output: false
```

**Example 4:**

```
Input: "([)]"
Output: false
```

**Example 5:**

```
Input: "{[]}"
Output: true
```

## analysis

1. 仔细审题，其实就是括号的及时配对，而不是说括号的左右各数要对，所以很自然都会想到栈。左括号入栈，碰到右括号就弹出来去配对。所以算法很直接简单。
2. 估计可以考虑的点是，不用一个个括号拿出来判断，感觉代码都是类似的。

## algorithm

```c++
/**
 * Runtime: 4 ms, faster than 61.50% of C++ online submissions for Valid Parentheses.
 * Memory Usage: 8.4 MB, less than 95.35% of C++ online submissions for Valid Parentheses.
 */
class Solution {
public:
    bool isValid(string s) {
        int len = s.length();
        if (len == 0)
            return true;
        
        stack<char> tmp;
        for (int i = 0; i < len; ++i) {
            if (s[i] == '[' || s[i] == '{' || s[i] == '(') {
                tmp.push(s[i]);
                continue;
            }
            
            if (s[i] == ']') {
                if (tmp.empty())
                    return false;
                char ch = tmp.top();
                if (ch != '[')
                    return false;
                tmp.pop();
            } else if (s[i] == '}') {
                if (tmp.empty())
                    return false;
                char ch = tmp.top();
                if (ch != '{')
                    return false;
                tmp.pop();
            } else if (s[i] == ')') {
                if (tmp.empty())
                    return false;
                char ch = tmp.top();
                if (ch != '(')
                    return false;
                tmp.pop();
            }
        }

        if (!tmp.empty())
            return false;
        return true;
    }
};
```



## epilogue

leetcode邮件过来的题目就先做了。