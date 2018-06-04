#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/29 13:48
@author: 柴顺进
@file: 二元运算符.py 
@software:rongda
@note: 
"""  
import numpy as np

# 对第一个数组中根据第二个数组中对应i ,计算i次方
mat = np.mat(np.array([1,2,3,4,5]))
I = np.mat(np.array([2,3,2,1,3]))
print("power",np.power(mat,I))

# 获取两个数组中对应元素的最大值与最小值，返回一个新的数组中
d2 = np.array([[22, 15],[5.4, 6.6]])
d3 = np.array([[15,28],[7.9,4.0]])
d4 = np.maximum(d2,d3)
print(d4)
d5 = np.minimum(d2,d3)
print(d5)

a = np.arange(4).reshape(2, 2)
like_a = np.zeros_like(a)
print(a)
print("like_a:\n",like_a)
