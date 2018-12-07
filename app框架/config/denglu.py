from appium import webdriver
import time
import selenium.webdriver.support.ui as ui

def denglu(zhanghao,passwd):
        desired_caps = {'platformName': 'Android',
                        'deviceName': '127.0.0.1:62001',
                        'appPackage': 'com.netease.cloudmusic',
                        'appActivity': 'activity.LoadingActivity'}

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        until = ui.WebDriverWait(driver, 30)
        print("立即体验")
        until.until(lambda dr: dr.find_element_by_id('com.netease.cloudmusic:id/mx').is_displayed())
        driver.find_element_by_id("com.netease.cloudmusic:id/mx").click()
        until.until(lambda dr: dr.find_element_by_id('com.netease.cloudmusic:id/py').is_displayed())
        print("点击抽屉菜单")

        driver.find_element_by_id("com.netease.cloudmusic:id/py").click()
        until.until(lambda dr: dr.find_element_by_id('com.netease.cloudmusic:id/abx').is_displayed())
        driver.find_element_by_id("com.netease.cloudmusic:id/abx").click()
        print("立即登录")
        time.sleep(2)

        driver.find_element_by_id("com.netease.cloudmusic:id/pt").click()
        time.sleep(3)
        print("手机号登录")

        driver.find_element_by_id("com.netease.cloudmusic:id/i4").send_keys("{}".format(zhanghao))
        time.sleep(3)
        print("输入手机号")

        driver.find_element_by_id("com.netease.cloudmusic:id/i2").send_keys("{}".format(passwd))
        time.sleep(3)
        print("输入密码")

        driver.find_element_by_id("com.netease.cloudmusic:id/pt").click()
        time.sleep(3)
        print("登录")

        return driver