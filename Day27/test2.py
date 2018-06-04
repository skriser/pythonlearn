#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/01 14:43
@author: 柴顺进
@file: test2.py 
@software:rongda
@note: 
"""
import numpy as np
'''
（1）用numpy中的随机函数np.random.rand(5,5)，
生成一个5x5的数组，并使用numpy中的切片、索引以及索引搜等方法，
将数据根据第二列的数据大小进行重新排序（图中数据仅作为演示用）
'''
arr1 = np.random.rand(5, 5)
arr3 = np.eye(5,5)
arr2 = arr1[:, 1]
indecis = np.argsort(arr2, axis=0)
print(indecis)
for i in range(5):
    arr3[i] = arr1[indecis[i]]
print("排序前的顺序是：\n",arr1)
print("********************")
print("排序后的顺序是：\n",arr3)