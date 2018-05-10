#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/08 17:28
@author: 柴顺进
@file: 09Xlutils.py 
@software:rongda
@note: xlutils 的使用
"""  
import xlrd
from xlutils.copy import copy
# 打开文件
workbook1 = xlrd.open_workbook('excelExample/某公司贸易数据.xlsx')
# 通过导入的copy 复制一份
workbookNew = copy(workbook1)
# 得到一个表
sheet1 = workbookNew.get_sheet(0)
#写文件
sheet1.write(3, 0, 'change')
#保存文件
workbookNew.save('excelExample/xlutils.xls')