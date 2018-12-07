#/etc/bin/env python
#-*- coding:utf-8 -*-
"""requests  第三方库 需要下载
爬虫：又叫 网络蜘蛛（spider）
模仿浏览器，根据自己制定的规则。批量下载网络中的资源
"""
# 正则表达式：匹配文件中的内容
# 到目的字符串中去查找
"""
模仿浏览器的模块：urllib , urllib3 , requests
匹配内容的模块：re , bs4 , xpath

爬虫分为两类：
1.聚焦爬虫：只爬取某个网站的资源，叫聚焦爬虫
2.搜索爬虫：爬取整个网络上的资源
"""
"""
面向对象的代码  
爬虫的第一步，分析网址的变化并请求
第二步；分析html文件  过滤并且下载想要的资源
第三部；保存  注意保存的权限和保存的格式
"""
"""
导入正则表达式模块   re  
只能匹配字符串
贪婪模式：尽可能多的去匹配最后的字符串
非贪婪模式：尽可能少的去匹配最后的字符串
带有 ？ 的是非贪婪模式  问号优先级高
带有 * 的是贪婪模式
. 匹配任意一个字符，出了换行符----------在编译的后面添加一个  ,re.S
 re.S 让 . 可以匹配包括换行符在内的所有字符
 re.I 匹配的字符不区分大小写
"""
import requests
import re
import xlwt
import xlrd
import xlutils
a = 'qwe1111111111156756qweqwe11111qweqwe1111111qweqwe1111114qweqwe115qwe'
# 将要匹配的正则编译
# b = re.compile('qwe(.*?)qwe')



class zzhu_1():

    def qingqiu(self,page):
        url = 'https://www.qiushibaike.com/text/page/{}/'.format(page)
        # 发送请求
        response = requests.get(url=url)
        # 读取结果的方式：
        # 1.以字符串的方式读取
        one_1 = response.text
        return one_1
        # 2.以字节码的方式获取
        # print(response.content.decode('utf -8'))
    def guolv(self,abc):
        shujv = []
        patt = re.compile('<div class="content">(.*?)</div>',re.S)
        items = patt.findall(abc)
        for i in items:
            i = i.replace('<span>','').replace('</span>','').replace('<br/>','').strip()
            if '查看全文' in i :
                i = i.replace('<span class="contentForAll">查看全文','').strip()
            shujv .append(i)
        return shujv

    def save(self,shujv):
        with open('pachong.txt','a',encoding='utf-8')as f :
            for i in shujv:
                f.write(i+'\n')


# qiushi = zzhu_1()
# for k in range(1,13):
#     one_1 = qiushi.qingqiu(k)
#     shujv = qiushi.guolv(one_1)
#     qiushi.save(shujv)
"""未完成"""
class NEW_1(object):
    def qingqiu(self,page):
        url = 'https://www.qiushibaike.com/text/page/{}/'.format(page)
        want = requests.get(url = url)
        new_1 = want.text
        return new_1

    def  guolv(self,a):
        shujv = []
        patt = re.compile('<div class="content">(.*?)</div>',re.S)
        items = patt.findall(a)
        for i in items:
            i = i.replace('<span>','').replace('</span>','').replace('<br/>','').strip()
            if '查看全文' in i :
                i = i.replace('<span class="contentForAll">查看全文','').strip()
            shujv.append(i)
        return shujv

    def save_1(self,shujv):
        with open('糗事百科.txt','a',encoding='utf-8') as n :
            for i in shujv :
                n.write(i+'\n')



class Douban():
    def __init__(self,page_1):
        self.page=page_1
    def qingqiu(self):
        url = 'https://book.douban.com/top250?start={}'.format(self.page)
        want = requests.get(url = url)
        new_1 = want.text
        return new_1

    def shuming(self,asd):
        shujv = []
        patt = re.compile('title="(.*?)"',re.S)
        items_1 = patt.findall(asd)
        for i in items_1:
            if '可试读' in i :
                # i = i.replace('可试读','').replace(',','')
                continue
            shujv.append(i)
        return shujv

    def jianjie(self,qqq):
        patt_1 = re.compile('<span class="inq">(.*?)</span>',re.S)
        items_2 = patt_1.findall(qqq)
        return items_2

    def save_1(self,m,n):
        new_1 = self.shuming(self.qingqiu())
        new_2 = self.jianjie(self.qingqiu())
        for k in range(1,len(new_1)+1):
            sheet.write(m,0,new_1[k-1])
            m+=1
            p_1.save('douban.xls')
        for j in range(1,len(new_2)+1):
            sheet.write(n,1,new_2[j-1])
            n+=1
            p_1.save('douban.xls')










f = xlwt.Workbook(encoding='utf-8')
f.save('douban.xls')
from xlutils.copy import copy
p = xlrd.open_workbook('douban.xls')
p_1 = copy(p)
sheet = p_1.get_sheet(0)
m = 1
n = 1
sheet.write(0, 0, '书名')
sheet.write(0, 1, '简介')
for i in range(0,226,25):
    douban = Douban(i)
    douban.save_1(m,n)

txt = xlwt.Workbook(encoding='utf-8')
for i in