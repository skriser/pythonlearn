#!usr/bin/env python  
#-*- coding:utf-8 *-
""" 
@time: 2018/04/23 2018/4/23 15:42
@author:chaishunjin 
@file: Variable.py 
@software:rongda
"""  
name ='张三'
age = '20'
sex = '男'
hobby = '抽烟，喝酒，烫头，学习娱乐，看电影！'
str(age)
print name + ',' +age +','+sex + ','+hobby

print name,age,sex,hobby

print id(3)
a = 3
b = 3
print id(a)
print id(b)
print id(hobby)
ws = '抽烟，喝酒，烫头，学习娱乐，看电影！'
print id(ws)