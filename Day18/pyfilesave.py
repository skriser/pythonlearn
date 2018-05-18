#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/17 14:52
@author: 柴顺进
@file: pyfilesave.py 
@software:rongda
@note: 五、编写python代码，将job.py文件中爬取的职位信息分别存储至mysql数据库中和excel表中
"""  
from Day18.job import getCollect
import openpyxl
from pymysql import connect
list_tup = getCollect()


def saveMysql(lists):
    conn = connect(host="localhost", user="root", password="root", charset="utf8", db="school")
    cursors = conn.cursor()
    sql_create = "create table if not exists `job_info`(`jname` varchar(50) ,`company` varchar(50),`location` varchar(100)," \
                 "`salary` VARCHAR (100));"
    sql_student = "insert into job_info VALUES ( '%s' , '%s' , '%s' , '%s');"

    cursors.execute(sql_create)
    for i in lists:
        cursors.execute(sql_student % i)
        conn.commit()
    cursors.close()
    conn.close()


def saveExcel(lists):
    lists.insert(0, ['职位名', '公司名', '地点', '薪资'])
    workbooks = openpyxl.Workbook()
    worksheets = workbooks.active
    for i in lists:
        worksheets.append(i)
    workbooks.save('mysqltest.xlsx')


saveMysql(list_tup)
saveExcel(list_tup)