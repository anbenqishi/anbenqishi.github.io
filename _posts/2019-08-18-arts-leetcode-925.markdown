---
layout: post
title: leetcode-925
categories: Algorithm leetcode
tags: algorithm leetcode ARTS
---

## [problem](https://leetcode.com/problems/long-pressed-name/)

Your friend is typing his `name` into a keyboard.  Sometimes, when typing a character `c`, the key might get *long pressed*, and the character will be typed 1 or more times.

You examine the `typed` characters of the keyboard.  Return `True` if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

**Example 1:**

```
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
```

**Example 2:**

```
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
```

**Example 3:**

```
Input: name = "leelee", typed = "lleeelee"
Output: true
```

**Example 4:**

```
Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
```

**Note:**

1. `name.length <= 1000`
2. `typed.length <= 1000`
3. The characters of `name` and `typed` are lowercase letters.

 ## analysis

1. 这个好像没啥好分析的，主要是注意审题吧，不要认为是把重复字符去掉再比较。其实是把多余的与前一个字符重复的字符去掉再比较。
2. 所以拿原有的字符串遍历，然后再遍历过程中，可能要让typed字符串多往前走几步，这个涉及到typed字符串的循环前进遍历。

## algorithm 

```c++
/**
 * Runtime: 0 ms, faster than 100.00% of C++ online submissions for Long Pressed Name.
 * Memory Usage: 8.4 MB, less than 100.00% of C++ online submissions for Long Pressed Name.
 */
class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        int name_len = name.length();
        int type_len = typed.length();
        if (name_len > type_len)
            return false;
        
        if (name[0] != typed[0])
            return false;

        for (int i = 1, j = 1; i < name_len; ++i, ++j) {
            if (name[i] == typed[j])
                continue;
            
            while (j < type_len) {
                if (typed[j] != typed[j - 1])
                    break;
                ++j;  
            }
            
            if (j >= type_len)
                return false;
            
            if (name[i] != typed[j])
                return false;
        }
        return true;
    }
};
```



## epilogue

又是leetcode邮件给我的题目。纯练手不生疏，感觉中等以上的题目我都要想半天，最近有点逃避，专挑软柿子捏了。