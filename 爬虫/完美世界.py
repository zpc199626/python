#/etc/bin/env python
#-*- coding:utf-8 -*-

import requests
import re
import os
import xlwt

class Wanmei:

    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}

    def txt_mulu(self):
        url = 'https://www.booktxt.net/0_31/'
        res_1 = requests.get(url=url,headers=self.head)
        html_mulu = res_1.content.decode('gbk')
        patt_mulu = re.compile('<dl>(.*?)</dl>',re.S)
        items_mulu = patt_mulu.findall(html_mulu)
        return items_mulu

    def txt_houzui(self):
        patt_houzui = re.compile(r'<dd><a href="(.*?)">',re.S)
        items_houzui = patt_houzui.findall(self.txt_mulu()[0])
        return items_houzui

    def txt_name(self):
        patt_name = re.compile(r'html">(.*?)</a>',re.S)
        items_name = patt_name.findall(self.txt_mulu()[0])
        return items_name

    def txt_zhengwen(self):
        f = open('wanmei.txt','a+',encoding='utf-8')
        for k in self.txt_houzui():
            url_1 = 'https://www.booktxt.net/0_31/'+ k
            res_zhengwen = requests.get(url=url_1,headers=self.head)
            html_zhengwen = res_zhengwen.content.decode('gbk')
            patt_txt = re.compile(r'<div id="content">(.*?)</div>')
            items_txt = patt_txt.findall(html_zhengwen)
            f.write(items_txt[0]+'/n')
        f.close()




head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}


url = 'https://www.amap.com/service/poiTipslite?&city=410200&geoobj=114.313981%7C34.692951%7C114.478776%7C34.906647&words=%E6%B2%99%E5%8E%BF%E5%B0%8F%E5%90%83'
res_1 = requests.get(url=url,headers=head)
html = res_1.content.decode('utf-8')  
print(html)