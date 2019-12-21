---
layout: post
title: 【tip】Linux下的代理小结
published： true
tags: ARTS tips proxy
categories: ARTS tips proxy
---

这里以Ubuntu为例。

这里主要以Ubuntu为例。

本来没有的事，某些团体硬要让人折腾。这里主要以Ubuntu为例。

1. 首先，你要有ss服务器；本地搞个ss客户端，启动即可，默认我们是启用socks代理；

2. 如果仅仅只是浏览器翻墙，有switchyOmega就好了，可以很好地支持是否代理访问；

3. 如果还想让git啊，go啊，或者命令行访问命令如wget、curl、apt等也经过代理，就要稍微费点事儿了（感觉是我自己费事，网络渣，效果差）；

4. 目前我没有看到比较通用的方案，所以简单描述下自己折腾过的方式，亲测可用，虽然好像不是那么好用（主要我这边网络本身太差...）;

5. 哦，对了，通用的翻墙方案都是ss，这个不再细说，这方面网上教程机会没啥很大差异。

6. 有用的[list](https://ssr.tools/495)，你懂的：`https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt`

   ### git

   主要是通过git config来配置，在Linux（MacOS）下就是home下的`.gitconfig`文件（windows的自己找找），通过如下配置来实现：

   ```bash
   git config --global http.proxy 'socks5://127.0.0.1:1080'
   git config --global https.proxy 'socks5://127.0.0.1:1080'
   ```

   之前试过，clone时有SSL错误的，有建议再配置如下：

   ```bash
   git config http.sslVerify false
   ```

   或是在config文件的http项下添加如下：

   ```bash    
   sslVerify = false
   ```

   当然有说这样配置极不安全的，慎用，只出现在某些场景下(本来这里应该有链接的，不巧之前没记录下来)。

   ==2019-12-20 update==

   在windows下clone github.com的仓库奇慢无比，我把github.com加入pac也不行。搜了下，普遍问题，用[如下方式](https://www.zhihu.com/question/27159393)解决，只针对github，避免clone其他仓库也受到影响：

   ```bash
# 后面的socks根据自己的代理设置做相应的变化：
   git config --global http.https://github.com.proxy socks5://127.0.0.1:1080
   git config --global https.https://github.com.proxy socks5://127.0.0.1:1080
   ```
   
   ### go

   我试用了两种方式，貌似都可以：

   第一种比较简单，直接设置[goproxy](https://juejin.im/post/5cd945946fb9a032060c47a3):

   ```bash
   export GO111MODULE=on # 我是1.12，配置此项貌似没显示，估计可以不用了
   export GOPROXY=https://goproxy.io
   ```

   你可以写进环境变量中。

   第二种还是[配置如何使用ss]([https://ybilly.com/2018/07/03/go-get%E5%88%A9%E7%94%A8ss%E7%9B%B4%E6%8E%A5%E7%BF%BB%E5%A2%99/](https://ybilly.com/2018/07/03/go-get利用ss直接翻墙/)):

   ```bash
set http_proxy=socks5://127.0.0.1:1080
   set https_proxy=socks5://127.0.0.1:1080
```
   
都说go会去都这两个变量，我也没去深究...
   
### Linux
   
这里主要是说curl/wget/apt这些命令行命令如何使用代理。
   
   #### curl/wget等
   
   主要问题貌似是不能直接使用ss的socks代理形式，需要转为使用privoxy转换一下，不赘述了，大家看[这篇文章](https://huangweitong.com/229.html)就好了，能实现根据pac来代理，蛮好的。
   
   #### apt

   由于我用的是UBUNTU系统，蛋疼的是，某一个仓库貌似只能翻墙上了，于是折腾了下，网上的意见主要就是在`/etc/apt/apt.conf.d/`文件夹下添加一个conf文件，内容大致如下：

   ```bash
# http/https代理是利用privoxy，参看curl/wget的设置
   Acquire::http::Proxy "http://127.0.0.1:8118";
   Acquire::https::Proxy "http://127.0.0.1:8118";
   Acquire::socks5::Proxy "socks://127.0.0.1:1080";
   ```
   
   配置后会变成对所有的apt网址生效，但是目前没有更好的pac方案（或者我没找到）。
   
   ### pip支持代理
   
   本地是windows7 + pip3环境，参考[stackoverflow其中一个答案成功](https://stackoverflow.com/questions/22915705/how-to-use-pip-with-socks-proxy)：
   
   ```bash
   pip install pysocks
   pip install -r requirements.txt --proxy socks5:127.0.0.1:1080
   ```
   
   
   
   ## 吐槽
   
   我这边网路太慢了，连接代理服务器也是断断续续，导致有些效果估计体现不出来，哭了。