#/usr/bin/env python
#-*- coding:utf-8 -*-

class Buycar():
    good = [{"name": "电脑", "price": 39999},
            {"name": "鼠标", "price": 1999},
            {"name": "游艇", "price": 2000000},
            {"name": "佩奇", "price": 20},
            {"name": "美女", "price": 80000}]
    car=[]
    def __init__(self,qian=0):
        self.money=qian


    def chaoshi(self):
        self.money=int(input("你带了多少钱"))
        for n,p in enumerate(self.good):
            print(n,p['name'],p['price'])
        while True:
            print("输入exit前往结账")
            num=input('输入商品编号:')
            if num =='exit':
                break
            else:
                self.car.append(self.good[int(num)])
                for n, p in enumerate(self.car):
                    print(n, p['name'], p['price'])
        while True:
            user=input("输入ok结账")
            sum=0
            if user=='ok':
                for k, v in enumerate(self.car):
                    sum += v['price']
                print('消费金额', sum)
            if sum <= self.money:
                print('购买成功')
                self.money = self.money - sum
                break
            else:
                print('余额不足，选择操作删除商品或者充值')
                pay = input("充值输入ok，删除输入del")
                if pay == 'ok':
                    self.cost()
                else:
                    self.shanchu()


    def shanchu(self):
        while True:
            print('已选购商品')
            for n, p in enumerate(self.car):
                print(n, p['name'], p['price'])
            print('删除完成输入ok，删除输入商品标号删除')
            moves=input('请输入编号:')
            if moves=='ok':
                break
            else:
                self.car.remove(self.car[int(moves)])


    def cost(self):
        moneys=int(input('充值金额:'))
        self.money+=moneys
        print('余额:',self.money)







paycar=Buycar()
paycar.chaoshi()