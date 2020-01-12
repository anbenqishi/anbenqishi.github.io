---
Layout: post
title: 【阅读】函数式编程术语
published: true
categories: ARTS rust functional 
tags: ARTS rust functional
---

## 原文

[Functional Programming Jargon in Rust](https://functional.works-hub.com/learn/functional-programming-jargon-in-rust-1b555)

## 概述

0. 原文用rust语言给出的例子，我不是很熟；这里主要是讲函数式的编程术语。

1. arity:函数的参数个数。一个函数的参数可能是确定的，也可能是不定的。

   ```rust
   let sum = |a: i32, b: i32| { a + b }; // The arity of sum is 2
   ```

2. Higher-Order Functions(HOF):高阶函数，它拿函数当作它的参数，或者它返回一个函数。

   ```rust
   let filter = | predicate: fn(&i32) -> bool, xs: Vec<i32> | {
       return xs.into_iter().filter(predicate).collect::<Vec<i32>>();
   };
   
   let is_even = |x: &i32| { x % 2 == 0 };
   
   filter(is_even, vec![1, 2, 3, 4, 5, 6]);
   ```

3. Closure:闭包，它是一个作用域，在其范围内当创建一个函数时，保持变量对函数有效（可用）。这个还是看下例子（给的这个例子不是说明partial application的吗，晕？）：

   ```rust
   let add_to = | x：i32 | { move | y : i32 | { x + y} };
   // 这里x=5在add_to_five闭包保持有效
   let add_to_five = add_to(5);
   //这里给y赋值3，由于闭包内的参数有效，所以可以计算x+y了
   add_to_five(3); // => 8
   ```

   很有用有没有，可以组装参数。提到的一个应用是在事件handlers中，在实际被call时，还可以访问到上层（parents）的参数。

4. Partial Application:有一个原始函数，我们再创建了一个新的函数，这个函数是在原始函数的基础上给部分其参数赋值生成的。这种行为我们称之为partially apply，即部分应用（感觉跟closure讲重了）。

   ```rust
   #[macro_use]
   extern crate partial_application;
   
   fn foo(a: i32, b: i32, c: i32, d: i32, mul: i32, off: i32) -> i32 {
       (a + b*b + c.pow(3) + d.pow(4)) * mul - off
   }
   
   let bar = partial!( foo(_, _, 10, 42, 10, 10) );
   
   assert_eq!(
       foo(15, 15, 10, 42, 10, 10),
       bar(15, 15)
   ); // passes
   ```

5. Currying:柯里化，即把一个拥有多个参数的函数，转换为每次只接受一个参数的函数。每次函数调用都只接受一个参数，并返回一个单参数函数，直到所有参数都被使用。举个例子：

   ```rust
   fn add(x: i32) -> impl Fn(i32)-> i32 {
       return move |y| x + y;
   }
   
   let add5 = add(5);
   add5(10); // 15
   ```

   

6. Auto Currying:把一个多参数的函数，转换成一个接受更少参数的函数。如果函数所需要的参数个数，恰好等于所给予的参数个数，则被求值。Rust语言当前暂不支持？

7. Referential Transparency:一个表达式，如果能被其值所替换，且不改变程序的行为，我们就说这是引用透明的。比如如下函数：

   ```rust
   let greet = || "Hello World!";
   ```

   `greet()`调用可以被`Hello World!`所替换，我们说`greet`是引用透明的。

8. Lambda:一个匿名函数，可以被当作一个值来使用。

   ```rust
   fn  increment(i: i32) -> i32 { i + 1 }
   
   let closure_annotated = |i: i32| { i + 1 };
   let closure_inferred = |i| i + 1;
   ```

9. Lambda Calculus:数学的一个分支，用函数来创建通用计算模型（注：不懂啥意思）。

10. Purity:我们说一个函数是pure的，其返回值只依赖于其输入，并且没有副作用。也就是说输入a，那么输出一定是b，不会说某一时刻输出不是b。

   ```rust
   let greet = |name: &str| { format!("Hi! {}", name) };
   
   greet("Jason"); // Hi! Jason
   ```

   下面是个反例：

   ```rust
   let name = "Jason";
   
   let greet = || -> String {
       format!("Hi! {}", name)
   };
   
   greet(); // String = "Hi! Jason"
   ```

   上述例子的输出依赖于函数以外的数据存储。

   ```rust
   let mut greeting: String = "".to_string();
   
   let mut greet = |name: &str| {
       greeting = format!("Hi! {}", name);
   };
   
   greet("Jason");
   
   assert_eq!("Hi! Jason", greeting); // Passes
   ```

   这个例子则是把函数外的状态给改变了（副作用）。

11. Side effects:一个函数或表达式有副作用，是指除了返回一个值外，它还与外部的可变状态交互。

    ```rust
    use std::time::SystemTime;
    
    let now = SystemTime::now();
    ```

    ```rust
    println!("IO is a side effect!");
    // IO is a side effect!
    ```

    

12. Idempotent:一个函数是幂等的，是说把函数的结果重新作为函数参数应用到函数上，不会产生不同的结果，即结果不变（这个是数学上的概念，可以从数学上来理解）。

    ```rust
    // Custom immutable sort method
    let sort = | x: Vec<i32> | -> Vec<i32> {
        let mut cloned_x = x.clone();
        cloned_x.sort();
        return cloned_x;
    };
    ```

    然后我们使用上述方法：

    ```rust
    let x = vec![2 ,1];
    let sorted_x = sort(sort(x.clone()));
    let expected = vec![1, 2];
    assert_eq!(sorted_x, expected); // passes
    ```

    还有，比如：

    ```rust
    let abs = | x: i32 | -> i32 {
        return x.abs();
    };
    
    let x: i32 = 10;
    let result = abs(abs(x));
    assert_eq!(result, x); // passes
    ```

    

13. Function Composition:函数合成，数学看很直观，就是$$f(x) = g(h(x))$$。f(x)就是个合成的函数。

    ```rust
    macro_rules! compose {
        ( $last:expr ) => { $last };
        ( $head:expr, $($tail:expr), +) => {
            compose_two($head, compose!($($tail),+))
        };
    }
    
    fn compose_two<A, B, C, G, F>(f: F, g: G) -> impl Fn(A) -> C
    where
        F: Fn(A) -> B,
        G: Fn(B) -> C,
    {
        move |x| g(f(x))
    }
    ```

    我们可以应用上述定义的函数：

    ```rust
    let add = | x: i32 | x + 2;
    let multiply = | x: i32 | x * 2;
    let divide = | x: i32 | x / 2;
    
    let intermediate = compose!(add, multiply, divide);
    
    let subtract = | x: i32 | x - 1;
    
    let finally = compose!(intermediate, subtract);
    
    let expected = 11;
    let result = finally(10);
    assert_eq!(result, expected); // passes
    ```

14. Point-Free Style:编写的函数定义没有显式声明其使用的参数。这种风格通常需要柯里化或是其他高阶函数。也称为Tacit programming（不知道怎么翻译，这段话没有例子也不清楚怎么理解）。

15. Predicate:断言是一个函数，对于给定值返回布尔值。通常是用来作为数组过滤的回调。看例子：

    ```rust
    let predicate = | a: &i32 | a.clone() > 2;
    
    let result = (vec![1, 2, 3, 4]).into_iter().filter(predicate).collect::<Vec<i32>>();
    
    assert_eq!(result, vec![3, 4]); // passes
    ```

16. Contracts:在运行时，一个函数或表达式的行为，对其输入输出有一系列的规则来保证其责任与义务，我们就说它是受契约约束的。契约被违反时，通常要报告错误。

    ```rust
    let contract = | x: &i32 | -> bool {
        return x > &10;
    };
    
    let add_one = | x: &i32 | -> Result<i32, String> {
        if contract(x) {
            return Ok(x + 1);
        }
        return Err("Cannot add one".to_string());
    };
    ```

    ```rust
    let expected = 12;
    match add_one(&11) {
        Ok(x) => assert_eq!(x, expected),
        _ => panic!("Failed!")
    }
    ```

17. Category:在范畴论中，一个category是objects和morphisms的集合。在编程中，一般把types当作objects，fuctions当作是morphisms。一个有效的category，需要遵循3条规则：

    1. 需要有identity morphism，映射一个object到它自身。如果`a`是某个category的一个object，那么就有一个函数`a -> a`。
    2. morphisms能够合成。如果再某个category中有`a`，`b`，`c`三个objects。`f`是一个morphism `a -> b`，`g`是一个morphism `b->c`。那么`g(f(x))`与`(g • f)(x)`等价。
    3. 合成需满足结合律。`f • (g • h)`与`（f • g）• h`。

18. Value:任何能够被赋值给变量的，都称为值。

    ```rust
    let a = 5;
    let b = vec![1, 2, 3];
    let c = "test";
    ```

19. Constant:一个变量，一旦其被赋值，不能再被重新赋值。

    ```rust
    let a = 5;
    a = 3; // error!
    ```

20. Variance:函数式编程中，variance refers to subtyping between more complex types related to subtyping between their components。Rust中的variance与再Scala或haskell中不同，用处主要是类型判断以及lifetime参数。例子如下：

    1. 默认情况下，所有的lifetimes都是co-variant的。除了`'static`，它的生命周期比其他的长。
    2. `'static`总是contra-variant的，无论其在哪里出现或使用。
    3. 如果你在`PhatomData`中使用`Cell<T>`或`UnsafeCell<T>`，那么它就是in-variant的。

21. Higher Kinded Type(HKT):Rust暂不支持。HKT是一种类型，但不是一种完整的类型，如声明一个类型名为`trait Functor<F<A>>`。Rust实现了一种轻量型的HKT。

    ```rust
    pub trait HKT<A, B> {
        type URI;
        type Target;
    }
    
    // Lifted Option
    impl<A, B> HKT<A, B> for Option<A> {
        type URI = Self;
        type Target = Option<B>;
    }
    ```

    HKT在函数式编程中比较重要（但是我没理解）。

22. Functor:一个object，实现了map函数，遍历object中的所有值，产生同类型的新functor，遵循两条规则：

    1. 保持同等性：`object.map(x => x) ≍ object`

    2. 可结合性：`object.map(compose(f, g)) ≍ object.map(g).map(f)`

       ​					其中f, g是两个任意函数。

    例如，下面可以看成是一个functor-like的操作：

    ```rust
    let v: Vec<i32> = vec![1, 2, 3].into_iter().map(| x | x + 1).collect();
    
    assert_eq!(v, vec![2, 3, 4]); // passes while mapping the original vector and returns a new vector
    ```

    如果借助HKT实现，可以定义一个表示Functor的trait：

    ```rust
    pub trait Functor<A, B>: HKT<A, B> {
        fn fmap<F>(self, f: F) -> <Self as HKT<A, B>>::Target
            where F: FnOnce(A) -> B;
    }
    ```

    然后使用它：

    ```rust
    impl<A, B> Functor<A, B> for Option<A> {
        fn fmap<F>(self, f: F) -> Self::Target
            where
                F: FnOnce(A) -> B
        {
            self.map(f)
        }
    }
    
    #[test]
    fn test_functor() {
        let z = Option::fmap(Some(1), |x| x + 1).fmap(|x| x + 1); // Return Option<B>
        assert_eq!(z, Some(3)); // passes
    }
    
    ```

    

23. Pointed Functor:一个object，有一个of函数，可以放任何single value。

    ```rust
    #[derive(Debug, PartialEq, Eq)]
    enum Maybe<T> {
        Nothing,
        Just(T),
    }
    
    
    impl<T> Maybe<T> {
        fn of(x: T) -> Self {
            return Maybe::Just(x);
        }
    }
    ```

    然后这么使用它：

    ```rust
    let pointed_functor = Maybe::of(1);
    
    assert_eq!(pointed_functor, Maybe::Just(1));
    ```

24. Lifting:在函数式编程中，Lifting意味着吧一个函数lift到一个上下文（一个Functor或Monad）中去。比如有一个函数`a -> b`，那么把它lift到`List`中去，签名就就会变成`List[a] -> List[b]`。

25. Equational Reasoning:如果一个应用由表达式组成，且没有副作用，那么关于系统的truths可以从parts中推导出来（@todo：没明白）。

26. Monoid:有一个函数可以把两个相同类型的object结合起来。最简单的一个monoid是数字的加法：

    ```rust
    1 + 1 // i32:2
    ```

    在这个例子中，数字就是object，`+`就是函数。

    在这种结合中，一个单位元必须也存在。加法的单位元是0。

    ```rust
    1 + 0 // i32: 1
    ```

    还有满足结合律：

    ```rust
    1 + (2 + 3) == (1 + 2) + 3  // bool: true
    ```

    数组的联结操作形成一个monoid：

    ```rust
    [vec![1, 2, 3], vec![4, 5, 6]].concat();
    // Vec<i32>: vec![1, 2, 3, 4, 5, 6]
    ```

    数组的单位元是`[]`：

    ```rust
    [vec![1, 2], vec![]].concat();
    // Vec<i32>: vec![1, 2]
    ```

    单位元和复合函数自身形成一个monoid：

    ```rust
    fn identity<A>(a: A) -> A {
        return a;
    }
    ```

    ```rust
    // foo是任意一个只有一个参数的函数。
    compose(foo, identity) ≍ compose(identity, foo) ≍ foo
    ```

    

27. Monad:一个monad是一个trait，它实现了Applicative和Chain的规格。chain类似于map，不过它把包裹的object给解开。chain类型可以实现如下：

    ```rust
    pub trait Chain<A, B>: HKT<A, B> {
        fn chain<F>(self, f: F) -> <Self as HKT<A, B>>::Target
            where F: FnOnce(A) -> <Self as HKT<A, B>>::Target;
    }
    
    impl<A, B> Chain<A, B> for Option<A> {
        fn chain<F>(self, f: F) -> Self::Target
            where F: FnOnce(A) -> <Self as HKT<A, B>>::Target {
            self.and_then(f)
        }
    }
    
    ```

    Monad就可以简单地从Chain和Applicative生成：

    ```rust
    pub trait Monad<A, F, B>: Chain<A, B> + Applicative<A, F, B>
        where F: FnOnce(A) -> B {}
    
    impl<A, F, B> Monad<A, F, B> for Option<A>
        where F: FnOnce(A) -> B {}
    
    #[test]
    fn monad_example() {
        let x = Option::of(Some(1)).chain(|x| Some(x + 1));
        assert_eq!(x, Some(2)); // passes
    }
    ```

    `pure`在其他函数式语言中称为`return`，`flat_map`在其他语言中称为`bind`。

28. Comonad: 一个拥有`extract`和`extend`函数的object。

    ```rust
    trait Extend<A, B>: Functor<A, B> + Sized {
        fn extend<W>(self, f: W) -> <Self as HKT<A, B>>::Target
        where
            W: FnOnce(Self) -> B;
    }
    
    trait Extract<A> {
        fn extract(self) -> A;
    }
    
    trait Comonad<A, B>: Extend<A, B> + Extract<A> {}
    ```

    可以实现Option：

    ```rust
    impl<A, B> Extend<A, B> for Option<A> {
        fn extend<W>(self, f: W) -> Self::Target
        where
            W: FnOnce(Self) -> B,
        {
            self.map(|x| f(Some(x)))
        }
    }
    
    impl<A> Extract<A> for Option<A> {
        fn extract(self) -> A {
            self.unwrap() // is there a better way to achieve this?
        }
    }
    ```

    Extract从一个fuctor中提取值。

    ```rust
    Some(1).extract(); // 1
    ```

    Extend是在Comonad是那个跑一个函数。

    ```rust
    Some(1).extend(|co| co.extract() + 1); // Some(2)
    ```

29. Applicative:一个Applicative functor是一个有`ap`函数的object。`ap`把object中的函数应用到同类型的其他对象的值上去。比如一个程序`g: (b: A) -> B`，要把它lift到`g: (fb: F<A>) -> F<B>`.需要引入一种HKT，称为`HKT3`。这个例子，我们使用Option数据类型。

    ```rust
    trait HKT3<A, B, C> {
        type Target2;
    }
    
    impl<A, B, C> HKT3<A, B, C> for Option<A> {
        type Target2 = Option<B>;
    }
    ```

    根据[Fantasy Land specification](https://github.com/fantasyland/fantasy-land#applicative)，Applicative为`ap`实现`Apply`，为`Pure`实现`of`。

    ```rust
    // Apply
    trait Apply<A, F, B> : Functor<A, B> + HKT3<A, F, B>
        where F: FnOnce(A) -> B,
    {
        fn ap(self, f: <Self as HKT3<A, F, B>>::Target2) -> <Self as HKT<A, B>>::Target;
    }
    
    impl<A, F, B> Apply<A, F, B> for Option<A>
        where F: FnOnce(A) -> B,
    {
        fn ap(self, f: Self::Target2) -> Self::Target {
            self.and_then(|v| f.map(|z| z(v)))
        }
    }
    
    // Pure
    trait Pure<A>: HKT<A, A> {
        fn of(self) -> <Self as HKT<A, A>>::Target;
    }
    
    impl<A> Pure<A> for Option<A> {
        fn of(self) -> Self::Target {
            self
        }
    }
    
    // Applicative
    trait Applicative<A, F, B> : Apply<A, F, B> + Pure<A>
        where F: FnOnce(A) -> B,
    {} // Simply derives Apply and Pure
    
    impl<A, F, B> Applicative<A, F, B> for Option<A>
        where F: FnOnce(A) -> B,
    {}
    ```

    使用Option Applicative：

    ```rust
    let x = Option::of(Some(1)).ap(Some(|x| x + 1));
    assert_eq!(x, Some(2));
    ```

30. Morphism:一个变换的函数（应该可以理解为从一个值transform到另一个值？）。

31. Endomorphism:是一个函数，输入的类型与输出的类型相同。

    ```rust
    // uppercase :: &str -> String
    let uppercase = |x: &str| x.to_uppercase();
    
    // decrement :: i32 -> i32
    let decrement = |x: i32| x - 1;
    ```

32. Isomorphism:两种类型的objects间的transformations，保持结构不丢失数据。

    如二维坐标可以存储为一个i32向量[2, 3]，或者一个结构体`{x: 2, y: 3}`。

    ```rust
    #[derive(PartialEq, Debug)]
    struct Coords {
        x: i32,
        y: i32,
    }
    
    let pair_to_coords = | pair: (i32, i32) | Coords { x: pair.0, y: pair.1 };
    let coords_to_pair = | coords: Coords | (coords.x, coords.y);
    assert_eq!(
        pair_to_coords((1, 2)),
        Coords { x: 1, y: 2 },
    ); // passes
    assert_eq!(
        coords_to_pair(Coords { x: 1, y: 2 }),
        (1, 2),
    ); // passes
    ```

    

33. Homomorphism:同态，就一个保存map的structure。事实上，一个functor就是一个categories间的同态，在映射下，它保持了原始category的structure。

    ```rust
    assert_eq!(A::of(f).ap(A::of(x)), A::of(f(x))); // passes
    assert_eq!(
        Either::of(|x: &str| x.to_uppercase(x)).ap(Either::of("oreos")),
        Either::of("oreos".to_uppercase),
    ); // passes
    
    ```

    

34. Catamorphism:一个`reductRight`函数，把一个函数应用到一个累加器和数组的每个值上去（从右到左），从而reduce到一个值上去。

    ```rust
    let sum = |xs: Vec<i32>| xs.iter().fold(0, |mut sum, &val| { sum += val; sum });
    
    assert_eq!(sum(vec![1, 2, 3, 4, 5]), 15);
    ```

35. Anamorphism：一个`unfold`函数。`unfold`即是`fold`的反操作，它从一个值生成一个list。

    ```rust
    let count_down = unfold((8_u32, 1_u32), |state| {
        let (ref mut x1, ref mut x2) = *state;
    
        if *x1 == 0 {
            println!("stopping!");
            return None;
        }
    
        let next = *x1 - *x2;
        let ret = *x1;
        *x1 = next;
    
        Some(ret)
    });
    
    assert_eq!(
        count_down.collect::<Vec<u32>>(),
        vec![8, 7, 6, 5, 4, 3, 2, 1],
    );
    ```

    

36. Hylomorphism: anamorphism 和 catamorphism的组合。

37. Apomorphism: paramorphism的反操作。类似anamorphism是catamorphism的反操作一样。paramorphism把累加器和已经被累加的值结合起来，apomorphism lets you unfold with potential to return early(这里的potential就看不懂了:cry:)。

38. Setoid:一个object，有一个`equals`函数，作用是与同类型的其他objects比较。有以下规则需要遵守：

    1. 反身性：`a.equals(a) == true`
    2. 对称性：`a.equals(b) == b.equals(a)`
    3. 传递性：`a.equals(b) ` && `b.equals(c)`，那么有`a.equals(c)`。

    把Vectore变成一个setoid，这里`Self`和`self`即是上面的a。

    ```rust
    trait Setoid {
        fn equals(&self, other: &Self) -> bool;
    }
    
    impl Setoid for Vec<i32> {
        fn equals(&self, other: &Self) -> bool {
            return self.len() == other.len();
        }
    }
    
    assert_eq!(vec![1, 2].equals(&vec![1, 2]), true); // passes
    ```

39. Semigroup:一个object，有一个`combine`函数，把它与其他同类型的object combine起来（注：combine什么作用？）。作为一个Semigroup需要满足以下规则：

    1. 结合律：`a.combine(b).combine(c)`等价于`a.combine(b.combine(c))`

       ```rust
       use itertools::concat;
       
       trait Semigroup {
           fn combine(&self, b: &Self) -> Self;
       }
       
       impl Semigroup for Vec<i32> {
           fn combine(&self, b: &Self) -> Vec<i32> {
               return concat(vec![self.clone(), b.clone()]);
           }
       }
       
       assert_eq!(
           vec![1, 2].combine(&vec![3, 4]),
           vec![1, 2, 3, 4],
       ); // passes
       
       assert_eq!(
           a.combine(&b).combine(&c),
           a.combine(&b.combine(&c)),
       ); // passes
       ```

40. Foldable:一个object，有一个`foldr/l`函数，可以把此object转变为其他类型。`rats`库里面只实现了`fold_right`，它等价于**Fantasy Land Foldable**的`reduce`，声明如下：

    ```rust
    fantasy-land/reduce :: Foldable f => f a ~> ((b, a) -> b, b) -> b
    ```

    ```rust
    use rats::foldable::Foldable;
    use rats::kind::IntoKind;
    use rats::kinds::VecKind;
    
    let k = vec![1, 2, 3].into_kind();
    let result = VecKind::fold_right(k, 0, | (i, acc) | i + acc);
    assert_eq!(result, 6);
    ```

    

41. Lens:它是一个类型，给其他数据结构提供getter和setter。

    ```rust
    trait Lens<S, A> {
        fn over(s: &S, f: &Fn(Option<&A>) -> A) -> S {
            let result: A = f(Self::get(s));
            return Self::set(result, &s);
        }
        fn get(s: &S) -> Option<&A>;
        fn set(a: A, s: &S) -> S;
    }
    
    #[derive(Debug, PartialEq, Clone)]
    struct Person {
        name: String,
    }
    
    #[derive(Debug)]
    struct PersonNameLens;
    
    impl Lens<Person, String> for PersonNameLens {
        fn get(s: &Person) -> Option<&String> {
            return Some(&s.name);
        }
    
        fn set(a: String, s: &Person) -> Person {
            return Person {
                name: a,
            }
        }
    }
    ```

    类似于面向对象里的。

    ```rust
    let e1 = Person {
        name: "Jason".to_string(),
    };
    let name = PersonNameLens::get(&e1);
    let e2 = PersonNameLens::set("John".to_string(), &e1);
    let expected = Person {
        name: "John".to_string()
    };
    let e3 = PersonNameLens::over(&e1, &|x: Option<&String>| {
        match x {
            Some(y) => y.to_uppercase(),
            None => panic!("T_T") // lol...
        }
    });
    
    assert_eq!(*name.unwrap(), e1.name); // passes
    assert_eq!(e2, expected); // passes
    assert_eq!(e3, Person { name: "JASON".to_string() }); // passes
    ```

    Lens是可以组合的，这样对于深度嵌套的数据可以容易进行不可变的（是指原数据不可变吧）更新。

    ```rust
    struct FirstLens;
    
    impl<A> Lens<Vec<A>, A> for FirstLens {
      fn get(s: &Vec<A>) -> Option<&A> {
         return s.first();
      }
    
      fn set(a: A, s: &Vec<A>) -> Vec<A> {
          unimplemented!();
      }
    }
    
    let people = vec![Person { name: "Jason" }, Person { name: "John" }];
    Lens::over(composeL!(FirstLens, NameLens), &|x: Option<&String>| {
      match x {
          Some(y) => y.to_uppercase(),
          None => panic!("T_T")
      }
    }, people); // vec![Person { name: "JASON" }, Person { name: "John" }];
    ```

    

42. Type Signature: Rust中的每个函数，都有表明他们参数的类型，以及返回值的类型（是指函数签名？）。

    ```rust
    // add :: i32 -> i32 -> i32
    fn add(x: i32) -> impl Fn(i32)-> i32 {
        return move |y| x + y;
    }
    
    // increment :: i32 -> i32
    fn increment(x: i32) -> i32 {
        return x + 1;
    }
    ```

    如果一个函数接受另一个函数作为其参数，后者会被括号包起来。

    ```rust
    // call :: (a -> b) -> a -> b
    fn call<A, B>(f: &Fn(A) -> B) -> impl Fn(A) -> B + '_ {
        return move |x| f(x);
    }
    ```

    字母a, b, c, d一般用来表示一般类型的参数。下面这个版本的`map`，第一个参数是一个函数，它把a类型的值转换为b类型，第二个参数是a类型的一个数组，返回值是b类型的一个数组。

    ```rust
    // map :: (a -> b) -> [a] -> [b]
    fn map<A, B>(f: &Fn(A) -> B) -> impl Fn(A) -> B + '_ {
        return move |x| f(x);
    }
    ```

43. Algebraic data type:一个复合类型，把其他类型放在一起。两个常见的代数类型是`sum`和`product`。

    1. Sum Type:两个类型组合成另一个类型。之所以取名为sum，是说结果类型的可能值的个数，是输入类型的和。

       ```rust
       enum WeakLogicValues {
          True(bool),
          False(bool),
          HalfTrue(bool),
       }
       // WeakLogicValues = bool + otherbool + anotherbool
       ```

    2. Product Type: 以一种让人熟悉的方式把类型结合在一起：

       ```rust
       struct Point {
           x: i32,
           y: i32,
       }
       // Point = i32 x i32
       ```

       之所以称为product，是说数据结构的所有可能值是不同值的乘积。许多语言有tuple类型，是product type的最简单形式。

44. Option:它是一个sum type，有2个cases，一般称为Some和None。Option一般用于组合函数，通常没有返回值。

    ```rust
    let mut cart = HashMap::new();
    let mut item = HashMap::new();
    item.insert(
        "price".to_string(),
        12
    );
    cart.insert(
        "item".to_string(),
        item,
    );
    
    fn get_item(cart: &HashMap<String, HashMap<String, i32>>) -> Option<&HashMap<String, i32>> {
        return cart.get("item");
    }
    
    fn get_price(item: &HashMap<String, i32>) -> Option<&i32> {
        return item.get("price");
    }
    ```

    ```rust
    fn get_nested_price(cart: &HashMap<String, HashMap<String, i32>>) -> Option<&i32> {
        return get_item(cart).and_then(get_price);
    }
    
    let price = get_nested_price(&cart);
    
    match price {
        Some(v) => assert_eq!(v, &12),
        None => panic!("T_T"),
    }
    ```

    Option通常也被称为Maybe（这是Haskell语言里面的叫法，终于知道一个了）。Some有时称为Just，None称为Nothing。

## 后记🐒

太多内容了，不好消耗，一个是函数式还不熟，一个Rust也还不熟，之前只看了一点点Haskell，完全不够用。学海无涯。估计还是多多回顾原文，包含了好多链接，或者哪天我好好补充完整。不过作者也说了，不用过于纠结术语了，主要还是学以致用。



