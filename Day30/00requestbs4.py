#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/06 9:07
@author: 柴顺进
@file: 00requestbs4.py 
@software:rongda
@note: 
"""
import chardet
import requests

r = requests.get('https://baidu.com')
r.encoding = 'utf-8' # 这个是对返回对象进行编码指定
code = chardet.detect(r.content)['encoding'] # 预先获取对象的编码格式
# 方法一，通过对返回对象声明编码
# r.encoding = code
# 方法二，直接解码
r.content.decode(code)
print(r.text)
# 编码存在问题
print(type(r.text))
