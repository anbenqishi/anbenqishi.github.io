---
layout: post
title: 在openSUSE中安装vtk和itk
published: true
tags: Linux
---

真是泪奔，昨天刚装好`openSUSE`虚拟机，装了几个软件后，提示硬盘空间不足，然后就进入半死机状态了，
唉，当初只给它分配了10GB空间，想不到丫的是个空间大户，哭了，昨天的辛苦工作又白费了。但是还是把那些软件的安装过程记录下，省得每次都Google浪费时间。


导师主要是怕其他`Linux`的发行版中没有需要的东西，所以他建议把代码放在openSUSE里面运行，当然要运行之前，
一些必要的软件要安装，就是：`QT`、`KDevelop`、`cmake`、`vtk`、`itk`。由于`openSUSE`默认安装时有一些必要的软件没有安装，
所以在安装上述软件之前，确保以下软件已经安装在机子上了（在`YAST2`里）：

+ automake
+ autoconf
+ g++（gcc套件）
+ libtool

其中`KDevelop`和`cmake`都可以从YAST2里面下载，所以较为方便，其他三个分别从官网下载即可，当然我们这里用的都是opensource的版本。

1.   QT的安装[http://www.qtcn.org/bbs/read.php?tid=22600](http://www.qtcn.org/bbs/read.php?tid=22600)
   进入下载页面：选择下载用于 Linux/X11 的 Qt 库 4.6.2 (160 Mb)
   
{% highlight c %}
# tar -zxvf qt-everywhere-opensource-src-4.6.2.tar.gz
# cd qt-everywhere-opensource-src-4.6.2   //这里可以把文件夹重命名为简单一点的名字，比如qt
# ./configure 
# gmake
# gmake install 
{% endhighlight %}

`qt-x11` 被安装到此目录下`/usr/local/Trolltech/Qt-4.6.2`
设定环境变量，在自己的家目录下的`.profile`或在`/etc/profile`中，添加下列代码(推荐在`/etc/profile`中)：
{% highlight c %}
QTDIR=/usr/local/Trolltech/Qt-4.6.2
PATH=$QTDIR/bin:$PATH
MANPATH=$QTDIR/doc:$MANPATH      //这个不设也可以
LD_LIBRARY_PATH=$QTDIR/lib:$LD_LIBRARY_PATH
export QTDIR PATH MANPATH LD_LIBRARY_PATH
{% endhighlight %}
（另：装了几次QT，每次装完再重启后系统就变慢了，郁闷，不知道什么原因）

2.  使用KDevelop的步骤[http://www.100ksw.com/jsj/linux/xxjc/178745.shtml](http://www.100ksw.com/jsj/linux/xxjc/178745.shtml)：
>
    + 新建一个工程
    + 写代码
    + Build->Run Automake & friends
    + Build->Run Configure
    + Build->Compile File
    + Build->Build Project
    + Build->Execute Program(Shift+F9)

注意：在 `4.Build->Run Configure` 这一步中很有可能会出现这个问题`configure: error: C++ compiler cannot create executables `这是kdevelop自身环境变量的设置问题。

　　在`kdevelop`中开启`Project Options`，然后在`Configure Options`的内容中，分别确认`C`和`c++`使用`compiler`，在各自的`Compiler command(cc)`和`Compiler command(cxx)`中分别填入`gcc`和`g++`.在对话框里面按下OK之后， IDE会问你是否要重建，选rerun即可。
(还有可参考[此文](http://hi.baidu.com/mrprogrammer/blog/item/bd53b6fb1e3f2b16a9d31140.html/cmtid/468bab7232a662168701b081))


3. vtk和itk的安装（以前自己整理的，参考了网上的一些文章）：

   itk篇：

    1. 在http://www.itk.org/ITK/resources/software.html中下好源码包
    2. 如果你想在全局安装，也就是安装在／opt或者/usr目录下，那么需要root权限.这里假设你要安装在自己的家目录下。
    3. 新建一个文件夹itk,再在这个目录下创建两个文件夹，分别是src,bin
    4. 把1中的压缩包解压到src目录下，这里假设解压出来的是InsightToolkit-3.16.0文件夹
    5. cd进入到bin目录下，运行ccmake ../src/InsightToolkit-3.16.0/
    6. 按c,把BUILD_EXAMPLES和BUILD_TESTING个OFF掉，不然耗时过长，个人认为可以把BUILD_SHARED_LIBS  ON,主要是预防一下，要是有用到再重来一次就悲剧了。若没出错则继续按g就退出了
    7. make   (这个时间长点）
         make install (这个很重要，切记切记，网上很多都没有这步)
    8. 搞定以后就可以测试是否安装成功,步骤如下：
    9. 在/src/Example/Installation目录下，有测试的程序HelloWorld.cxx，带有CMakeLists.txt，把这两个
        文件拷出来到一个文件夹中（可以随便新建一个）
    10. 终端下cd 进入到这个文件夹中，运行 ccmake ./  这个可以设置itk的路径，在ITK_DIR这个选项填入你的bin路径，即类似XXX/itk/bin
    11. 按c，无出错，再按g退出
    12. cmake .
    13. make
    14. ./HelloWorld    如果输出正常就说明安装成功了。
    (补充一个，不知是否必要 ，反正没损伤：
           `export LD_LIBRARY_PATH=/usr/local/lib/InsightToolkit`
      还有在`/etc/ld.so.conf`里也添加路径 `/usr/local/lib/InsightToolkit`    )
    (发觉这篇[文章](http://blog.csdn.net/zhangcunli/archive/2009/09/24/4587354.aspx)讲得也蛮清楚的:)

vtk篇：

  1. 在http://www.vtk.org/VTK/resources/software.html中下好Source and Data两个包
  2. 新建一个文件夹vtk,把上面两个包解压缩到此处，同时再建一个文件夹bin.
  3. 在终端下cd到这个bin目录下
  4. 运行  ccmake ../VTK    (这个VTK就是刚才从Source中解压出来的，文件名最好不要变)根据提示进行操作，一般默认的就可以了，下面是一些选项的解释:

  >    * build_examples:询问是否编译vtk中的例子
  >   * build_testing:就是vtk开发者用来测试vtk代码的一些例子，我们常通过它们和Example下的例子学习vtk，是否编译它们，看个人喜好
  >   * build_shared_libs:如果设置为off，则只声称lib文件，用于c++开发是够了；如果设置为on则将多声称dll文件，在同时要使用python脚本调用vtk程序时，就必须编译生成动态库，要设置为on
  >   * cmake_install_prefix:这个比较重要，就是以后要安装vtk的路径。有些人又要问，我编译完了不就可以用vtk了吗，为什么还要安装？对，不安装其实可以，安装的好处就是可以从 1G多的文件中提取出.h .lib .dll等精华，安装在指定目录下，并修改系统环境变量
  >   * vtk_data_root:一般地，cmake可以自己找到vtkdata的路径，但如果没有，把vtkdata路径填上即可，告诉cmake，vtk需要的数据都在哪里

  5. 按c进行配置，没出错，按g就可以退出来了。
  6. make     (花时间的说）
  7. `sudo make install`    (sudo就是说要在root权限下，按提示输入密码即可)
  8. `sudo export LD_LIBRARY_PATH=/usr/local/lib/vtk-5.4`
  9. 往`/etc/profile`里添加如下查找路径：
  
{% highlight c %}
C_INCLUDE_PATH=/usr/local/include/vtk-5.4:$C_INCLUDE_PATH
export C_INCLUDE_PATH
CPLUS_INCLUDE_PATH=/usr/local/include/vtk-5.4:$CPLUS_INCLUDE_PATH
export CPLUS_INCLUDE_PATH
{% endhighlight %}
  这是因为编译时可能会出现无法找到头文件的问题，而`C/C＋＋`的头文件查找路径包含有`/usr/local/include`，但不会继续进入子文件中，即不会去查找`/usr/local/include/vtk-5.4`.最后在`/etc/ld.so.conf`里也添加路径`/usr/local/lib/vtk-5.4`.
         
暂时就这些，继续搞系统！