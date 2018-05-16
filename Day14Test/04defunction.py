#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/13 9:58
@author: 柴顺进
@file: 04defunction.py 
@software:rongda
@note: 4.定义一个函数，用于返回某列表各个元素的平方组成的列表
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
"""


def sqrt1(list1):
    list2 = []
    for i in list1:
        list2.append(i**2)
    return list2


list1 = [i for i in range(20)]
print(sqrt1(list1))