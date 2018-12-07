#!/usr/bin/env python
#-*- coding:utf-8 -*-

import xlrd
class all_data():

    def car_PID(self):
        shujv = []
        f = xlrd.open_workbook(r"F:/python/加购物车/data/car_1.xlsx")
        sheet = f.sheet_by_name('PID_1')
        hang = sheet.nrows
        for i in range(1,hang):
            jieguo = sheet.row_values(i)
            shujv.append(jieguo)
        return shujv

    def car_UID(self):
        shujv = []
        f = xlrd.open_workbook(r"F:/python/加购物车/data/car_1.xlsx")
        sheet = f.sheet_by_name('UID_1')
        hang = sheet.nrows
        for i in range(1,hang):
            jieguo = sheet.row_values(i)
            shujv.append(jieguo)
        return shujv

    def cheek_data(self):
        shujv = []
        f = xlrd.open_workbook(r"F:/python/加购物车/data/car_1.xlsx")
        sheet = f.sheet_by_name('cheek')
        hang = sheet.nrows
        for i in range(1,hang):
            jieguo = sheet.row_values(i)
            shujv.append(jieguo)
        return shujv


    def car_run(self):
        f = open('run_main.txt','r',encoding='utf-8')
        shujv = f.readlines()
        f.close()
        return shujv

