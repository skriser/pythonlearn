#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/08 16:55
@author: 柴顺进
@file: 08ExcelWriter.py 
@software:rongda
@note: 
"""  
import xlwt
from openpyxl.writer.excel import ExcelWriter
# 导入前面是文件和文件夹，在python中文件和文件夹小写，类名大写
# 导入的只能从文件夹开始
from Day11.excelExample.sssss import TestOTG
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('表01')
sheet.write(0,1,'test text')
wbk.save('./text.xls')
print('ok')