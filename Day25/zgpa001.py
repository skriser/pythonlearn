#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/30 17:59
@author: 柴顺进
@file: zgpa001.py 
@software:rongda
@note: 
"""  
import tushare as ts
from scipy import signal
from matplotlib import pyplot as plt
ZGPA_ALL = ts.get_hist_data('000001',start='2015-01-05',end='2018-05-30')
data = ZGPA_ALL.index
close = ZGPA_ALL["close"]
y = signal.detrend(close)
# print(close)
plt.plot(data,close,'o',data,close,'-')
plt.plot(data,close,'o',data,close-y,'-')
plt.show()