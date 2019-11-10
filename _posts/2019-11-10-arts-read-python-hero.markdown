---
Layout: post
Title: 【阅读】学习Python：从0到英雄
Published: true
Categories: ARTS python
Tags: ARTS python
---

## 原文

## [Learning Python: From Zero to Hero](https://medium.com/free-code-camp/learning-python-from-zero-to-hero-120ea540b567)

## 概述 

1. 什么是Python？根据Python始祖Guido大佬的话来说：Python是高级编程语言，其核心设计哲学是代码可读性，语法上允许程序员可以用少量代码来表达概念。

2. 对我（作者）而言，学习Python的第一理由是...它比较漂亮（呵呵...），无论是编码或者是表达思路都比较自然；另一个原因是Python可以用在很多场景中，如数据科学，web开发以及机器学习等。Quora，Pinterest和Spotify都使用Python作为其后端web开发语言。所以开始学一点Python吧。


### 基础

1. 变量

   可以把变量当成一个存储有值的单词。比如你想要用一个变量“one”存储数值“1”，可以这么做：

   ```python
   one = 1
   ```

   很简单对不对。刚刚我们把数值`1`赋值给变量`one`了。

   ```python
   two = 2
   some_number = 10000
   ```

   你可以把任意值赋值给任意变量，就像上面我们做的那样。

   除了整数，我们同样可以使用布尔值（True/False），字符串，单精度浮点值以及其他数据类型。

   ```python
   # booleans
   true_boolean = True
   false_boolean = False
   
   # string
   my_name = "Leandro Tk"
   
   # float
   book_price = 15.80
   ```

2. 控制流：条件语句

   “If”使用一个表达式来评估一条语句是真是假，如果是真的，就执行“if”里面的语句。

   ```python
   if True:
     print("Hello Python If")
   
   # 2比1大，所以将执行print语句
   if 2 > 1:
     print("2 is greater than 1")
   ```

   如果“if”表达式是false的，那么else将会被执行。

   ```python
   if 1 > 2:
     print("1 is greater than 2")
   else:
     print("1 is not greater than 2")
   ```

   同样你还可以使用“elif”语句：

   ```python
   if 1 > 2:
     print("1 is greater than 2")
   elif 2 > 1:
     print("1 is not greater than 2")
   else:
     print("1 is equal to 2")
   ```

3. 循环/迭代

   在python可以以不同的方式迭代，这里介绍两种方法：`while`和`for`。

   while循环：语句为真，while里面的语句将会得到执行。所以下面将会打印1到10.

   ```python
   num = 1
   
   while num <= 10:
       print(num)
       num += 1
   ```

   while循环需要一个循环条件。如果条件一直为真，则会持续迭代下去。

   ```python
   loop_condition = True
   
   while loop_condition:
       print("Loop Condition keeps: %s" %(loop_condition))
       loop_condition = False
   ```

   `loop condition`为真，则会一直迭代，直到我们设置为`False`。

   For循环：以下循环会实现上述while循环一样的功能，打印1到10。

   ```python
   for i in range(1, 11):
     print(i)
   ```

### List：集合｜数组｜数据结构

你想把数值1存在一个变量中，后来你又想存2，3，4，5...有没有不用一堆变量来存储上述整数的方式？确实有，list就是这样的一种集合，用来存储值的表。

```python
my_integers = [1, 2, 3, 4, 5]
```

那如何从上述list中获取其中一个值呢？有个“index（索引）”的概念，list的第一个元素是index 0，第二个是index 1，以此类推。上例子更明白一点：

```python
my_integers = [5, 7, 1, 3, 4]
print(my_integers[0]) # 5
print(my_integers[1]) # 7
print(my_integers[4]) # 4
```

如果想存储整数以外的类型，如string，可以这么干：

```python
relatives_names = [
  "Toshiaki",
  "Juliana",
  "Yuji",
  "Bruno",
  "Kaio"
]

print(relatives_names[4]) # Kaio
```

