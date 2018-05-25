#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/08 14:29
@author: 柴顺进
@file: 05CSVWriter.py 
@software:rongda
@note: 写一个csv文件
"""
import csv

# 1. 打开文件，如果不存在就新建一个
with open('csvExample/CSVTest.csv', 'w+') as filew:
    # 用变量存储
    writer1 = csv.writer(filew)
    # row 行,写一行信息
    writer1.writerow(['id', 'url', 'keywords','sdf'])
    data = [(1, 'http://www.baidu.com', 'bd'), (2, 'http://www.baidu.com', 'bd2')]
    # 写入多行数据，rows是进行批量写入
    writer1.writerows(data)
    writer1.writerow(['id', 'url', 'keywords'])
    writer1.writerows(data)
