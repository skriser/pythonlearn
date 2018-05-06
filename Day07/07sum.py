#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/03 2018/5/3 14:42
@author: 柴顺进
@file: 07sum.py 
@software:rongda
@note:
"""
# 自定义函数求列表或者元组的和，通过return返回
# 模拟range()功能

def sum1(list1):
    count = 0
    for i in list1:
        count = count + i
    return count

list1 = [1,2,3,4,5,6,7]
tup1 = (1,2,3,4,5,6,7,7)
print sum1(list1)
print sum1(tup1)

range
range()

def range1(num):
    list2 = []
    i = 0
    while i < num:
        list2.append(i)
        i += 1
    return list2


print range1(5)