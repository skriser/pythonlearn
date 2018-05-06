#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/04 2018/5/4 11:24
@author: 柴顺进
@file: 03filter.py 
@software:rongda
@note: filter(function,参数)过滤，使用lambda实现的函数

"""


def is_odd(n):
    return n % 2 == 1


list1 = range(1, 11)
# filter第一个是过滤条件，第二个是
newList = filter(lambda n: n % 2 == 1, list1)
print newList
newList = filter(lambda n: n > 1, list1)
# newList = filter(True, list1)
print newList

print is_odd(3)
