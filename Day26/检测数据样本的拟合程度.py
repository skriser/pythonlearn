#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/31 10:19
@author: 柴顺进
@file: 检测数据样本的拟合程度.py 
@software:rongda
@note: 
"""  
from scipy import stats

# 检测数据样本和正态分布的拟合程度
normalExample = stats.norm.rvs(size=100)

# 方法一：用偏度函数获取
skew, pvalue = stats.skewtest(normalExample)
print("pvalue-1:",pvalue)

# 方法二：用峰度计算函数获取
kurtosis, ktpvalue = stats.kurtosistest(normalExample)
print("pvalue-2:",ktpvalue)

# 方法三：用normaltest函数
normpvalue = stats.normaltest(normalExample)
print("pvalue:",pvalue)
