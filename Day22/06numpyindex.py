#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/25 14:50
@author: 柴顺进
@file: numpyindex.py 
@software:rongda
@note: 切片，索引
"""  
import numpy as np

# 一维数组
heros = np.array(["韩信", "赵云", "孙尚香", "孙悟空", "阿珂"], dtype="U8")
# 索引访问
print(heros[2])
# 切片使用
print(heros[:2])
print(heros[3:]);print(heros[-2:])
# 二维数组
heros1 = np.array([["苏烈", "程咬金", "廉颇"], ["后羿", "公孙离", "狄仁杰"]], dtype="U8")
print(heros1.shape)
print(heros1[1][2]) # 行，列
print(heros1[1, 2]) # 直接将行列放在一个里面用逗号隔开也可以
print(heros1[:, 1]) # 获取两行中的中间一列
print(heros1[:, ::2]) # 获取列步长2
