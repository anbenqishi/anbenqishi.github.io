---
layout: post
title: Linux下使用Google Test C++
published: true
tags: Linux C++
---

   昨天想找个C++的测试框架时，发现了Google开源测试框架。虽然没用过其他的C++测试框架，但作为一个G Fan，马上开工使用。不过昨天只是阅读了它的Primer，今天在Fedora 12下安装试用。
   
  安装就是典型的configre make make install，这就不罗嗦。倒是安装完后，要记得进入/etc/ld.so.conf中添加路径/usr/local/lib，因为gtest的共享库就放在那呢，否则运行的话会提示说找不到某某库。
  
  gtest的例子官网上都有给出啦，讲下注意事项：编译的话用的是这个命令：
  
      gcc $(gtest-config --ldflags --libs) -o xxx  xxx.cpp
      
  获得输出文件后，
  
      gtester [-o test.log] -k xxx
      
  其中中括号里面的是可选的，如果你想要把测试结果保存起来的话。
  
  你还可以参看这两篇文章：
  
 [google开源测试框架的使用(一)](http://tech.ddvip.com/2009-02/1234225401107951.html)
 
 [google开源测试框架的使用(二)](http://tech.ddvip.com/2009-02/1234225491107952.html) 
        
  然后就可以好好玩下这个框架了，具体请看这个玩转gtest系列教程：
  
[玩转gtest](http://www.cnblogs.com/coderzh/archive/2009/04/06/1426755.html)
               
  写下，方便查阅。