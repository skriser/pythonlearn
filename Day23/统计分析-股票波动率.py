#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/28 15:06
@author: 柴顺进
@file: 统计分析-股票波动率.py 
@software:rongda
@note: 
"""  
import numpy as np

close = np.loadtxt("data.csv", delimiter=",", usecols=(6))

# 计算简单收益率：相邻两天的差除去前一天的价格
returns = np.diff(close)/close[:-1]
print(returns)
# 对数收益率：首先对所有的收盘价取自然对数
logs = np.log(close)
# print(logs)
diffLogClose = np.diff(logs)
print("取得对数收益率：", diffLogClose)
# 对数收益率的标准差
std = np.std(diffLogClose)
print("对数收益率的标准差：", std)
# 年波动率等于对数收益率的标准差除以其均值，再除以交易日倒数的平方根，交易日252天
annual_volatility = std/np.mean(diffLogClose)
tmp2 = np.sqrt(1/252)
y_rate = annual_volatility/tmp2
print("年化波动率是多少", y_rate)
#
mouth_annual_volatility = std/np.mean(diffLogClose)/np.sqrt(1/12)
print("月波动率是多少", mouth_annual_volatility)