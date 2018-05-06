#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/06 14:03
@author: 柴顺进
@file: 07CreateClass2.py 
@software:rongda
@note: 
"""


class Employee:
    count = 0
    name = 'sdf'

    def __init__(self, name, salary):
        # 前后编写带有语义的时候容易记忆参数
        # self 是代表当前的对象实例的数据。
        self.name = name
        self.salary = salary
        self.address = 'sfa'
        Employee.count += 1

    def showCount(self):
        print '已经有%d位小伙伴' % Employee.count

    def showInfo(self):
        print 'Name:', self.name, 'Salary', self.salary


# e1 = Employee('na11me', 2000)
# e1.showCount()
# e2 = Employee('nam1e', 4000)
# e2.showCount()
# print e1.name, e2.address
# print Employee.name
