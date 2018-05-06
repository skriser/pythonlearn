#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/04 2018/5/4 11:34
@author: 柴顺进
@file: 04map.py 
@software:rongda
@note: 根据提供的函数对指定序列进行批量处理
"""  
#
#
# def square(x):
#     return x**2
#
#
# list1 = range(10)
# new_list = map(square, list1)
# print new_list
#
# list2 = [1, 11, 111, 1111, 11111, 111111]
# new_list2 = map(square, list2)
# print new_list2
#
# new_list3 = map(lambda x: x**2, list1)
# print new_list3

list3 = map(lambda x, y: x+y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print list3
