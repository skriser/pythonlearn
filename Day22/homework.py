#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/25 18:21
@author: 柴顺进
@file: homework.py 
@software:rongda
@note: 
"""
import numpy as np

# 1、创建一个维数组，将其倒置输出结果
a = np.arange(8)
a1 = a[::-1]
print(a)
print(a1)
#
# # 2.创建一个行值是从 0到4的5*5 5*5矩阵
b = np.array([np.arange(5), np.arange(5), np.arange(5), np.arange(5), np.arange(5)])
print(b)
c = np.arange(5)
d = np.vstack((c,c,c,c,c))
print(d)


# 3、创建一个 10*10 10*10 的数组，并且边框是 1，里 面是 0。效果图如下：
z = np.ones((10, 10))
print(z)
print("###################################################")
z[1:9, 1:9] = 0
print(z)
