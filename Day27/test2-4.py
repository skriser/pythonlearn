#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/01 15:35
@author: 柴顺进
@file: test2-4.py 
@software:rongda
@note: 
"""  
'''
编写代码，实现查找出两个numpy数组中相同的元素
数组一： [ 0 10 20 40 60] 
数组二：[10, 30, 40]
结果：[10 40] 
'''
import numpy as np

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
result = arr1.compress(mask)
print(result)
