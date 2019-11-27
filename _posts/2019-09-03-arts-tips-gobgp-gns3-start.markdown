---
title: centos中安装gns3&&开跑gobgp?
layout: post
published: true
categories: gobgp 
tags: network gobgp 
---

自己曾经做过bgp，还用了蛮长的一段时间。先前看到有用go实现bgp的项目，一直想玩，各种耽搁。这次工作刚好又有关联性，就想学习一下gobgp这个项目。一来学习go，之前看过语法一直还没有看过实际项目；二来温习一下bgp协议，同时看看gobgp这个项目实现，与我之前做的项目的差异，取长补短。

gobgp目前看来只适合在linux中跑，官方也只提供了Linux的release；想要在mac中重新编译一遍，估计又要折腾好久。还是等完玩一遍gobgp再决定是否自己编译吧。

## 安装gns3之路

1. 先安装[图形界面](https://www.cnblogs.com/Amedeo/p/8323787.html)，因为gns3要使用界面的说；

2. Virtual box新增配置host-only网络，并在centos7虚拟机中使能：先全局新增host-only网卡，再配置，后在虚拟机设置中使能；

3. 在自己中意的terminal中开始按[教程](https://gns3.com/discussions/how-to-install-gns3-on-centos-7-)操作安装gns3；

4. 几乎完成了，折腾了一下分辨率以及host-only网络，安装了vbox的扩展增强包，虽然最后效果不理想，效果还行；然后磁盘空间又不足了，赶紧下了哥bleachbit清理了一下。结果，然后，还是碰到了一个悲剧：我是用vbox安装的centos虚拟机，然后安装一个cisco的switch镜像时，弹出要支持KVM才行，但是我确定有勾选了，还是不行，搜了一圈，在gns3的论坛上有[如下解答](https://www.gns3.com/qa/-the-remote-server-doesn-t-suppo)，无语了：

   > If KVM support is required (and this is the case for for the most new appliances e.g. Juniper), first of all one needs (for Intel CPUs) Intel VT-EPT (Extended Page Tables) - VT-x is not enough! On Linux one doesn't need VM, on Windows / Mac VM has to run in VMWare, not VirtualBox...

   摆明了说vbox貌似还是不支持此种设置，晕死。不折腾了，我还是用vmware fusion + ubuntu再装一次的了。

5. ubuntu比较不怎么折腾，安装好了，安装cisco-nvos switch的时候提示我内存不足，竟然开口就要3G。我去，当内存不要钱啊！那个拓扑还要3台设备哪，9G？！直接把我机子撑爆的节奏吗？罢了罢了。我不弄了。

   

   ## gobgp

   按这个[教程](https://www.sdnlab.com/22918.html)初步了解下gobgp的使用就好了。大概知道怎么用，后续自己编译看代码深入学习吧。

   

   