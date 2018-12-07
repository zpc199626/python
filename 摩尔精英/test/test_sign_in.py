#!/user/bin/env python
#-*- coding:utf-8 -*-
import unittest
from 摩尔精英.config.turn_up import open
import selenium.webdriver.support.ui as ui
from time import sleep



open = open()
class test_sign(unittest.TestCase):

    def test_1(self):
        open.open_Chrom()
        open.dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
        sleep(2)
        n = open.dr.window_handles
        sleep(2)
        open.dr.switch_to_window(n[-1])
        sleep(1)
        self.assertEqual(len(n),2)


    def test_2(self):
        open.open_login()
        until = ui.WebDriverWait(open.dr, 10)
        until.until(lambda dr: dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/li[2]/a/img').is_displayed())
        open.dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/li[2]/a/img').click()
        until = ui.WebDriverWait(open.dr, 10)
        until.until(lambda dr: dr.find_element_by_xpath('//*[@id="btn-primary"]').is_displayed())
        n = open.dr.title
        self.assertEqual(n,'登录领英')
        open.dr.quit()

    def tearDown(self):
        open.dr.quit()



