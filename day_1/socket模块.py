#/etc/bin/env python
#-*- coding:utf-8 -*-
"""socket:套接字，提供了网络间的通讯的基本功能（向网络发送请求和应答网络请求）
"""

# TCP server 端
import socket
"""创建socket，封装协议"""
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket.AF_INET:是IPv4的协议 ，socket.SOCK_STAREAM:是tcp的协议
""" 绑定IP和端口号  bind接收到的参数是元组"""
host_s = ('192.168.0.26',3000)
s.bind(host_s)
"""监听  数字是最大等待数"""
s.listen(6)
while True:
"""接收请求"""
    a,b = s.accept()  # 第一个结果a：是客户端的连接信息。 第二个结果b:是客户端的IP地址和端口号
"""接收数据"""
    msg = a.recv(1024)  #1024代表的是每次接收的最大字节数  最大的是1024 不能更大了
    print(msg.decode('utf-8'))
"""发送响应"""
    reg = 'what are you 弄啥嘞？'
    a.send(reg.encode('utf-8'))



# UDP server 端
# import socket
# """创建socket，封装协议"""
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #socket.AF_INET:是IPv4的协议 ，socket.SOCK_DGRAM:是udp的协议
# """ 绑定IP和端口号  bind接收到的参数是元组"""
# host_s = ('192.168.0.93',3000)
# s.bind(host_s)
#
# while True:
#     a,b = s.recvfrom(1024)  #接收数据 第一个变量a:客户端发送的请求数据  第二个变量b:客户端的IP地址和端口号
#     print(a.decode('utf-8'))
#     print(b)
#     msg = '大马猴'
#     # msg = input('冷酷仙境_z：')
#     s.sendto(msg.encode('utf-8'),b)

