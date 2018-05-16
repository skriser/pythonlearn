#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/16 15:06
@author: 柴顺进
@file: CC.py 
@software:rongda
@note: 
"""
from Day17.connect import getConnect

conn = getConnect("localhost", "root", "root", "shop", "utf8")
curs = conn.cursor()
sql = 'insert into commoditytype VALUES (%s,"%s")'
print(sql%("null","'书籍'"))
curs.execute(sql % ('null','sss'))
conn.commit()



#
# def insert(data):
#     conn = getConnect("localhost", "root", "root", "shop", "utf8")
#     curs = conn.cursor()
#     sql = 'insert into commodity VALUES (null,%s)'
#     curs.execute(sql % data)
#     conn.commit()
