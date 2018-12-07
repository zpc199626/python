# /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time
from one_tests.report import HTMLTestRunnertest


class Test_rep():

    def run_some(self):
        suit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(r'..\test',
                                                        pattern='*.py')
        suit.addTest(discover)
        print(suit)
        now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
        f = open(r'f:/python/one_tests/report/web测试报告.html', 'wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='赵鹏程',
                                                   description='测试结果如下',
                                                   title='考试测试报告',
                                                   stream=f,
                                                   )
        runner.run(suit)
        f.close()

aa = Test_rep()
aa.run_some()