#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/28 10:29
@author: 柴顺进
@file: 数组的属性.py 
@software:rongda
@note: 
"""
import numpy as np

#
# example = np.arange(24).reshape(3, 4, 2)
#
# # 1.ndimi 数组的维度
# print("维度：", example.ndim)
# # 2.size数组元素的个数
# print("元素的个数：", example.size)
# # 3.itemsize数组中每个元素所占的字节数
# print("元素的每个元素占的字节数：", example.itemsize)
# # 4.nbytes整个数组所占字节数
# print("元素的每个元素占的字节数：", example.nbytes)
# print("元素的每个元素占的字节数：", example.size*example.itemsize)
# # 5.T数组的转置结果
# print("原数组\n",example)
# print("转置的结果\n", example.T)
# # 6.real 复数数组的实际部分
# comp = np.array([2+5j, 6+3j, 4+2j])
# real = comp.real
# print("复数的实际部分：\n", real)
# # 7.imag 复数数组的虚部
# imag = comp.imag
# print("复数的虚部分：\n", imag)
# # 8.求comp 复数数组的每个元素的模
# print("复数数组的每个元素的模", np.sqrt(real**2+imag**2))
# # 9.将数组展平
print("*******************************************")
iterator1 = np.arange(9).reshape(3,3)
result1 = iterator1.flat
for it1 in result1:
    print(it1)