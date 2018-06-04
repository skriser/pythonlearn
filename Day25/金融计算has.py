#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/30 10:08
@author: 柴顺进
@file: 金融计算has.py 
@software:rongda
@note: 
"""
import numpy as np
'''
举例：某用户去银行存款，假设年利率 3% 、每季度续存金额 10 元、存 5年以及存款 1000 ，则计算 5年后可领取多少金额。
求未来钱数
'''
print(np.fv(0.03/4,5*4,-10,-1000))

'''
pv 函数 —— 计算现值（ present value present valuepresent value present value present value ）是指资产在当前时刻的价值。
现值有以下 4个参数决定 —— 利率、期数每支付金额以及终值
语法格式如下： 语法格式如下： 语法格式如下： numpy.fv(rate, nper , pmt , fv[, when='end’])
#参数： rate raterate：每一期的利率（ rate of interest）。
nper nper：期数。
pmt ：paymentpayment payment 。每期支付金额
fv ： future value，终值。如果是贷款终值为零
when when：{{‘begin’, 1}, {‘end’, 0}},
2举例：某用户去银行存款，假设年利率 3% 、每季度续存金额 10 元、存 5年后可领 1376.0963320，则计算 5年前存取的本金是多 少金额。
'''
print(np.pv(0.03/4,5*4,-10,1376.0963320407982))

'''
np.npv(rate,values)
rate:折现率
values:现金流
03.投资 100，收入39,59,55,20，折现率为28.1% 则净现值为
'''
print(np.npv(0.281,[-100, 39, 59, 55, 20]))

'''
举例：某同学房贷 20 万，准备 15 年还清，利率为 7.5% 7.5% ，则每 月需还贷多少金额？
pmt = np.pmt(0.075/12, 15*12,200000) 计算还款金额
'''
pmt = np.pmt(0.075/12, 15*12,200000)

'''
小明房贷 70 万，年利率 4% ，准备还 20 年，
则每月供多少？
'''
pmt1 = np.pmt(0.04/12, 20*12,700000)
print("每月需要还款{}元".format(-pmt1))

'''
举例：某同学房贷 20 万，年利率为 7.5% 7.5% ，每月能还贷 2000 ，则 需要还多少期？
np.nper(0.075/12,-2000,200000) 计算还款期数
'''
nper = np.nper(0.075/12,-2000,200000)
month = np.ceil(nper)
year = np.ceil(month/12)
print("需要还{}年", year)

print((18.5-14.30)/14.30)