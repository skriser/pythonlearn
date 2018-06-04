#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@time: 2018/05/28 14:16
@author: 柴顺进
@file: 统计分析2.py
@software:rongda
@note:
"""
import numpy as np
open1, high, close= np.loadtxt("data.csv",delimiter=",", usecols=(3, 4, 6),unpack=True)
# 求极差:计算股票最高价的极差 最大值减去最小值
ptp = np.ptp(high)
print("股票的极差", ptp)

# max1 = np.max(high)
# min1 = np.min(high)
# ptp2 = max1 - min1
# print("股票的极差", ptp2)

# 求中位数 np.median()
median = np.median(close)
print("股票的中位数", median)
# 验证是否正确

close.sort()
print(close)
if close.size % 2 == 0:
    print((close[int(close.size/2)]+close[int(close.size/2)-1])/2)
else:
    print(close[int((close.size-1)/2)])

# 计算方差 np.var()
print("收盘价的方差：", np.var(close))
print("开盘价的方差：", np.var(open1))
