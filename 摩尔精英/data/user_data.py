#!/usr/bin/env python
#-*- coding:utf-8 -*-
import xlrd

class User():

    def user_name(self):
        shujv = []
        f = xlrd.open_workbook(r'f:/python/摩尔精英/data/user.xlsx')
        sheet = f.sheet_by_name('邮箱注册')
        hang = sheet.nrows
        for i in range(1,hang):
            aa = sheet.row_values(i)
            shujv.append(aa)
        return shujv

    def user_yanzheng(self):
        shujv = []
        f = xlrd.open_workbook(r'f:/python/摩尔精英/data/user.xlsx')
        sheet = f.sheet_by_name('邮箱验证')
        hang = sheet.nrows
        for i in range(1,hang):
            aa = sheet.row_values(i)
            shujv.append(aa)
        return shujv