接下来演示如何往list中添加元素。最常用的方法是`append`。

```python
bookshelf = []
bookshelf.append("The Effective Engineer")
bookshelf.append("The 4 Hour Work Week")
print(bookshelf[0]) # The Effective Engineer
print(bookshelf[1]) # The 4 Hour Work Week
```

看上面的例子就知道`append`很简单的，你值得拥有。

### Dictionary：键值数据结构

我们现在知道list是以整数为index，那有没有其他类型可以作为index的呢？这时候Dictionary结构就出场了，它是一个键值对的集合。看例子：

```python
dictionary_example = {
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}
```

其中key是作为索引指向value。所以我们获取value的方式也显而易见了。

```python
dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian"
}

print("My name is %s" %(dictionary_tk["name"])) # My name is Leandro
print("But you can call me %s" %(dictionary_tk["nickname"])) # But you can call me Tk
print("And by the way I'm %s" %(dictionary_tk["nationality"])) # And by the way I'm Brazilian
```

Dictionary的另一个特点是，你可以把任意类型当作它的value。Look：

```python
dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian",
  "age": 24
}

print("My name is %s" %(dictionary_tk["name"])) # My name is Leandro
print("But you can call me %s" %(dictionary_tk["nickname"])) # But you can call me Tk
print("And by the way I'm %i and %s" %(dictionary_tk["age"], dictionary_tk["nationality"])) # And by the way I'm Brazilian
```

像list一样，我们往Dictionary里添加元素的方法如下：

```python
dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian"
}

dictionary_tk['age'] = 24

print(dictionary_tk) # {'nationality': 'Brazilian', 'age': 24, 'nickname': 'Tk', 'name': 'Leandro'}
```

### Iteration：遍历数据结构

list的迭代是很简单的。

```python
bookshelf = [
  "The Effective Engineer",
  "The 4 hours work week",
  "Zero to One",
  "Lean Startup",
  "Hooked"
]

for book in bookshelf:
    print(book)
```

对于一个hash的数据结构，我们还是可以使用for循环的。

```python
dictionary = { "some_key": "some_value" }

for key in dictionary:
    print("%s --> %s" %(key, dictionary[key]))
    
# some_key --> some_value
```

这里我们是以Dictionary为例，还有另一种遍历方式：

```python
dictionary = { "some_key": "some_value" }

for key, value in dictionary.items():
    print("%s --> %s" %(key, value))

# some_key --> some_value
```

上面的两个参数`key` 和`value`，我们可以使用任意的其他名字来命名。

```python
dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian",
  "age": 24
}

for attribute, value in dictionary_tk.items():
    print("My %s is %s" %(attribute, value))
    
# My name is Leandro
# My nickname is Tk
# My nationality is Brazilian
# My age is 24
```

### Classes和Objects

1. 一点理论

   Objects可以看作是现实世界物件如汽车，狗或自行车的一种表示。Objects有两个主要特征：数据和行为。

   比如汽车有数据：几个轮子，几个门，座位数；还有行为：加速，停止，还剩多少油等。

   在面向对象编程中，数据即是属性（attributes），行为即是方法（methods）。

   而classes是每个object创建的蓝图。现实中汽车都有一个共同的模型（或者说大同小异）：引擎，轮子，门啊等等。每辆车就是基于这种相同的蓝图创建出来的。

