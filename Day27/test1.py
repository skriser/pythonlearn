#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/01 14:38
@author: 柴顺进
@file: test1.py 
@software:rongda
@note: 
"""
import numpy as np
# 1、请写出numpy中创建数组的方式，至少不少于3种（10分）

ndarray = np.array([1,2,3])
ndarray1 = np.array(range(10))
ndarray2 = np.arange(10)
print(type(ndarray2))