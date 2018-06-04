#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/28 11:17
@author: 柴顺进
@file: 保存数据.py 
@software:rongda
@note: 
"""  
import numpy as np

example = np.arange(24).reshape(3, 8)
# numpy的ndarray 数组保存到文本文件中
# savetxt(filename,data)
# data: 需要保存的数据
# 总股本变更保存1,2维度的数据
np.savetxt("example.txt", example)
print("保存完成")
