#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/22 10:53
@author: 柴顺进
@file: 01pymongoquery.py
@software:rongda
@note: 
"""  
from pymongo import MongoClient

conn = MongoClient("localhost")
db = conn.myschool
grade_1_3 = db.grade_1_3
person1 = {
    "name": "妲己",
    "sex": "女",
    "age": 1000,
    "hobby": ["弹琴", "画画", "跳舞"]
}
person2 = {
    "name": "安琪拉",
    "sex": "女",
    "age": 16,
    "hobby": ["看书", "玩火", "蹲草丛"]
}
grade_1_3.insert([person1, person2])
