#/usr/bin/env python
#-*- coding:utf-8 -*-
class Dnf():
    def __init__(self,name,HP,MP,LV=0,NJ):
        self.na = name
        self.hp = HP
        self.mp = MP
        self.lv = LV
        self.nj = NJ

    def type_lmfv(self):
        self.hp = self.hp-1000
        self.nj = self.nj-10
        self.mp = self.mp-1000
        self.lv = self.lv+1

    def type_ll(self):
        self.hp = self.hp-800
        self.nj = self.nj-5
        self.mp = self.mp-500
        self.lv = self.lv+0.5

    def zhuangtai(self):
        mm = "姓名:{}; 血量:{}; 蓝量:{}; 等级:{}; 耐久:{} ".format(self.na,self.hp,self.mp,self.lv,self.nj)
        print(mm)
        if 0<self.hp<1000:
            print('请使用血瓶')
        elif self.hp<=0:
            print('角色死亡')

        if self.mp<1000:
            print('请使用蓝瓶')

        if self.nj<10:
            print('请修理装备')

    def xueping(self):
        self.hp+=1000

    def lanping(self):
        self.mp+=1000

    def xiuli(self):
        self.nj=50

dao = Dnf('鬼剑士',6000,5000,10,50)
gun =  Dnf('格斗家',3000,6000,5,50)
mofa = Dnf('魔法师',4000,10000,10,40)

dao.type_ll()
gun.type_lmfv()
mofa.type_lmfv()

dao.type_ll()
gun.type_lmfv()
mofa.type_lmfv()


dao.type_ll()
gun.type_lmfv()
mofa.type_lmfv()

dao.zhuangtai()
gun.zhuangtai()
mofa.zhuangtai()