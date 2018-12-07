#!/usr/bin/env python
#-*- coding:utf-8 -*-

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import re
dr = webdriver.Chrome()
dr.get('https://192.168.0.254:8889')
sleep(2)
username = dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input')
username.clear()
sleep(2)
username.send_keys('administrator')
sleep(2)
dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[2]/input').send_keys('Bane@7766')
sleep(2)
pa = dr.find_element_by_xpath('//*[@id="checkinfo"]').find_elements_by_tag_name('img')
patt = re.compile(r'imgs/(.*?).gif',re.S)
# print(pa)
pa_Input = []
for i in pa:
    x = i.get_attribute('src')
    pa_Input.append(patt.findall(x)[0])
for k in range(len(pa_Input)):
    dr.find_element_by_xpath('//*[@id="input1"]').send_keys(pa_Input[k])
sleep(2)
dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()  #登录按钮
sleep(2)
#点击确认
wd = dr.switch_to_alert()
# print(wd.text)
wd.accept()
sleep(3)
#切换到内嵌窗口
Deputywindow = dr.find_element_by_xpath('//*[@id="Content"]/frame[1]')
dr.switch_to_frame(Deputywindow)
sleep(2)
#点击防火墙按钮
wd_1 = dr.find_element_by_id('04_image')
wd_1.click()
sleep(2)
#点击策略按钮
mm = dr.find_element_by_id('04_wrap').find_elements_by_tag_name('div')
for i in mm:
    ActionChains(dr).move_to_element(i).perform()
    # print(i.get_attribute('title'))
    if '策略'==i.get_attribute('title'):
        sleep(1)
        i.click()
sleep(2)
dr.switch_to.default_content() #退出到原始的页面
sleep(2)
dr.switch_to_frame('main')
sleep(2)
dr.find_element_by_xpath('//*[@id="content"]/form[2]/table/tbody/tr/td[2]/div/div/a').click()
sleep(2)
RuleName = dr.find_element_by_name('txt_ruleName')
RuleName.clear()
sleep(1)
RuleName.send_keys('zpc1')
sleep(2)
dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td/div/div[1]/a').click()
sleep(10)
# dr.quit()


#携程
# dr = webdriver.Chrome()
# dr.get('http://www.ctrip.com/')
# dr.find_element_by_id('searchHotelLevelSelect').click()
# sleep(2)
# wd = dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# # dian.click()
# for i in wd:
#     i.click()
#     sleep(2)
# sleep(5)
# dr.quit()



#百度
# dr = webdriver.Chrome()
# dr.get('https://www.baidu.com/')
# sleep(2)
# dr.find_element_by_id('kw').send_keys('boss直聘')
# sleep(2)
# dr.find_element_by_id('su').click()
# sleep(2)
# dr.find_element_by_id('m50747392').find_element_by_xpath('//*[@id="w-ko5g6n"]/div/h2/a[1]').click()
# sleep(2)
# n = dr.window_handles
# dr.switch_to_window(n[-1])
# sleep(2)
# dr.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[1]/form/div[1]/p/input').send_keys('软件测试工程师')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[1]/form/button').click()
# sleep(10)
# dr.quit()




