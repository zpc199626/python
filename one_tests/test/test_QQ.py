#!/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest
from one_tests.config.QQ import login
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

login = login()

class test_QQ(unittest.TestCase):

    def test_1(self):
        dr = webdriver.Chrome()
        dr.get('https://qzone.qq.com/')
        dr.switch_to_frame('login_frame')
        sleep(1)
        dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        sleep(1)
        dr.find_element_by_xpath('//*[@id="u"]').send_keys('34424308')
        sleep(1)
        dr.find_element_by_xpath('//*[@id="p"]').send_keys('pengpeng0206.')
        sleep(1)
        dr.find_element_by_xpath('//*[@id="login_button"]').click()
        print('55')
        sleep(4)
        for i in range(20):
            try:
                m = dr.find_element_by_xpath('//*[@id="newVcodeArea"]/div[1]/div/div[1]/a').is_displayed()
                # for i in range(20):
                #     aaa = dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
                #     dr.switch_to_frame(aaa)
                #     but = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
                #     move = dr.find_element_by_xpath('//*[@id="slide"]')
                #     ActionChains(dr).drag_and_drop_by_offset(but,170,0).perform()
                #     sleep(1)
            except:
                zz = dr.find_element_by_xpath('//*[@id="QZ_Toolbar_Container"]/div/a').is_displayed()
                self.assertTrue(zz)
                # self.assertEqual(1,1)
                dr.quit()
                break
            else:
                aaa = dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
                dr.switch_to_frame(aaa)
                but = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
                move = dr.find_element_by_xpath('//*[@id="slide"]')
                ActionChains(dr).drag_and_drop_by_offset(but, 170, 0).perform()
                sleep(1)


    def test_2(self):
        dr = webdriver.Chrome()
        dr.get('https://item.jd.com/26689180344.html?jd_pop=41dec140-c10d-4ab9-9d0f-c0830f1cce24&abt=0')
        sleep(2)
        dr.find_element_by_xpath('//*[@id="InitCartUrl"]').click()
        sleep(2)
        txt = dr.find_element_by_xpath('//*[@id="result"]/div/div/div[1]/div[1]/h3').text
        self.assertEqual(txt,'商品已成功加入购物车！')
        dr.quit()

    #
    # def test_3(self):
    #
    #     dr = webdriver.Chrome()
    #     dr.get('https://qzone.qq.com/')
    #     dr.switch_to_frame('login_frame')
    #     sleep(1)
    #     dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
    #     sleep(1)
    #     dr.find_element_by_xpath('//*[@id="u"]').send_keys('344243081')
    #     sleep(1)
    #     dr.find_element_by_xpath('//*[@id="p"]').send_keys('pengpeng0206.')
    #     sleep(1)
    #     dr.find_element_by_xpath('//*[@id="login_button"]').click()
    #     sleep(2)
    #
    #     zz = dr.find_element_by_xpath('//*[@id="QZ_Toolbar_Container"]/div/a').is_displayed()
    #     self.assertTrue(zz)
    #     dr.quit()


if __name__ == '__main__':
    unittest.main()