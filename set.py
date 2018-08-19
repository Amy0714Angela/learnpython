#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#set只存储key，不存储value，而key又不重复，因此set中不存在重复的key
#要创建一个set，需要提供一个list作为输入集合
s = set([1,2,3]);
print("s结果只是显示set中有哪几个元素，不表示set是有序的:",s);#{1,2,3}
#重复元素在set中自动被过滤
s = set([1,1,2,2,3,4,5]);
print("重复元素在set中自动被过滤：",s);#{1, 2, 3, 4, 5}
#添加元素add
print("s ：",s);#{1, 2, 3, 4, 5}
print("添加元素：",s.add(6));#None
print("添加元素后s ：",s);#{1, 2, 3, 4, 5}
#删除元素remove
print("删除元素：",s.remove(1));#None
print("删除元素后s ：",s);#{2, 3, 4, 5, 6}
#两个set可做交集、并集
s1 = set([1,2,3,4,5]);
s2 = set([2,3,5,6,7,8]);
print("两个set做交集：",s1 & s2);#{2, 3, 5}
print("两个set做并集：",s1 | s2);#{1, 2, 3, 4, 5, 6, 7, 8}