#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/28 15:38
@author: 柴顺进
@file: 统计分析-筛选.py 
@software:rongda
@note: 
"""  
import numpy as np

close = np.loadtxt("data.csv", delimiter=",",usecols=(6))

# 对数收益率
log_rate = np.diff(np.log(close))
print(log_rate)

# 筛选出对数收益率大于0的所有元素的索引
indices = np.where(log_rate > 0)
print("收益率大于0的索引为：",indices)

# 根据索引值获取相应位置的元素
result = np.take(log_rate,indices)
print(result)

# 求阶乘np.prod
arr = np.array([5, 2, 7, 8])
prod = np.prod(arr)
print("阶乘：",prod)

# 2.累积乘积np.cumprod()
cumArr = np.array([2, 3, 4, 5])
cumprod = np.cumprod(cumArr)
print("累乘法",cumprod)

# 3.将数组中所有比给定的最大值大的元素设置为最大值
# 所有比给定的最小值小的元素设置为最小值np.clip(num1,num2)
# 介于最大值和最小值之间的数保持不变
test = np.array([3,56,7,44,22,18])
print(test.clip(48, 20))

# 筛选出对数收益率中大于0的元素
mask = log_rate>0
print(mask)
res = log_rate.compress(log_rate>0)
print(res)
