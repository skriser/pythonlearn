#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/29 10:42
@author: 柴顺进
@file: 创建随机数组.py 
@software:rongda
@note: 
"""
import numpy as np
from matplotlib import pyplot as plt
# 创建正态分布数组
# normal = np.random.normal(size=500)
# print(normal)
# plt.hist(normal)
# plt.show()
# 创建一个beta分布的随机样本
# beta = np.random.beta(a=.5, b=.5, size=1000)
# # plt.hist(beta)
# # plt.show()
#
# # 产生4X4随机正太分布样本
# normal2 = np.random.normal(size=(100,100))
# # print("normal,4X4:\n",normal2)
# # plt.hist(normal2)
# # plt.show()
#
# # 产生某个范围内的随机整数数组5x5 范围1-50
# numbers = np.random.randint(1, 50, [5, 5])
# # num_mat = np.mat(numbers)
# # print(num_mat)
#
# # 产生0--1之间的随机浮点数
# floatNum = np.mat(np.random.random(10))
# print(floatNum)

# 随机抽取一个某范围内的数
num = np.random.choice(10) # 在0--10之间随机抽取一个
num = np.random.choice(5,10) # 在0--5之间取10个
print(num)