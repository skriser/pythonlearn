#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/25 17:12
@author: 柴顺进
@file: 11npcombination.py 
@software:rongda
@note: 数组的组合
"""
import numpy as np
'''
vstack 按垂直方向拼接数组np.vstack((arr2, arr1))
hstack 按水平方向拼接数组np.hstack((arr2, arr1))
column_stack 按列拼接数组
row_stack 按行方向拼接数组
concatnete 
dstack 
'''
arr1 = np.arange(9).reshape(3, 3)
print(arr1)
print("******************arr1*************************")
arr2 = arr1*2
print(arr2)
print("******************arr2*************************")
# vstack 按垂直方向拼接数组 vertical 垂直的
result_vstack = np.vstack((arr2, arr1))
print(result_vstack)
print("******************result_vstack*************************")
# hstack 按水平方向拼接数组 horizontal
result_hstack = np.hstack((arr2, arr1))
print(result_hstack)
print("******************result_hstack*************************")
# column_stack 按列拼接数组，列增加，行不变，和hstack结果一样
result_colstack = np.column_stack((arr2, arr1))
print(result_colstack)
print("******************result_colstack*************************")
# row_stack 按行拼接数组，行增加，列不变，和vstack结果一样
result_rowstack = np.row_stack((arr2, arr1))
print(result_rowstack)
print("******************result_rowstack*************************")
