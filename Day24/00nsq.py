#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/29 10:24
@author: 柴顺进
@file: 00nsq.py 
@software:rongda
@note: matrix numpy 中的矩阵
"""  
import numpy as np
# 矩阵的创建 1 ：直接使用分号隔开的字符串创建
mat = np.mat("1 2 3;4 5 6;7 8 9")
arr = np.arange(1, 10).reshape(3, 3)
print(mat)
print(arr)
print(type(mat))
print(type(arr))
# 矩阵的创建二:使用numpy数组创建矩阵
mat2 = np.mat(arr)
print(mat2)
print(type(mat2))
# 从已有的矩阵中通过bmat函数复合创建矩阵
A = np.eye(2)
B = A*2
print(A)
print(B)
mat3 = np.bmat("A B;B A")
print(mat3)