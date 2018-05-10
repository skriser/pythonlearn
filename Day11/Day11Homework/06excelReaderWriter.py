#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/09 11:26
@author: 柴顺进
@file: 06excelReaderWriter.py 
@software:rongda
@note: 6、分别获取两个工作表（ sheet ）中的一列信息，合并到一起放在一个新 的工作表（ sheet ）中
"""
import xlrd
import xlwt


class ExcelReaderWriter(object):

    def excelReader(self,filename):
        workbook1 = xlrd.open_workbook(filename)
        sheet1 = workbook1.sheet_by_index(0)
        data1 = sheet1.cell_value(0, 1)
        sheet2 = workbook1.sheet_by_index(1)
        data2 = sheet2.cell_value(0, 1)
        datas = [data1, data2]
        print(datas)
        return datas

    def excelWriter(self,filename,datas):
        workbook2 = xlwt.Workbook()
        # 疑问，每次出现都会写入一个新的sheet里面么，还是不存在这个sheet才会写入
        sheet1 = workbook2.add_sheet('合并sheet数据')
        sheet1.write(0, 1, datas)
        workbook2.save(filename)


excel2 = ExcelReaderWriter()
excel2.excelWriter('../excelExample/某公司贸易数据.xlsx',excel2.excelReader('../excelExample/某公司贸易数据1.xls'))
