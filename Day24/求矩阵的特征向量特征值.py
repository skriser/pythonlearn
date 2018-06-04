
#!usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/29 15:43
@author: 柴顺进
@file: 求矩阵的特征向量特征值.py 
@software:rongda
@note: 
"""  
import numpy as np

vector = np.mat("3 -2;1 0")
print(vector)

# 求向量的特征值
eigenvalues = np.linalg.eigvals(vector)
# 同时求特征值与特征向量
eigenavalues, eigvector = np.linalg.eig(vector)

print(eigenvalues,eigvector)

#奇异值分解
vector1 = np.mat("4 11 14;8 7 -2")
# print() 调用svd()对矩阵进行奇异值分解
U,sigma,V = np.linalg.svd(vector1,full_matrices=False)
print("U为\n{}\n,Sigma为\n{}\n,V=为\n{}\n".format(U,sigma,V))
# 奇异值相乘
print("product",U*np.diag(sigma)*V)