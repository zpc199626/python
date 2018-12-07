#!/usr/bin/python
#-*- coding:utf-8 -*-
#Author: 白志强
#@Time: 2018/7/13 16:41

from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
"""创建窗口"""
windows = Tk()
"""定义窗口的标题"""
windows.title('hello')
"""设置窗口的大小"""
windows.geometry('300x400')
"""定义一个文本的标签"""
tag = Label(windows,text='你好',font=("微软雅黑",15))
"""将标签放在窗口的那个位置"""
tag.grid(row=0, column=0)
"""定义一个按钮的标签"""
bu = Button(windows, text="不喜欢",width=10,
                 height=2, command='bu')
bu.grid(row=3, column=0, sticky=W)
"""显示窗口"""
windows.mainloop()
