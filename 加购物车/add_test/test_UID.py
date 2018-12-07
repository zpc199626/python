#!/usr/bin/env python
#-*_ coding:utf-8 -*_
import unittest
from 加购物车.config.car_config import add_car
from 加购物车.data.car_data import all_data
ALL_DATA = all_data()


class buycar(unittest.TestCase):
    Buy_true_car = add_car.add_one_car
    Buy_UID_err = add_car.add_two_car
    Buy_FAIL = add_car.add_F
    shujv = ALL_DATA.car_UID()

    def test_1(self):
        HTMl = self.Buy_true_car(int(self.shujv[0][0]),int(self.shujv[0][1]))
        self.assertEqual(int(HTMl['code']),int(self.shujv[0][2]))
        self.assertEqual(HTMl['msg'],self.shujv[0][3])

    def test_2(self):
        HTML = self.Buy_UID_err(self.shujv[1][0])
        self.assertEqual(HTML['msg'],self.shujv[1][3])

    def test_3(self):
        HTML = self.Buy_FAIL(self.shujv[2][0],self.shujv[2][1])
        self.assertIn(self.shujv[2][4],HTML)

    def test_4(self):
        HTML = self.Buy_FAIL(self.shujv[3][0],self.shujv[3][1])
        self.assertIn(self.shujv[3][4],HTML)

    def test_5(self):
        HTML = self.Buy_FAIL(self.shujv[4][0],self.shujv[4][1])
        self.assertIn(self.shujv[4][4],HTML)





if __name__ == "__main__":
    unittest.main()


