#!usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/27 10:54
@author: 柴顺进
@file: spider.py 
@software:rongda
@note: 
"""

# 深度优先代码
def depth_tree(tree_node):
    if tree_node is not None:
        print(tree_node._data)
        if tree_node._left is not None:
            return depth_tree(tree_node._left)
        if tree_node._right is not None:
            return depth_tree(tree_node._right)


# 广度优先算法
def level_queue(root):
    # 利用队列实现树的广度优先遍历
    if root is None:
        return
    my_queue = []
    node = root
    my_queue.append(node)
    while my_queue:
        node=my_queue.pop(0)
        print(node.elem)
        if node.lchild is not None:
            my_queue.append(node.lchild)
        if node.rchild is not None:
            my_queue.append(node.rchild)