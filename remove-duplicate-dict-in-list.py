#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#去掉list中重复的dict类型数据  参见：https://codeday.me/bug/20171001/76617.html
#[{'a'：123，'b'：1234},{'a'：3222，'b'：1234},{'a'：123，'b'：1234}]
#想要结果： [{'a'：123，'b'：1234},{'a'：3222，'b'：1234}]

l = [{'a':123,'b':1234},{'a':3222,'b':1234},{'a':123,'b':1234}];
#去重但不能保留原有排序

#[dict_items([('a', 123), ('b', 1234)]) , dict_items([('a', 3222), ('b', 1234)]) , dict_items([('a', 123), ('b', 1234)])]
print([d.items() for d in l]);#列表生成器，见：廖雪峰python教程，获取 list中的每个字典列表dict_items
#[(('a', 123), ('b', 1234)), (('a', 3222), ('b', 1234)), (('a', 123), ('b', 1234))]
print([tuple(d.items()) for d in l]);#将dict_items转成tuple元组类型，即将 字典列表转换为元组列表,其中元组包含字典的项目（元组可以被哈希）
#{(('a', 3222), ('b', 1234)), (('a', 123), ('b', 1234))}
print(set([tuple(d.items()) for d in l]));#使用set删除重复数据
#[(('a', 3222), ('b', 1234)), (('a', 123), ('b', 1234))]
print([t for t in set([tuple(d.items()) for d in l])]);#转成list
#[{'a': 3222, 'b': 1234}, {'a': 123, 'b': 1234}]
print([dict(t) for t in set([tuple(d.items()) for d in l])]);#将tuple元组转成字典
#print("去重但不能保留原有排序:",[dict(t) for t in set([tuple(d.items()) for d in l])]);

#去重并保留原有排序
seen = set()
new_l = []
for d in l:
    t = tuple(d.items())
    if t not in seen:
        seen.add(t)
        new_l.append(d)
print("去重并保留原有排序：",new_l);
