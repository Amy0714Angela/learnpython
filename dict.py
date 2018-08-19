#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85};
print('Michael\'s score is',d['Michael']);
#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['Adam'] = 67;
print("添加数据到dict:",d);#{'Michael': 95, 'Bob': 75, 'Tracy': 85, 'Adam': 67}
#一个key对应一个value
d['Adam'] = 98;
print("dict重新为一个已经存在的key赋值:",d);#{'Michael': 95, 'Bob': 75, 'Tracy': 85, 'Adam': 98}
#避免key不存在的错误，有两种方法：
#1) 判断key是否存在
print("判断key是否存在:",'Thomas' in d);#False
#2) 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print("dict get()，若key不存在，返回None:",d.get('Thomas'))#None
print("dict get()，若key不存在，自己指定的value:",d.get('Thomas',-1));#-1
#删除key
print("删除key:",d.pop('Bob'));#75
print("删除key Bob后dict:",d);#{'Michael': 95, 'Tracy': 85, 'Adam': 98}

