#!/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest
from 摩尔精英.report import HTMLTestRunnertest
import time

class Test_rep():

    def run_some(self):
        pass

    def run_all(self):
        suit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(r'..\test',
                                                        pattern='test*.py')
        suit.addTest(discover)
        now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
        f = open(r'f:/python/摩尔精英/report/登陆按钮测试报告.html', 'wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='赵鹏程',
                                                   description='测试结果如下',
                                                   title='摩尔精英测试报告',
                                                   stream=f)
        runner.run(suit)
        f.close()

run = Test_rep()
run.run_all()
