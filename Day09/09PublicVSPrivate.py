#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/06 15:19
@author: 柴顺进
@file: 09publicvsprivate.py 
@software:rongda
@note: 公有变量和私有变量
"""


class JustCounter:
    __private_count = 0
    public_count = 0

    def __init__(self):
        pass

    def count(self):
        self.__private_count += 1 # 访问私有变量通过self
        JustCounter.public_count += 1 # 访问公有变量使用className


counter1 = JustCounter()
counter1.count()
counter1.count()
print JustCounter.public_count
print counter1.public_count
counter2 = JustCounter()
counter2.count()
counter2.count()
print JustCounter.public_count
print counter2.public_count
