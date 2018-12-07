#!/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep

class open():




    def open_Chrom(self):
        self.dr  = webdriver.Chrome()
        self.dr.get('http://www.moore.ren')
        sleep(2)

    def open_login(self):
        self.dr  = webdriver.Chrome()
        self.dr.get('http://www.moore.ren/login/login.htm')
        sleep(2)

    def open_email(self):
        self.dr = webdriver.Chrome()
        self.dr.get('http://www.moore.ren/register/register.htm')
        sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[1]/div[1]/li[2]').click()
        sleep(1)


    def down(self):
        self.dr.quit()

