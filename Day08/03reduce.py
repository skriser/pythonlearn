#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/04 11:46
@author: 柴顺进
@file: 03reduce.py 
@software:rongda
@note: 对参数序列中元素进行总体计算
[1, 2, 3, 4, 5, 6, 7]
((1+2)+3)...
"""  


def add(x, y):
    return x+y


list1 = reduce(add, [1, 2, 3, 4, 5])

list2 = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
