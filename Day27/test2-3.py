#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/01 15:16
@author: 柴顺进
@file: test2-3.py 
@software:rongda
@note: 
"""
import numpy as np
'''
编写代码，判断第数组一中的每个元素在数组二中是否存在
数组一：[ 0 10 20 40 60]
数组二：[0, 40] 
结果：[ True False False True False] 
'''
arr1 = np.array([0,10,20,40,60])
arr2 = np.array([0,40])
arr3 = np.arange(arr1.size)
for i in range(arr1.size):
    flag = 0
    for j in range(arr2.size):
        if arr1[i] == arr2[j]:
            flag +=1
    if flag:
        arr3[i] = True
    else:
        arr3[i] = False
mask = arr3 == 1
print(mask)



