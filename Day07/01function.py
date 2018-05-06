#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/03 2018/5/3 11:12
@author: 柴顺进
@file: 01function.py 
@software:rongda
@note: 函数的基础知识学习
"""


def print_me(str1):
    # type: (str1) -> str1
    # 输出指定内容
    print str1

print_me( '初来乍到fun' )

def sayhello():
    print "你好"

sayhello()

def zhazhi(name,fruit):
    print name, '炸出了', fruit, '汁'

zhazhi('小红','苹果')