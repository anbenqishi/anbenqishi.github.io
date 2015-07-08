---
layout: post
title: openSuSE设置VMWARE的网络连接 
published: true
tags: Linux
---

一不小心把自己机子上的openSUSE弄垮了，搞了一上午还是不行--菜鸟就是菜鸟。没法，只能装个虚拟机了-导师说最好在openSUSE下吧代码运行起来。
痛苦啊，上次在本地机子上装openSUSE的时候就费了好一阵时间--因为还要装一些特定的软件，make的时间老长了的说。

这次的虚拟机安装还算顺利，就是上不了网，弄了好久，终于根据网上的说明成功搞定，为了避免以后忘记，
转载于此，原文请见：[http://www.5dlinux.com/article/1/2007/linux_8865.html](http://www.5dlinux.com/article/1/2007/linux_8865.html)

-----------------------华丽的分割线------------------------------------------------
   
这两天在XP上装个虚拟机（SUSE），但SUSE不能上网，网上搜索了下结合自己的实际总结下：

使用hostonly模式共享上网

1.  在VM>>settings里设置网卡为hostonly模式，使得网络只由宿主承担，虚拟机只是和宿主位于另一个虚拟的局域网。
2.  在windows下的网络连接中，vmnet1是hostonly的接口，而Vmnet8是就是我们要使用的NAT的网络接口。因此将我们原来可用的“本地连接”对相应虚拟机网卡vmnet1共享，这里如果选择了hostonly必须对vmnet1共享(很重要)，具体方式是右键单击“本地连接”，选择“属性”，再选择“高级”，勾选共享
3.  实际上此时宿主相对虚拟机的ip地址为192.168.0.1，因此将Linux的ip设置为192.168.0.XXX，XXX不等于1，然后DNS和网关地址都为192.168.0.1。这样共享上网便设置成功.
4.  重起服务  service network restart

现在我的SUSE可以上网了，但XP依旧不能使用SAMBA和FTP去连SUSE，郁闷中（我在公司的PC都可以连接，但同样的方法在虚拟机上好像不行了）