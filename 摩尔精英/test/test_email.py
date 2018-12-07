#!/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest
from 摩尔精英.config.turn_up import open
from 摩尔精英.data.user_data import User
from time import sleep
open = open()
user = User()
shujv = user.user_name()

class test_email_sign(unittest.TestCase):

    def test_1(self):
        open.open_email()
        open.dr.find_element_by_id('emailInput').send_keys('{}'.format(shujv[0][0]))
        sleep(1)
        open.dr.find_element_by_id('passwordInput').send_keys('{}'.format(shujv[0][1]))
        sleep(1)
        open.dr.find_element_by_xpath('//*[@id="userForm"]/input[7]').click()
        sleep(1)
        bn = open.dr.find_element_by_xpath('/html/body/div[2]/div/div/h2').is_displayed()
        sleep(1)
        self.assertTrue(bn)

    def test_2(self):
        open.open_email()
        open.dr.find_element_by_id('emailInput').send_keys('{}'.format(shujv[1][0]))
        sleep(1)
        open.dr.find_element_by_id('passwordInput').send_keys('{}'.format(shujv[1][1]))
        sleep(1)
        open.dr.find_element_by_xpath('//*[@id="userForm"]/input[7]').click()
        sleep(1)
        bn = open.dr.find_element_by_xpath('//*[@id="userForm"]/div[1]/span').text
        self.assertEqual(bn,shujv[1][2])

    def test_3(self):
        open.open_email()
        open.dr.find_element_by_id('emailInput').send_keys('{}'.format(shujv[2][0]))
        sleep(1)
        open.dr.find_element_by_id('passwordInput').send_keys('{}'.format(shujv[2][1]))
        sleep(1)
        open.dr.find_element_by_xpath('//*[@id="userForm"]/input[7]').click()
        sleep(1)
        bn = open.dr.find_element_by_xpath('//*[@id="userForm"]/div[1]/span').text
        self.assertEqual(bn,shujv[2][2])

    def test_4(self):
        open.open_email()
        open.dr.find_element_by_id('emailInput').send_keys('{}'.format(shujv[3][0]))
        sleep(1)
        open.dr.find_element_by_id('passwordInput').send_keys('{}'.format(shujv[3][1]))
        sleep(1)
        open.dr.find_element_by_xpath('//*[@id="userForm"]/input[7]').click()
        sleep(1)
        bn = open.dr.find_element_by_xpath('//*[@id="userForm"]/div[2]/span').text
        self.assertEqual(bn,shujv[3][2])

    def tearDown(self):
        open.down()

if __name__ == '__main__':
    unittest.main()