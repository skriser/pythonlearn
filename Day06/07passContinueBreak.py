#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/02 2018/5/2 13:36
@author: 柴顺进
@file: 07passContinueBreak.py 
@software:rongda
@note: pass ,continue,break 都只对当前的这一层循环起作用
"""

# pass 保证程序的完整性

# continue 跳过本次循环
for i in range(4):
    print i
    for j in range(5):
        # if j == 2:
        #  break
        #  #continue
        print j,
    print