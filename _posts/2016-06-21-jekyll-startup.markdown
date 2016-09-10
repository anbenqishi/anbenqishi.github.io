---
layout: post
title: jekyll启动问题
published: true
tags: blog
---


有好久没写了，今天启动jekyll，老是提示错误：

<pre>
F:\GitHub\anbenqishi.github.io>jekyll serve --trace
Configuration file: F:/GitHub/anbenqishi.github.io/_config.yml
            Source: F:/GitHub/anbenqishi.github.io
       Destination: F:/GitHub/anbenqishi.github.io/_site
      Generating...
                    done.
  Please add the following to your Gemfile to avoid polling for changes:
    gem 'wdm', '>= 0.1.0' if Gem.win_platform?
 Auto-regeneration: enabled for 'F:/GitHub/anbenqishi.github.io'
Configuration file: F:/GitHub/anbenqishi.github.io/_config.yml
D:/RUBY21-X64/lib/ruby/2.1.0/socket.rb:206:in `bind': Permission denied - bind(2) for 127.0.0.1:4000 (Errno::EACCES)
</pre>

google一下你就知道：[http://stackoverflow.com/questions/28565086/jekyll-3-0-beta-on-window-7-permission-denied](http://stackoverflow.com/questions/28565086/jekyll-3-0-beta-on-window-7-permission-denied)

问题应该是4000端口被人占用，懒得根据第一个答案来找出到底是谁占用的，直接根据解答二，先install wdm，再配置换个端口解决。

记录一下，免得以后出现问题又搞半天。

