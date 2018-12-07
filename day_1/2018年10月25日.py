#/etc/bin/env python
#-*- coding=utf-8 -*-
import xlwt
import xlrd
import xlutils
import pymysql
import os
import re

# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('python_1')
# sheet.write(0,0,'好的')
# f.save('ec_1.xls')
T = xlrd.open_workbook(r'../爬虫/douban.xls')
sheet = T.nsheets
print(sheet)
sheet = T.sheets()[0]
sheet_2 = T.sheet_by_name('dushu')
hang = sheet.nrows
lie = sheet.ncols
for i in range(hang):
    file = sheet.row_values(i)
    print(file)
    fi = open('shu.txt','a',encoding='utf-8')
    fi.write(file[0]+'\n')
fi.close()
