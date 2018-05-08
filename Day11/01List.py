#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/08 9:36
@author: 柴顺进
@file: 01List.py 
@software:rongda
@note: list的基本函数
"""

list1 = [1, 2, 3, 4, 5, 6]
# # 取长度
print len(list1)
# # 取最大值
# print max(list1)
# # 取最小值
# print min(list1)
# 在结尾添加一个对象

list1.append('a')
list1.append([1, 3, 4])
print list1

# extend() 一次性增加多个元素在结尾，这个是对可迭代对象的添加，区别于append的是append把添加的当成一个元素
list1.extend([1, 2, 3, 4, 5, 56, 'as'])
print list1
# index() 从列表中找到某个值，返回第一个对象的位置
print list1.index(1)
# insert() 插入到列表中一个值
list1.insert(0, 0)
# remove() 删除第一个匹配项
list1.remove(3)
# reverse() 反转函数布袋排序
list1.remove(0)
print list1
# sort() 对原列表进行排序
list1.sort()
print list1

# 实现 去掉最大值和最小值 求剩余平均数
# grade = [100, 66, 75, 90, 100, 50, 73]
#
#
# def avgsGrade(args):
#     args = args[:]
#     args.remove(max(args))
#     args.remove(min(args))
#     print sum(args) / len(args)
#
#
# def avgsGrade1(args):
#     args = args[:]
#     args.sort()
#     args.pop(0)
#     args.pop(-1)
#     print sum(args) / len(args)
#
#
# def avgsGrade2(args):
#     print (sum(args)-max(args)-min(args))/((len(args)-2)*1.0)
#
#
# avgsGrade(grade)
# avgsGrade1(grade)
# avgsGrade2(grade)


