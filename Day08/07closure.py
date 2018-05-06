#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/04 14:32
@author: 柴顺进
@file: 07closure.py 
@software:rongda
@note: 闭包
"""  


def outer():
    a = 10

    def inner():
        return a
    return inner


num1 = outer()
print num1()


def outer(a):
    b = 10

    def inner(c):
        return a+b+c
    return inner


num1 = outer(10)(5)
num2 = outer(20)(10)
print num1
print num2


def line_conf(a, b):
    # 用来生成一个统一的式子
    def line(x):
        return a*x + b
    return line


line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
line3 = line_conf(20, 10)

# 用def写个 2x + 3 和 10x +5的值


def lin_conf(a, b, x):
    return a*x + b



