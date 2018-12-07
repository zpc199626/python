#/etc/bin/env python
#-*- coding:utf-8 -*-

import requests
import re
import os

class Picture:

    def __init__(self,pag):
        self.page = pag

    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}

    def qingqiu(self):
        url_1 = 'http://www.doutula.com/article/list/?page={}'.format(self.page)
        response = requests.get(url=url_1,headers=self.head)
        html = response.content.decode('UTF-8')
        return html

    def mulu_link(self):
        patt = re.compile(r'http://www.doutula.com/article/detail/[0-9]{7}',re.S)
        items_1 = patt.findall(self.qingqiu())
        return items_1

    def tu_link(self):
        tupian = []
        for i in self.mulu_link():
            if len(i) == 0:
                self.mulu_link().remove(i)
            else:
                res_1 = requests.get(i,headers=self.head)
                new_html = res_1.content.decode('utf-8')
                patt_1 = re.compile(r'<td>(.*?)</td>',re.S)
                items_2 = patt_1.findall(new_html)
                for k in items_2:
                    patt_2 = re.compile(r'<img src="(.*?)" alt=')
                    items_3 = patt_2.findall(k)
                    tupian.append(items_3)
        return tupian

    def name_save(self):
        name = []
        for i in self.mulu_link():
            if len(i) == 0:
                self.mulu_link().remove(i)
            else:
                res_name = requests.get(i,headers=self.head)
                name_html = res_name.content.decode('utf-8')
                patt_name = re.compile(r'<td>(.*?)</td>',re.S)
                items_name = patt_name.findall(name_html)
                for k in items_name:
                    patt_3 = re.compile(r'alt="(.*?)"',re.S)
                    items_5 = patt_3.findall(k)
                    name.append(items_5)
        return name

    def tu_link_save(self):
        tu_save = []
        for k in self.tu_link():
            if 'https' not in k[0]:
                self.tu_link().remove(k)
            else:
                tu_save.append(k[0])
        return tu_save

    def save(self):
        m = 0
        for i in self.tu_link_save():
            res_2 = requests.get(i)
            tu_save = res_2.content
            if 'jpg' in i :
                with open(r'./picture/{}.jpg'.format(m),'wb') as file_1:
                    file_1.write(tu_save)
            else:
                with open(r'./picture/{}.gif'.format(m),'wb') as file_1:
                    file_1.write(tu_save)
            m+=1



