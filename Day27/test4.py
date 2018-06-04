#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/01 16:57
@author: 柴顺进
@file: test4.py 
@software:rongda
@note: 
"""
import numpy as np
'''
Order_id: 订单id号
Account_id:消费账户id
Account_to:消费账号
Amoount:消费金额
K_symbol:无效数据列

请根据跟定的数据集，编写python代码实现如下需求：
（1）	根据bank_to字段，用numpy统计出每不同bank_to字段下所有消费记录的均值、最大值、最小值、并求和。
（2）	然后将每个字段分类下的所有消费记录写入到一个新的csv文件中， 
输出文件中包含：CD.csv   IJ.csv  QR.csv    AB.csv
'''
# t = np.dtype([("order_id", np.int32), ("account_id", np.int32), ("bank_to", np.str_,40),("account_to", np.int32),("amount", np.int32),("k_symbol", np.int32)])
# bank_to,amount = np.loadtxt('order.csv', delimiter=",",dtype=np.str_,usecols=(2,4),unpack=True,skiprows=1)
# CD_amount = np.compress(bank_to == "CD",amount)
# CD_amount.astype(np.float32)
# CD_mean = np.mean(CD_amount.astype(np.float32))
#
# list1 = ['CD','IJ','QR','AB']
# for i in range(4):
#     tmp = np.compress(bank_to == list1[i], amount)
#     tt = tmp.astype(np.float32)
#     avg1 = np.mean(tt)
#     min1 = np.min(tt)
#     max1 = np.max(tt)
#     sum1 = np.sum(tt)
#     print("{}的均值是：{}，最小值为：{}，最大值为：{}，求和为{}".format(list1[i],avg1,min1,max1,sum1))
data = np.loadtxt('order.csv', delimiter=",",dtype=np.str_,skiprows=1)
indecis_cd = np.where(data[:,2] == "CD")
indecis_ij = np.where(data[:,2] == "IJ")
indecis_qr = np.where(data[:,2] == "QR")
indecis_ab = np.where(data[:,2] == "AB")
order_id,account_id,bank_to,account_to,amount,k_symbol =\
data[:,0],data[:,1],data[:,2],data[:,3],data[:,4],data[:,5]
cd_data = []
ij_data = []
qr_data = []
ab_data = []
list1 = []
for i,order,accountid,bank,account,amount,symbol in zip(range(len(order_id)),order_id,account_id,bank_to,account_to,amount,k_symbol):
    if (np.array(indecis_cd) == i).any():
        cd_data.append([order,accountid,bank,account,amount,symbol])
    elif (i == np.array(indecis_ab)).any():
        ab_data.append([order,accountid,bank,account,amount,symbol])
    elif (i == np.array(indecis_ij)).any():
        ij_data.append([order,accountid,bank,account,amount,symbol])
    elif (i == np.array(indecis_qr)).any():
        qr_data.append([order,accountid,bank,account,amount,symbol])

np.savetxt("CD.csv", cd_data, delimiter=",", fmt="%s",newline="\n")
np.savetxt("IJ.csv", ij_data, delimiter=",", fmt="%s",newline="\n")
np.savetxt("QR.csv", qr_data, delimiter=",", fmt="%s",newline="\n")
np.savetxt("AB.csv", ab_data, delimiter=",", fmt="%s",newline="\n")

