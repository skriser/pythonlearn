#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/29 15:28
@author: 柴顺进
@file: 方程组求解.py 
@software:rongda
@note: 
"""  
import numpy as np

'''
x-2y+z = 0
0x+2y-8z = 0
-4x+5y+9z = -9
'''
a = np.mat("1 -2 1;0 2 -8;-4 5 9")
b = np.array([0,0,9])
print(a)
print(b)
result = np.linalg.solve(a,b)
print(result)