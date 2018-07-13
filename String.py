#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('I\'m ok.');
print('I\'m learning\npython.');
print('\\\n\\');
print('\\\t\\');
print(r'\\\t\\');#默认不转义
print('''line1
line2
line3''');# '''...'''的格式表示多行内容，类似html中pre标签
#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print("获取单个字符的整数表示：",ord('A'));#65
print("获取单个字符的整数表示：",ord('中'));#20013
print("把整数编辑转成对应的字符：",chr(66));#B
print("把整数编辑转成对应的字符：",chr(25991));#文
print("把整数编辑转成十六进制：",'\u4e2d\u6587');#中文
#字节类型数据
print("字节类型数据：",b'ABC');#b'ABC'
#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'));#b'ABC'
print('ABC'.encode('UTF-8'));#b'ABC'
print('中文'.encode('UTF-8'));#b'\xe4\xb8\xad\xe6\x96\x87'
#从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'));#'ABC'
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('UTF-8'));#中文
#bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'));#中 \xff被忽略
#字符长度 len() str中包含多少个字符
print(len('ABCDEFG'));#7
print(len('中文测试字符长度'));#8
#字节数  len()  bytes中包含多少个字节数
print(len(b'ABCDEFG'));#7
print(len(b'\xe4\xb8\xad\xe6\x96\x87'));#6
print(len('中文测试'.encode('utf-8')));#12
#1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。

#格式化 : 在Python中，采用的格式化方式和C语言是一致的，用%实现
print('Hello, %s ' % 'world');  # %s字符串
print('Hi, %s,you have %d$.' % ('Amy',10000));#Hi, Amy,you have 10000$.
#格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%02d-%02d' % (3,1));#03-01
print('%2d-%02d' % (3,1));# 3-01
print('%2d-%2d' % (3,1));# 3- 1
print('%2d-%2d' % (3,1));# 3- 1
print('%0.2f' % 3.1415926)#3.14
print('%.5f' % 3.14)#3.14000
print('%.f' % 3);#3  ？？？？？？？？？？？？？？？？？
print('%.f' % 3.0);#3  ？？？？？？？？？？？？？？？？
print('%f' % 3);#3.000000
#%s永远起作用，它会把任何数据类型转换为字符串
print('Age : %s . Gender : %s' % (25 ,True));#Age : 25 . Gender : True   将整数及布尔值转为字符串
#%是一个普通字符
print('growth rate: %d %%' % 7);#growth rate: 7 %


