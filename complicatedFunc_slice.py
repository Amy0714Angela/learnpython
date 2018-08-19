# -*- coding: utf-8 -*-
#高级特性：切片
#取前N个元素，也就是索引为0-(N-1)的元素，可以用循环
#字符串'xxx'也可以看成是一种list，每个元素就是一个字符
rlist = [];
rtuple = ();
rstr = '';
n = 3;
List = ['a','b','c','d','e'];
Tuple = (1,2,3,4,5);
str = 'abcde';
for i in range(n):
    rlist.append(List[i]);
    #rtuple.append(Tuple[i]);#tuple不可变，没有append方法
    #rstr.append(str[i]);#'str' object has no attribute 'append'
print("取list前3个元素：",rlist);
#print("取tuple前3个元素：",rtuple);
#print("取str前3个字符：",rstr);
#取指定索引范围的操作，，用循环十分繁琐，python提供了切片（slice）操作
print("切片list：索引从0开始至索引3，不包含索引3，",List[0:3]);
print("切片tuple：索引从0开始至索引3，不包含索引3，",Tuple[0:3]);
print("切片string：索引从0开始至索引3，不包含索引3，",str[0:3]);#abc
print("切片list：索引从0开始可省略，不包含索引3，",List[:3]);
print("切片tuple：索引从0开始可省略，不包含索引3，",Tuple[:3]);
print("切片str：索引从0开始可省略，不包含索引3，",str[:3]);#abc
print("切片list：索引从2开始至索引6，不包含索引6,",List[2:6]);#['c', 'd','e']
print("切片tuple：索引从2开始至索引6，不包含索引6,",Tuple[2:6]);#[3,4,5]
print("切片str：索引从2开始至索引6，不包含索引6,",str[2:6]);#cde

#倒数切片
#倒数第一个元素索引值为-1
print("取倒数两个元素list：",List[-2:]);
print("取倒数两个元素tuple：",Tuple[-2:]);
print("取倒数两个元素str：",str[-2:]);#de
print("取倒数第二个元素list：",List[-2:-1]);#['d']
print("取倒数第二个元素tuple：",Tuple[-2:-1]);#(4,)
print("取倒数第二个元素str",str[-2:-1]);#d
#0 - 99的数列
L = list(range(100));
T = tuple(range(100));
#前10个数
print("取前10个数list:",L[:10]);
print("取前10个数tuple:",T[:10]);
#取后10个数
print("取后10个数list:",L[-10:]);
print("取后10个数tuple:",T[-10:]);
#取11-20个数
print("取第11-20个数list:",L[10:20]);
print("取第11-20个数tuple:",T[10:20]);
#前10个数，每2个取1个：偶数
print("取前10个数，每2个取1个 list:",L[:10:2]);#[0, 2, 4, 6, 8]
print("取前10个数，每2个取1个 tuple:",T[:10:2]);#(0, 2, 4, 6, 8)
#前10个数，每2个取1个：奇数
print("取前10个数，每2个取1个 list:",L[1:11:2]);#[1, 3, 5, 7, 9]
print("取前10个数，每2个取1个 tuple:",T[1:11:2]);#
#所有数每5个取一个
print("所有数，每5个取1个 list:",L[::5]);#[0, 5, 10, 15....90, 95]
print("所有数，每5个取1个 tuple:",T[::5]);#(0, 5, 10, 15....90, 95)
#原样复制list 或 tuple
print("原样复制list:",L[:]);
print("原样复制tuple:",T[:]);

#practice
Str = ' abcde ';
print("使用strip方法去除首尾空格:%s" % Str.strip());





