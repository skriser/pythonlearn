#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/06 10:30
@author: 柴顺进
@file: 01Decorators.py 
@software:rongda
@note: 装饰器,装饰器的使用，函数作为参数传入到装饰函数中
"""  

# 插入日志性能测试，事务处理，缓存，权限校验等拓展功能
# 记录某函数执行的总时间
import time


def compute_time():
    print 'hello'
    # 在线程里面停止两秒
    time.sleep(2)
    print 'world'


compute_time()


def compute_time1():
    start_time = time.time()
    print 'hello'
    time.sleep(2)
    print 'world'
    end_time = time.time()
    msecs = end_time - start_time
    print '时间差是：%d' %(msecs * 1000)


compute_time1()


def compute_decorator(fun):
    start_time = time.time()
    fun()
    end_time = time.time()
    print 'time is %f' % ((end_time-start_time)*1000)


# 把需要装饰的函数给f ，这样作为参数传入进去
# 如果在函数名后面带上（）后就会执行，那么f得到的是函数的返回值:None
print compute_time()
print compute_time
f = compute_time
compute_decorator(f)

