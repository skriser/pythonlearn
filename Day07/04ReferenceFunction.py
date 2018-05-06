#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/03 2018/5/3 11:49
@author: 柴顺进
@file: 04ReferenceFunction.py 
@software:rongda
@note: 引用传递，会改变传递进来的原来的参数的值
"""
x = [1, 2, 3]
print 'a=', id(x)


def fun_a(y):
    y[0] = 4


fun_a(x)
print id(x)
print x


def changeList(x):
    x.append('new')


list1 = [1, 2, 3]
print list1
changeList(list1)
print list1

