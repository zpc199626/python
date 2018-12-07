#/usr/bin/env python
# -*- coding:utf-8 -*-

"""
# 常用模块的使用 ：1。pymysql 对mysql数据库操作。
# 开启mysql服务器授权
# 如果连接超时 去x虚拟机里输入 iptables -F  清空防火墙
# """
# import pymysql
# # abc = pymysql.connect(host='192.168.0.35',
# #                 port=3306,
# #                 user='root',
# #                 password='123456',
# #                 charset='utf8')
# """创建游标"""
# # aaa = abc.cursor()
# """执行SQL语句"""
# # aaa.execute('show databases;')
# """读取上一句sql语句的结果；括号中数字代表读取几个结果；如果没有读取完，剩下的结果会被fetchall读取"""
#
# """默认读取一个，数字大于结果个数会读取所有"""
# # print(aaa.fetchmany())
#
# """读取上一句sql语句的结果 (元组)"""
# # print(aaa.fetchall())
#
# """每次只读取一个结果，本身有迭代功能（自己会累加）"""
# # print(aaa.fetchone())
#
# # aaa.execute('create database yiku;')

"""往数据库中批量导入文件"""
# abc = pymysql.connect(host='192.168.0.35',
#                 port=3306,
#                 user='root',
#                 password='123456',
#                 charset='utf8')           #连接数据库
# aaa = abc.cursor()                        #创建游标
# aaa.execute('use yiku;')                  #选择库
# # aaa.execute('create table biao3(姓名 char(30),年龄 int,班级 char(30));')  #创建表格
# list = ['mlxg',1,'电竞一班',1000]
# for i in range(30):                       #使用循环写入多条数据
#     aaa.execute('insert into biao3 values("{}","{}","{}","{}");'.format(list[0],list[1]+i,list[2],list[3]))
#     abc.commit() #提交数据
# #
# aaa.execute('select * from biao3;')
# for i in aaa.fetchall():
#     print(i)                              #查看表数据

"""从数据库中将内容导入到txt文件"""

# abc = pymysql.connect(host='192.168.0.35',
#                 port=3306,
#                 user='root',
#                 password='123456',
#                 charset='utf8')                # 连接数据库
# aaa = abc.cursor()                             # 创建游标
# aaa.execute('use yiku')                        #选择库
# with open('a.txt','w',encoding='utf-8') as f:  #创建、打开文件
#     aaa.execute('desc biao3;')
#     bb=aaa.fetchall()                          #读取表头
#     f.write("{},{},{}".format(bb[0][0],bb[1][0],bb[2][0],bb[3][0])+'\n')  #写入表头
#     aaa.execute('select * from biao3;')
#     cc=aaa.fetchall()                          #读取表数据
#     for i in cc:
#         f.write("{},{},{}".format(i[0],i[1] ,i[2])+'\n')      #写入表数据
"""------------------------------------------------------------------------"""


"""数据库命令小循环"""
# while True:
#     abc = pymysql.connect(host='192.168.0.35',
#                           port=3306,
#                           user='root',
#                           password='123456',
#                           charset='utf8')
#     y = input('>>>输入exit退出>>>')
#     aaa = abc.cursor()
#     aaa.execute('use yiku;')
#     aaa.execute(y)
#     xianshi = aaa.fetchall()
#     print(xianshi)
#     abc.commit()  # 提交数据
#     if y=='exit':
#         break



"""os 模块 python自带的模块

作用 ： python与自带系统之间的交互"""
import os
"""执行命令"""
# xian=os.popen('ping 192.168.0.1')
# print(xian.read())

""" 获取当前所在位置"""
# print(os.getcwd())

"""切换目录  #两个斜杠或者前面加 r 是为了让转义字符不转义"""
# os.chdir(r'C:\')

"""创建目录  如果不加路径就在当前路径下创建"""
# os.mkdir('aaa')

"""创建递归目录"""
# os.makedirs(r'bbb\ccc\sss')

"""删除目录"""
# os.rmdir('aaa')

"""删除递归目录"""
# os.removedirs(r'bbb\ccc\sss')

"""删除文件"""
# os.remove('lina.py')

"""获取当前目录下面的所有文件"""
# print(os.listdir(r"C:"))

"""更改文件名"""
# os.rename(r'../爬虫/2018年10月24日.py','斗图啦.py')

"""将文件名与路径分隔开"""
# os.path.split(r'E:/python/day_1/常用模块.py')
"""注意：分割的是字符串与有无此文件或路径无关"""

"""将文件的后缀名与路径分割开"""
# os.path.splitext(r'E:/python/day_1/常用模块.py')
"""注意：分割的是字符串与有无此文件或路径无关"""

"""判断是否为普通文件"""
# print(os.path.isfile('zhao.txt'))

"""判断是否为目录文件"""
# print(os.path.isdir(r'E:/python/day_1'))

"""判断是否为链接文件"""
# print(os.path.islink('a.txt'))


def tongji():
    m=1
    n=1
    os.chdir(r'E:\作业')
    for i in os.listdir():
        if os.path.isfile(i):
            print(m,'普通文件','{}'.format(i))
            m+=1
        elif os.path.isdir(i):
            print(n,'目录文件','{}'.format(i))
            n+=1
    print('普通文件',m-1)
    print('目录文件',n-1)


