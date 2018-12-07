#/usr/bin/env python
#-*- coding:utf-8 -*-
good = [{"name":"电脑","price":39999},
        {"name":"鼠标","price":199},
        {"name":"游艇","price":2000000},
        {"name":"佩奇","price":998},
        {"name":"美女","price":80000},
        {"name":"维密超模","price":120000}]
def gd(a):
    for n,p in enumerate(a):
        print(n,p['name'],p['price'])
money=int(input("你带了多少钱:"))
while True:
    print('余额:', money)
    print("商品列表")
    for n,p in enumerate(good):
        print(n,p['name'],p['price'])
    con=input('买东西输入任意继续，不买输入exit')
    if con=='exit':
        break
    else:
        car = []
        pp=[n for n in range(len(good))]
        while True:
            num=input('输入商品编号:')
            if num =='exit':
                break
            else:
                car.append(good[int(num)])
                gd(car)
                print("输入exit退出")
        while True:
            print('已选购商品')
            for n, p in enumerate(car):
                print(n, p['name'], p['price'])
            move=input("删除输入del,完成输入ok")
            if move=='del':
                for n, p in enumerate(car):
                    print(n, p['name'], p['price'])
                moves=input('请输入编号:')
                car.remove(car[int(moves)])
            elif move=='ok':
                break
        while True:
            user=input("输入ok结账")
            sum=0
            if user=='ok':
                for k,v in enumerate(car):
                    sum+=p['price']
                print('消费金额',sum)
                if sum<money:
                    print('购买成功')
                    money=money-sum
                    break
                else:
                    print('余额不足请充值')
                    print('已选购商品')
                    for n, p in enumerate(car):
                        print(n, p['name'], p['price'])
                    move = input("删除商品输入del,完成输入ok")
                    if move == 'del':
                        for n, p in enumerate(car):
                            print(n, p['name'], p['price'])
                        moves = input('请输入编号:')
                        car.remove(car[int(moves)])
                        continue
                    elif move == 'ok':
                        moneys = int(input('充值金额:'))
                        money += moneys
                        print('余额:', money)
                        continue

