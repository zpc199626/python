#!/usr/bin/env python
#-*- coding:utf-8 -*-


import requests

class add_car():

    def add_one_car(self,a,b):
        url = 'http://www.zhaoapi.cn/product/addCart'
        canshu = {"Uid":"{}".format(a),"Pid":"{}".format(b),"Token":"ADF8EFB3DFDC298D1F4C55F2D308D4BF"}
        header = {'Content-Type':'application/x-www-form-urlencoded'}
        res = requests.post(url=url,data=canshu,headers=header)
        html = res.json()
        return html

    def add_two_car(self,b):
        url = 'http://www.zhaoapi.cn/product/addCart'
        canshu = {"Pid":"{}".format(b),"Token":"ADF8EFB3DFDC298D1F4C55F2D308D4BF"}
        header = {'Content-Type':'application/x-www-form-urlencoded'}
        res = requests.post(url=url,data=canshu,headers=header)
        html = res.json()
        return html

    def add_three_car(self,a):
        url = 'http://www.zhaoapi.cn/product/addCart'
        canshu = {"Uid":"{}".format(a),"Token":"ADF8EFB3DFDC298D1F4C55F2D308D4BF"}
        header = {'Content-Type':'application/x-www-form-urlencoded'}
        res = requests.post(url=url,data=canshu,headers=header)
        html = res.json()
        return html

    def add_F(self,a,b):
        url = 'http://www.zhaoapi.cn/product/addCart'
        canshu = {"Uid":"{}".format(a),"Pid":"{}".format(b),"Token":"ADF8EFB3DFDC298D1F4C55F2D308D4BF"}
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        res = requests.post(url=url, data=canshu, headers=header)
        html = res.content.decode('utf-8')
        return html

    def cheek_car(self,a):
        url = 'http://www.zhaoapi.cn/product/addCart'
        canshu = {"Uid":"{}".format(a),"Token":"ADF8EFB3DFDC298D1F4C55F2D308D4BF"}
        header = {'Content-Type':'application/x-www-form-urlencoded'}
        res = requests.post(url=url,data=canshu,headers=header)
        html = res.json()
        return html

    def cheek_err(self):
        url = 'http://www.zhaoapi.cn/product/addCart'
        canshu = {"Token":"ADF8EFB3DFDC298D1F4C55F2D308D4BF"}
        header = {'Content-Type':'application/x-www-form-urlencoded'}
        res = requests.post(url=url,data=canshu,headers=header)
        html = res.json()
        return html

    def cheek_F(self,a):
        url = 'http://www.zhaoapi.cn/product/addCart'
        canshu = {"Uid":"{}".format(a),"Token":"ADF8EFB3DFDC298D1F4C55F2D308D4BF"}
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        res = requests.post(url=url, data=canshu, headers=header)
        html = res.content.decode('utf-8')
        return html






