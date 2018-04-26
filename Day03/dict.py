# !usr/bin/env python
# -*- coding:utf-8 *-
""" 
@time: 2018/04/26 2018/4/26 9:41
@author:chaishunjin 
@file: dict.py 
@software:rongda
@note: 字典的基本使用
"""
# 创建字典 空字典进行赋值
dict1 = {}
print dict1
dict1['age'] = 20
print dict1

# 赋值式的添加或创建
person = {'name': 'qiwsir', 'language': 'python', 'name': 'yuwen'}
person['name2'] = 'qiwsir2'
print person  # 顺序发现随机

# 通过dict()把元组变为字典
tup1 = (['name1', 'baidu'], ['name2', 'google'])
website = dict(tup1)
website = dict((['name1', 'baidu'], ['name2', 'google']))
print website
# 4.直接使用key = value
ad = dict(name='qiwsir', age=22)
print ad

# 5 使用fromkeys() 只能使用两个参数。
web = {}.fromkeys(('first','seconde'),'facebook')
print web
web1 = {}.fromkeys(['first','seconde'],'facebook')
web = {}.fromkeys(('first','seconde'),('facebook','facebook2'))
print web
print web1

# 访问：
print person['name']

# 删除字典
class1 = {'name':'小李','age':18,"sex":"女"}
import  json
print json.dumps(class1).decode('unicode-escape')
print class1
print class1['name']