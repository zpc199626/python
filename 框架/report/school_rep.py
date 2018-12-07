# /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time
from 框架.report import HTMLTestRunnertest


class Test_rep():

    def run_some(self,a):
        suit = unittest.TestSuite()
        for i in a:
            discover = unittest.defaultTestLoader.discover(r'..\hao_test',
                                                           pattern='{}.py'.format(i.strip()))
            suit.addTest(discover)
        print(suit)
        now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
        f = open(r'f:/python/框架/report/学校接口测试报告.html', 'wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='赵鹏程',
                                                   description='测试结果如下',
                                                   title='好分数测试报告',
                                                   stream=f,
                                                   )
        runner.run(suit)
        f.close()


    def run_everyone(self):
        suit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(r'..\hao_test',
                                                       pattern='test*.py')
        suit.addTest(discover)
        print(suit)
        now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
        f = open(r'f:/python/框架/report/学校接口测试报告.html', 'wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='赵鹏程',
                                                   description='测试结果如下',
                                                   title='好分数测试报告',
                                                   stream=f,
                                                   )
        runner.run(suit)
        f.close()
