# /usr/bin/env python
# -*- coding : utf-8 -*-
import random
import os


#对文件的操作 ： open() 函数
#  格式  open('文件名','权限','编码方式')
# '文件名' ：如果不加路径，表示的是当前目录下的文件。如果此目录下有这个文件，那么就操作这个文件，如果没有就创建。
#           如果有路径的话，要在路径上加上一个双斜杠，表示不转义或者在路径前边加 r
# 权限 ：指的是代码对文件的操作权限；
#   w:写    r:读    a:追加  w+:写 读  r+：读 写 a+：追加 读  wb：  rb：  ab：以字节码的格式
# write(写入的内容) 只能是字符串
# read() :读取文件中所有内容，结果是字符串类型。
# readlines() :读取文件中所有内容，结果是列表，列表中的每一个元素，是文件中的每一行。
# readline() : 读取文件中一行内容，结果为字符串类型。 #每次只读取一行，重复使用时会迭代
# 追加使用的函数依然是 write() write具备不换行的功能
# 上下文管理器  with语句  #原理：___enter__、__exit__
# 对上下文的打开和关闭强制执行的操作
# 格式：  with 打开的文件 as 变量名:


"""
异常处理语句
异常：因代码的逻辑关系导致的程序中断。
异常处理（异常捕获）：对将要发生的异常进行预防。
可以针对某一种异常或者多种异常去处理。
"""
"""try ... except...
 格式： try:
           执行语句  #....也许会发生异常的语句
       except：     #默认是处理所有的异常。
           执行语句
"""
# 当你只想处理一种异常时，在except语句后面加上异常类型。 NameError TypeError ArithmeticError
# Exception :表示所有的异常。
# try:
#     a='123'
#     print(a+1)
# except TypeError as x:  # as 后面可以将异常描述交给一个变量
#     print(x)
# 如果想要写多个except后面只能有一个异常。

# 报错的格式：1、报错的位置 2、报错的内容 3、报错的类型和描述。

# try...except...else... 原理：只要 try 语句中没有异常，就执行 else
# 例题
try:
    a='123'
    # print(a+1)
except:
    print('hello')
else:
    print('ok')

# try...except...finally... 原理：finally语句一定会被执行。
# try:
#     print(0)
# except:
#     print(0)
# finally:
#     print('hello')

# raise  #触发异常（用来自定义异常）
# m=int(input('你猜猜这是啥'))
# if m == 1:
#     raise Exception('瞅你能的')
# else:
#     print(m)
# print(1)

# 导入语句  # 把使用的库导入到本文件中  import
"""下载库"""
# 1.pip 下载；
# pip：python 自带的一个组件。
# 作用：用来下载网络上面的 python 库
# 用法：在cmd中直接输入pip install 库名称；
# form 文件名 import 函数名  # 从文件中导入函数、
# from 文件名 import * #  从文件中导入所有函数
# 导入写在文件最前面





# with open('zhao.txt','a',encoding='utf-8') as f:
#     for i in range(10):
#         f.write('123'+'\n')
# f= open('zhao.txt','r',encoding='utf-8')
# b=f.read()
# f.close()
# for i in b :
#     if '\n' == i :
#         b.remove(i)
#         print(b)
#     if i.startswith('a') :
#         b.remove(i)
#         print(b)
# c=len(b)
# print(b)
#
# for i in range(1,11):
#     f=open("{}.txt".format(i),"w",encoding='utf-8')
#     for x in range(10):
#         f.write('{}'.format(x)+'\n')
# f.close()


#多行字符串
#
# f=open('zhao.txt','a',encoding='utf-8')  # 打开一个新的文件。
#
# for i in range(1, 10):  #向文件中写入九九乘法表
#     for j in range(1, i + 1):
#         f.write("{}*{}={}\t".format(j,i,i*j))
#     f.write('\n')
#
#
# print(f.readlines()[3:5])
# f.close()  #关闭文件

# """取txt文档中的值"""
# f = open('a.txt','r',encoding='utf-8')
# biao=f.read()
# print(biao)
# bb=biao.split('\n')
# print(bb)
# print(len(bb))

# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""小兔子"""
# f1 = 1
# f2 = 1
# for i in range(1, 22):
#     print('%12ld %12ld' % (f1, f2)),
#     if (i % 3) == 0:
#         print()
#     f1 = f1 + f2
#     f2 = f1 + f2

# with open('n.txt','a+',encoding='utf-8') as f:
#     f.write('hello,word')
#     f.seek(16)
#     print(f.readlines())

for i in range(10):
    os.mkdir('mulu_{}'.format(i))
    with open('wenjian{}'.format(i),'a+',encoding='utf-8') as f:
        f.write('第{}个'.format(i+1))
        f.seek(0)
        print(f.read())
    os.remove('wenjian{}'.format(i))
    os.rmdir('mulu_{}'.format(i))
