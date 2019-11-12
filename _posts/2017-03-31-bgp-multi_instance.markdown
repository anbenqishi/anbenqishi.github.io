---
layout: post
title: BGP多实例
published: true
tags: bgp network
categories: network
---

## [Cisco ASR9000系列路由器](http://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/asr9k_r5-2/routing/command/reference/b_routing_cr52xasr9k/b_routing_cr52xasr9k_chapter_01.html)

每个BGP实例都是一个独立的进程，运行在相同或是不同的RP/DRP节点上。BGP实例维持各自的前缀表，不与其他实例共享。在分布式BGP情况下，不需要一个通用的Adj-RIB-in（bRIB）（**？？**）。实例间不相互通信，也不与对端建立邻居。每个实例都可以单独与其他设备建立邻居。

Multi-AS BGP使能每个BGP实例配置不一样的AS号。
多实例与多AS BGP提供以下能力：

- 在单台设备上，使用一个通用路由框架，合并多台设备提供的服务；
- 在不同的BGP实例上使能不能不同的AF，达到隔离地址族的作用；
- 在不同的BGP实例上分发peer会话，提升会话规模，可以容纳更多的peer会话；
- 不同的BGP实例拥有各自的BGP路由表，提升整体路由规模（尤其是RR场景）；
- 在特定场景下，改善BGP收敛性能（？？）；
- 所有实例都支持所有的BGP功能，包括NSR；
- The load and commit router-level operations can be performed on previously verified or applied configurations.

限制：
- 最多支持4个BGP实例；
- 每个BGP实例需要一个唯一的router-id；
- 每个BGP实例只能配置一个AF（VPNv4, VPNv6 && RT-Constrain地址族可以配置在多个BGP实例下）；
- 如果实例配置了IPv4/IPv6 Labeled-Unicast地址族，那么IPv4/IPv6 Unicast也需要在同一个地址族下；
- 如果实例配置了IPv4/IPv6 Unicast地址族，那么IPv4/IPv6 Multicast也需要在同一实例下；
- 一个实例的所有配置变化可以一起commit；但是多个实例的配置变化不能一起commit。（**？？**）
- 其他补充[（cisco论坛）](https://supportforums.cisco.com/discussion/11719386/bgp-multi-instances)：
    - 如果VPNv4/VPNv6地址族横跨多个实例，实例不共享VRF路由表；
    - 有互导需要的所有VRF必须配置在同一BGP实例下，实例间不能进行互导；
    - MDT SAFI, MVPN SAFI && MVPN-specific BGP需要配置在同一个实例节点下。使用者需要确认所有的multicast VRFs配置在同一个实例下。此实例会与multicast进程通信。
    - IPv4 Unicast/IPv4 Labeled-unicast可以在一个实例上，而IPv6 Unicast/IPv6 Labeled-unicast在另一个实例上；
    - 实例间的peer地址必须唯一；
配置：      
	**router bgp** *as-number* [**instance** *instance-name*]  
	**no router bgp** [*as-number*]  
router# configure  
router(config)# router bgp 100 instance inst1  

## [Juniper](https://www.juniper.net/techpubs/en_US/junos/topics/reference/configuration-statement/routing-instances-edit.html)

版本： Junos OS Release 7.4

语法： routing-instances *routing-instance-name* { ... }






