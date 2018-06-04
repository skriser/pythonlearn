#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/28 16:59
@author: 柴顺进
@file: test.py 
@software:rongda
@note: 
"""  
'''
文件中的数据为给定时间范围内某股票，现要求：
获取该内交易日周一、二三四五分别对应的平均
收盘价及哪天平均收盘价最高，哪天的低。
'''
import numpy as np
from datetime import datetime


# 将日期格式字符串转化得到星期数：
def datestr2num(s):
    return  datetime.strptime(s.decode("utf8"),"%d-%m-%Y").date().weekday()

# 使用转化器参数
dates, close = np.loadtxt("data.csv", delimiter=",", usecols=(1, 6), converters={1:datestr2num} , unpack=True)
print("日期：", dates)
print("收盘价：", close)

# 提取日期的数据
average = []
for i in range(5):
    # 根据星期数条件得到一个mask数组
    mask = dates == i
    # 根据mask数组筛选出星期数为i的所有收盘价
    weekday = close.compress(mask)
    # 计算出星期数为i的收盘价的均价添加到average数组中
    dayAvg = np.mean(weekday)
    average.append(dayAvg)
print(average)
# 获取数组中最大值的索引
maxIndex = np.argmax(average)
print("星期{}收盘价平均最高".format(maxIndex+1))
minIndex = np.argmin(average)
print("星期{}收盘价平均最低".format(minIndex+1))