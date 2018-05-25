#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/22 10:21
@author: 柴顺进
@file: 00pymongo.py 
@software:rongda
@note: 使用python操作MongoDB
"""  
from pymongo import MongoClient

# 1.连接MongoDB数据库
conn = MongoClient("localhost")
# 2.关联某个数据库
'''
关联某个数据库 ：连接名.数据库名
1.关联的数据库存在，则直接关联该数据库
2.关联数据库不存在，则创建该数据库
'''
db = conn.myschool
# 3.关联数据表：关联数据表集合和关联数据库一样的
grade_1_3 = db.grade_1_3
# 4.对表数据的相关操作
result = grade_1_3.find({}, {"_id": 0, "name": 1})
# 5.通过for对结果进行迭代
# for document in result:
#     print(document)
# 6.插入数据
info = {"name": 'gaogao', "age": 7, "sex": "0","hobby":["游戏","音乐","电影","画画"]}
grade_1_3.insert_one(info)

