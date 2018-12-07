#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = ('192.168.0.104',5000)
s.bind(host)

while True:
    a,b = s.recvfrom(1024)
    print(a.decode('utf-8'))
    print(b)
    msg = 'nihao '
    s.send(msg.encode('utf-8'),b)
