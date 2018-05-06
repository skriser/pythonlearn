#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/06 11:23
@author: 柴顺进
@file: 02decorators.py 
@software:rongda
@note: 装饰器及其调用

1.装饰器一旦加上以后如果想用不加的就去掉@
2.对装饰器参数的使用不同通过*args来存储
3.多个装饰器使用每行一个装饰器约等于 d1(d2(fun))
"""
import time


def decorator1(arg):
    # 这个是装饰器函数
    def wrapper(a, b):
        # wrapper 英文意思是：包装纸
        startTime = time.time()
        arg(a,b)
        endTime = time.time()
        print '时间差是：', (endTime-startTime)*1000
    return wrapper


@decorator1
def fun(a, b):
    print 'hello ,ddd'
    time.sleep(1)
    print (a+b)


fun(3, 4)
f = fun
f(3, 5)
