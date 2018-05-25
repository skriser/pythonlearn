#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/25 16:10
@author: 柴顺进
@file: 08test.py 
@software:rongda
@note: 
"""  
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a[3:4])
print(a[0:len(a):2])
print(a[::-1])
print(a[::-2])