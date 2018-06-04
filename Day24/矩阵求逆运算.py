#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/29 15:20
@author: 柴顺进
@file: 矩阵求逆运算.py 
@software:rongda
@note: 
"""  
import numpy as np

A = np.mat(np.array([[0, 1, 2],
                     [1, 0, 3],
                     [4, -3, 8]]))

print("A:\n", A)
A_ = np.linalg.inv(A)
print("A_:\n", A_)

print("A*A_:\n", A*A_)
