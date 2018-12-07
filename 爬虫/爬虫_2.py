#/etc/bin/env python
#-*- coding:utf-8 -*-
import requests
import re
import os
import xlwt
import xlrd
import xlutils

"""
反爬：组织爬虫程序批量下载资源
常见的反爬手段：1.header
"""
# for n in range(3,13):
#     url_1 = 'http://www.doutula.com/article/list/?page={}'.format(n)
#     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
#     response = requests.get(url=url_1,headers=head)
#     html = response.content.decode('UTF-8')
#     patt = re.compile('http://www.doutula.com/article/detail/[0-9]{7}')
#     items_1 = patt.findall(html)
#
#     for i in items_1:
#         response = requests.get(url=i,headers=head)
#         html_1 = response.content.decode('UTF-8')
#         patt_1 = re.compile('<img src="(.*?)" alt=')
#         items_2 =patt_1.findall(html_1)
#         patt_2 = re.compile('class="wr pl">(.*?)</td>')
#         items_3 = patt_2.findall(html_1)
#         # print(items_3)
#         for k,j in enumerate(items_2):
#             tupian = requests.get(j)
#             resl = tupian.content
#             if 'jpg' in j:
#                 with open(r'./biao/{}{}.jpg'.format(items_3[k][0:3],k),'wb')as f:
#                     f.write(resl)
#             elif 'gif' in j:
#                 with open(r'./biao/{}{}.gif'.format(items_3[k][0:3],k),'wb')as f:
#                     f.write(resl)



