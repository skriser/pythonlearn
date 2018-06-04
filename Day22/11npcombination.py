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
# row_stack 按行拼接数组，行增加，列名   不变，和vstack结果一样
result_rowstack = np.row_stack((arr2, arr1))
print(result_rowstack)
print("******************result_rowstack*************************")
# concatenate();axis值控制是行合并还是列合并
m1 = np.arange(9).reshape(3, 3)
m2 = m1*2
result_concatenate = np.concatenate((m1, m2),axis=1)
print(result_concatenate)
print("******************result_concatenate*************************")
clomn_stack = np.column_stack((m1, m2))
hstact_ = np.hstack((m1, m2))
result_concatenate1 = np.concatenate((m1, m2), axis= 1)
# 深度合并dstack();将两个数组每个都展成一列垂直；每层行数取决于开始的拼接对象的行数
d_stack = np.dstack((m1, m2, arr2))
print(d_stack)
print("d_stack.shape:",d_stack.shape)
print("******************d_stack*************************")