"""统计目录下有几个普通文件，几个目录文件"""
# os.chdir(r'E:\作业')
# putong = [y for y in os.listdir() if os.path.isfile(y)]
# mulu = [x for x in os.listdir() if os.path.isdir(x)]
# print(len(putong))
# print(len(mulu))

"""统计后缀名"""
# m=0
# for i in os.listdir(r'E:/python/day_1'):
#     if '.py' in os.path.splitext(i):
#         m+=1
# print(m)

"""
xlwt 需要下载的模块
作用：给excel表格写入数据
xlrd
作用：读取excel表格中的数据
xlutils
作用：给excel表格中追加数据
"""
import xlwt
"""打开一个空白文件"""
# f = xlwt.Workbook(encoding='utf-8')

"""添加一个标签页,括号中写标签页的名称"""
# sheet = f.add_sheet('python_1')

"""
写入数据
三个参数：
第一个代表多少行，第一行从0开始；
第二个代表多少列，第一列从0开始；
第三个代表写入的内容。
"""
# sheet.write(0,1,'内容')

"""保存文件"""
# f.save('text1.xls')

"""批量添加30条信息"""
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('python_1')
# a=('姓名','年龄','班级')
# b=('小明',11,5)
# for i in range(31):
#     if i == 0 :
#         for k in range(3) :
#             sheet.write(i,k,a[k])
#     else:
#         for j in range(3):
#             sheet.write(i,j,b[j])
# f.save('text2.xls')

"""将数据从txt文件导入到excel表格中"""
# f = open('a.txt','r',encoding='utf-8')
# biao=f.readlines()
# hang=len(biao)
# p = xlwt.Workbook(encoding='utf-8')
# sheet = p.add_sheet('python_1')
# for i in range(hang):
#     for j in range(3):
#         sheet.write(i,j,biao[i].split(',')[j])
# p.save('text_5.xls')

"""数据库导入excel表格"""
abc = pymysql.connect(host='192.168.0.35',
                port=3306,
                user='root',
                password='123456',
                charset='utf8')            #连接数据库
aaa = abc.cursor()                         #创建游标
aaa.execute('use yiku')                    #选择库

aaa.execute('desc biao3;')                 #读取表头
bb=aaa.fetchall()
print(bb)
aaa.execute('select * from biao3')        #读取表数据
cc=aaa.fetchall()
hang=len(cc)
print(cc)
p = xlwt.Workbook(encoding='utf-8')        #打开空白excel文件
sheet = p.add_sheet('python_1')            #创建空白页
for i in range(hang):                      #循环写入数据
    if i == 0 :
        for k in range(len(bb)):
            sheet.write(i,k,bb[k][0])
    else:
        for j in range(len(bb)):
            sheet.write(i,j,cc[i][j])
p.save('text_5.xls')                       #保存并退出

"""从txt文档导入到数据库"""
# abc = pymysql.connect(host='192.168.0.35',        #连接数据库
#                       port=3306,
#                       user='root',
#                       password='123456',
#                       charset='utf8')
# tag = abc.cursor()                                #创建游标
# tag.execute('use yiku;')                          #使用库
# # tag.execute('create table biao4(姓名 char(30),年龄 int,班级 char(30));')      #创建表
# with open('a.txt','r+',encoding='utf-8')as f:                                  #打开txt文件
#     qqq = f.read()                                                             #读取txt文件中内容
#     shujv=qqq.split('\n')                                                      #去掉‘\n’
# shu = len(shujv)                                                               #统计txt文件中有多少行
# for i in range(0,shu):                                                         #循环将txt文件中内容写入到数据库中
#     shujv_1 = shujv[i+1].split(',')
#     tag.execute('insert into biao4 values("{}","{}","{}");'.format(shujv[0],shujv[1],shujv[2]))
#     abc.commit()
# tag.execute('select * from biao4;')                                            #查看数据库中表数据
# for i in tag.fetchall():
#     print(i)
# abc.close()                                                                    #关闭


"""从数据库中将内容导入到txt文件"""

# abc = pymysql.connect(host='192.168.0.35',
#                 port=3306,
#                 user='root',
#                 password='123456',
#                 charset='utf8')                # 连接数据库
# aaa = abc.cursor()                             # 创建游标
# aaa.execute('use yiku')                        #选择库
# with open('a.txt','w',encoding='utf-8') as f:  #创建、打开文件
#     aaa.execute('desc biao3;')
#     bb=aaa.fetchall()                          #读取表头
#     f.write("{},{},{}".format(bb[0][0],bb[1][0],bb[2][0],bb[3][0])+'\n')  #写入表头
#     aaa.execute('select * from biao3;')
#     cc=aaa.fetchall()                          #读取表数据
#     for i in cc:
#         f.write("{},{},{}".format(i[0],i[1] ,i[2])+'\n')      #写入表数据
"""------------------------------------------------------------------------"""

#
if ord('a')==97 :
    print('味道好极了，我们美国人说vrey good')
print(ord('o'))