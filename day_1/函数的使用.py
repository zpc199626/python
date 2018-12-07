# /usr/bin/env python
# -*- coding: utf-8 -*-
#

# python 上函数的格式；
# def 函数名() :
#   执行语句
# 调用函数：函数名（）

# 函数名的规则和变量名的规则是一样的
# 函数的传参：
# 1.必须参数；def 函数名(参数名):
#            执行语句块
# 2.默认函数；当你传入时，使用默认的数值；当你不传入时，使用初始值。
# 3.可变长参数； # 1.def 函数名(*args)
                #        执行语句
                # 2.def 函数名(**kwargs)
                #       执行语句
# “*” ：将左右的元素变成一个元组传入； “**” ：接受的参数值只能是键值对。
# 三种参数混合使用优先级：必须参数>默认参数>可变长参数
#
# 变量的作用域：函数中的变量属于局部变量；在函数外边的变量属于全局变量。
# global  ：将局部变量变成全局变量。
# def test_n()   #在函数外边的变量属于全局变量。
#     global a
#     a = 999    # 将局部变量变成全局变量。
#     print(a)

# return    1.函数的结束语；
#           2.将结果返回给调用者
# lambda  匿名函数   用来定义函数
# 格式：  函数名 = lambda:表达式
# 列表推导式
# 将语句放在列表中，产生的结果变成列表的元素。
# b = [x for x in range(10) if x > 5 and x < 9]   # 条件可以用 and 连起来用
# m = [m+2 for m in range(10) if m > 5]
# print(b)
# print(m)

# python内置函数；
# max()  #列表中最大的数；
# min()  #列表中最小的数；
# 元组也可以使用。

# hex() :将十进制转换为十六进制；
# print(hex(20))   # 将十进制转换为十六进制；
# print(oct(20))   # 将十进制换换为八进制；
# print(bin(20))   # 将十进制转换为二进制；
# print(int(0o20))   # 将其他进制数转换成十进制；
# a,b = divmod(100,16)  #整除求余


# a=['{}*{}={}'.format(j,i,i*j) for i in range(1,10) for j in range(1,i+1)]
# print(a)
#
# a=[x for x in range(100,1000) if x==(x//100)**3+(x//10%10)**3+(x%10)**3 ]  #水仙花数
# a=[1,2,2,4,5]

# b=[{i:j} for i,j in enumerate(a)]
# print(b)
# print(b[0][0])
# for i,j in enumerate(b):
#     print(i,j)
# m = 0
# a = [i for i in range(0,100,2)]
# print(a)


# print(a,b)
# aa=lambda x,y: x+y
# bb=lambda x,y: x-y
# cc=lambda x,y: x*y
# dd=lambda x,y: x/y
#
# def calc(x,z,y):
#     if z =='+':
#         print(aa(x,y))
#     if z=='-':
#         print(bb(x,y))
#     if z=='*':
#         print(cc(x,y))
#     if z=='/':
#         print(dd(x,y))
#
#
# def jiu(y,x):
#     for i in range(y,x):
#         for j in range(1,i+1):
#             print("{}*{}={}".format(i,j,i*j),end="\t")
#         print()
# def relike(a):
#     b=[]
#     for x in a :
#         if x not in b :
#             b.append(x)
#     print(b)
#
# def moved(a):
#     a = a.split(' ')
#     for i in a:
#         if a.count(i)>1:
#             for k in range(1,a.count(i)):
#                 a.remove(i)
#     return a       #将return 后边的数据返回给调用者

def test1(a):
    # a=c.split(',')
    y=[]
    for x,b in enumerate(a) :
    a[x]=int(b)
    for i in a:
        for j in a:
            for k in a:
                if i!=j and i!=k and j!=k:
                    p='{}{}{}'.format(i,j,k)
                    if p not in y :
                        y.append(p)
    return y

def pkf(a):                  #将列表中的数字变成整数
    for x,y in enumerate(a) :
        a[x]=int(y)
    return a
# pp=['1','2','3','4','5','6','7']
# pkf(pp)
# print(pp)
#
# x=[{n:m} for n,m in enumerate([1,2,3,4,5,6])]
# print(x)
#
#
# # c = input('输入四个数，以逗号为分开')
#
# # print(test1([1,2,3,4]))
# b=['2','4','6','8','10']
# m=[x for x in pkf(b)]
# print(m)

# a=[(j) for j in range(101)]
# print(a)
# b=5
# num=input('>>>')
# pp=[n for n in range(5)]
# print(pp)
# if num in pp:
#     print('ok')

try:
    print('1')
except:
    print('2')