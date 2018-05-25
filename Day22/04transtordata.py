#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/25 14:09
@author: 柴顺进
@file: 04transtordata.py
@software:rongda
@note: numpy数据类型转换
"""  
import numpy as np

print(np.float64(42))
print(np.int8(42.0))
print(np.bool(42))
print(np.bool(0))
print(np.bool(42.0))
print(np.float64(True))
print(np.float32(False))

a1 = np.array([2, 2, 3, 34], dtype=np.bool)
print(a1)
a2 = np.array(["张三", "李四", "王五", "大麻子"])
print(a2.dtype)
print(a2)

print(np.arange(7,dtype="f"))