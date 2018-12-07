# /usr/bin/env python
# -*- coding: utf-8 -*-
#接口测试：发送请求 验证响应是否符合需求的过程
import requests
import unittest
"""unittest是python自带单元测试自动化测试框架
只要包含四个：unittest.TestCase：用来做用例管理的
              unittest.TestSuite: 测试套件，将多个测试用例集合在一起
              unittest.TestLoader：将测试用例加载到测试套件中
              unittest.TestRunner：执行
其中还封装了检验返回的结果的方法（也就是断言）"""

# class hao:
#     def test_school(self,a):
#         url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
#         canshu = {"filterInput":"{}".format(a)}
#         header = {'Content-Type':'application/x-www-form-urlencoded',
#         'Accept': '*/*',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'zh-CN,zh;q=0.9',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
#         'Cookie':'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'}
#         res = requests.get(url=url,headers=header,params=canshu)
#         html = res.json()
#         assert html['code'] == 0      #  """断言方式"""


class T_haofenshu(unittest.TestCase):


    def setUp(self):      #主要作用是：初始化测试环境，在每次执行测试用例前执行。
            url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
            canshu = {"filterInput": "{}".format('北京')}
            header = {'Content-Type': 'application/x-www-form-urlencoded',
                      'Accept': '*/*',
                      'Accept-Encoding': 'gzip, deflate, br',
                      'Accept-Language': 'zh-CN,zh;q=0.9',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
                      'Cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'}
            res = requests.get(url=url, headers=header, params=canshu)
            self.html = res.json()

    def test_1(self):
        self.assertEqual(self.html['code'], 0,msg='对了')

    def test_2(self):
        self.assertEqual(self.html['msg'],'学校快查成功',msg='好的')

    def test_3(self):
        assert self.html['code'] == 1

    def tearDown(self):    #清理环境，每次用例后执行
        print('123')

if __name__ =='__main__':
    unittest.main()
