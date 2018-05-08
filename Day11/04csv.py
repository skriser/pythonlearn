#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/08 14:09
@author: 柴顺进
@file: 04csv.py 
@software:rongda
@note: CSV文件的读取
"""  
import csv
with open('csvExample/销售相关企业信息.csv', 'r') as csvfile:
    # 打开 一个文件只读，把它赋给csvfile(这个是命名自定义的)
    read = csv.reader(csvfile)
    for i in read:
        print(i)