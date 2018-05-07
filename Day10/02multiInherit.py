#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/07 13:33
@author: 柴顺进
@file: 02multiInherit.py 
@software:rongda
@note: 多重继承
"""  


class Person(object):

    def eye(self):
        print 'two eyes'

    def speak(self):
        print '说的是person的'


class Girl(object):
    def color(self):
        print 'the girl\'s is white'

    def speak(self):
        print '说的是gril的'


class HotGirl(Person, Girl):
    def eye(self):
        print 'big eyes'


# 先调用本身的方法，本身没有方法的再调用父类方法，父类之间有相同的方法时候，这个时候按照继承的顺序（person，girl）从左到右，谁在继承前面用谁的。
littegirl = HotGirl()
littegirl.eye()
littegirl.speak()

print dir(HotGirl)