---
layout: post
title: linux 下glut.h使用
published: true
tags: Linux
---

linux下编写OpenGL程序的一些准备工作
需要用到的软件包有两个，glut 和tmake,分别可以从以下两个网址下载：

http://www.opengl.org/resources/libraries/glut/glut-3.7.tar.gz
ftp://ftp.trolltech.com/freebies/tmake/tmake-1.8.tar.gz
下载后的文件假设都放在/usr/src中

+ 首先是安装glut库，以下是从www.linux.com找到的编译glut库的手册(http://www.linux.org/docs/ldp/howto/Nvidia-OpenGL-Configuration/instglut.html)。
<pre>
Install GLUT 3.7 Distribution (optional)
If you installed the MesaDemos/MesaLib package, then you have already installed GLUT 3.7 since it is included with MesaDemos. However, you may be interested in installing the GLUT
manpages and you can skip right to the "Install GLUT manual pages", below ...
Installing GLUT is a bit tricky. I'm not too familiar with imake, the program that it uses to manage the Makefiles, and didn't quite see how to get GLUT to install to where I wanted it (/usr/lib,
but MesaDemos will do this without any trouble though). It can be done manually anyhow:
cd /usr/src
tar -xvzf glut-3.7.tar.gz
cd glut-3.7
Read the file: README.linux
cd linux
READ the file: README
cp Glut.cf ..
cd ..
Edit Glut.cf: remove any Mesa references.
Replace any -lMesaGL -lMesaGLU with -lGL -lGLU if needed.
In particular, replace:
   OPENGL = $(TOP)/../lib/libMesaGL.so
   GLU = $(TOP)/../lib/libMesaGLU.so
with:
   OPENGL = -lGL
   GLU = -lGLU
./mkmkfiles.imake
cd lib/glut
cp /usr/src/glut-3.7/linux/Makefile .
Edit the Makefile: remove any Mesa references.
Replace any -lMesaGL -lMesaGLU with -lGL -lGLU if needed.
In particular, replace:
   OPENGL = $(TOP)/../lib/libMesaGL.so
   GLU = $(TOP)/../lib/libMesaGLU.so
with:
   OPENGL = -lGL
   GLU = -lGLU
make  （这里可能会遇到错误：“unrecognized command line option "-m486" ”，只要把Makefile里的-m486全换成-mtune=i486即可）
ln -s libglut.so.3.7 libglut.so
ln -s libglut.so.3.7 libglut.so.3
cp -d libglut.* /usr/lib
cd ..
cd gle
# make a shared lib for libgle
make
gcc -shared -o libgle.so.3.7 *.o
ln -s libgle.so.3.7 libgle.so
ln -s libgle.so.3.7 libgle.so.3
cp -d libgle.* /usr/lib
cd ..
cd mui
# make a shared lib for libmui
make
gcc -shared -o libmui.so.3.7 *.o
ln -s libmui.so.3.7 libmui.so
ln -s libmui.so.3.7 libmui.so.3
cp -d libmui.* /usr/lib
        # Install the GLUT manual pages (not included with MesaDemos)
cd /usr/src/glut-3.7
make SUBDIRS=man Makefile
cd man/glut
make install.man
ldconfig
cd ../../progs/demos/ideas
# edit the Makefile, change OPENGL = -lGL and GLU = -lGLU
make
./ideas
# test compiling some demos
# take a look at which libraries have to be linked (-lX11 ...) in
# the Makefiles. Qt's tmake program available at www.troll.no
# is a quick way to make a Makefile but you have to edit it
# and add the -l needed.
ideas如果运行成功的话，说明glut已经可以用了。
(悲剧的是我并没有运行成功，出现错误了：
../../../lib/glut/libglut.so: undefined reference to `glXQueryChannelRectSGIX'
../../../lib/glut/libglut.so: undefined reference to `glXBindChannelToWindowSGIX'
../../../lib/glut/libglut.so: undefined reference to `glXQueryChannelDeltasSGIX'
../../../lib/glut/libglut.so: undefined reference to `glXChannelRectSGIX'
../../../lib/glut/libglut.so: undefined reference to `glXChannelRectSyncSGIX'
collect2: ld returned 1 exit status
make: *** [ideas] 错误 1
     希望谁能帮忙解答下)
上面的几步中,下载的glut包放在/usr/src目录下，如果放在其他目录下，将/usr/src改为相应的目录即可。
此外应该注意的是两个Makefile文件的修改
改 
·   OPENGL = $(TOP)/../lib/libMesaGL.so
   GLU = $(TOP)/../lib/libMesaGLU.so
为
   OPENGL = -lGL
   GLU = -lGLU
因为所指定的目录中没有libMesaGL.so和libMesaGLU.so。
</pre>

+ 之后是tmake的配置，后面我们可以用它来生成pro工程文件和makefile文件。
    - 先将下载的tmake解压缩，tar -zxvf tmake-1.8.tar.gz
得到tmake-1.8目录,之后设置两个环境变量：PATH和TMAKEPATH
    <pre>
    PATH=$PATH:/usr/src/tmake-1.8/bin
    export PATH
    TMAKEPATH=/usr/src/tmake-1.8/lib/linux-g++
    export TMAKEPATH
    </pre>

    - 新建一个测试目录test，将glut-3.7目录下的progs/redbook目录下的hello.c复制到test目录中
    - 之后生成一个pro文件：progen -o hello.pro
    - 然后生成makefile文件：tmake hello.pro -o Makefile
    - 编辑生成的Makefile文件，在加载动态连接库的行里面加入 -lglut -lXi -lXmu
    - 保存，make。
    
+ `./hello` 可以看到运行结果就可以了。