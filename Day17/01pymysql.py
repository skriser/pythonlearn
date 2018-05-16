#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/16 10:52
@author: 柴顺进
@file: 01pymysql.py 
@software:rongda
@note: 使用pymysql进行操作mysql数据库
"""  
import pymysql

# 获取连接对象
connect = pymysql.connect(host="localhost", user="root", password="root",db="shop",
                          charset="utf8", port=3306)

# 2.从连接对象中获取游标
cursor = connect.cursor()

# 3.组装SQL语句
sql = 'select * from stu_score'

# 4.执行SQL语句
cursor.execute(sql)
# 5.如果是insert,update
# connect.commit()
# # 6.处理获取结果
# one = cursor.fetchone()
# print(one)
# two = cursor.fetchone()
# print(one)
# # 获取多条
# many = cursor.fetchmany(4)
# print(many)
# 游标是会移动的，在获取中fetchone 和fethcmany,fetchall都从游标记录访问的地方
# 6.获取所有记录
all = cursor.fetchall()
data = []
for i in all:
    data.append(list(i))
print(data)

condition = True
while condition:
    item = cursor.fetchone()
    data.append(item)
    condition = item
# 7.关闭连接
cursor.close()
connect.close()
