#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/10 10:17
@author: 柴顺进
@file: savexcel.py 
@software:rongda
@note: 
"""
from openpyxl import Workbook


class SaveExcelData(object):

    def __init__(self, dataList, tittle, filename):
        self.dataList = dataList
        self.tittle = tittle
        self.filename = filename

    def saveData(self):
        # 1.实例化对象
        workbook = Workbook()
        # 2.激活一个工作簿
        sheet = workbook.active
        # 3.给表定一个标题
        sheet.tittle = self.tittle
        # # 5.1横向行赋值。通过append()方法，按照行添加数据,append 一次添加一行
        for i in self.dataList:
            sheet.append(i)
        # 6.保存
        workbook.save(self.filename)