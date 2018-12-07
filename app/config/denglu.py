from appium import webdriver
from time import sleep
import selenium.webdriver.support.ui as ui


def login_wy(a,b):
    desired_caps = {'platformName': 'Android',
                    # 'platformVersion':'5.0',
                    'deviceName': '127.0.0.1:62001',
                    'appPackage': 'com.netease.cloudmusic',
                    'appActivity': 'activity.LoadingActivity'}
    drive = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    until = ui.WebDriverWait(drive, 30)
    until.until(lambda dr: dr.find_element_by_id('com.netease.cloudmusic:id/mx').is_displayed())
    drive.find_element_by_id('com.netease.cloudmusic:id/mx').click()
    until.until(lambda dr: dr.find_element_by_id('com.netease.cloudmusic:id/py').is_displayed())
    drive.find_element_by_id('com.netease.cloudmusic:id/py').click()
    until.until(lambda dr: dr.find_element_by_id('com.netease.cloudmusic:id/abx').is_displayed())
    drive.find_element_by_id('com.netease.cloudmusic:id/abx').click()
    until.until(lambda dr: dr.find_element_by_id('com.netease.cloudmusic:id/aih').is_displayed())
    drive.find_element_by_id('com.netease.cloudmusic:id/aih').click()
    sleep(2)
    drive.find_element_by_id('com.netease.cloudmusic:id/i1').send_keys('{}'.format(a))
    sleep(2)
    drive.find_element_by_id('com.netease.cloudmusic:id/i2').send_keys('{}'.format(b))