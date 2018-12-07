#!/usr/bnn/env python
#-*- coding:utf-8 -*-
from appium import webdriver
from time import sleep
import selenium.webdriver.support.ui as ui
import unittest
# desired_caps = {'platformName':'Android',
#                 # 'platformVersion':'5.0',
#                 'deviceName':'127.0.0.1:62001',
#                 'appPackage':'com.mooreshare.app',
#                 'appActivity':'ui.activity.splash.SplashActivity'}
#
# drive = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# sleep(3)
# drive.find_element_by_id('com.mooreshare.app').click()
# sleep(3)



class music(unittest.TestCase):


    def setUp(self):
        desired_caps = {'platformName': 'Android',
                        # 'platformVersion':'5.0',
                        'deviceName': '127.0.0.1:62001',
                        'appPackage': 'com.netease.cloudmusic',
                        'appActivity': 'activity.LoadingActivity'}
        self.drive = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

        self.until = ui.WebDriverWait(self.drive,10)

    def test_one(self):

        self.until.until(lambda dr: dr.find_element_by_id('com.netease.cloudmusic:id/mx').is_displayed())
        self.drive.find_element_by_id('com.netease.cloudmusic:id/mx').click()
        self.until.until(lambda dr: dr.find_element_by_id('com.netease.cloudmusic:id/py').is_displayed())
        self.drive.find_element_by_id('com.netease.cloudmusic:id/py').click()
        self.until.until(lambda dr: dr.find_element_by_id('com.netease.cloudmusic:id/abx').is_displayed())
        self.drive.find_element_by_id('com.netease.cloudmusic:id/abx').click()
        self.until.until(lambda dr: dr.find_element_by_id('com.netease.cloudmusic:id/aih').is_displayed())
        self.drive.find_element_by_id('com.netease.cloudmusic:id/aih').click()
        sleep(2)
        self.drive.find_element_by_id('com.netease.cloudmusic:id/i1').send_keys('zpc19960216@163.com')
        sleep(2)
        self.drive.find_element_by_id('com.netease.cloudmusic:id/i2').send_keys('zpc199626@.')
        sleep(2)
        self.drive.find_element_by_id('com.netease.cloudmusic:id/pt').click()
        sleep(2)
        self.drive.find_element_by_id('com.netease.cloudmusic:id/py').click()
        sleep(1)
        n = self.drive.find_element_by_id('com.netease.cloudmusic:id/ac2').text

        self.assertEqual(n,'师父丶')

    def tearDown(self):
        self.drive.quit()


if __name__ == '__main__':
    unittest.main()