---
layout: post
title: test markdown blog
published: true
tags: 随笔 记事
---

![有帮助的截图](../assets/screenshot.jpg)
sfssdfewrsfs

{{date}}

大师傅士大夫
{% for post in site.posts %}
<li>
  <a href="{{ post.url }}">{{ post.title }}</a>
</li>
{% endfor %}

{{ site.url }}

"{{ post.url }}"

{% highlight ruby linenos %}
def show
  @widget = Widget(params[:id])
  respond_to do |format|
    format.html # show.html.erb
    format.json { render json: @widget }
  end
end
{% endhighlight %}

{% highlight python linenos %}
def show
  @widget = Widget(params[:id])
  respond_to do |format|
    format.html # show.html.erb
    format.json { render json: @widget }
{% endhighlight %}

{% include footer.html %}

