# -*- coding: utf-8 -*-
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85};
d["Amy"] = 100;
print("dic : ",d);

#判断key是否不存在的二种方式：
#1） prop in dic
print("判断属性是否存在：",'Thomas' in d);
#dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print("判断属性是否存在：",d.get('Thomas'));#None
print("判断属性是否存在：",d.get('Thomas',-1));#-1
#删除一个key，用pop(key)方法
print("删除一个key：",d.pop("Bob"));#75
print("删除一个key后：",d);#{'Michael': 95, 'Tracy': 85, 'Amy': 100}

