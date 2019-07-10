---
layout: post
title: leetcode-1
published: true
categories: Algorithm leetcode
tags: ARTS leetcode algorithm
---


## Problem

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution, and you may not use the *same* element twice.

**Example:**

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

## Analysis

1. 简单题，题目本身没有对复杂度有限制要求。所以其实可以直接来，思路就是通过两个循环遍历来得到结果：第一层循环即是针对整个数组依次遍历，计算要得到target所需要的另一个整数n；第二层循环即对剩下的数组中所有数，找到等于n的数即可。话可能说的不明白，直接上代码就清楚了。
2. 看第一版代码可以知道，耗费的时间其实挺长的（针对其他答案而言），空间利用尚可。不过这年头，时间往往更宝贵一点，所以是否可以把时间再缩减一点。看来应该是个空间换时间的方案。
3. 第一版中是个O($n^2$)的时间复杂度，是否可以做到O(n)？注意到最外层的循环是为了找到数组中每一个数字a所对应的另一个数字b（从而使得相加等于target），那么如果我们可以给数组做个索引，从而可以快速定位数组中是否含有b。注意到C++中的map查找有log(n)的查找效率，遍历一遍数组的时间复杂度是O(n)。这样我们就有了nlog(n)的时间复杂度了（还没达到O(n)）。
4. 主要想法就是以每个数组中的数字num为key，它的下标i为value，即有num_map[num] = i，建议一张映射表。这样在遍历过程中，我们能够逐渐建立起这个map，同时在这个map中查找b即可（简称"回头望月"，因为遍历过程不断往回看已经在map中的值）。代码见第二版。
5. 运行结果可以看到，时间大大减少了。不过还有很大的改进空间（都进不了90%）。

## Algorithm

```c++
/*
 * version 1
 * Runtime: 112 ms, faster than 39.67% of C++ online submissions for Two Sum.
 * Memory Usage: 9 MB, less than 99.70% of C++ online submissions for Two Sum.
*/
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i, j;
        for (i = 0; i < nums.size(); ++i) {
            int left = target - nums[i];
            for (j = i + 1; j < nums.size(); ++j) {
                if (nums[j] == left)
                    return vector<int>{i,j};
            }
        }
        return vector<int>{};        
    }
};
```

```c++
/*
 * version 2
 * Runtime: 12 ms, faster than 72.27% of C++ online submissions for Two Sum.
 * Memory Usage: 10 MB, less than 44.66% of C++ online submissions for Two Sum.
 */
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> tmp;
        for (int i = 0; i < nums.size(); ++i) {
            int left = target - nums[i];            
            auto search = tmp.find(left);
            if (search != tmp.end()) {
                return vector<int>{tmp[left], i};
            }
            tmp[nums[i]] = i;
        }
        return vector<int>{};        
    }
};
```



## Epilogue

1. 细节是魔鬼，写第二版总是出现一些小的问题，主要是没有想通透，边想边改。
2. 简单的题目，大家更容易会去想有没有更好的解决方案（因为困难题能做出来就阿弥陀佛了:)），大佬们都在追求极致。