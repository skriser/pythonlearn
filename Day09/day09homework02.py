#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/06 16:30
@author: 柴顺进
@file: day09homework02.py 
@software:rongda
@note: 
"""  
# .定义一个学生类。有下面的类属性： 1 姓名 2 年龄 3 成绩（语文，数学，英语)[每课成绩的类型为整数]
# 类方法： 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
# 写好类以后，可以定义2个同学测试下: zm = Student('zhangming',20,[69,88,100]) 返回结果： zhangming 20 100


class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        self.grade.reverse()
        return self.grade[0]


zm = Student('zhangming', 20, [69, 88, 100])

print zm.get_name(), zm.get_age(), zm.get_course()

