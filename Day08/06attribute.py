#!usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/04 14:25
@author: 柴顺进
@file: 06attribute.py 
@software:rongda
@note: 函数的属性
"""  


def fun_a(x):
    return x


fun_a.alert = 'hello'
fun_a.hobby = ['play', 'swin']
fun_a.pp = lambda: 'haha'


print fun_a.alert
print fun_a.hobby
print fun_a.pp