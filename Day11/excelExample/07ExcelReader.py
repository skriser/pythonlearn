#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/08 16:12
@author: 柴顺进
@file: 07ExcelReader.py
@software:rongda
@note: 
"""  
import xlrd
myworkbook = xlrd.open_workbook('某公司贸易数据.xlsx')
# 读取工作簿

# 读取工作表list
mysheets = myworkbook.sheets()
# 获取第一张表
mysheet1 = mysheets[0]
mysheet2 = myworkbook.sheet_by_index(0)
mysheet3 = myworkbook.sheet_by_name('产品类别')
mysheet4 = myworkbook.sheet_loaded('产品类别')
# 获取行和列的数量
myrows = mysheet1.nrows # 行
mycols = mysheet1.ncols # 列
# 获取行和列的内容
for i in range(myrows):
    myRowValues = mysheet1.row_values(i)
    print(myRowValues)

print('-------------------------------------------------------')
for j in range(mycols):
    myColValues = mysheet1.col_values(j)
    print(myColValues)

# 读取每一个单元格，输出里面的内容
# for i in range(myrows):
#     for j in range(mycols):
#         mycell = mysheet1.cell(i, j)
#         myCellValue = mycell.value
#         print(myCellValue)

# 获取单个单元格
print(mysheet1.cell(4, 2).value) # 先获取对象，在获取value值

print(mysheet1.cell_value(1, 2)) # 直接根据索引获得value值
