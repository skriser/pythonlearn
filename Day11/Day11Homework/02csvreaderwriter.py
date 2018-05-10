#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/09 10:25
@author: 柴顺进
@file: 02csvreaderwriter.py 
@software:rongda
@note: 2、写入文件，然后读取打印，效果如下
"""  
import csv

class CsvWriterReader(object):

    def __init__(self):
        self.list1 = [[1001, '上海', '经济'], [1002, '北京', '政治'], [1003, '成都', '文化']]

    def csvWriter(self,filename):
        with open(filename,'w',newline='') as wcsv:
            writer1 = csv.writer(wcsv)
            writer1.writerows(self.list1)

    def csvReader(self,filename):
        with open(filename,'r') as rcsv:
            reader1 = csv.reader(rcsv)
            for i in reader1:
                print(i)


csvwr = CsvWriterReader()
csvwr.csvWriter('mycsv.csv')
csvwr.csvReader('mycsv.csv')