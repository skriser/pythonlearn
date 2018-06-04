#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/01 15:02
@author: 柴顺进
@file: test2-2.py 
@software:rongda
@note: 
"""
import numpy as np
'''
用numpy至少两种方法生成如下所示的数组 10x10
[[111111]
[10000001]
[10000001]
[10000001]
[1111111]
]
'''
# 方法一
arr1 = np.ones((10, 10))
arr1[1:9, 1:9] = 0
print(arr1)
# 方法二
arr2 = np.zeros((10, 10))
arr2[0]= 1
arr2[-1]=1
arr2[:,0]=1
arr2[:,-1]=1
print(arr2)

