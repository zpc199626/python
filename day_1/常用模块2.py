#/usr/bin/env python
#-*- coding:utf-8 -*-
import pymysql
import xlwt
import os
import xlrd

"""读取excel表格 ， xlrd模块"""

"""打开一个文件"""
# f = xlrd.open_workbook(r'../爬虫/douban.xls')

"""两种获取标签页的方式 
    1.通过索引值来获取
    2.通过标签页的名称来获取"""

"""获取标签页的个数"""
# sheet = f.nsheets
# print(sheet)

"""索引获取标签页"""
# sheet = f.sheets()[0]

"""获取所有标签页的名称"""
# print(f.sheet_names())

"""括号中填写操作的标签页"""
# sheet = f.sheet_by_name('python_1')

"""获取文件中有对少行"""
# print(sheet.nrows)

""" row_values 读取第几行的内容，第一行从0开始"""
# print(sheet.row_values(0))

"""读取excel表格中所有 行 内容"""
f = xlrd.open_workbook(r'../爬虫/douban.xls')
sheet = f.sheets()[0]
# sheet = f.sheet_by_name('python_1')
a=sheet.nrows
print(a)
for i in range(a):
    print(sheet.row_values(i))

"""获取有多少列"""
# print(sheet.ncols)

"""读取excel表格中 列 的内容  第一列从0开始"""
print(sheet.col_values(0))

"""读取某个单元格的内容"""
# print(sheet.cell(0,0).value)



""""向excel表格中追加内容"""
# import xlrd
from xlutils.copy import copy
# f = xlrd.open_workbook('text_5.xls')

"""复制文件"""
# new_f = copy(f)

"""操作复制的文件 
   复制的文件只能用索引来获取标签页
"""
# sheet = new_f.get_sheet(0)

"""填写追加的内容"""
# sheet.write(1,4,'哈哈哈')
# new_f.save('text_5.xls')
#
# for i in range(30):
#     sheet.write(i,4,'笨蛋')
#     new_f.save('text_5.xls')

import paramiko
"""这个模块封装了ssh协议 作用是远程连接"""

"""创建一个ssh客户端"""
# ssh123 = paramiko.SSHClient()

"""把将要连接的主机添加到 know_hosts 文件中"""
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh123.connect(hostname='192.168.0.35',
#                port=22,
#                username='root',
#                password='123456')

"""执行命令，产生三个结果
   第一个变量：执行的命令，输入
   第二个变量：命令的结果，输出
   第三个变量：命令的报错
"""
# stuin,stuout,stuerr=ssh123.exec_command('ls -al')

"""命令结果的读取"""
# print(stuout.read().decode())

"""---------------------只能输入有结果的命令---------------------"""

# ssh123.close() #断开连接

"""小循环"""
# ssh123 = paramiko.SSHClient()
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh123.connect(hostname='192.168.0.35',
#                port=22,
#                username='root',
#                password='123456')
# while True:
#     a = input('>>>exit退出>>>')
#     if a == 'exit':
#         break
#     else:
#         stuin,stuout,stuerr = ssh123.exec_command(a)
#         print(stuout.read().decode())
# ssh123.close()

"""传输文件"""

"""创建一个传输通道
   接收的只能是元组"""
# ssh23 = paramiko.Transport(('192.168.0.35'))
# ssh23.connect(username='root',
#               password='123456')
"""传输文件只用 sftp 协议，创建一个 sftp 实例"""
# sftp = paramiko.SFTPClient.from_transport(ssh23)

"""get 是从linux下载文件到本地"""
# sftp.get('Python-3.6.3.tgz','aaa.gz')

"""put 是从本地向liunx上上传文件"""
# sftp.put('字串的函数.py','/home/字串的函数.py')

# sftp.close()



"""数据从excel表格导入到txt文件"""
f = xlrd.open_workbook('text_5.xls')            # 打开text.xls 表格
txt = open('b.txt','w',encoding='utf-8')        # 打开或创建文件b.txt
# sheet = f.nsheets                             # 查看标签页的个数
sheet  = f.sheets()[0]                          # 通过索引获取标签页
hang = sheet.nrows                              # 统计行数
lie = sheet.ncols                               # 统计列数
for i in range(hang):                           # 循环写入内容
    p=sheet.row_values(i)                       # 将每一行的内容赋予一个变量
    for k in range(lie):
        if k == lie-1:
            txt.write('{}'.format(p[k])+'\n')  #当写入最后一列的时候，不加逗号
        else:
            txt.write('{},'.format(p[k]))


"""------------------------------------------------------------------------------"""


"""数据从exce表格导入数据库"""
# depot = pymysql.connect(host='192.168.0.35',
#                         port=3306,
#                         user='root',
#                         password='123456'
#                         charset='utf8')                         # 连接数据库
# tag = depot.cursor()                                            # 创建游标
# # tag.execute('create database erku;')                          # 创建库
# tag.execute('use erku;')                                        # 使用库
# tag.execute('create table biao5(姓名 char(30),年龄 int,班级 char(30),战力 int);')           # 创建表
# xls = xlrd.open_workbook('text_5.xls')                          # 打开excel表格
# sheet = xls.sheet_by_name('python_1')                           # 通过名字选择标签页
# hang = sheet.nrows                                              # 统计行
# lie = sheet.ncols                                               # 统计列
# for i in range(1,hang):                                         # 写入内容
#     pp = sheet.row_values(i)                                    # 将每一行的内容赋予一个变量
#     tag.execute("insert into biao5 values('{}','{}','{}','{}');".format(pp[0],pp[1],pp[2],pp[3]))
# tag.execute('select * from biao5;')                             # 查看表内容
# print(tag.fetchall())                                           # 显示上一步的内容
# tag.close()                                                     # 关闭数据库

"""------------------------------------------------------------------------------------------------------------------"""


"""发送邮件"""
import smtplib  # 发送邮件的协议
import email.mime.text  # 处理发送的内容
import email.mime.multipart  #  处理邮件的表头

sender = 'zpc1996@163.com'  #  发送者
recver = ['zpc19960216@163.com',
          '15837806865@163.com',
          'm18790714939_1@163.com',
          'xcz201807@163.com']   #  接收者
server = 'smtp.163.com'          #  服务器地址
passwd = 'pengpeng0206'             #  授权码
# 创建一个空邮件
message = email.mime.multipart.MIMEMultipart()
# 发件人
message['from'] = sender
# 收件人
message['to'] = ','.join(recver)
# 主题
message['subject'] = 'python lenrn'
# 正文
text = """
你好，这里是2060年的时空邮件，你只需支付2000块，就可以试用该服务。
"""
# 处理文本信息
text = email.mime.text.MIMEText(text)
# 将处理后的信息添加到邮件里
message.attach(text)

"""添加附件"""
att1 = email.mime.text.MIMEText(open('1.jpg','rb').read(),'base64','utf-8')
att1["Content-type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="1.jpg"'
message.attach(att1)
att2 = email.mime.text.MIMEText(open('1.jpg','rb').read(),'base64','utf-8')
att2["Content-type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="1.jpg"'
message.attach(att2)
# 定义服务器和端口
smtp123 = smtplib.SMTP_SSL(server,465)
# 登录服务器
smtp123.login(sender,passwd)
# 发送邮件
smtp123.sendmail(sender,recver,message.as_string())
# 断开连接
smtp123.close()

#
# print('asd'.isalpha())
