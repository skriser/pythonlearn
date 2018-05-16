
#!usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/16 16:25
@author: 柴顺进
@file: homework.py 
@software:rongda
@note: 
"""  
import pymysql
import openpyxl


def getConnect(host, user, password, db, charset):
    return pymysql.connect(host=host, user=user, password=password, db=db, charset=charset)
def insertData(data,conn1):
    sql = "insert into movieRank VALUES('%s','%f','%f','%d','%f')"
    curs = con.cursor()
    curs.execute(sql % data)
    conn1.commit()
    print("插入{}条数据成功！".format(curs.rowcount))


data = ('犬之岛',617.35,0.0908,2,1309.09)
data1 = ('湮灭',135.34,0.0199,9,5556.77)
con = getConnect("localhost", "root", "root", "movies", "utf8")
insertData(data, con)
insertData(data1, con)


def query(sql, con):
    curs = con.cursor()
    curs.execute(sql)
    con.commit()
    allRes = curs.fetchall()
    fieldTitle = curs.description
    return fieldTitle, allRes


sql = 'select * from movieRank'
result = query(sql, con)
list1 = []
list2 = []
for j in result[0]:
    list1.append(j[0])
list2.append(list1)
for i in result[1]:
    list2.append(i)


def saveData(list_data,filename):
    # 1.实例化对象
    workbook = openpyxl.Workbook()
    # 2.激活一个工作簿
    sheet = workbook.active
    # 3.给表定一个标题
    sheet.tittle = 'mysshe'
    # # 5.1横向行赋值。通过append()方法，按照行添加数据,append 一次添加一行
    for i in list_data:
        sheet.append(i)
    # 6.保存
    workbook.save(filename)


saveData(list2,'homework_csj.xlsx')

