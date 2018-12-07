#/etc/bin/env python
#-*- coding:utf-8 -*-
import socket
# """TCP客户端"""
# """创建socket  封装协议"""
# soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# """连接服务器  接收参数是元组"""
# a = ('192.168.0.104',5000)
# soc.connect(a)
# """发送请求"""
# aaa = '你好啊'
# soc.send(aaa.encode('utf-8'))
# """接收响应"""
# msg = soc.recv(1024)
# print(msg.decode('utf-8'))
# #
# """UDP客户端"""
while True:
    """创建socket  封装协议"""
    soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    """发送请求数据"""
    a = ('192.168.0.104',5000)
    # b = input('世界尽头_z：6')
    # reg = b
    reg = '你真好，你真是个'
    soc.sendto(reg.encode('utf-8'),a)
    """接收响应"""
    c = soc.recv(1024)
    print(c.decode('utf-8'))