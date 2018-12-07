# /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from 框架.report import HTMLTestRunnertest
from 框架.config.学校_接口 import school_查询
from 框架.data.读取_数据 import all_data
All = all_data()

class 考试(unittest.TestCase):
    tes_school = school_查询.school_快查
    shujv = All.school_data()


    # def test_1(self):
    #     Html = self.tes_school(self.shujv[0][0])
    #     self.assertEqual(Html['code'],int(self.shujv[0][1]))
    #     self.assertIn(len(Html['data']),range(int(self.shujv[0][2])))

    def test_2(self):
        Html = self.tes_school(self.shujv[1][0])
        self.assertEqual(Html['code'],int(self.shujv[1][1]))
        self.assertEqual(len(Html['data']),int(self.shujv[1][2]))

    def test_3(self):
        Html = self.tes_school(self.shujv[2][0])
        self.assertEqual(Html['code'],int(self.shujv[2][1]))
        self.assertIn(len(Html['data']),range(int(self.shujv[2][2])))

    def test_4(self):
        Html = self.tes_school(self.shujv[3][0])
        self.assertEqual(Html['code'],int(self.shujv[3][1]))
        self.assertEqual(len(Html['data']),int(self.shujv[3][2]))
