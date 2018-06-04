#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/03 21:05
@author: 柴顺进
@file: test5.py 
@software:rongda
@note: 
"""
from scipy import stats
import numpy as np
from matplotlib import pyplot as plt
'''
5、	编写python代码，用随机函数生成一个有100个样本点的正态分布数据集，并根据数据集完成如下需求
（1）	求数据样本的偏度和峰度，根据偏度和峰度值判断数据样本是正偏还是负偏，是高峡峰还是低阔峰
（2）	使用matplotlib库绘制出数据样本的分度直方图
（3）	编写代码说明在数据集中有多少个样本比1大，有多少个数据样本比1小
'''

norm = stats.norm.rvs(size=100)

# 计算偏度
# skew, pvalue = stats.skewtest(norm)
# if skew>0:
#     print("这个是正偏")
# elif skew<0:
#     print("这个是负偏")
#
# # 计算峰度
# kurt, pvalue = stats.kurtosistest(norm)
# if kurt> 0:
#     print("这个是高狭峰")
# elif kurt<0:
#     print("这个是低阔峰")
#
# # 使用matplotlib绘制直方图
# plt.hist(norm)
# plt.show()
ndarray = np.compress(norm > 1,norm)
ndarray1 = np.compress(norm < 1,norm)
print("数据集中有{}个样本比1大，有{}个数据样本比1小".format(ndarray.size,ndarray1.size))