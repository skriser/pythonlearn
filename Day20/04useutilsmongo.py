#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/22 11:44
@author: 柴顺进
@file: 04useutilsmongo.py 
@software:rongda
@note: 
"""  
from Day20.mongoutils import Connect

grade_1_3 = Connect("myschool", "grade_1_3").get()
students = grade_1_3.find({},{"_id":0})
for docment in students:
    print(docment)
