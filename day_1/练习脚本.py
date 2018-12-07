#/usr/bin/env python
# -*- coding:utf-8 -*-
import random
# 循环语句    for  while
# for 语句
# 格式
# 注意：1.没有do 和 done
#       2.冒号和缩进
# for 变量名 in 范围 ： # 范围：指的是有一组数据的集合
#     执行语句
#     执行语句
#     执行语句
#     ......
# a = [1,2,3,4,5,3]
# for i in a :
# 	print(i)

#取数字范围 range()  :将数字变成一个范围，只有一个数字时默认从零开始。
#                                       有两个数字时 第一个数字时起始值，第二个数字时结束值。
#                                       有三个数字时，第三个数字是递进。
# for i in range(11):
# 	print(i)
# for i in range(1,11):
# 	print(i)
# for i in range(1,15,2):
# 	print(i)

# print(sum(range(101)))  # 计算1-100的和

# b=0                     # 计算1-100的和
# for i in range(1,101):
# 	b=b+i
# print(b)


# a = {'name':'xiao','age':30.0,'nnn':'mmm'}
# for i,j in a.items() : #items() 取字典中所有的键值对。
# 	print(type(i))
# 	print(i)
# 	print(type(j))
# 	print(j)

# a=0
# b=0
# for i in range(1,100,2):
# 	a+=i
# for j in range(0,100,2):
# 	b+=j
# print(a-b)


# a = '28'
# for i in enumerate(a):   # enumerate() :将下标位置和元素对应
# 	print(i)



# a = ['电脑','计算机','MP3']
# for i,j in enumerate(a):
# 	print(i+1,j)
#
# b=int(input('商品编号'))
# print(a[b-1])



# 循环嵌套 ： 循环语句中嵌套其他语句（判断语句，循环语句）
# b=0
# for a in range(1,100):
# 	if a % 2 == 0 :
# 		b -= a 
# 		print(b)
# 	else:
# 		b += a 
# 		print(b)
# print(b)



# 循环嵌套循环  for……for……
# 大循环循环一次，小循环循环一轮。



# 不换行 print(j,end=' ')

#九九乘法表
# for i in range(1,10):
# 	for j in range(1,i+1):
# 		print('%d*%d=%d' % (i,j,i*j),end="\t")
# 		# print("{}*{}={}".format(i,j,i*j),end="\t")
# 	print()



# continue  结束本次循环  break 结束循环



# for ……  else ……语句  原理：只要循环没有被 break掉，就执行 else 语句
# a = ['dsf','wefe','qw']
# for i in a :
# 	if len(i) ==2:
# 		break
# else:
# 	print('完美')



# 质数之和
# c = 0
# for i in range(2,100):
# 	for b in range(2,i+1):
# 		if i%b==0:
# 			break
# 	if i==b:
# 		c=c+i
# print(c)

# a=0
# for i in range(2,101):
# 	for j in range(2,i):
# 		if i%j==0:
# 			break
# 	else:
# 		a+=i
# print(a)

# 阶乘
# a = int(input('>>>>>>>'))
# b=1
# d=0
# for i in range(1,a+1):
# 	b=b*i
# 	d+=b
# print(d)

# 三次猜数字
# a = random.randrange(1,10) #从1-10之间随机产生一个数。
# c=3
# for i in range(3):
# 	b = int(input('输入你的数字：'))
# 	c-=1
# 	# print('你还有{}次机会'.format(c))
# 	if a > b :
# 		print("老公，加油！！！")
# 		print('你还有{}次机会'.format(c))
# 		continue
# 	elif a < b:
# 		print('老公你真大！！！')
# 		print('你还有{}次机会'.format(c))
# 		continue
# 	else:
# 		print('老公你真猛！！！')
# 		break
# else:
# 	print('笨蛋')

#去重
# a=[31,23,25,26,27,23,23,27,278]
# a = input('输入数字，用空格隔开:')
# a=a.split(' ')

# a=[1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]
# for i in a:
# 	if a.count(i)>1:
# 		for k in range(1,a.count(i)):
# 			a.remove(i)
# print(a)
# 第二种
# b=[]
# for x in a :
# 	if x not in b :
# 		b.append(x)
# print(b)


