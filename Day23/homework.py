# -*- coding:utf-8 -*-
""" 
@time: 2018/05/28 19:50
@author: 柴顺进
@file: homework.py
@software:
@note: 
"""

import numpy as np
arr1 = np.array([[100000,10000,7500],[1,15,20]])
arr2 = np.array([[20000,11000,9000],[1,20,15]])

# A公司的工资数组
A1 = np.array([100000])
A2 = np.full((15),10000)
A3 = np.full((20),7500)
arrA = np.concatenate((A1,A2,A3),axis=0)

# B公司的工资数组
B1 = np.array([20000])
B2 = np.full((20),11000)
B3 = np.full((15),9000)
arrB = np.concatenate((B1,B2,B3),axis=0)


#求加权均值
# 公司的带权平均值
companyA = np.average(arr1[0],weights=arr1[1])
companyB = np.average(arr2[0],weights=arr2[1])
print("A公司的带权平均值：",companyA)
print("B公司的带权平均值：",companyB)

#求中位数
medianA = np.median(arrA)
medianB = np.median(arrB)
print("A公司的工资中位数：",medianA)
print("B公司的工资中位数：",medianB)