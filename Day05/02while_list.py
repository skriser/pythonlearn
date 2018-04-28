#!usr/bin/env python  
# -*- coding:utf-8 -*-

import random
""" 
@time: 2018/04/28 2018/4/28 9:29
@author: 柴顺进
@file: 02while_list.py 
@software:rongda
@note: 4、使用while循环求列表[12,27,3,26,8,33]中的奇偶数，并分别存放新的 列表中
"""  




# 猜数字：猜1-100某个数，记录猜的次数，猜中为止 ,区间判断加入进去，完善异常逻辑
def judge(userInput):
    flag = 1
    while flag:
        print "需要输入[1,100]之间的数！"
        if not userInput.strip().isdigit():
            userInput = raw_input("请重新猜222：")
    else:
        return int(userInput)

numRan = random.randint(1, 100)
count = 0
list1 = [1, 100]
# print numRan
print "电脑已生成0--100之间的神秘数字，猜中有奖"
userInput = judge(raw_input("请输入你猜的1--100中的任意一个数："))
while numRan != userInput:
    count += 1
    if numRan > userInput:
        list1[0] = userInput
    else:
        list1[1] = userInput
    print "这个数字区间", list1
    print "您已猜了", count,"次"
    userInput = judge(raw_input("请重新猜wwwad ："))
else:
    print "最初的数是:", numRan, "恭喜你猜中了"

