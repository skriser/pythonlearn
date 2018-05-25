#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/25 17:08
@author: 柴顺进
@file: 10nptranspose.py 
@software:rongda
@note: 数组的转置
"""  
import numpy as np

arr = np.arange(24).reshape(4,6)
print(arr)

arr_T = arr.transpose()
print("********************************")
print(arr_T)