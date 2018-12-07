#!/usr/bin/python
#-*- coding:utf-8 -*-

from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk

def closeWindow():
    # 设置提示信息
    messagebox.showinfo(title='警告', message='想啥呢，小老弟')

def closeallwindow():
    # 销毁所有窗口
    window.destroy()

def Win():
    # 顶级窗口 在原窗口之上又创建了个
    love = Toplevel(window)
    love.geometry("300x100+520+260")
    love.title("啥都别说，先奶")
    label = Label(love, text="IG冲鸭", font=("微软雅黑", 20))
    label.pack()
    btn = Button(love, text="确定", width=10, height=2,command=closeallwindow)
    btn.pack()

def come_on():
    come = Toplevel(window)
    come.geometry("300x100+520+260")
    come.title("啥都别说，先奶")
    label = Label(come, text="加油有什么用，点冠军", font=("微软雅黑", 20))
    label.pack()
    btn = Button(come, text="我这就去", width=10, height=2,command = come.destroy)
    btn.pack()
    come.protocol('WM_DELETE_WINDOW', closecome_on)

def closecome_on():
    # messagebox.showinfo(title='再考虑一下', message='再考虑考虑')
    # return
    come_on()



window = Tk()
window.title('我画你猜')
window.geometry('250x310+300+200')
tag_1 = Label(window,text='IG冲鸭',font=("微软雅黑",15))
tag_1.grid(row=0,column=0)
bu_y = Button(window,text='冠军',width=10,height=0,command = Win)
bu_y.grid(row = 3,column = 1,sticky = E)
bu_n = Button(window,text='加油',width=10,height=0,command = come_on)
bu_n.grid(row = 3,column = 0,sticky = E)
img = Image.open('aa.jpg')
photo = ImageTk.PhotoImage(img)
imagephoto = Label(window,image=photo)
imagephoto.grid(row=1, columnspan=3)
window.protocol('WM_DELETE_WINDOW', closeWindow)
window.mainloop()
