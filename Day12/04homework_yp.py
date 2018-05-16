# -*- coding: utf-8 -*-
#4、使用xlrd获取execl文件中的任意内容
import xlrd
from datetime import date,datetime

myWorkbook = xlrd.open_workbook('test04.xlsx')
mySheet = myWorkbook.sheet_by_index(0)
#计算出合并的单元格有哪些
colspan = {}
print('mySheet:merged_cells:'+ str(mySheet.merged_cells))
# if mySheet.merged_cells:
#     for item in mySheet.merged_cells:
#         print('item:'+str(item))
#     # 通过循环进行组合，从而得出所有的合并单元格的坐标
#         for row in range(item[0],item[1]):
#             for col in range(item[2],item[3]):
#             # 合并单元格的首格是有值的，所以在这里进行了去重
#                 if(row,col) !=(item[0],item[2]):
#                     colspan.update({(row,col):(item[0],item[2])})
# print(colspan)  #{(2,4):(1,4)}
# # 读取单元格数据
# for row_index in range(mySheet.nrows):
#     for col_index in range(mySheet.ncols):
#     # 假如碰见合并的单元格坐标，取合并的首格的值即可
#         if colspan.get((row_index,col_index)):
#             mycellvalue = mySheet.cell_value(*colspan.get((row_index,col_index)))
#             print(mycellvalue)
#         else:
#         #获取单元格内容的数据类型ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
#             if mySheet.cell(row_index,col_index).ctype == 3:
#                 date_value = xlrd.xldate_as_tuple(mySheet.cell_value(row_index,col_index),myWorkbook.datemode)
#                 mycellvalue = date(*date_value[:3]).strftime('%Y/%m/%d')
#                 print(mycellvalue)
#             else:
#                 mycellvalue = mySheet.cell_value(row_index,col_index)
#                 print(mycellvalue)

# rows = mySheet.nrows
# cols = mySheet.ncols
# for i in range(rows):
#     for j in range(cols):
#         mycellvalue = mySheet.cell_value(i,j)
#         print('这个是第',i,'行','第',j,'列',mycellvalue)
# mycellvalue1 = mySheet.cell(rows-1,cols-1).value
# print(mycellvalue1)
# print(mySheet.cell_value(1,2))
