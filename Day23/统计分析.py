#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/28 13:16
@author: 柴顺进
@file: 统计分析.py 
@software:rongda
@note: 
"""
import numpy as np
# 加载收盘价和成交量
close, amount = np.loadtxt("data.csv", delimiter=",", usecols=(6, 7), unpack=True)
# average(arr1, weights=arr2)求加权平均 arr1 为数据，arr2为对应的权重
print("收盘价：\n", close)
print("成交量：\n", amount)
# 成交量加权平均价 每天的收盘价x当天成交量之和除去总的成交量
average = np.average(close,weights=amount)
print("加权平均价：\n", average)

# 收盘价的计算平均值
mean = np.mean(close)
print("收盘价的平均价格", mean)
avg = np.average(close)  # 不加权重值就是求计算平均值
print("收盘价的平均价格", avg)

# 最大值最小值np.max(ndarray) np.min(ndarray)
max1 = np.max(close)
min1 = np.min(close)
print("收盘价的最大值", max1)
print("收盘价的最小值", min1)
exa = np.arange(24).reshape(2, 3, 4)
print(np.max(exa))

# 编写一个可以实现求最大最小
exa = np.arange(24).reshape(2, 3, 4)
zexa = exa.flatten()

def getMaxMin(adarray):
    ad = adarray.flat
    max1, min1=ad[0], ad[0]
    for ite in ad:
        if max1 < ite:
            max1 = ite
        if min1 > ite:
            min1 = ite
    return max1, min1
