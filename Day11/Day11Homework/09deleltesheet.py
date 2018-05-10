#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/10 8:53
@author: 柴顺进
@file: 09deleltesheet.py 
@software:rongda
@note: 9、删除已存在工作簿中的某个表
"""  
from openpyxl import load_workbook

workbook1 = load_workbook('09test.xlsx')
print(workbook1)
print(workbook1['wsd'])
workbook1.remove(workbook1['wsd'])
# 需要保存一下要不然不生效
workbook1.save('09test.xlsx')