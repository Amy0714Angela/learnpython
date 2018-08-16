classmates = ['amy','tony','tina'];
print("有序列表：",classmates);
#list 长度
lens = len(classmates);
print("列表长度：",lens);
print("列表第一项：",classmates[0]);
print("列表第二项：",classmates[1]);
print("列表第三项：",classmates[2]);
print("最后一个选项的索引：",lens - 1);
print("使用负数获取列表最后一项：",classmates[-1]);
print("使用负数获取列表最后第二项：",classmates[-2]);
print("使用负数获取列表最后第三项：",classmates[-3]);
#添加元素 append
classmates.append("the new classmates");
print("向列表最后添加元素：",classmates);
#插入到指定位置 insert
classmates.insert(1,'jack');
print("向列表指定位置添加元素：",classmates);
#删除末尾元素 pop()
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


#动态输入内容操作List及Tuple
listEle = ['A','B','C'];
#在数组末尾追加元素  数组名.append()
eleAdd = input("请输入要追加的元素：");
listEle.append(eleAdd);
print("动态追加元素后：",listEle);
#在指定位置追加元素  数组名.insert()
replaceEle = input("请输入要替换的元素:");
replaceIndex = input("请输入要替换的索引位置：");
listEle.insert(int(replaceIndex),replaceEle);
print("动态insert元素后：",listEle);#['A', 'replace', 'B', 'C', 'test']

