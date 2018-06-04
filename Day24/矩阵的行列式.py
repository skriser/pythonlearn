#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/29 16:39
@author: 柴顺进
@file: 矩阵的行列式.py 
@software:rongda
@note: 
"""  
import numpy as np

vector = np.mat("3 4;5 6")
# 求行列式
det = np.linalg.det(vector)
print(det)