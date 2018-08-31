# -*- coding: utf-8 -*-
from collections import Iterable;
#高级特性：迭代
#Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象(dict,string)上
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    #因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
    print("key为:",key,",value值为：",d[key]);
#默认情况下dict迭代key，也可以迭代value
for value in d.values():
    print("value值为：",value);
#或者key,value同时迭代
for key,value in d.items():
    print("key为：",key,",value值为：",value);
#######迭代字符串
str = "abc";
for ch in str:
    print("字符：",ch);

######判断一个对象是否可迭代:使用collections模块的Iterable类型判断
print("str是否可迭代：",isinstance('abc',Iterable));#True
print("list是否可迭代：",isinstance(['a','b','c'],Iterable));
print("tuple是否可迭代：",isinstance(('a','b','c'),Iterable));
print("int是否可迭代：",isinstance(20,Iterable));#False
print("boolean是否可迭代：",isinstance(True,Iterable));#False

#要对list实现类似Java那样的下标循环
#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for index,value in enumerate(['A','B','C']):
    print(index,value);

#for 同时引用两个变量
for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y);
for m,n in ([1,1],[2,8],[3,27],'ab'):
    print(m,n); #a b 只能是两个字符,因字符串是可迭代对象

#practice
#if L == []:
#    return (None,None);
