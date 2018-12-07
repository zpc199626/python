#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import re
import pymysql

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
url = 'https://www.zhipin.com/job_detail/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&scity=101010100&industry=&position='
response = requests.get(url=url, headers=head)
html = response.content.decode('UTF-8')
patt = re.compile(' <div class="job-list">(.*?)<div class="page">',re.S)
item = patt.findall(html)
patt_1 = re.compile('<li>(.*?)</li>',re.S)
item_2 = patt_1.findall(item[0])

zhiwei = []
patt_zhiwei = re.compile('<div class="job-title">(.*?)</div>',re.S)
for i in item_2:
    item_3 = patt_zhiwei.findall(i)
    zhiwei.append(item_3[0])

xinzi = []
patt_xinzi = re.compile('<span class="red">(.*?)</span>',re.S)
for k in item_2:
    item_4 = patt_xinzi.findall(k)
    xinzi.append(item_4[0])

addres = []
patt_addres = re.compile('<p>(.*?)<em class="vline">',re.S)
for j in item_2:
    item_5 = patt_addres.findall(j)
    addres.append(item_5[0])

exp = []
patt_exp = re.compile('</em>(.*?)<em class="vline">',re.S)
for u in item_2:
    item_6 = patt_exp.findall(u)
    exp.append(item_6[0])

# xueli = []
# patt_xueli = re.compile('</em>(.*?)</p>',re.S)
# for o in item_2:
#     item_7 = patt_xueli.findall(o)
#     xueli.append(item_7[0])

name = []
patt_name = re.compile('custompage" target="_blank">(.*?)</a></h3>',re.S)
for p in item_2:
    item_8 = patt_name.findall(p)
    name.append(item_8[0])


abc = pymysql.connect(host='192.168.0.35',
                port=3306,
                user='root',
                password='123456',
                charset='utf8')
aaa = abc.cursor()
# aaa.execute('show databases')
# print(aaa.fetchall())
aaa.execute('use erku')
aaa.execute('create table boss(name char(30),xinzi char(30),exp char(30),addres char(100),zhiwei char(20))')
for i in range(len(name)):
    aaa.execute('insert into boss values("{}","{}","{}","{}","{}");'.format(name[i],xinzi[i],exp[i],addres[i],zhiwei[i]))
    abc.commit()

aaa.execute('select * from boss;')
for i in aaa.fetchall():
    print(i)