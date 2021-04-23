---
layout: post
title: 【TIPS】Linux下git clone代理问题
published: true
categories: git ARTS
tags: git ARTS
---

在Linux下，git clone翻墙失败：

````bash
root@p4-16:~# git clone https://github.com/p4lang/scapy-vxlan
Cloning into 'scapy-vxlan'...
fatal: unable to access 'https://github.com/p4lang/scapy-vxlan/': gnutls_handshake() failed: The TLS connection was non-properly terminated.
````

之前在某处看到说，原生的git是使用gnutls加密，对于使用proxy来说可能会有问题，建议重新编译成openssl的，于是根据网上教程一番折腾，还是不行：

````bash
 OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to github.com:443
````

根据[stackoverflow的这个回答](https://stackoverflow.com/questions/49345357/fatal-unable-to-access-https-github-com-xxx-openssl-ssl-connect-ssl-error#comment85690804_49345357)，我重新考虑了下自己的代理配置。整理了下大概配置了如下git config:

````bash
http.sslverify=false      # 不建议设置，安全性问题，而且后来看对问题没有帮助
http.sslbackend=openssl   #如果是使用gnutls的话，这么写会fail
http.proxy=socks5://127.0.0.1:1080 #Windows无此设置
https.proxy=socks5://127.0.0.1:1080 #Windows无此设置
http.https://github.com.proxy=socks5://127.0.0.1:1080
https.https://github.com.proxy=socks5://127.0.0.1:1080
remote.origin.proxy=socks5://127.0.0.1:1080 #Windows无此设置
url.https://.insteadof=git://   #这个应该关系不大
````

后来经过几次系统更新后，git貌似又被换回`gnutls`了，于是放弃`openssl`这条路了。

重新思考下代理，socks5代理是可行的，我用浏览器可以正常翻。而且在Windows上这么设置确实ok。

想到之前某处有说过sock5代理可能git不能很好支持？想到还是换成http代理试试吧，参照[这篇post](https://srelinux.blogspot.com/2020/01/1.html)把privoxy给安上了。然后把git的代理改了：

````bash
http.proxy=http://127.0.0.1:8118
https.proxy=http://127.0.0.1:8118
http.https://github.com.proxy=http://127.0.0.1:8118
https.https://github.com.proxy=http://127.0.0.1:8118
````

bong~终于ok了。

### linux wget代理

参考[此篇](https://www.cnblogs.com/frankyou/p/6693256.html)，把`/etc/wgetrc`的内容拷贝到本地命名为`.wgetrc`，内容如下：

```bash
#You can set the default proxies for Wget to use for http, https, and ftp.
# They will override the value in the environment.
https_proxy = http://127.0.0.1:8087/
http_proxy = http://127.0.0.1:8087/
ftp_proxy = http://127.0.0.1:8087/

# If you do not want to use proxy at all, set this to off.
use_proxy = on
```

这样不会影响到全局。由于我是刷脚本，不是敲`wget`命令，如果指示一次命令使用，可以用如下方式：

````bash
wget -c -r -np -k -L -p -e "http_proxy=http://127.0.0.1:8087" http://www.subversion.org.cn/svnbook/1.4/
````

即用`-e`带出代理命令。