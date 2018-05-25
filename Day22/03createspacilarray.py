#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/25 13:35
@author: 柴顺进
@file: createspacilarray.py 
@software:rongda
@note: 创建特殊的数组
"""  
import numpy as np

# 1.创建值为零的矩阵
# 1.创建一维的矩阵10列
zeros1 = np.zeros([10, ])
print(zeros1)

# 1.创建二维的矩阵，2x2
zeros2 = np.zeros([2, 2])
print(zeros2)
# 1.创建三维的 3x3
zeros3 = np.zeros([3, 3])
print(zeros3)

# 2.创建指定函数的矩阵
full1 = np.full([2, 2], 10)
print(full1)

# 3.创建对角矩阵,注意对角矩阵必须是方阵
eye1 = np.eye(2)
print(eye1)
eye2 = np.eye(5)
print(eye2)
# 将方阵的对角线上的左下角或右上角移动
eye3 = np.eye(3, k=1) # 向右上角移动
print(eye3)
eye4 = np.eye(3, k=-1)
print(eye4)
# 创建一个由 0-1之间的随机数矩阵2x3
random1 = np.random.random([2, 3])
print(random1)
