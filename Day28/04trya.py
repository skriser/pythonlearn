#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/04 15:21
@author: 柴顺进
@file: 04trya.py 
@software:rongda
@note: 
"""  
import urllib2

req = urllib2.Request('https://blog.csdn.net/cecrel')

try:
    res = urllib2.urlopen(req)
except urllib2.HTTPError,e:
    print dir(e)
    print e.code
    print e.msg
except urllib2.URLError, e:
    print dir(e)
    print e.reason

print 'over'