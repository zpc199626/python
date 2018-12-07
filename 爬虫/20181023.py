#/etc/bin/env python
#-*- coding:utf-8 -*-

import requests
import re
import os
import xlwt
import xlrd
import xlutils
from xlutils.copy import copy
# """爬取简单的图骗"""
# url = 'http://ac.qq.com/ComicView/index/id/505430/cid/1'
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
# response = requests .get(url=url,headers=head)
# html = response.content.decode('utf-8')
# patt = re.compile('<img src="(.*?)" />')
# items = patt.findall(html)
# # print(items)
# for i,j in enumerate(items):
#     mote = requests.get(j)
#     tupian = mote.content
#     with open(r'./mote/{}.jpg'.format(i),'wb') as f:
#         f.write(tupian)
#
#
# txt = xlwt.Workbook(encoding='utf-8')
# txt.save('shu.xls')


"""爬取数据到excel表格（保存在了不同的标签页）"""
# for p in range(0,226,25):
#     url = 'https://book.douban.com/top250?start={}'.format(p)
#     response = requests.get(url = url)
#     html = response.content.decode('utf-8')
#     patt = re.compile('title="(.*?)"')
#     items_1 = patt.findall(html)
#     shuming = []
#     for i in items_1:
#         if '可试读' in i:
#             continue
#         else:
#             shuming.append(i)
#     print(shuming)
#
#     patt_1 = re.compile('<span class="inq">(.*?)</span>')
#     items_2 = patt_1.findall(html)
#     from xlutils.copy import copy
#     txt = xlrd.open_workbook('shu1.xls')
#     new_txt = copy(txt)
#     sheet = new_txt.add_sheet('diyiye{}'.format(p))
#     sheet.write(0,0,'书名')
#     sheet.write(0,1,'简介')
#     for i,j in enumerate(shuming):
#         sheet.write(i+1,0,j)
#     for n,m in enumerate(items_2):
#         sheet.write(n+1,1,m)
#     new_txt.save('shu1.xls')



class Excel:

    def __init__(self,p):
       self.page = p
    shuming = []
    def qingqiu(self):
        url = 'https://book.douban.com/top250?start={}'.format(self.page)
        response = requests.get(url = url)
        html = response.content.decode('utf-8')
        return html

    def sming(self):
        patt = re.compile(r'title="(.*?)"',re.S)
        items_1 = patt.findall(self.qingqiu())
        for i in items_1:
            if '可试读' in i:
                continue
            else:
                self.shuming.append(i)
        return self.shuming

    def zjia(self):
        txt = xlrd.open_workbook('shu.xls')
        new_txt = copy(txt)
        # sheet = new_txt.add_sheet('diyiye{}'.format(p))
        sheet = new_txt.add_sheet('diyiyen')
        sheet.write(0,0,'书名')
        sheet.write(0,1,'简介')
        for i,j in enumerate(self.sming()):
            sheet.write(i+1,0,j)
        for n,m in enumerate(self.jjie()):
            sheet.write(n+1,1,m)
        new_txt.save('shu.xls')

    def all_in(self):
        patt_3 = re.compile(r'<td valign="top">(.*?)</td>',re.S)
        items_all = patt_3.findall(self.qingqiu())
        return items_all

    def jianjie(self):
        jianjie_1 = []
        for i in self.all_in():
            jianjie = re.findall(r'<span class="inq">(.*?)</span>',i,re.S)
            if len(jianjie) == 0:
                jianjie_1.append('没有')
            else:
                jianjie_1.append(jianjie)
        return jianjie_1

    def same(self):
        if 'shu.xls' not in os.listdir():
            f = xlwt.Workbook()
            sheet = f.add_sheet('豆瓣读书')
            sheet.write(0,0,'书名')
            sheet.write(0,1,'简介')
            for q in range(len(self.sming())):
                sheet.write(q+1,0,self.sming()[q])
                sheet.write(q+1,1,self.jianjie()[q])
            f.save('shu.xls')
        else:
            ff = xlrd.open_workbook('shu.xls')
            sheet = ff.sheets()[0]
            hang = sheet.nrows
            new_ff = copy(ff)
            sheet_1 = new_ff.get_sheet(0)
            for w in range(len(self.sming())):
                sheet_1.write(w+hang,0,self.sming()[w])
                sheet_1.write(w+hang,0,self.jianjie()[w])
            new_ff.save('shu.xls')



# for i in range(0,226,25):
#     excel = Excel(i)
#     excel.same()

