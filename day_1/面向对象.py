# /usr/bin/env python
# -*- coding : utf-8 -*-

# 面型对象  ：将函数进行分类和封装，使开发更高效。
# 面向对象只关注输入或者输出

# 在python上通过类来实现某个对象的功能
# 类 ： 属性（每种方法必须具备的条件） 、 方法（函数在类里面就叫方法）
# class Lianxi(object):# 为了和函数名区分。类名首字母一般为大写
#     def nine(self):
#         print('hello')  #self 是类的实例化
#
#     def four(self):
#         print('你好')

# Lianxi().four()
# # 对象：是类的实例化
# aa=Lianxi()
# aa.four()
# aa.nine()

# 实例化：自定义的实例化：方便在类的外部调用
        #内质实例化：方便在类的内部去调用

#
# class cheng():
#     def jiecheng(self):
#         n=1
#         m=0
#         for i in range(1,6):
#             n*=i
#             m+=n
#         return m
#
#     def zhishu(self):
#         b=self.jiecheng()
#         print(b)
# cheng().zhishu()


# 继承 ：一个新的类拥有旧的类的所有方法
# class jicheng(cheng):
#     pass
# bb=jicheng()
# bb.jiecheng()
#
# print(bb.jiecheng())
# object : 一切的基类
# 多继承：一个新的类拥有多个旧的类的所有方法
# 如果继承的多个类中有相同的方法（名字相同）那么使用的是最左边的的类中的方法
# 私有方法：只属于本类的方法
# 定义私有方法：在方法名前面加上两个下划线
# class Text_1():
#     def __fang(self):
#         for i in range(2):
#             print(i)
#
#
# class Text_2(Text_1,cheng):
#
#     def fan(self):
#         a=0
#         for i in range(101):
#             a+=i
#         print(a)
#
# text_1=Text_2()
# text_1.zhishu()

# 多态 ：又叫方法重写
#
# class egg():
#     def __init__(self,a,b):# 可以用来定义全局函数
#         self.name = a
#         self.nianji = b
#     def fin(self):
#         print('hello %s,几年%d年级'%(self.name,self.nianji))
#
#     def sta(self,a):
#         print('hello %s'%(a))
#
# oo = egg('zhao',3)
# oo.sta(123)
#
#
# class dnf():
#     def __init__(self,name,xueliang,zhanli):
#         self.name =name
#         self.xueliang = xueliang
#         self.zhanli = zhanli
#
#     def daguai(self,jiangyan=0):
#         self.xueliang += 1000
#
#     def xiulian(self):
#         self.xueliang+=1000
#         self.zhanli+=1000
#
#     def pk(self):
#         self.xueliang-=1000
#
#     def print_xue(self):
#         print('%s还有%s血量，战力%s'%(self.name,self.xueliang,self.zhanli))
#


class Lianxi():
    def zhishu(self,x,y):
        c=0
        for i in range(x,y):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                c+=i
        print(c)
        return c

    def huiwen(self,x):
        b=x[::-1]
        if x==b:
            print('是回文')
        else:
            print('不是回文')


    def jiecheng(self,a):
        a = int(a)
        b=1
        d=0
        for i in range(1,a+1):
            b=b*i
            d+=b
        print(d)
        return d

    def qvchong(self,a):
        b=[]
        for x in a :
            if x not in b :
                b.append(x)
        print(b)
        return b

    def shuixianhua(self,x,y):
        for i in range(x,y):
            a=i//100
            b=i//10%10
            c=i%10
            if i==a**3+b**3+c**3:
                print(i)
                return i
    def maopao(self,a):
        aa=a.split(' ')
        b=len(aa)
        for i in range(b):
            for j in range(i+1,b):
                if int(aa[i])>int(aa[j]):
                    t=aa[i]
                    aa[i]=aa[j]
                    aa[j]=t
        print(aa)
if __name__ == '__main__':
    print('hello')