2. Python面向对象编程模式：ON

   我们直接看下Python的class语法：

   ```python
   class Vehicle:
       pass
   ```

   Objects是class的实例。可以这样创建一个实例：

   ```python
   car = Vehicle()
   print(car) # <__main__.Vehicle instance at 0x7fb1de6c2638>
   ```

   这里，Vehicle是class，car就是object。现在我们给Vehicle类添加属性：轮子数，tank类型，座位数以及最高速度。

   ```python
   class Vehicle:
       def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
           self.number_of_wheels = number_of_wheels
           self.type_of_tank = type_of_tank
           self.seating_capacity = seating_capacity
           self.maximum_velocity = maximum_velocity
   ```

   每创建一个Vehicle对象就会继承这些属性。这里使用了`init`方法，我们称之为构造器方法。我们来构造一辆Tesla Model S。

   ```python
   tesla_model_s = Vehicle(4, 'electric', 5, 250)
   ```

   四轮，电动，五座，最高速250km/h。客官还满意吗？所有的属性都已经设置了。不过，我们如何获取这些属性的值呢？使用的是方法（methods），发送一个消息给对象来请求。这就是对象的行为。我们实现一下：

   ```python
   class Vehicle:
       def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
           self.number_of_wheels = number_of_wheels
           self.type_of_tank = type_of_tank
           self.seating_capacity = seating_capacity
           self.maximum_velocity = maximum_velocity
   
       def number_of_wheels(self):
           return self.number_of_wheels
   
       def set_number_of_wheels(self, number):
           self.number_of_wheels = number
   ```

   这里实现了两个方法：`number_of_wheels`和`set_number_of_wheels`。我们称之为`getter`和`setter`----前一个方法获取属性值，后一个方法给属性赋值。

   其实在Python中，我们还可以用`@property`（装饰器）来定义`getters1`和`setters`。来看一下吧：

   ```python
   class Vehicle:
       def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
           self.number_of_wheels = number_of_wheels
           self.type_of_tank = type_of_tank
           self.seating_capacity = seating_capacity
           self.maximum_velocity = maximum_velocity
       
       @property
       def number_of_wheels(self):
           return self.__number_of_wheels
       
       @number_of_wheels.setter
       def number_of_wheels(self, number):
           self.__number_of_wheels = number
   ```

   我们可以像使用属性一样来使用这两个方法：

   ```python
   tesla_model_s = Vehicle(4, 'electric', 5, 250)
   print(tesla_model_s.number_of_wheels) # 4
   tesla_model_s.number_of_wheels = 2 # setting number of wheels to 2
   print(tesla_model_s.number_of_wheels) # 2
   ```

   方法使用起来像属性，这是挺pythonic范儿的用法。当然方法还有其他用法。

   ```python
   class Vehicle:
       def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
           self.number_of_wheels = number_of_wheels
           self.type_of_tank = type_of_tank
           self.seating_capacity = seating_capacity
           self.maximum_velocity = maximum_velocity
   
       def make_noise(self):
           print('VRUUUUUUUM')
   ```

   我们调用这个方法，它简单地打印出字符串“VRUUUUUUUM”而已。

   ```python
   tesla_model_s = Vehicle(4, 'electric', 5, 250)
   tesla_model_s.make_noise() # VRUUUUUUUM
   ```

   

### 封装：隐藏信息

封装就是限制对对象数据和方法的直接访问。也就是说，从外部来看，对象的内部表示是被隐藏起来的。只有对象自身能够与内部数据交互。我们先弄懂下什么是public，什么是non-public。

1. 公有（public）实例变量

   对一个Python类来说，可以在构造函数中初始化public实例变量。

   ```python 
   class Person:
       def __init__(self, first_name):
           self.first_name = first_name
   ```

   我们把`first_name`参数值传给了public实例变量。

   ```python
   tk = Person('TK')
   print(tk.first_name) # => TK
   ```

   而在下面这个类中，

   ```python
   class Person:
       first_name = 'TK'
   ```

   我们没有传参，所有的对象实例都有一个类属性初始化为“TK”。

   ```python
   tk = Person()
   print(tk.first_name) # => TK
   ```

   我们学习了public实例变量和类属性。其实public的含义是可以去操作这个变量的值。也就是我们可以进行get和set操作。

   ```python
   tk = Person('TK')
   tk.first_name = 'Kaio'
   print(tk.first_name) # => Kaio
   ```

   这里就把`first_name`的值给修改了，因为它是public的嘛。

