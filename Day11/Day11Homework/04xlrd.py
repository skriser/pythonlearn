#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/09 10:39
@author: 柴顺进
@file: 04xlrd.py 
@software:rongda
@note: 4、使用xlrd获取execl文件中的任意内容
"""  
import xlrd


class ExcelReader(object):

    def getExcelDataWithRow(self, filename):
        workbook1 = xlrd.open_workbook(filename)
        sheet1 = workbook1.sheet_by_index(0)
        myrows1 = sheet1.nrows
        for i in range(myrows1):
            myrows_value = sheet1.row_values(i)
            print(myrows_value)

    def getExcelDataWithCol(self, filename):
        workbook1 = xlrd.open_workbook(filename)
        sheet1 = workbook1.sheet_by_index(0)
        ncols1 = sheet1.ncols
        for i in range(ncols1):
            ncols_value = sheet1.col_values(i)
            print(ncols_value)

    def getExcelDataWithCell(self,filename):
        workbook1 = xlrd.open_workbook(filename)
        sheet1 = workbook1.sheet_by_index(0)
        ncols1 = sheet1.ncols
        nrows1 = sheet1.nrows
        for i in range(nrows1):
            for j in range(ncols1):
                ncell_value = sheet1.cell_value(i,j)
                print(ncell_value)


excleReader = ExcelReader()
excleReader.getExcelDataWithRow('../excelExample/某公司贸易数据.xlsx')
excleReader.getExcelDataWithCol('../excelExample/某公司贸易数据.xlsx')
excleReader.getExcelDataWithCell('../excelExample/某公司贸易数据.xlsx')