#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/25 11:36
@author: 柴顺进
@file: 02createtwod.py
@software:rongda
@note: 二维数组的创建
"""  
import numpy as np

d2 = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8]])
a = np.arange(5)
b = np.arange(5, 10)
d2_1 = np.array([a, b])
d2_2 = np.array([np.arange(5), np.arange(5, 10)])
print(d2)
print(d2_1)
print(d2_2)

d3 = np.array([[
                [1, 2,  3],
                [4, 5,  6]
                ], [
                [7, 8,  9],
                [0, 10, 11]
                ]])

print(d3.shape)