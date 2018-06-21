#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/04 14:19
@author: 柴顺进
@file: 04try.py 
@software:rongda
@note: 出现异常怎么处理
"""  
import urllib2

try:
    req = urllib2.Request("http://www.baidu.com")
    res = urllib2.urlopen(req)
except urllib2.URLError, e:
    print e.reason
print 'over'
