#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/10 9:14
@author: 柴顺进
@file: 08homework02.py 
@software:rongda
@note: 8、使用openpyxl简单的编写一个写入数据到execl小案例，如下图所示：
openpyxl是可以进行xlsx进行保存和读写
"""  
from openpyxl import Workbook
from openpyxl import load_workbook

# 1.实例化对象
workbook = Workbook()
# 2.激活一个工作簿
sheet = workbook.active
# 3.给表定一个标题
sheet.tittle = 'homework8'
# 4.创建数据
data = [
    ['HTML', 'CSS', 'javascript'],
    ['this is a1', '', 'this is c1'],
    ['hehe', '', '', 'haha']
]
# # 5.1横向行赋值。通过append()方法，按照行添加数据,append 一次添加一行
# for i in data:
#     sheet.append(i)
# 5.2 按照列添加数据
col_name = ['A%d', 'B%d', 'C%d', 'D%d']
newData = list(zip(*data))
for i in range(len(newData)):
    for j in range(len(newData[i])):
        sheet[col_name[i] % (j+1)] = newData[i][j]




# 6.保存
workbook.save('test08.xlsx')