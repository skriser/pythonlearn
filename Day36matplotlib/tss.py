#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/26 9:37
@author: 柴顺进
@file: tss.py 
@software:rongda
@note: 
"""  
from matplotlib import pyplot as plt
plt.rcParams["font.sans-serif"]=['SimHei']  # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示负号

plt.figure(figsize=(8, 4))
plt.plot([1,2,3,4],[4,7,29,16],label='简单折线图')  # 折线图 第一个list是x,第二个是y
plt.plot([2,3,4],[10,14,12],label='简单折线图2')
# plt.show()
# 完善图表
# 添加轴标签
plt.xlabel('X轴')
plt.ylabel('Y轴')
# 为图表添加标题
plt.title('为图表添加标题')
# 为图表添加小图标(图例) # 小图标就是图中的小的示意图
plt.legend()
# 为图表添加小图标,确定小图表的位置
plt.legend(loc='upper left')
# 显示图表
plt.show()