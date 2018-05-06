#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/03 2018/5/3 15:33
@author: 柴顺进
@file: 08variable.py 
@software:rongda
@note: 全局变量和局部变量
"""  

total = 0

print total


def sum1(arg1, arg2):
    global total
    total = arg1 + arg2
    print total
    return total


print total
sum1(11, 33)
print total
