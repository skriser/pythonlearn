
#!usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/04 10:57
@author: 柴顺进
@file: 01baidu.py 
@software:rongda
@note: 
"""  
import urllib
from urllib import request

# 1.设置url地址
req = request.Request('http://www.baidu.com')

# 2.获取访问网站后，网站返回的对象
res = request.urlopen(req)

# 3.处理浏览器返回对象
# 3.1 如读取
print(res.read().decode("utf-8"))
#查看对象的属性和对应的返回信息
print(dir(res))
print(res.url)
print(res.code)
print(res.msg)