#！/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd

class all_data():
    def school_data(self):
        shujv_1 = []
        f = xlrd.open_workbook(r'f:/python/框架/data/te_school.xls')
        sheet = f.sheets()[0]
        num = sheet.nrows
        for i in range(1,num):
            aa = sheet.row_values(i)
            shujv_1.append(aa)
        return shujv_1

    def run_name(self):
        txt_1 = open(r'f:/python/框架/data/runner.txt', 'r')
        duqv = txt_1.readlines()
        txt_1.close()
        return duqv
