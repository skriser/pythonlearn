#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/28 11:29
@author: 柴顺进
@file: 加载数据.py 
@software:rongda
@note: 
"""  
import numpy as np
'''
numpy 加载csv文件数据
np.loadtxt(filepath,delimiter,usecols,unpack)
filepath:加载文件的路径
delimiter:数据文件分隔符
usecols:加载数据文件中列索引
unpack:当加载多列数据时是否需要将数据列进行解耦赋值给不同的变量
'''

datas = np.loadtxt("data.csv", delimiter=",", usecols=(6,7))
# print(data)
print(datas.shape)
# 从data中切片分别取出收盘价和成交量
close = datas[:,0]
amount = datas[:,1]
print("收盘价：", close)
print("成交量：", amount)

# 当加载CSV文件的多列数据时可以使用unpack将加载的数据列进行解耦到不同的数组中
# 将usecols 里面的对应数据给前面的对用数据
close1, amount1 = np.loadtxt("data.csv", delimiter=",", usecols=(6, 7), unpack=True)

print("收盘价：", close1)
print("成交量：", amount1)