# #水仙花数
# for i in range(100,1000):
# 	a=i//100
# 	b=i//10%10
# 	c=i%10
# 	if i==a**3+b**3+c**3:
# 		print(i)

#选择排序法
# a=input("输入一组数字")
# aa=a.split(' ')
# # print(aa)
# b=len(aa)
# for i in range(b):
# 	for j in range(i+1,b):
# 		if int(aa[i])>int(aa[j]):
# 			t=aa[i]
# 			aa[i]=aa[j]
# 			aa[j]=t
# print(aa)


# 冒泡排序法
# a=input("输入一组数字")
# aa=a.split(' ')
# # print(aa)
# b=len(aa)
# for i in range(b):
# 	for j in range(b-1):
# 		if int(aa[j])>=int(aa[j+1]):
# 			t=aa[j]
# 			aa[j]=aa[j+1]
# 			aa[j+1]=t
# print(aa)

#判断字符串是否有回文 (完成)
# a = input("输入一个字符串:")
# b=len(a)//2
# for i in range(b):
# 	if a[i]!=a[-i-1]:
# 		print('no')
# 		break
# else:
# 	print('是回文')

# b=a[::-1]
# if a==b:
# 	print('是回文')
# else:
# 	print('不是回文')


# #打印列表中第一大和第二大的数（完成）
# a = input('输入数字,用空格隔开:')
# a=a.split(' ')
# p=len(a)
# pkf(a)
# # for x,y in enumerate(a) :
# # 	a[x]=int(y)
# v=a.copy()
# v.sort()
# m=v.count(v[-1])
# for n in range(p):
# 	if v[-1]==a[n]:
# 		print(a[n])
# 	if v[-1-m]==a[n]:
# 		print(a[n])




# 四个数组成三位数
# c = input('输入四个数，以逗号为分开')
# a=c.split(',')
# y=[]
# pkf(a)
# # for x,b in enumerate(a) :
# # 	a[x]=int(b)
# for i in a:
# 	for j in a:
# 		for k in a:
# 			if i!=j and i!=k and j!=k:
# 				p='{}{}{}'.format(i,j,k)
# 				if p not in y :
# 					y.append(p)
# print(y)
# print(len(y))


# 不使用int 将字符串变成整数。
# a=input('>>>>>')
# b = a[::-1]
# s=0
# for i,j in enumerate(b):
# 	for h in range(10):
# 		if str(h)==j:
# 			s=s+h*10**i
# print(s)

# 十进制转换十六进制
# a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# b = int(input('>>>>>>'))
# f = ''
# while True:
# 	c = b%16
# 	b = b//16
# 	f+=a[c]
# 	if b == 0:
# 		break
# print(f[::-1])

# 将列表中的最大的放到第一位，最小的放在最后一位。
# a = [12,34,45,566]
# a = a.index(max(a))
# c = a.index(mim(a))
#
# a[b],a[0]=a[0],a[b]
# a[c],a[-1]=a[-1],a[c]
# print(a)

# 将列表中的元素向左挪一位
# a = [23,34,45,56,1]
# c = len(a)
# for i in range(c-1):
# 	a[i],a[i+1]=a[i+1],a[i]
# 	# b=a[i]
# 	# a[i]=a[i+1]
# 	# a[i+1]=b
# print(a)


# 一个数的因数之和等于他本身。
# for a in range(1,10000):
# 	x=0
# 	for i in range(1,a):
# 		b=a%i
# 		if b==0 :
# 			x+=i
# 	if x==a:
# 		print(a)


# # 一个有顺序的列表，随机加入一个数，加在数的正确位置
# b=[1,2,3,4,5,6,7,8,9,10.11,12,23,56,78,90,123,456,789]
# c=int(input('写个数吧:'))
# m=len(b)
# for i in range(m):
# 	if b[i]<=c<=b[i+1] :
# 		b.insert(i+1,c)
# 		break
# 	elif c<b[0]:
# 		b.insert(0,c)
# 		break
# 	elif c>b[-1]:
# 		b.insert(m,c)
# 		break
# print(b)


# 杨辉三角
# a=5
# for i in range(a):
# 	print(' '*i,'* '*a)
# 	a-=1
#
# b=5
# for k in range(b):
# 	print(' *'*b)
# 	b-=1