#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/04/28 2018/4/28 13:43
@author: 柴顺进
@file: 05zipAndDict.py 
@software:rongda
@note: zip 使用字典的默认keys来进行迭代对象
"""
list1 = (1, 2, 3)
dict1 = {'num1': 'one', 'num2': 'two', 'num1': 'three'}
# .keys() 获取字典中所有的键值 .values()获取字典中所有的值
# print dict1.keys()
# print dict1.values()
# print zip(list1, dict1)
#
# list2 = [1, 2]
# # append 操作是无返回值的，所以打印是None
# print list2.append(3)

# 反向操作 zip(*xxx)
num1 = [2, 4, 6, 8]
num2 = [1, 3, 5, 7]
result = zip(num1, num2)
print result
result.append((10, 19))
print result
print zip(* result)
