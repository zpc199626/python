# /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import unittest
import HTMLTestRunne
import HTMLTestRunnertest
import time
import xlrd



def tes_school(a):
    url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
    canshu = {"filterInput":"{}".format(a)}
    header = {'Content-Type':'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Cookie':'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'}
    res = requests.get(url=url,headers=header,params=canshu)
    html = res.json()
    return html

def tse_数据():
    shujv_1 = []
    f = xlrd.open_workbook('111.xls')
    sheet = f.sheets()[0]
    num = sheet.nrows
    for i in range(1,num):
        aa = sheet.row_values(i)
        shujv_1.append(aa)
    return shujv_1

class 练习(unittest.TestCase):
    # def setUp(self):      #主要作用是：初始化测试环境，在每次执行测试用例前执行。
    #     print('长江长江我是黄河')

    def test_1(self):
        shujv = tse_数据()
        Html = tes_school(shujv[0][0])
        self.assertEqual(Html['code'],int(shujv[0][1]))
        self.assertIn(len(Html['data']),range(int(shujv[0][2])))

    def test_2(self):
        shujv = tse_数据()
        Html = tes_school(shujv[1][0])
        self.assertEqual(Html['code'],int(shujv[1][1]))
        self.assertEqual(len(Html['data']),int(shujv[1][2]))

    def test_3(self):
        shujv = tse_数据()
        Html = tes_school(shujv[2][0])
        self.assertEqual(Html['code'],int(shujv[2][1]))
        self.assertIn(len(Html['data']),range(int(shujv[2][2])))

    def test_4(self):
        shujv = tse_数据()
        Html = tes_school(shujv[3][0])
        self.assertEqual(Html['code'],int(shujv[3][1]))
        self.assertEqual(len(Html['data']),int(shujv[3][2]))

    # def tearDown(self):    #清理环境，每次用例后执行
    #     print('收到，完毕')

if __name__ =='__main__':
    #创建一个测试套件
    suit = unittest.TestSuite()
    #添加测试用例,将测试用例添加到测试套件中。
    # suit.addTest(练习('test_1'))
    # suit.addTest(练习('test_2'))
    # suit.addTest(练习('test_3'))
    # suit.addTest(练习('test_4'))
    suit.addTest(unittest.makeSuite(练习))  #会主动的到类的里面找到类中所有的以test开头的函数，并添加到测试套件中。
    #设置时间
    now = time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
    f = open('qqq.html','wb')
    runner = HTMLTestRunnertest.HTMLTestRunner(tester='赵鹏程',
                                               description='测试结果如下',
                                               title='好分数测试报告',
                                               stream=f,
                                               )
    runner.run(suit)
    f.close()

    # unittest.main()
