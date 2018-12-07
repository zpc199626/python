#/usr/bin/env python
# -*- coding:utf-8 -*-
# # list(列表) ：一组数据的集合（等同于shell上的数组）
# # 以中括号为标识，以逗号隔开的  eg：[元素1，元素2，元素3]
# # 作用 ：是用来储存数据的。
# # 特点：1.可变的  2.支持索引  3.支持切片
# # 切片：在一组数据中只取某一个或者某一个叫做切片
# a = [2,'qwe',3,['asdf','qwer',44],4,5] #多层数据
# print(a[:])  #查看列表中所有元素
# print(a[0])  #查看列表中某个元素
# print(a[0:3]) #显示0-2的元素
# print(a[1][-1]) #显示二层列表中最后一个元素

#列表中的内置函数

# a = [2,'qwe',3,44,44,['asdf','qwer',44],4,5]
# c=len(a)
# print('第一个',c)
# a.append(['qw','we'])
# print('第二个',a)
# a.insert(1,'[123,234]')
# print('第三个',a)
# a.remove(['asdf','qwer',44])
# print('第四个',a)
# b = a.index(4)
# print('第五个',b)
# d = a.count(44)
# print('第六个',d)

# a.append('qwe') # 将括号中的元素添加到列表中;注意：只能添加一个
#              # 添加在最后
# a.insert(2,'abc') #第一个参数是下标位置，第二个是参数添加元素。
# remove :删除某个元素。
# pop() ：
# a.remove(['asdf','qwer',44])
# c = a.index(3)  #获取某元素的下标值
# # 第二个python的内置函数 len() 统计某数据类型中有多少个元素
#  # len() 统计某数据类型中有多少个元素
# c = a.count(3)  #统计某元素在列表中的个数
# d = len(a)
# print(d)

# b = [12,23,34,45,56,67,1]
# a = [234,345,456,567,1,b]
# a[5].reverse()
# print(a)
# print(type(print(a)))


# a = (12,12,23,34,45,56,56,56,7,78,78,111)
# a=list(set(a))   # 去除列表中重复的元素
# a.sort()
# print(a)
# a.reverse()
# print(a)



# b.reverse() # 反转列表
# b.sort()  #排序  默认是升序  只能是同种数据类型  列表没办法排序
# b.reverse()
# # copy 浅复制：只能复制一层的数据
# import copy
# b=[12,123,45,67,'ewr']
# a = [121,233,1232,b]
# f=copy.deepcopy(a)  # 深复制 完全复制
# a.append(100)
# a[3].append(100)
# a.extend(b) # 将b列表中的所有元素更新到a列表中

# a = [12,23,34,45,56,3]
# b = [23,34,546,678,88]
#
# b.extend(a)
# print(b)


# import copy
# f = copy.deepcopy(b)
# # f = b.copy()
# a.append('qwe')
# print(f)
# # b.extend(a)
# b[5].append('wert')
# print('最终的B:',b)




# tuple(元组)  一组数据的集合
# 以括号为标识 ， 以逗号隔开
# 特点：1.不可变的  2.支持索引  3.支持切片

# a = (12,234,354,56,'qwe')
# c = a.count(12) #统计某元素在元组中有多少个
# d = a.index(234) #获取某元素的下标位置的值
# print(c)
# print(d)
# a = (12,34,45,567,78,'etr','tyy')
# print(len(a))


# dict（字典） 存储数据的 ，数据格式： key = value
# 以大括号为标识，以逗号隔开
# 特点：可变的 2.无序的 3. 不支持索引
a = {'name':'xiaoming','age':20,"sex":'nan','sec':[90,50]}
b = {'aa':'bb'}
# 添加
a['hhh']=123456
# a.pop('name')  #删除key所在的键值对
# a.popitem()  # 默认删除最后一个
# b = a.keys() #获取所有的key
# c = a.values() # 获取所有的值
# b = a.items()  #获取所有的键值对
# a.update(b)   # 将字典b中的所有元素更新到a中
print(a)
# 不支持索引：不支持通过下标位置去取值
# 支持通过key取值
# a['name'] = '123'  # 修改key的值
# print(a['sec'][0])


# set(集合）  一组数据的结集合 存储数据的
# 以大括号来标识，以逗号分隔开 {1,2,3,4,5}
# 特点：1.不重复的  2.无序的  3.不支持索引  4.可变的
# a = {12,234,45,56,12,'qwe','asd'}
# a.add(10)  #添加一个元素，元素不能是列表
# a.pop()  # 默认删除最后一个  随机删除一个
# a.remove(12)  # 删除括号中的元素
# a.clear()
# b = {12,234,11,22,33}
# a.update(b)  #将集合 b中的所有元素更新到 a中
# 并集  |
# c = a|b
# print(c)

# a=input("想啥呢:")
# a=int(a)
# print(type(a))

# a = "qwerqwe"
# print(a[2:5])
 


