#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/30 9:07
@author: 柴顺进
@file: 数组元素的抽取.py 
@software:rongda
@note: 
"""  
import numpy as np

# a = np.arange(10)
# # 生成一个抽取数组元素的花式索引
# condition = a % 2 == 0
#
# # np.extarct()根据给定条件提取数组元素
# even = np.extract(condition, a)
# print("数组总的偶数项：", even)
#
# print(np.compress(condition, a))
# print(a.compress(condition))
#
# # 用take函数实现提取偶数项结合 np.where()
# indices = np.where(a%2 == 0)
# print("所有偶数项的索引",indices)
# print("even3:",a.take(indices))

# 提取数组中的非零元素np.nonzero()
arr = np.array([[0,1,2],
                [0,3,4],
                [0,5,6]])


print(arr[np.nonzero(arr)])