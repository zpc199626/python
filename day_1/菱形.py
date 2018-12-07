#/usr/bin/env python
#-*- coding:utf-8 -*-


from time import sleep
# class lianxi:
#     def ling(self):
#         line = int(input('请输入菱形行数'))
#         for i in range(1,line+1):
#             for j in range(1,line+1-i):
#                 print(' ',end='')
#             for k in range(1,2*i):
#                 print('*',end='')
#             print()
#         for i in range(1,line):
#             for j in range(1,i+1):
#                 print(' ',end='')
#             for k in range(1,2*line-2*i):
#                 print('*',end='')
#             print()

import time

from selenium import webdriver
#打开浏览器
# dr = webdriver.Chrome()
#请求的网址
# dr.get('https://www.baidu.com')
# time.sleep(3)
#通过ID属性定位 定位到id=__(括号中写属性的值)
# dr.find_element_by_id('kw').send_keys('赵丽颖')
# time.sleep(2)
# dr.find_element_by_id('su').click()
#通过class属性定位，定位到class=__的位置
# dr.find_element_by_class_name('s_ipt').send_keys('赵丽颖')

#通过name属性的值定位
# dr.find_element_by_name('wd').send_keys('守护甜心')
# time.sleep(2)
# dr.find_element_by_id('su').click()



# time.sleep(1)
# dr.get('https://www.jd.com')
# time.sleep(2)
# dr.back()
# time.sleep(2)
# dr.forward()



#为了保证所有的测试用例都在同一个环境下去测试
#s设置浏览器大小
# dr.set_window_size(400,400)
# time.sleep(2)
# #设置浏览器打开的位置
# dr.set_window_position(500,200)
# time.sleep(2)
# #浏览器最大化
# dr.maximize_window()
# time.sleep(2)
# dr.minimize_window()



#获取 网站的标题
# print(dr.title)
#获取网址的地址
# print(dr.current_url)


# time.sleep(5)
# dr.quit()  #关闭浏览器


#webdriver模拟人的行为

dr = webdriver.Chrome()
dr.get('http://www.moore.ren/login/login.htm')
sleep(2)
dr.find_element_by_id('emailInput').send_keys('344243081@qq.com')
sleep(1)
dr.find_element_by_id('passwordInput').send_keys(123456)
sleep(1)
dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').click()
sleep(2)
dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[2]/div/ul/li[4]/a').click()
sleep(1)
# dr.find_element_by_xpath('//*[@id="notification_admin_contact"]').send_keys('17633804992')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="notification_admin"]/div[2]/div[1]').click()
dr.find_element_by_class_name('cancel').click()
URL = dr.current_url
print(URL)
sleep(3)
dr.quit()