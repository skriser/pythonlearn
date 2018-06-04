
#!usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/29 17:05
@author: 柴顺进
@file: 搜索函数.py 
@software:rongda
@note: 
"""  
import numpy as np

a = np.array([[12,56,-34],[18,20,6]])

argmax = np.argmax(a,axis=0)
# print(argmax)

a1 = np.arange(5)
print("寻找到插入位置下表",np.searchsorted(a1,[-2, 7]))
indices =np.searchsorted(a1,[-2, 7])
# 根据下表插入相应的数据
res = np.insert(a1,indices,[-2,7])
print(res)
