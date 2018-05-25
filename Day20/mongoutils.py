#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/22 11:12
@author: 柴顺进
@file: mongoutils.py 
@software:rongda
@note: 
"""  
from pymongo import MongoClient


class Connect(object):
    def __init__(self, dbName, collection):

        self.con = MongoClient("localhost")
        self.db = self.con[dbName]
        self.collection = self.db[collection]

    def get(self):
        return self.collection


if __name__ == "__main__":
    template = Connect().get()
    scores = template.find({}, {"id": 0})

    for docment in  scores:
        print(docment)

