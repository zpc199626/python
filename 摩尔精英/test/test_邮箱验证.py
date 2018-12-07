#!/user/bin/env python
#-*- coding:utf-8 -*-
import unittest
from 摩尔精英.config.turn_up import open
from 摩尔精英.data.user_data import User
import selenium.webdriver.support.ui as ui
from time import sleep
open = open()
user = User()
shujv = user.user_yanzheng()

class email_cheek(unittest.TestCase):

    def setUp(self):
        open.open_login()
        sleep(1)
        open.dr.find_element_by_id('emailInput').send_keys(shujv[0][0])
        sleep(1)
        open.dr.find_element_by_id('passwordInput').send_keys(int(shujv[0][1]))
        sleep(1)
        open.dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').click()
        sleep(2)


    def test_1(self):
        open.dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[2]/div/p[2]/a').click()
        sleep(2)
        name = open.dr.title
        self.assertEqual(name,shujv[1][2])

    def test_2(self):
        open.dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[2]/div/ul/li[2]/a').click()
        sleep(2)
        n = open.dr.window_handles
        open.dr.switch_to_window(n[-1])
        T = open.dr.title
        self.assertEqual(T,shujv[2][2])

    def test_3(self):
        open.dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[2]/div/ul/li[4]/a').click()
        tst = open.dr.find_element_by_xpath('//*[@id="colorbox"]').is_displayed()
        print(tst)
        self.assertTrue(tst)

    def test_4(self):
        open.dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[2]/div/ul/li[4]/a').click()
        sleep(1)
        open.dr.find_element_by_xpath('//*[@id="notification_admin_contact"]').send_keys('17633804992')
        sleep(1)
        open.dr.find_element_by_xpath('//*[@id="notification_admin"]/div[2]/div[1]').click()
        URL =open.dr.current_url
        self.assertEqual(URL,shujv[3][2])

    def test_5(self):
        open.dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[2]/div/ul/li[4]/a').click()
        sleep(1)
        open.dr.find_element_by_class_name('cancel').click()
        sleep(1)
        URL = open.dr.current_url
        self.assertEqual(URL,shujv[4][2])
        sleep(1)

    def tearDown(self):
        open.dr.quit()






if __name__ =='__main__':
    unittest.main()