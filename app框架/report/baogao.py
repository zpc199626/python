from app框架.report.HTMLTestRunnertest import HTMLTestRunner
import unittest
import time

def baogao(wenjian):
    suit = unittest.TestSuite()
    for i in wenjian:
        discover = unittest.defaultTestLoader.discover(r'..\test_wangyiyun',pattern='{}.py'.format(i))
        suit.addTest(discover)
    now = time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
    f = open(r'f:\python\app框架\report\网易云测试报告.html','wb')
    runner = HTMLTestRunner(title='网易云测试报告',description='报告如下',tester='赵鹏程',stream=f)
    runner.run(suit)
    f.close()