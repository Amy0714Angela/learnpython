classmates = ['amy','tony','tina'];
print("有序列表：",classmates);
lens = len(classmates);
print("列表长度：",lens);
print("列表第一项：",classmates[0]);
print("列表第二项：",classmates[1]);
print("列表第三项：",classmates[2]);
print("最后一个选项的索引：",lens - 1);
print("使用负数获取列表最后一项：",classmates[-1]);
print("使用负数获取列表最后第二项：",classmates[-2]);
print("使用负数获取列表最后第三项：",classmates[-3]);
#添加元素
classmates.append("the new classmates");
print("向列表最后添加元素：",classmates);
#插入到指定位置
classmates.insert(1,'jack');
print("向列表指定位置添加元素：",classmates);
#删除末尾元素
classmates.pop();
print("删除末尾元素：",classmates);
#删除指定位置元素
classmates.pop(1);
print("删除指定位置元素:",classmates);
#替换指定位置元素
classmates[1] = 'Sarah';
print("替换指定位置元素：",classmates);
#不同数据类型列表
list = ["Amy",124,True,3<2];
print("不同数据类型列表：",list);#['Amy', 124, True, False]
#列表中包含子列表
subLists = ['python', 'java', ['asp', 'php'], 'scheme'];
print("列表中包含子列表：",subLists);
subListLen = len(subLists);
print("列表中包含子列表的总长度：",subListLen);#4
#空列表
emptyList = [];
print("空列表：",len(emptyList));
