#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/25 11:11
@author: 柴顺进
@file: 01createnumpy.py 
@software:rongda
@note: 常规创建数组的方法
"""  
import numpy as np

# 1.使用arange()函数
a = np.arange(5)

# 2.利用python中的list进行创建 np.array(list)
b = np.array([12,5,5,5,7.0,13.1])
print(b)

# 3.创建一个从a-b范围内取n点的等间距分布的数组
'''
np .linspace(start,end,points,endpoints)
start 开始数据
end  结束数据
points ：在start--end之间取得点的个数
endpoints: 是否取到最后一个数据end的值
'''
c = np.linspace(0, 10, 4, endpoint=False)
print(c)

print(c.shape) # 返回一个元组，存放对象每维度上的大小
print(c.dtype) # 获取 NumPy 数组元素的类型


'''
二维数组的创建
'''

d2 = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8]])
# 列数要一致，要不就会错误
print(d2.shape)
print(d2)
