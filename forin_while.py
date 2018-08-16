# -*- coding: utf-8 -*-
#for ... in
#依次把list或tuple中的每个元素迭代出来
names = ['Amy','Tina','Bob'];#list
names_tuple = ('Adma','Git','webpack');
for name in names:
    print("学生：",name);
for name_tuple in names_tuple:
    print("tuple学生：",name_tuple);
#1-10的整数之和
sum = 0;
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x;
print("1到10整数和：",sum);#55
#range()函数：生成一个整数序列
rangeArr = range(5);
print("range()函数生成整数序列:",rangeArr);#range(0, 5)
rangeList = list(range(5));
print("range()函数生成整数序列后,list()函数再转成list：",rangeList);#[0, 1, 2, 3, 4]
sum_list = 0;
#print(list(range(101)));#[0,....,100]
for x in range(101):
    sum_list = sum_list + x;
print("range list函数生成的和：",sum_list);#5050

#while
sum_while = 0;
n = 99;
while n>0:
    #print(n);
    sum_while = sum_while + n;
    n = n - 2;
print("100以内所有奇数之和：",sum_while);#2500
#practice
L = ['Bart', 'Lisa', 'Adam'];
for name in L:
    print("hello,%s" % name);#hello,Bart 输出结果没有空格
    print("hello,",name);#hello, Lisa  输出结果有空格
for name in L:
    print("hello,{0}".format(name));#hello,Bart 输出结果没有空格