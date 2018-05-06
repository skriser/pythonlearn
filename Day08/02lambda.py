#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/04 2018/5/4 11:12
@author: 柴顺进
@file: 02lambda.py 
@software:rongda
@note: 匿名函数
"""  


def fun_a(x):
    # 函数再返回函数
    return lambda y: x + y*2


# 将上面的函数转换为lambda后
lambda x:lambda y:x+y*2


# 第一次执行fun_a
sum1 = fun_a(10) # sum1 还是一个函数
# sum1 = lambda y: 10+y
print sum1(20)

# 函数再执行函数，这里连续执行
t1 = fun_a(20)(5)
print t1
