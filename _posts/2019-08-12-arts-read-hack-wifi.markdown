---
layout: post
title: 【阅读】如何hack wifi
published: true
categories: ARTS kali
tags: ARTS kali
---



## 原文

[How to Hack Wi-Fi: Get Anyone’s Wi-Fi Password Without Cracking Using Wifiphisher](https://medium.com/@NullByteWht/how-to-hack-wi-fi-get-anyones-wi-fi-password-without-cracking-using-wifiphisher-1d0a6c95f67a)

## 概述

1. 获取wifi密码最快捷的方式就是社会工程了。最强有力的攻击手段就是wifi钓鱼了，它是这样的一种工具，阻断internet连接直到绝望的用户通过伪造的固件更新界面输入wifi密码。

2. 暴力破解往往费时费力，还取决于字典的复杂度。wifi钓鱼让你防不胜防，想想你在忙碌的时候断网了，这个时候即使你可能察觉到某些不一样，还是想着赶紧先上网再说吧，这样就直接落入陷阱了。
3. 欺骗的手法类似如下：某个wifi热点被截断了，导致任何连接这个热点的访问都是失效的，也就是用户感觉断网了。这时候热点里有一个同名的其他热点，不需要密码；于是你在又试了几遍原来的wifi热点后，转而登录使用了这个热点；而连上这个热点后，它提示你需要进行路由器的固件更新，看起来像是刚才那个热点之所以连不上是因为还没有进行更新，现在需要你输入密码授权更新，网络才能恢复正常。是的，还会模拟一个更新的界面，几分钟以后终于网络恢复正常了…...其实后台他们正在试验你的密码呢！
4. 是不是心动了，你也可以做了。试试Kali Linux吧。直接`apt install wifiphisher`就可以了。
5. 接下来竟然是模拟教程，我去，我看这篇文章干嘛来着...

## 后话

只是做翻译练习，选错文章了。顺便提了个醒，公共wifi谨慎使用...