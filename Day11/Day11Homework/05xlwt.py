#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/09 10:59
@author: 柴顺进
@file: 05xlwt.py 
@software:rongda
@note: 5、在xlwt创建Excel文件内容时，设置字体样式，如下图所示
"""  
import xlwt
from xlwt import Font, XFStyle


class ExcelWriter(object):

    def excelWriter(self, filename):
        workbook1 = xlwt.Workbook()
        sheet1 = workbook1.add_sheet('表01')
        sheet1.write(0, 0, 'Unformated value')
        sheet1.write(0, 1, '大家好')
        # 设置字体样式
        font1 = Font()
        font1.name = '华文琥珀'
        style = XFStyle()
        style.font = font1
        sheet1.write(1, 0, 'Formated value', style)
        workbook1.save(filename)


excel2 = ExcelWriter()
excel2.excelWriter('test1.xls')
