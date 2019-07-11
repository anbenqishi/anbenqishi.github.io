---
Layout: post
title: leetcode-3
published: true
categories: Algorithm leetcode
tags: algorithm leetcode ARTS
---

## problem

Given a string, find the length of the **longest substring** without repeating characters.

**Example 1:**

```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```

**Example 2:**

```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## analysis

1. 暴力法：找出所有子串，每个子串判断是否符合规则，若符合，则记录长度；不符合，则丢弃。其中规则的判断即判断是否有重复字符，可以使用set来实现。最后所有长度取一个最大值。
2. 从暴力法延伸一下，对于字符串a来说，我们从头开始遍历，直到a[i]…a[j]这一段才出现重复字符，那么从a[i]到a[j+1]，直到end,我们其实都知道这些子串都是不满足规则的，不用再做判断了。同时上述隐含了：a[i]到a[j-1]是没有重复字符的，我们记录下此时的长度为j-i。
3. 接上，如果a[i]到a[j]包含重复字符，那么i应该前进一步，判断从i+1起的子串是否满足规则（初识时i=0，j=0）。我们是否知道a[i+1]到a[j]是没有重复字符的？不知道！由于a[i]已经被踢出set了，我们可以再次去判断a[j]是否还与a[i+1]…a[j-1]中的字符重复。如果重复，则i+1还要继续前进一步，然后再判断；如果没有重复，记录下当前的最长长度，然后j再往前走一步，判断是否重复。如此，直到结束。
4. 更进一步，如果我们知道a[i]…a[j]这一段中，与a[j]最近的，且与其重复的下标位置k，i <= k < j且a[k]==a[j]，那么i可以直接跳转到k，而不必一步一步走向k。这样的话，我们需要建立起字符与索引的对应关系，想到map倒蛮合适的。
5. 这样，我们让i直接跳转到index(a[k]) + 1即可，即下一个不等于a[j]的字符上去，设为$j^{'}$，这样从$j^{'}$到j的长度即为$j - j^{'} + 1$。可以看到，i只要跟着j一直往前跳着走即可。不必一步一步往前挪，也不用i停j走，或是i走j停这样反复判断子串长度。

## algorithm 

```c++
/**
* version 1
* Runtime: 28 ms, faster than 42.60% of C++ online submissions for Longest Substring Without * Repeating Characters.
* Memory Usage: 13.2 MB, less than 26.97% of C++ online submissions for Longest Substring 
* Without Repeating Characters.
*/
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        unordered_set<char> my_set;
        int ans = 0, i = 0, j = 0;
        while (i < n && j < n) {
            /* not duplicate */
            if (my_set.find(s[j]) == my_set.end()){              
                my_set.insert(s[j++]);
                ans = max(ans, j - i);
            } else {
                my_set.erase(s[i++]);
            }
        }
        return ans;        
    }
};
```

```c++
/**
* version 2
* Runtime: 16 ms, faster than 71.70% of C++ online submissions for Longest Substring Without * Repeating Characters.
* Memory Usage: 10.9 MB, less than 42.64% of C++ online submissions for Longest Substring 
* Without Repeating Characters.
*/
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        map<char, int> my_map;
        int ans = 0, i = 0;
        for (int j = 0; j < n; ++j) {
            /* find in map */
            if (my_map.find(s[j]) != my_map.end()){   
                /* move i to next-not-equal-index */
                i = my_map[s[j]] < i ? i : my_map[s[j]] + 1;
            }
            /* index substraction need plus 1 */
            ans = max(ans, j - i + 1);
            my_map[s[j]] = j;
        }
        return ans;        
    }
};
```



## epilogue 

实现第二个版本耗了一些时间，主要是在下标位置的计算，以及最大长度的计算两者之间没有统一，造成时常出错。最开始i没有及时走到下一个上去（即代码中的+1操作），然后同时考虑长度计算值是否需要+1的问题，导致互相影响，一直出错。