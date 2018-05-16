#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/15 9:05
@author: 柴顺进
@file: mysql.py 
@software:rongda
@note: 讲解mysql的基本用法
"""
# mysql的约束条件： 主键，外键，唯一性，自增长


# 事务的四个特性
# 1.原子性，mysql的事务是不可分割的，一个事务或者全部完成或者全部失败
# begin
# insert
# insert
# commit 这种必须三条都同时完成才能执行，执行有问题都不执行
# 2.一致性：数据库在进行事务改动的时候，前后不能破坏我们数据库的约束
# 3.隔离性：数据库对应的事务的操作不能互相影响
# 4.持久性：在我们commit后，对应的数据应该持久化，只要commit后，就不能丢失数据
# mysql事务的四个隔离级别
# RU 未提交读 造成脏读 --明显不能使用
# RC 提交读   造成幻读
# RR 可重复读  容易造成死锁
# SERI 序列化 完全串行化执行对应的事务
# 事务的隔离级别越高，事务隔离的安全性越高，性能越低
# 查询mysql事务隔离级别 show variable like "%iso%"
# 例子完成转账 需要至少两个SQL，一个是加钱，一个是减钱；这个要同时一起
# mysql 一条SQL语句就是一条事务，
# -- 显式开启事务：开启事务后要显式的提交；
# start TRANSACTION;
# insert into `subject` VALUES
# (NULL,'高等数学-1',120,1),
# (NULL,'高等数学-2',110,2),
# (NULL,'高等数学-3',100,3),
# (NULL,'高等数学-4',130,4);
# SELECT * from `subject` -- 可以看到里面有插入的数据了。这个是以日志的形式存储到日志中，没有更新数据仓库的磁盘上
# ROLLBACK -- 事务回滚，上面的插入就没了
# --  只要事务没有提交就出现异常退出就会自动回滚
# COMMIT;
# JDBC操作事务


