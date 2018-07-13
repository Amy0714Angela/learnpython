# -*- coding: utf-8 -*-
print(abs(-100));
print(abs(12.34));
#print(abs(12,34));#only one argument
#print(abs('a'));#错误的参数类型
print(max(1, 2));#2
print(max(2, 3, 1, -5));#3
#print(max(2, 3,'ab', -5));#not supported between instances of 'str' and 'int'
#print(max(2, 3,int('ab'), -5));#invalid literal for int() with base 10: 'ab'
#print(max(2, 3,int('2ab'), -5));#invalid literal for int() with base 10: '2ab'
#print(max(2, 3,'24', -5));#not supported between instances of 'str' and 'int'
print(max(2, 3,int('24'), -5));#24

#数据类型转换
#int
print(int('123'));#123
print(int(123.45));#123
print(int(True));#1
print(int(False));#0
#float
print(float('123'));#123.0
print(float('123.45'));#123.45
print(float(True));#1.0
print(float(False));#0.0
#str
print(str(123.45));#'123.45'
print(str(True));#'True'
print(str(False));#'False'
#bool
print(bool('123'));#True
print(bool(123.45));#True
print(bool(0));#False
print(bool('None'));#True
print(bool(''));#False

#利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串
print(hex(ord('A')));#0x41  65
print(hex(ord('中')));#0x4e2d  20013
print(hex(255));#0xff
print(hex(1000));#0x3e8

#自定义函数
def my_abs(x):
    #规范参数类型
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type');
    if(x>=0):
        #return None;
        return;# 同return None;
    else:
        return -x;
print("自定义abs函数：",my_abs(-9));#9
print("自定义abs函数：",my_abs(9));#None

#空函数nop()   定义一个什么事也不做的空函数，可以用pass语句
def nop():
    pass;
def isTeenager(x):
    if(x>18):
        pass;
    elif(x>13):
        print("is teenager");
    else:
        print("little child");
print("测试pass语句：",isTeenager(20));
print("测试pass语句：",isTeenager(16));
print("测试pass语句：",isTeenager(10));
#print("测试自定义abs函数自定义规范：",my_abs('A'));#给出正确提示bad operand type

#返回多个值：返回多值其实就是返回一个tuple，语法上可将括号去掉
import math;
def move(x,y,step,angle=0):#angle默认值为0
    nx = x + step * math.cos(angle);
    ny = y - step * math.sin(angle);
    return nx,ny;
x,y = move(100,100,60,math.pi/6);
print(x,y);#151.96152422706632   70.0

#practice
def quadratic(a,b,c):




