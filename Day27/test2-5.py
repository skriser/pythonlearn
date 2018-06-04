#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/01 15:38
@author: 柴顺进
@file: test2-5.py 
@software:rongda
@note: 
"""
import numpy as np
'''
（5）编写代码，实现查找出给定数组中比10大的数，返回新的数组values,同时给出比10大的数在原数组中的索引
给定数组：[[ 0 10 20] [20 30 40]]
求如下数组：
Values: [20 20 30 40]
索引数组： (array([0, 1, 1, 1]), array([2, 0, 1, 2])) 
'''
arr1 = np.array([[0, 10, 20], [20, 30, 40]])
temp = arr1.flatten()
values = temp.compress(temp>10)
print(values)
indecis = np.where(arr1>10)
print(indecis)