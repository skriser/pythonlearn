#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/25 16:25
@author: 柴顺进
@file: 09ArrayExtendDimensions.py 
@software:rongda
@note: 数组维度扩展
"""  
import numpy as np

line = np.arange(24)
print(line)

# 将line改变为2层,3行,4列;line本来是一个一维数组
result = line.reshape(2, 3, 4) # reshape 是对视图进行修改，不修改line本身
# print(result)
# 方法二 shape
line.shape = (2, 3, 4) # shape改变数组的形状，会修改数组本身
# print(line)

# 方法三
line.resize(2, 2, 6) # resize修改数组的形状会修改数组本身
# print(line)

# 把已经更改的再变回来
# 方法一
# line.resize(24)
# print(line)
# 方法二
# result1 = line.reshape(24)
# print(result1)
# 方法三
# line.shape = 24
# print(line)
# 方法四
d1 = line.ravel()
d1[0] = 1  # d1 和 line使用的是同一份元数据，修改d1会改变line
print(d1)
print(line)
# 方法五
d2 = line.flatten()
d2[0] = 1  # d2 是 line复制的一份数据，修改d2，不会改变line
print(d2)
print(line)
# 方法四与方法五之间的区别