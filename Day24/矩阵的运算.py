#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/29 11:23
@author: 柴顺进
@file: 矩阵的运算.py 
@software:rongda
@note: 
"""  
import numpy as np

mat1 = np.mat(np.array([2,6,5]))
mat2 = np.mat(np.array([2,6,5]))

# 矩阵的加法
addres = np.add(mat1,mat2)
print(addres)
# s数组的乘法
multires = np.multiply(mat1,mat2) # 这个函数是数组的相乘
print(multires)
# 矩阵的乘法
mat3 = np.mat(np.arange(6).reshape(2, 3))
mat4 = np.mat(np.arange(6).reshape(3, 2))
print("矩阵的相乘mat3*mat4:\n",mat3*mat4) # 这个是矩阵的乘法
# 数组的除法
divide1 = np.divide(mat1, mat2)
print(divide1)
# 数组的除法并将结果向下取整
res = np.floor_divide(mat1, mat2)
print(res)
# 矩阵直接相除
print(mat1/mat2)
print(mat1//mat2)

# 取模运算
np.mod(mat1, mat2)
mat1%mat2
np.fmod(mat2/mat1)
