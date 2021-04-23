---
layout: post
title: 【阅读】25个python snippets
published: true
categories: ARTS python
tags: ARTS python
---

## 原文

[25 Useful Python Snippets to Help in Your Day-to-Day Work](https://medium.com/better-programming/25-useful-python-snippets-to-help-in-your-day-to-day-work-d59c636ec1b)

## 内容

Python语言的优势，相比于其他语言：

1. 兼容大部分平台和系统；
2. 较多的开源框架和工具；
3. 可读可维护的代码；
4. 健壮的标准库；
5. 标准测试驱动开发。

言归正传，25个有用的代码片段奉上，可用于日常任务。

1. 交换两个变量值

   ```python
   a = 5                               
   b = 10         
   a, b = b, a      
   print(a) # 10                               
   print(b) # 5
   ```

2. 判断偶数

   ```python
   def is_even(num):
     return num % 2 == 0
   is_even(10) # True
   ```

3. 分割多行字符串到list中

   ```python
   def split_lines(s):
     return s.split('\n')
   
   split_lines('50\n python\n snippets') # ['50', ' python', ' snippets']
   ```

4. 对象内存占用

   ```python
   import sys
   print(sys.getsizeof(5)) # 28
   print(sys.getsizeof("Python")) # 55
   ```

5. 字符串反转

   ```python
   language = "python"                                
   reversed_language = language[::-1]                                                                 print(reversed_language) # nohtyp
   ```

6. 打印字符串n次

   ```python
   def repeat(string, n):
     return (string * n)
   repeat('python', 3) # pythonpythonpython
   ```

7. 回文检查

   ```python
   def palindrome(string):
       return string == string[::-1]
   palindrome('python') # False
   ```

8. 多个字符串连接成一个字符串

   ```python
   strings = ['50', 'python', 'snippets']
   print(','.join(strings)) # 50,python,snippets
   ```

9. list第一个元素

   ```python
   def head(list):
     return list[0]
   print(head([1, 2, 3, 4, 5])) # 1
   ```

10. 寻找两个list的所有不同元素（相当于并集）

    ```python
    def union(a,b):
      return list(set(a + b))
    union([1, 2, 3, 4, 5], [6, 2, 8, 1, 4]) # [1,2,3,4,5,6,8]
    ```

11. 寻找list中所有不同的元素(去除重复元素)

    ```python
    def unique_elements(numbers):
      return list(set(numbers))
    unique_elements([1, 2, 3, 2, 4]) # [1, 2, 3, 4]
    ```

12. 求多个数的平均值

    ```python
    def average(*args):
      return sum(args, 0.0) / len(args)
    average(5, 8, 2) # 5.0
    ```

13. 检查list中元素是否都不同

    ```python
    def unique(list):
        if len(list)==len(set(list)):
            print("All elements are unique")
        else:
            print("List has duplicates")
    unique([1,2,3,4,5]) # All elements are unique
    ```

14. list中元素的出现频次

    ```python
    from collections import Counter
    list = [1, 2, 3, 2, 4, 3, 2, 3]
    count = Counter(list)
    print(count) # {2: 3, 3: 3, 1: 1, 4: 1}
    ```

15. 寻找list中频次最高的元素

    ```python
    def most_frequent(list):
        return max(set(list), key = list.count)
    numbers = [1, 2, 3, 2, 4, 3, 1, 3]
    most_frequent(numbers) # 3
    ```

16. 角度转化为弧度

    ```python
    import math
    def degrees_to_radians(deg):
      return (deg * math.pi) / 180.0
    degrees_to_radians(90) # 1.5707963267948966
    ```

17. 计算代码执行时间

    ```python
    import time
    start_time = time.time()
    a,b = 5,10
    c = a+b
    end_time = time.time()
    time_taken = (end_time- start_time)*(10**6)
    print("Time taken in micro_seconds:", time_taken) # Time taken in micro_seconds: 39.577484130859375
    ```

18. 计算list中数的最大公约数

    ```python
    from functools import reduce
    import math
    def gcd(numbers):
      return reduce(math.gcd, numbers)
    gcd([24,108,90]) # 6
    ```

19. 寻找string中的所有不同字符

   ```python
   string = "abcbcabdb"   
   unique = set(string)
   new_string = ''.join(unique)
   print(new_string) # abcd
   ```

20. 使用lambda函数

   ```python
   x = lambda a, b, c : a + b + c
   print(x(5, 10, 20)) # 35
   ```

21. 使用map函数

   ```python
   def multiply(n): 
       return n * n 
     
   list = (1, 2, 3) 
   result = map(multiply, list) 
   print(list(result)) # {1, 4, 9}
   ```

22. 使用filter函数

   ```python
   arr = [1, 2, 3, 4, 5]
   arr = list(filter(lambda x : x%2 == 0, arr))
   print (arr) # [2, 4]
   ```

23. 使用列表推导

   ```python
   numbers = [1, 2, 3]
   squares = [number**2 for number in numbers]
   print(squares) # [1, 4, 9]
   ```

24. 使用分片操作

   把一个序列切分成两部分再进行处理。

   ```python
   def rotate(arr, d):
     return arr[d:] + arr[:d]
     
   if __name__ == '__main__':
     arr = [1, 2, 3, 4, 5]
     arr = rotate(arr, 2)
     print (arr) # [3, 4, 5, 1, 2]
   ```

25. 使用链式函数

   ```python
   def add(a, b):
       return a + b
   def subtract(a, b):   
       return a - b
   a, b = 5, 10
   print((subtract if a > b else add)(a, b)) # 15
   ```

## 后话

都是蛮简单的snippets，最后一个链式函数之前还真看见过，学习了。