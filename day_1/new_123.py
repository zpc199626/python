#/usr/bin/env python
#-*- coding:utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
import random


# dr = webdriver.Chrome()
# dr.get('http://www.moore.ren/')
# sleep(2)
# # wd = dr.find_elements_by_class_name('menu-box')
# wd = dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]')
# print(wd)
# # print(wd.get_attribute('class'))  # 获取元素的某一个属性的值
# # for i in wd:
# #     ActionChains(dr).move_to_element(i).perform()
# #     sleep(2)


# sleep(5)
# dr.find_element_by_id('emailInput').send_keys('zpc1996@163.com')
# sleep(2)
# dr.find_element_by_id('passwordInput').send_keys('qwer@123')
# sleep(4)
# dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').click()
# sleep(4)
# #通过文本定位  保证定位元素的唯一性
# dr.find_element_by_link_text('企业').click()
# sleep(3)
# #通过模糊文本来定位
# dr.find_element_by_partial_link_text('海').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/dl[2]/dd/a[2]').click()
# sleep(2)
# dr.find_element_by_css_selector('body > div.main > div > div > div.content-left > div.search-tool > dl:nth-child(3) > dd > a:nth-child(11)').click()
# sleep(6)
# dr.quit()


# dr = webdriver.Chrome()
# dr.get('http://www.alltuu.com/login?url=http://www.alltuu.com/v')
# sleep(3)
# dr.set_window_size(1000,800)
# # dr.maximize_window()
# sleep(2)
# dr.find_element_by_id('loginUsername').send_keys('17633804992')
# sleep(2)
# wd = dr.find_element_by_tag_name('ul').find_elements_by_tag_name('li')
#
# # for i in range(10):
# #     a = random.randrange(0, 8)
# #     ActionChains(dr).move_to_element(wd[a]).perform()
# #     sleep(1)
# for i in wd:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(1)
#     if i.text == '17633804992':
#         i.click()
#         print(dr.title)
#         print(dr.current_url)
#
# sleep(3)
# dr.find_element_by_id('loginPassword').send_keys('qwer@123')
# sleep(3)
# dr.find_element_by_id('login').click()
# sleep(10)
# dr.quit()


#处理窗口
# dr = webdriver.Chrome()
# dr.get('http://www.moore.ren/')
# dr.maximize_window()
# # print(dr.current_window_handle)  #获取当前窗口的句柄
# sleep(2)
# dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
# sleep(2)
# n = dr.window_handles#获取虽有窗口的句柄
# dr.switch_to.window(n[-1])
# sleep(2)
# dr.find_element_by_id('emailInput').send_keys('zpc1996@163.com')
# sleep(2)
# dr.find_element_by_id('passwordInput').send_keys('qwer@123')
# sleep(3)
# dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').click()
# sleep(2)


# c = dr.find_element_by_class_name('login-email')
# ActionChains(dr).move_to_element(c).perform()
# sleep(3)


# dr = webdriver.Chrome()
# dr.get('https://qzone.qq.com/')
# sleep(2)
# dr.switch_to.frame("login_frame") #切换到内嵌框架中（只能根据ID或者name属性的值切换）
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('59676651')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('pengpeng0206')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
aaa = dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
dr.switch_to_frame(aaa)
tag_1 = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
end = dr.find_element_by_xpath('//*[@id="slide"]/div[1]')
sleep(3)
for i in range(50):
    ActionChains(dr).drag_and_drop_by_offset(tag_1,188,0).perform()
    sleep(1)

# dr.switch_to.default_content() #退出到原始的页面
# dr.switch_to.parent_frame()  #返回父框架（填写父框架的ID，name）

# sleep(10)
# dr.quit()


# dr = webdriver.Chrome()
# dr.get('http://www.alltuu.com')
# sleep(7)
# #移动滚动条 是属于浏览器的  JavaScript语言编写的
# # js = "var q=document.documentElement.scrollTop=1000"  #控制滚动条的JavaScript代码  最后面数字代表滚动的高度，数字越大越考下
# # dr.execute_script(js)   #执行JavaScript语句
# wd = dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[2]/div[4]/div/div[1]/p[1]')
# js = "arguments[0].scrollIntoView()"
# dr.execute_script(js,wd)
# dr.quit()









dr = webdriver.Chrome()
dr.get('http://www.moore.ren/')


#设置控制器等待  (判断元素是否出现，出现就执行就下来的操作，等待时间到期不出现就报错)
until = ui.WebDriverWait(dr,10)
until.until(lambda dr: dr.find_element_by_xpath('//*[@id="user-nomal"]/div[2]/ul/li[2]/a').is_displayed())
dr.maximize_window()
sleep(2)
#截图并保存
dr.get_screenshot_as_file('ass.png')


dr.get_screenshot_as_png()
dr.save_screenshot('asd.png') #保存截图


dr.quit()

#is_displayed() 判断元素是否显示 结果是布尔值（true Flase）
#is_enabled() 判断元素是否是灰化状态