2. non-public实例变量

   相对的，我们可以定义non-public实例变量（PEP8里提到：我们一般不使用private这个词，因为Python中没有什么属性真的是private的）。语法上的不同在于：对于non-public实例变量，变量名前使用下划线“_”标识。这其实是一个convention，而不是一种强约束。

   ```python
   class Person:
       def __init__(self, first_name, email):
           self.first_name = first_name
           self._email = email
   ```

   其中`_email`就是我们所定义的non-public实例变量。

   ```python
   tk = Person('TK', 'tk@mail.com')
   print(tk._email) # tk@mail.com
   ```

   我们还是可以获取和更新这个变量的。所以它其实是个convention，但是我们要把它看成是API non-public的一部分。在类定义中使用方法去获取更新这个变量才是正确的做法。

   ```python
   class Person:
       def __init__(self, first_name, email):
           self.first_name = first_name
           self._email = email
   
       def update_email(self, new_email):
           self._email = new_email
   
       def email(self):
           return self._email
   ```

   这么用：

   ```python
   tk = Person('TK', 'tk@mail.com')
   print(tk.email()) # => tk@mail.com
   # tk._email = 'new_tk@mail.com' -- treat as a non-public part of the class API
   print(tk.email()) # => tk@mail.com
   tk.update_email('new_tk@mail.com')
   print(tk.email()) # => new_tk@mail.com
   ```

   

3. public方法

   这个方法可以在类外使用：

   ```python
   class Person:
       def __init__(self, first_name, age):
           self.first_name = first_name
           self._age = age
   
       def show_age(self):
           return self._age
   ```

   像这样：

   ```python
   tk = Person('TK', 25)
   print(tk.show_age()) # => 25
   ```

4. non-public方法

   这个方法的定义，前面还是使用下划线哦。

   ```python
   class Person:
       def __init__(self, first_name, age):
           self.first_name = first_name
           self._age = age
   
       def _show_age(self):
           return self._age
   ```

   可以这么用：

   ```python
   tk = Person('TK', 25)
   print(tk._show_age()) # => 25
   ```

   但是不建议。还是建议这么用(使用public方法)：

   ```python
   class Person:
       def __init__(self, first_name, age):
           self.first_name = first_name
           self._age = age
   
       def show_age(self):
           return self._get_age()
   
       def _get_age(self):
           return self._age
   
   tk = Person('TK', 25)
   print(tk.show_age()) # => 25
   ```

### 继承：行为和特征

一些对象有common的地方，如行为和特征。比如，儿子会继承老子的一些行为和特征。在面向对象编程中，类可以从其他类继承行为和特征。我们以Car为例，电动车会继承车的一些属性。我们来定义车类：

```python
class Car:
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
```

定义实例：

```python
my_car = Car(4, 5, 250)
print(my_car.number_of_wheels)
print(my_car.seating_capacity)
print(my_car.maximum_velocity)
```

我们定义一下继承关系，这里父类是作为参数传给子类的，其他啥都不用做，因为父类都为我们做好了：

```python
class ElectricCar(Car):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Car.__init__(self, number_of_wheels, seating_capacity, maximum_velocity)
```

我们用一下：

```python
my_electric_car = ElectricCar(4, 5, 250)
print(my_electric_car.number_of_wheels) # => 4
print(my_electric_car.seating_capacity) # => 5
print(my_electric_car.maximum_velocity) # => 250
```

完美。

### 我们学到了什么

1. Python的变量如何工作的；
2. 条件语句如何工作的；
3. 循环（while & for)如何工作的；
4. 如何使用Lists：集合｜数组；
5. Dictionary键值集合；
6. 如何在上述数据结构中迭代；
7. 对象和类；
8. 属性是对象的数据；方法是对象的行为；
9. 使用`getters`和`setters`，以及property装饰器；
10. 封装：隐藏信息；
11. 继承：行为和特征。

## 自己的话

python入门教程，当然学完肯定还是成为不了hero的...很久没用Python，它说到装饰器那个用法的时候以前竟然都没用过，惭愧。