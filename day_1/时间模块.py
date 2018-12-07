#/etc/bin/env python
#-*- coding:utf-8 -*-
import time
"""时间戳 ：代表从公园1970年经过的秒数"""
# print(time.time())
"""本地时间  结果为一个元组  默认显示的是当前时间
   年，月，日，时，分，秒，星期，一年的第几天，是否为夏令时：1代表是，0代表不是
   取索引值时仅取出数字
"""
# # 参数：是填时间戳
# print(time.localtime(30000000000))
"""格式化成现代化时间"""
# print(time.strftime('%Y %m %d %H:%M:%S %w',time.localtime(15000000000)))
"""将现代化时格式化成元组"""
# now_1 = time.strptime('2018 1 1','%Y %m %d')
"""将元组的时间转换为时间戳  元组必须为9个 有效值为前六个"""
# now_2 = (1999,12,12,12,12,12,12,12,0)
# print(time.mktime(now_1))
"""休眠"""
# time.sleep(10)
# print(123)
"""输入一个现代化日期（年月日）， 输出今年是否为闰年，输出今天是星期几，输出今天是一年中的第几天"""
# now_3 = input(">>输入年月日>>")
# now_2 = time.strptime("{}".format(now_3),'%Y %m %d')
# if (now_2[0]%4 == 0 and now_2[0]%100 != 0) or now_2[0]%400 == 0:
#     time.sleep(2)
#     print('{}是闰年,今天是星期{}，是一年中的第{}天'.format(now_2[0],now_2[6]+1,now_2[7]))
# else:
#     time.sleep(2)
#     print('{}是平年,今天是星期{}，是一年中的第{}天'.format(now_2[0],now_2[6]+1,now_2[7]))
#
"""输入日期，输出日期的前一天"""
# now_3 = input(">>输入年月日>>")
# now_2 = time.strptime("{}".format(now_3),'%Y %m %d')
# now_1 = (now_2[0],now_2[1],now_2[2],now_2[3],now_2[4],now_2[5],now_2[6],now_2[7],now_2[8])
# now_4 = time.mktime(now_1)
# print(time.strftime('%Y %m %d %H:%M:%S %w',time.localtime(now_4-86400)))

a = [i for i in range(0)]
print(a)