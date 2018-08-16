#当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1,2);
print("tuple : ",t);
#可获取指定索引值
print("指定索引值0：",t[0]);
print("指定索引值1：",t[1]);
#空tuple
emptyT = ();
print("空tuple:",emptyT);
#只有一个元素的tuple
onlyOneElementTuple = (1,);
noCommaElementTupel = (1);
print("只有一个元素时要添加上逗号来消除歧义：",onlyOneElementTuple);#(1,)
print("无逗号时列表：",noCommaElementTupel);#1
#"可变tuple"
changableTuple = ('a', 'b', ['A', 'B']);
changableTuple[2][0] = 'X';
changableTuple[2][1] = 'Y';
print("可变tuple：",changableTuple);#('a', 'b', ['X', 'Y'])
#practice
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
];
# 打印Apple:
print("打印apple:",L[0][0]);
# 打印Python:
print("打印Python:",L[1][1]);
# 打印Lisa:
print("打印Lisa:",L[2][2]);