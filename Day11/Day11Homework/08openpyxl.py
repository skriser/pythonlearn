#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/10 8:52
@author: 柴顺进
@file: 08openpyxl.py 
@software:rongda
@note: 8、使用openpyxl简单的编写一个写入数据到execl小案例，如下图所示：
https://blog.csdn.net/u014647208/article/details/78684812 # 不错的案例
"""

# 使用openpyxl进行读写操作
from openpyxl import Workbook
# list_a = ['HTML','this is al','hehe']
# list_b = ['CSS']
# list_c = ['javascript','this is c1']

workbook1 = Workbook()
sheet1 = workbook1.active ## 得到正在运行的表

list_d = ['','','haha']
sheet1['A1'] = 'HTML'
sheet1['A2'] = 'this is al'
sheet1['A3'] = 'hehe'
sheet1['B1'] = 'CSS'
sheet1['C1'] = 'javascript'
sheet1['C2'] = 'this is c1'
sheet1['D3'] = 'haha'
workbook1.save("08test.xlsx")