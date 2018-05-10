#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/09 11:38
@author: 柴顺进
@file: 07xlutilsPractice.py
@software:rongda
@note: 7、 使用 xlutils 向原有的 Excel 文件中添加数据
"""  

import xlrd
from xlutils.copy import copy

workbook = xlrd.open_workbook('test07.xlsx')
workbooknew = copy(workbook)
ws = workbooknew.get_sheet(0)
ws.write(2, 0, 1000)
ws.write(2, 1, 'javascript')
ws.write(3, 0, 1001)
ws.write(3, 1, 'HTML')
workbooknew.save('test07.xls')

