---
layout: page
title: About
description: 生活设计与实现
keywords: 
comments: true
menu: 关于
permalink: /about/
---

一个普通人。  
一个曾经还想改变世界的普通人。  
一个因为在电脑上玩游戏而踏入编程世界的非游戏码农。  

## 联系

{% for website in site.data.social %}
* {{ website.sitename }}：[@{{ website.name }}]({{ website.url }})
{% endfor %}

## Skill Keywords

{% for category in site.data.skills %}
### {{ category.name }}
<div class="btn-inline">
{% for keyword in category.keywords %}
<button class="btn btn-outline" type="button">{{ keyword }}</button>
{% endfor %}
</div>
{% endfor %}
