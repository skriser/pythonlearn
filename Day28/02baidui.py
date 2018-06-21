#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/04 11:34
@author: 柴顺进
@file: 02baidui.py 
@software:rongda
@note: 
"""  
from urllib import request

# 1.设置url地址
req = request.Request('http://www.baidu.com')
# 2.增加头部信息
req.add_header('User-Agent',"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1")
# 设置IP代理地址
req.set_proxy('114.215.95.188:3128', 'http')



# 2.获取访问网站后，网站返回的对象
res = request.urlopen(req)

# 3.处理浏览器返回对象
# 3.1 如读取
print(res.read().decode("utf-8"))
