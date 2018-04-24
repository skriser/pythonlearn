#!usr/bin/env python  
#-*- coding:utf-8 *-
""" 
@time: 2018/04/24 2018/4/24 14:26
@author:chaishunjin 
@file: 05Tuple.py 
@software:rongda
@note: 元组的基础学习
"""  
# print 'hello'
# print ("hello")
# print ("hello",) #元组；只有一个值的元组要有一个逗号
# #创建元组
# tup1 = (1,2,'abc') #直接括起来
# tup2 = 'a','b','c',1  #不用括号直接创建元组
# #通过tuple() 函数把某种数据转换为元组
# tup3 = tuple('hello')
# tup4 = tuple([1,2,3])
# tup5 = tuple((4,5,6))
# print tup1+tup2
# del tup1
# print tup1

# tup = ('duan','jin','zhangsan','lisi',1,2)
# for i in tup:
#     print i
#
# for i in tup:
#     print i,  #加逗号直接打印在同一行；

tup1 = ('duan','jin','张三','李四',1,2)
# for i in tup1:
#     print i,
# print "\n"

print tup1  #输出会出现转码问题
#解决办法
#1.通过json自带方法
import json
print json.dumps(tup1).decode("unicode-escape")
