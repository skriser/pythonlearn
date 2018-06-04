#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/28 9:44
@author: 柴顺进
@file: 01splitarr.py 
@software:rongda
@note:  数组的分割
"""
import numpy as np
full = np.arange(9).reshape(3, 3)
print(full)
# 默认按照行分割
axis0 = np.split(full, 3, axis=0)
axis01 = np.split(full, 3)
print(axis0[0], axis0[1], axis0[2])
print(axis01)
# 按照列进行分割
axis1 = np.split(full,3,axis=1)
print(axis1)
# 水平分割，hsplit 分割成列，并按照列
hsplit = np.hsplit(full, 3)
print(hsplit)

# 垂直分割， 分割成行
vsplit = np.vsplit(full, 3)

# 深度分割dsplit :2x2x2
print("#########################################")
d3 = np.arange(8).reshape(2,2,2)
print(d3)
d_split = np.dsplit(d3,2)
print("#########################################")
print(d_split)