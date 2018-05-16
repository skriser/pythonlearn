#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/13 10:01
@author: 柴顺进
@file: 05defunction02.py 
@software:rongda
@note: 5.定义函数返回某纯数字组成的列表或者元组的和
"""


def sum1(list1):
    sum1 = 0
    for i in list1:
        sum1 = sum1 + i
    return sum1


tup1 = (1, 2, 3, 4, 5)

print(sum1(tup1))
