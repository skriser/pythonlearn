#!usr/bin/env python  
# -*- coding:utf-8 *-
""" 
@time: 2018/04/26 2018/4/26 16:18
@author: 柴顺进
@file: Homework02.py 
@software:rongda
@note: if elif Python 控制流程作业
"""  
# 1输入三个整数x,y,z，请把这三个数由大到小输出。
x = int(raw_input("请输入X："))
y = int(raw_input("请输入Y："))
z = int(raw_input("请输入Z："))
if x > y and x > z:
    if y > z:
        print x, y, z
    else:
        print x, z, y
elif y > z:
    if z > x:
        print y, z, x
    else:
        print y, x, z
else:
    if y > x:
        print z, y, x
    else:
        print z, x, y

# if x>y>z:
#     print x, y, z
# elif x>z>y:
#     print x, z, y
# elif y>x>z:
#     print y, x, z
# elif y>z>x:
#     print y, z, x
# elif z>x>y:
#     print z, x, y
# else:
#     print z, y, x

# 2.依次输入三角形的三边长，判断能否生成一个三角形。
x = int(raw_input("请输入三角形的第一条边："))
y = int(raw_input("请输入三角形的第二条边："))
z = int(raw_input("请输入三角形的第三条边："))
if ((x + y) > z) and ((x + z) > y) and ((z + y) > x):
    print "可以组成一个三角形"
else:
    print "无法组成一个三角形"

# 3、依次输入三角形的三边长，判断能否生成一个等腰三角形。
x = int(raw_input("请输入三角形的第一条边："))
y = int(raw_input("请输入三角形的第二条边："))
z = int(raw_input("请输入三角形的第三条边："))
if ((x + y) > z) and ((x + z) > y) and ((z + y) > x):
    if (x == y) or (y == z) or (x == z):
        print "这是等腰三角形"
    else:
        print "不是等腰三角形"
else:
    print "无法组成一个三角形"

# 4、依次输入三角形的三边长，判断能否生成一个直角三角形。
x = int(raw_input("请输入三角形的第一条边："))
y = int(raw_input("请输入三角形的第二条边："))
z = int(raw_input("请输入三角形的第三条边："))
if ((x + y) > z) and ((x + z) > y) and ((z + y) > x):
    if (x**2 + y**2 == z**2) or (x**2 + z**2 == y**2) or (y**2 + z**2 == x**2):
        print "这是直角三角形"
    else:
        print "不是直角三角形"
else:
    print "无法组成一个三角形"

# 5、猜拳游戏： 用户输入石头、剪刀或布，电脑也会出一个招，要求得出 最终结果，显示胜利玩家。
# 提示1：用数字代表猜拳    提示2：使用条件判断语句    提示3：import random    random.randint(m,n )为取m-n随机整数的方法
# import random
# print "##猜拳游戏##"
# print "你可以输入 1:(表示剪刀) 2:(表示石头) 3:(表示布)"
# userInput = int(raw_input("请输入你要出的是剪刀(1)，石头(2)，布(3)："))
# dict1 = {1: '剪刀', 2: '石头', 3: '布'}
# cpuInput = random.randint(1, 3)
# print "您出的是：" + dict1[userInput]
# print "电脑出的是：" + dict1[cpuInput]
# if userInput == cpuInput:
#     print "恭喜您，平局；再来一局吧！"
# elif ((userInput == 1) and (cpuInput == 3)) or ((userInput == 2) and (cpuInput == 1)) or \
#         ((userInput == 3) and (cpuInput == 2)):
#     print "您赢了！！！"
# else:
#     print "您输了！！"


import random
dict2 = {'剪刀': 1, '石头': 2, '布': 3}
dict1 = {1: '剪刀', 2: '石头', 3: '布'}
print "***************************猜拳游戏************************************"
print "你可以输入 1:剪刀 2:石头 3:布"
numPlay = 1
numWin = 0
while(True):
    if numPlay == 1:
        print "***************************猜拳游戏第", numPlay, "局************************************"
    else:
        print "***************************猜拳游戏第",numPlay , "局,您已经赢了",numWin,"局，真厉害！！************************************"
    userInput = raw_input("请输入你要出的是剪刀，石头，布：")
    if( userInput == "剪刀" or  userInput == "石头" or  userInput == "布" ):
        cpuInput = random.randint(1, 3)
        print "您出的是：" + userInput
        print "电脑出的是：" + dict1[cpuInput]
        userInput = dict2[userInput]
        if userInput == cpuInput:
            print "恭喜您，平局；再来一局吧！"
        elif ((userInput == 1) and (cpuInput == 3)) or ((userInput == 2) and (cpuInput == 1)) or \
                ((userInput == 3) and (cpuInput == 2)):
            print "您赢了！！！"
            numWin += 1
        else:
            print "您输了！！"
        numPlay += 1
    else:
        print "您的输入有问题，请重新输入.^.^"