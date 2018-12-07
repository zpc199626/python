#!/usr/bin/env python
#-*_ coding:utf-8 -*_
import unittest
from 加购物车.config.car_config import add_car
from 加购物车.data.car_data import all_data
ALL_DATA = all_data()


class buycar(unittest.TestCase):
    cheek_car = add_car.cheek_car
    cheek_err = add_car.cheek_err
    cheek_FAIL = add_car.cheek_F
    shujv = ALL_DATA.cheek_data()

    def test_1(self):
        HTMl = self.cheek_car(int(self.shujv[0][0]))
        self.assertEqual(int(HTMl['code']),int(self.shujv[0][1]))
        self.assertEqual(HTMl['msg'],self.shujv[0][2])

    def test_2(self):
        HTML = self.cheek_err()
        self.assertEqual(HTML['msg'],self.shujv[1][2])

    def test_3(self):
        HTML = self.cheek_FAIL(self.shujv[2][0])
        self.assertIn(self.shujv[2][3],HTML)

    def test_4(self):
        HTML = self.cheek_FAIL(self.shujv[3][0])
        self.assertIn(self.shujv[3][3],HTML)

    def test_5(self):
        HTML = self.cheek_FAIL(self.shujv[4][0])
        self.assertIn(self.shujv[4][3], HTML)