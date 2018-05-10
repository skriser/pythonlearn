#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/09 9:32
@author: 柴顺进
@file: 01csvrandom.py
@software:rongda
@note: 1、生成随机数并写入文件，然后读取打印，效果如下：
"""
import random
import csv
# 1.随机数生成：uniform（）


class CsvRandomWriterReader(object):

    def __init__(self):
        self.list1 = []
        for i in range(4):
            list2 = []
            for j in range(4):
                random_num = random.uniform(-1, 1)
                list2.append(random_num)
            self.list1.append(list2)
        self.list1[0][3] = '欢迎'
        self.list1[1][3] = '光临'

    def writerCsv(self,filename):
        with open(filename, 'w', newline='') as random_file_writer:
            writer1 = csv.writer(random_file_writer)
            writer1.writerows(self.list1)

    def readCsv(self, filename):
        with open(filename, 'r') as random_file_reader:
            reader1 = csv.reader(random_file_reader)
            for n in reader1:
                print(n)


csvrandom = CsvRandomWriterReader()
csvrandom.writerCsv('csj.csv')
csvrandom.readCsv('csj.csv')