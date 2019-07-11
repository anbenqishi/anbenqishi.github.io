---

layout: post
title: leetcode-4
published: true
categories: Algorithm leetcode
tags: ARTS leetcode algorithm

---

## [problem](https://leetcode.com/problems/median-of-two-sorted-arrays/)

> There are two sorted arrays **nums1** and **nums2** of size m and n respectively.
>
> Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
>
> You may assume **nums1** and **nums2** cannot be both empty.
>
> **Example 1:**
>
> ```
> nums1 = [1, 3]
> nums2 = [2]
> 
> The median is 2.0
> ```
>
> **Example 2:**
>
> ```
> nums1 = [1, 2]
> nums2 = [3, 4]
> 
> The median is (2 + 3)/2 = 2.5
> ```

## analysis

1. 从时间复杂度上看，显然都不能完全遍历一把两个数组；$log$的时间复杂度第一时间蹦出来的应该都是二分查找吧；

2. 如果两个数组的总个数是奇数，显然median是其中一个数；如果是偶数，则会是两个数的平均数；

3. 方便讨论，设为数组A，B，且`len(A)=m` , `len(B)=n`;

4. 基于二分查找的思想，我们要把数组分成两部分，折半砍（不砍不行，连遍历你都使不出来）。假设我们已经成功找到了median，它是A或B中的某个数，或是AB中某两个数的平均和。AB两个数组就分成了两个部分：

   | left_part（i, j）       | right_part（m - i, n - j）  |
   | ----------------------- | --------------------------- |
   | A[0], A[1], …, A[i - 1] | A[i], A[i+1], …, A[m - 1]   |
   | B[0], B[1], …, B[j - 1] | B[j], B[j + 1], …, B[n - 1] |

5. 显然基于中位数的概念，$median\geq max(left\_part)$ && $median \leq min(right\_part)$，也就是说

   ​	1. $max(left\_part) \leq min(right\_part)$

   且有

   ​	2. $len(left\_part) = len(right\_part)$

    (且慢，不是可能有奇数的总个数吗，不能等吧…对的对的，这时候我们可以有$len(left\_part) = len(righ\_part) + 1$就行了，不影响讨论，后面也不影响我们编程，此时median必然在left_part)。

6. 根据上面两个式子我们可以得到关于数组以及数组下标的关系：

   1. B[j - 1] <= A[i] && A[i - 1] <= B[j] (暂时不考虑i j = 0 m的情况)
   2. $i + j = m - i + n - j (+ 1)$，转换成$i$与$j$之间的关系式为$i = 0 \sim m, j = \frac{m+n+1}{2}- i$，其中需设有$n\geq m$，因为保证j不能为负数。
   3. 进一步，根据总个数情况，得到median的结果为：
      1. 若是奇数，则$median = max(A[i - 1], B[j - 1])$
      2. 若是偶数，则$median = \frac{max(A[i - 1], B[j - 1]) + min(A[i], B[i])}{2}$

7. 式子2中是否+1，对于最终i j间的关系式子没有影响。可以看到最终式子加一了，那么默认了总个数为奇数的情况，对于总个数为偶数是否有影响？从程序的角度看，其实是与没有$+1$的式子相等的。所以上述式子对于一般情况均适用。

8. 有了6中的关系，其实程序结构就差不多出来了：通过二分查找$i \in [0, m]$，来找到满足6中1式子的关系，其中$j$由6中式子2给出；不满足的情况只有两种（把6中1式子取非就得到了）：$B[j - 1] > A[i]$, $A[i - 1] > B[j]$；前者说明i取小了，需要增加（二分哦），后者说明i取大了，需要减小（继续二分）。最终得到结果（结果见算法）。

9. 考虑之前说过的特殊情况，即$i = 0, i = m, j = 0, j = n$的情况，此时我们不看6(1)式了，回到开始，即5(1)式。我们是根据5(1)推出的6(1)。

   1. $i = 0$的情况，说明left_part没有A数组成员，那么我们只要满足$B[j - 1] \leq A[i]$即可，更简单了；

   2. $i = m$的情况，说明right_part没有A数组成员了，那么只要满足$A[i -1] \leq B[j]$即可，也简单了。

   3. j的情况类似。总结一下，在6(1)的基础上，可以写为：

      `(j == 0 || i == m || B[j - 1] <= A[i]) && (i == 0 || j == n || A[i - 1] <= B[j])`

   4. 上述式子取个非，就可以得到其他两种不满足的情况

## Algorithm 

```python
def median(A, B):
  m, n = len(A), len(B)
  if m > n:
    A, B, m, n = B, A, n, m
  if n == 0:
    return 0  # abnormal
  
  imin, imax, half = 0, m, (m + n + 1) / 2
  while imin <= imax:
    i = (imin + imax) / 2
    j = half - i
    if i < m and B[j - 1] > A[i]: # i太小了，注意这里没有j>0的判断，优化掉了，可以想想为啥？
      imin = i + 1
    elif i > 0 and A[i - 1] > B[j]: # i太大了，注意这里也没有j<n的判断，同样的小优化
      imax = i - 1
    else: # 找到了，那么就看看是奇是偶吧，同样需要注意到数组下标情况
      if i == 0:
        max_of_left = B[j - 1]
      elif j == 0:
        max_of_left = A[i - 1]
      else:
        max_of_left = max(A[i - 1], B[j - 1])
      if (m + n) % 2 == 1: # 奇数情况
      	return max_of_left
      
      if i == m:
        min_of_right = B[j]
      elif j == n:
        min_of_right = A[i]
      else:
        min_of_right = min(A[i], B[j])
      return (max_of_left + min_of_right) / 2.0
```



## Epilogue

其实刚拿到题目有点懵，而且还看了某位大牛多年前写的solution，看上去太复杂了，也不容易理解，还容易出错，就放弃了。后面是看了官网的solution后在琢磨的，所以不是完全自己的想法，我只是根据自己的理解码出来，一方面也是想看看自己是否真的理解了。