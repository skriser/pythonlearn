#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/18 16:26
@author: 柴顺进
@file: mysqlquerypaging.py
@software:rongda
@note: 分页查询
"""
from pymysql import connect

conn = connect(host="localhost", user="root", password="root", charset="utf8", db="school")
cursors = conn.cursor()

# 定义变量，保存当前页码
currentPage = 1
# 定义变量保存每页显示记录数
pageNum = 10
for page in range(1, 20):
    # 组装SQL
    sql_ = "select * from job_info limit %d,%d "
    startIndex = (page-1)*pageNum
    cursors.execute(sql_ % (startIndex, pageNum))
    print("*************第{}页数据*****************".format(page))
    for row in cursors.fetchall():
        print(row)


def query_pagination(page_index, page_number):
    sql_ = "select * from job_info limit %d,%d "
    startIndex = (page_index - 1) * page_number
    cursors.execute(sql_ % (startIndex, page_number))
    print("*************第{}页数据*****************".format(page))
    for row in cursors.fetchall():
        print(row)

