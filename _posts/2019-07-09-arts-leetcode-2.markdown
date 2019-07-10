---
layout: post
title: leetcode-2
published: true
categories: Algorithm leetcode
tags: ARTS leetcode algorithm
---

## [problem](https://leetcode.com/problems/add-two-numbers/)

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order** and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example:**

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

## analysis

1. 遍历链表的操作，假设这是两个链表a, b，其中`len(a) > len(b)`。会先走一遍其中最短的一个链表b，然后把a中剩下的部分拼接起来即可。
2. 主要注意进位操作，两个个位数相加，最多进位1.
3. 注意最终的结果是返回新创建的链表头，而不是链表尾。可能一不小心，指针跟着链表走，结果找不到头，导致返回值错误。
4. 提交几次后发现，除法与求余操作会多消耗几毫秒，改成直接用加减操作了。

## algorithm

```c++
/**
 * Runtime: 16 ms, faster than 98.65% of C++ online submissions for Add Two Numbers.
 * Memory Usage: 10.3 MB, less than 71.85% of C++ online submissions for Add Two Numbers.
 *
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *result;
        ListNode *p, *q, *current;
        int left;
		int tmp;

        left = 0;
        current = NULL;
        result = NULL;
		if (l1 && l2) {
			tmp = l1->val + l2->val;
            /* not use tmp/10 for runtime sake. */
			left = tmp - 10 < 0 ? 0 : 1;
			current = new ListNode(tmp - 10 < 0 ? tmp : (tmp - 10));
			result = current;
		}
        for (p = l1->next, q = l2->next; p && q; p = p->next, q = q->next) {
			tmp = p->val + q->val + left;
			left = tmp - 10 < 0 ? 0 : 1;
            
			current->next = new ListNode(tmp - 10 < 0 ? tmp : (tmp - 10));
			current = current->next;
        }
        if (left || p || q) {
			/* the longer list wins */
            ListNode *remain = p ? p : q; 
            /* first, check the remain. */
            if (remain){
                for (; remain; remain = remain->next){
					tmp = remain->val + left;
					left = tmp - 10 < 0 ? 0 : 1;
                    
					current->next = new ListNode(tmp - 10 < 0 ? tmp : (tmp - 10));
					current = current->next;
                }
            }
            /* all done, something left? */
            if (left) {
				current->next = new ListNode(1);
            }
        }
        return result;
    }
};
```



## epilogue

主要还是细节，思路想明白了，下笔的时候一些小细节反而容易翻车。