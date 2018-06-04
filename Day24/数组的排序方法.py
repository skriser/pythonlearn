#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/29 16:43
@author: 柴顺进
@file: 数组的排序方法.py 
@software:rongda
@note: 
"""  
import numpy as np

arr = np.array([4,5,23,11,56,78,25])
# sort排序
# arr.sort()
# print(arr)
# 2.返回元素排序后的索引；返回值是索引，索引位置是根据数据排序确定
# argsort = np.argsort(arr)
# print(argsort)

d2 = np.array([[12, 8, 36], [22, 45, 9]])
# d2.sort(axis=0) # 行不变，对应列对比
# print(d2)
# d2.sort(axis=1) # 列不变，行进行对比排序
# print(d2)

# 将多维数组按列排序后返回列索引
print(np.argsort(d2, axis=0))
# # 将多维数组按行排序后返回行索引
# print(np.argsort(d2,axis=1))
