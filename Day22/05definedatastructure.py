#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/25 14:26
@author: 柴顺进
@file: 05definedatastructure.py 
@software:rongda
@note: 自定义numpy数据类型
因为在numpy中数据同一个矩阵中存储的是一致的数据，所以不能在一个矩阵中混合使用不同
的数据类型，这就要用户自定义数据类型了
"""
import numpy as np

arr2 = np.array([1, "2", 2+3j])
print(arr2)
print(arr2.dtype)
arr3 = np.array([4,5,6,6.0,True]) # 会进行向上转型
print(arr3)
'''
：利用 dtype 创建一个存储商店库信息的数据类
用一个长度为 0个字符的串来记录商品名称，
用一32 位的整数来记录商品库存量，最后用一个 32 位的单精度浮点数来记录商品价格。
效果如下：
name    num     price
DVD     42      3.14
Butter  13      2.72
'''
# 先定义一个混合类型
t = np.dtype([("name", np.str_, 40), ("num", np.int32), ("price", np.float32)])
print(t)

# 使用自定义类型;使用元组的不可分割性
products = np.array([("DVD", 42, 3.14), ("Butter", 13, 2.72)], dtype=t)
print(products)

# 获取products数组中有几个元素
print(products.size)
# 通过两层循环获取值
for i in range(products.size):
    for j in range(len(products[i])):
        print(products[i][j])

# 通过定义的数据类型来获取每个里面的值
for i in range(products.size):
    print(products[i]["name"])
    print(products[i]["num"])
    print(products[i]["price"])

