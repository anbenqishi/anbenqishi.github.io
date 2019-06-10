---

layout: post
title: 数据库及实例的启动与关闭
published: true
tags: SQL Oracle

---

当一个实例启动后，Oracle将令此实例与制定的数据库共同工作。当数据库与实例关联后就称为这是一个`mounted database`，可以被open。

启动Oracle DB并使其可以为所有用户提供服务的三个步骤如下：

1. 启动实例（读取初始化参数；创建SGA和后台进程），读取数据库`control_file`(可参看`CONTROL_FILE`参数)，获取`datafile`及`redo log file`名；
2. mount数据库。当DB处于挂载状态时，管理员可以进行维护性工作。此时DB的常规操作都是被禁止的。
3. open数据库。打开`datafile`及`redo log file`名。实例将请求一个或多个`undo tablespace`（参看参数`UNDO_MANAGEMENT`）。

Open mode: Read only，意即不能向`datafile`及`redo log file`写入信息。

`standby database`是一个与`primary database`完全相同的副本，它能在发生灾难时保证系统的持续可用性。

`clone database`是专供按时间点恢复表空间功能使用的DB副本。

关闭一个DB及其相关实例：

1. `close DB`:不能执行一班操作，`control file`依旧打开中；
2. `unmount DB`:DB与实例分离，实例仍存于内存中，`control file`关闭；
3. shutdown实例：清除SGA，终止后台进程。

## 进程体系结构

连接connection时用户进程和oracle实例间的通信通道。这个`communication pathway`是通过进程间的通信机制或网络软件建立的。

会话session是用户通过用户进程和oracle实例建立的连接。

用户可以通过`V$BGPROCESS`视图查询关于后台进程的信息。

用户执行`COMMIT`语句时，`LGWR`进程在重做日志缓冲区内存储一条提交记录，并将此记录与所提交事务的重做条目立即写入磁盘。而此事务对DB的修改将等到最高效的时机才被写入磁盘。这被称为快速提交`fast commit`机制。

`SMON`负责进行recovery工作IF necessary。当一个user process失败后，`PMON`将对其进行恢复。

`RECO`是在分布式数据库环境中自动地解决分布式事务错误的后台进程。

`Job Queue Process`的功能是进行批处理。这种进程用于运行用户的作业，能够提供作业调度服务。

共享服务进程（`Snnn`）的`PGA`中不存储和用户有关的信息（指session memory），只包含stack space和process-specific variables。

程序接口`program interface`是数据库服务器与数据库应用程序之间的software layer。

## Q&&A

### Q: public schema ?

A: public is rather a schema than a role, because it contains objects like synonyms and database links. However, it is a special user that is created by Oracle.

`select name from sys.user$ where user#=1;`

Every grants to public applies to any user, and any object of public can be accessed by any user.

### Q: 脱机表空间？

### Q：检查点事件（CKPT）是如何发生的？

