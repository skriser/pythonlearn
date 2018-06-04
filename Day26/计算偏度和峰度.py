#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/31 9:08
@author: 柴顺进
@file: 计算偏度和峰度.py 
@software:rongda
@note: 
"""
from scipy import stats
from matplotlib import pyplot as plt
import numpy as np

# 画一个简单的直方图
# 随机采样一个年龄人群个数
population_ages = [22,55,62,45,21,22,34,42,42,4,99,28,35,30,25,27,49,111,37,44,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]


# 绘图操作显示图表
# plt.hist(population_ages,bins)
# plt.show()

normalExample = stats.norm.rvs(size=50)

# 计算正态分布样本点的偏度和数据样本与正太分别拟合的程度
skew, pvalue = stats.skewtest(normalExample)
# 偏度表征概率分布密度曲线相对于平均值不对称程度的特征数skew>0正偏，skew<0偏
print("偏度：",skew) # 大于0是正偏度

# 将数据样本绘制
# plt.hist(normalExample)
# plt.show()

# 计算峰度 ,这个计算是相对于正太分布的值，因为正太分布的峰度为3，计算中会减去3
kurtosis ,pvalue = stats.kurtosistest(normalExample)
print("峰度",kurtosis)
