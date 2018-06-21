# -*- coding:utf-8 -*-

import xlwt  # 导入xlwt模块

wbk = xlwt.Workbook()  # 创建工作簿

sheet = wbk.add_sheet('表01')  # 创建工作表

sheet.write(0, 1, 'test text')     # 第1行第2列写入内容

wbk.save('./excel/test.xls')  # 保存 Excel 文件

print("ok")
