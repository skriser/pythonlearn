#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/25 9:19
@author: 柴顺进
@file: 00numpy.py 
@software:rongda
@note: numpy入门
"""
import numpy as np
import time
# a = [x**2 for x in range(3)]
# b = [x**3 for x in range(3)]
# print(a)
# print(b)

# c = np.arange(3) # 产生一个0-2的数值
# d = np.arange(3)
# print(type(c))
# print(c)
# print(c**2)
# result = c**2+d**3
# print(result)


# def numpySum(n):
#     '''
#     np.arange(start,end,step,data_type)
#     start 开始位置
#     end  结束位置
#     step 步长
#     data_type：numpy数据类型
#     '''
#     a = np.arange(n)**2
#     b = np.arange(n)**3
#     c = a + b
#     return c
#
#
# result = numpySum(1292)
# print(result)

def numpySum(n):
    '''
    np.arange(start,end,step,data_type)
    start 开始位置
    end  结束位置
    step 步长
    data_type：numpy数据类型
    '''
    a = np.arange(0, n, 1, np.int64)**2
    b = np.arange(0, n, 1, np.int64)**3
    c = a + b
    return c


def countTime(arg):
    def wrapper(n):
        startTime = time.time()
        arg(n)
        endTime = time.time()
        print(arg, "执行耗时是：", (endTime-startTime)*1000)
        return arg(n)
    return wrapper


@countTime
def multiplication(n):
    a = np.arange(0, n, 1, np.int64)
    b = np.arange(0, n, 1, np.int64)
    return a * b


def create(n,num):
    a = []
    for i in range(n):
        a.append(i**num)
    return a

# 0~n的平方的列表
# a = create(3,2)
# print(a)
# b = create(3,3)
# print(b)
@countTime
def pythonsum(n):
    a = create(n,2)
    b = create(n,3)

    c = [] #存放结果
    for i in range(len(a)):
        c.append(a[i]+b[i])
    return c


ss = multiplication(1000000)
dd = pythonsum(1000000)
# print(type(ss))
# print(ss)