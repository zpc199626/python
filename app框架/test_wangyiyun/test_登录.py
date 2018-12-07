import unittest
from app框架.config.denglu import denglu
from app框架.date.duqu import duqu
import time

class test_登录(unittest.TestCase):
    shuju = duqu()
    def test_1(self):
        driver = denglu(self.shuju[0][0],self.shuju[0][1])
        time.sleep(10)
        driver.find_element_by_id("com.netease.cloudmusic:id/py").click()
        time.sleep(10)
        title = driver.find_element_by_id('com.netease.cloudmusic:id/ac2')
        self.assertEqual(title.text, "用户507297819")
        print("登陆成功")

    def test_2(self):
        driver = denglu(int(self.shuju[1][0]), self.shuju[1][1])
        time.sleep(5)
        title = driver.find_element_by_id("com.netease.cloudmusic:id/pt")
        self.assertEqual(title.text,"登录")
        print("登陆失败")

    def test_3(self):
        driver = denglu(int(self.shuju[2][0]), int(self.shuju[2][1]))
        time.sleep(5)
        title = driver.find_element_by_id("com.netease.cloudmusic:id/pt")
        self.assertEqual(title.text, "登录")
        print("登陆失败")

