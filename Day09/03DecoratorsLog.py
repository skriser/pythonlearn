#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/06 13:12
@author: 柴顺进
@file: 03DecoratorsLog.py 
@software:rongda
@note: 
"""


def trace_func(func):
    '''''
    A decorate function to track all function invoke information with DEBUG level
    Usage:
    @trace_func
    def any_function(any parametet)
    '''

    def tmp(*args, **kargs):
        print 'Start %s(%s, %s)...' % (func.__name__, args, kargs)
        return func(*args, **kargs)

    return tmp


@trace_func
def log_test_with_empty_parameter():
    pass


@trace_func
def log_test_with_many_parameter(a_int, b_string, c_list, d_dict):
    pass


@trace_func
def log_test_with_key_parameter(a='www', b=1, c=[1, 2]):
    pass


if __name__ == '__main__':
    log_test_with_empty_parameter()

    log_test_with_many_parameter(1, 'wwww', [1, 2, 'c'], {1: 'a', 2: 'ww'})
    log_test_with_key_parameter(1, 'wwww', c=[3, 4])