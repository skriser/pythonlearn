#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/25 15:32
@author: 柴顺进
@file: threeDimensionsArray.py 
@software:rongda
@note: 三维数组的使用
"""  
import numpy as np

# 创建三维矩阵数组2x2x5
heros = np.array([
                [
                    ["苏烈", "程咬金", "廉颇", "亚瑟"],
                    ["后羿", "公孙离", "狄仁杰", "鲁班"]
                ],
              [
                  ["王昭君", "安其拉", "貂蝉", "小乔"],
                  ["孙膑", "大乔", "鬼谷子", "蔡文姬"]],
              [
                  ["凯", "刘邦", "孙悟空", "刘备"],
                  ["项羽", "刘禅", "庄周", "东皇太一"]]], dtype="U10")
# print(heros)
# # 找到庄周 ，三维索引
# print(heros[2, 1, 2])
# print(heros[2][1][2])

# 切片
# 分别获取第一二三层
# print(heros[0])
# print(heros[1])
# 获取 ['公孙离' '大乔' '刘禅']
print(heros[:, 1, 1])
# 获取第二层的数
print()