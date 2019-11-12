---
layout: post
title: python问题记录1
published: true
categories: python scapy
tags: python scapy
---

## python pip更新包

一次性更新所有需要更新的包，这条命令是[stackoverflow](https://stackoverflow.com/questions/2720014/how-to-upgrade-all-python-packages-with-pip)上给出的（为啥pip自身不支持更新所有包呢？可能是因为包依赖问题，pip不想背锅吧）

```bash
pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U
```

## scapy问题1

我在Linux上安装的是`Python 2.7.12, scapy 2.2.0-dev`版本，我在win上安装的是`Python 3.7.0, scapy 2.4.3`版本，如下命令，在linux上正常，在win下报错了：

```python
## linux
>>> ans, unans = sr(IP(dst=["yahoo.com","slashdot.org"])/TCP(dport=[22,80,443],flags="S"))
>>> ans.nsummary(lfilter = lambda (s,r): r.sprintf("%TCP.flags%") == "SA")
0000 IP / TCP 192.168.193.158:ftp_data > 98.137.246.8:https S ==> IP / TCP 98.137.246.8:https > 192.168.193.158:ftp_data SA / Padding
0001 IP / TCP 192.168.193.158:ftp_data > 216.105.38.15:https S ==> IP / TCP 216.105.38.15:https > 192.168.193.158:ftp_data SA / Padding
0002 IP / TCP 192.168.193.158:ftp_data > 216.105.38.15:http S ==> IP / TCP 216.105.38.15:http > 192.168.193.158:ftp_data SA / Padding
0003 IP / TCP 192.168.193.158:ftp_data > 98.137.246.8:http S ==> IP / TCP 98.137.246.8:http > 192.168.193.158:ftp_data SA / Padding
                
## win
>>> ans, unans = sr(IP(dst=["yahoo.com","slashdot.org"])/TCP(dport=[22,80,443],flags="S"))
>>> ans.nsummary(lfilter = lambda (s,r): r.sprintf("%TCP.flags%") == "SA")
  File "<ipython-input-105-eaf1a954d65e>", line 1                         
    ans.nsummary(lfilter = lambda (s,r): r.sprintf("%TCP.flags%") == "SA")
                                  ^                                       
SyntaxError: invalid syntax                                               
                                                                                                     >>>                                          
```

不知道是python的接口变了，还是scapy的接口变了，但我是按[scapy官方教程](https://scapy.readthedocs.io/en/latest/usage.html#starting-scapy)敲的命令。看这个教程的print语法，明显是是2.x的。稍微看了下3.x的lambda，貌似是参数表是不带括号的。去带括号确实就不报错了。

## scapy问题2

```python
## win(Linux上貌似不支持traceroute函数，估计那个scapy版本还不支持)
>>> a = traceroute(["www.baidu.com", "www.secdev.org"], verbose=0)
>>> a.world_trace()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-111-e557f2028815> in <module>
----> 1 a.world_trace()

AttributeError: 'tuple' object has no attribute 'world_trace'
>>> a
(<Traceroute: TCP:22 UDP:0 ICMP:16 Other:0>,
 <Unanswered: TCP:22 UDP:0 ICMP:0 Other:0>)
>>>
```

解决方式如下（也是从这个[回答](https://stackoverflow.com/questions/17290114/attributeerror-tuple-object-has-no-attribute)上得到的启发）：

```python
# 我们要把调用形式改为即可：
>>> a[0].world_trace()
```

而且在win上要跑起`traceroute_map(["www.google.co.uk", "www.secdev.org"])`这个python命令，还需要安装`cartopy`模块，看上去一个很不好安装的模块，暂时放弃（可以看这个[回答](https://stackoverflow.com/questions/53697814/using-pip-install-to-install-cartopy-but-missing-proj-version-at-least-4-9-0)）。