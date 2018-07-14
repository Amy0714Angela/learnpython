#用户输入信息
name = input('please enter your name : ');
print("hello",name);
print("1024 * 768 =",1024 * 768 );
print('''line1 line1 line1
line2 line2 line2
line3 line3 line3''');#多行字符串
print(r'''hello,\n
world''');#多行不转义
print("布尔值True：",True);
print("布尔值False：",False);
print("布尔值3>2：",3>2);
print("布尔值3>5：",3>5);
print("AND 与运算 ：",True and True);
print("AND 与运算 ：",True and False);
print("AND 与运算 ：",False and False);
print("AND 与运算 5>3 and 2>3：",5>3 and 2>3);
print("OR 或运算 ：",True or True);
print("OR 或运算 ：",True or False);
print("OR 或运算 ：",False or False);
print("OR 或运算 5>3 or 2>3 ：",5>3 or 2>3);
print("not 或运算 ：",not True);
print("not 或运算 ：",not False);
print("not 或运算 3>2 ：", not 3>2);
age = 10;
if age>19:
    print('adults');
elif age>=13:
    print('teenagers');
else:
    print('child');
print("空值：",None);
print("0 ",0);
print("10/3 = ",10/3);
print("即使整除结果也是浮点数 10/2 = ",10/2);
print("地板除// : 10//2 = ",10//2);
print("即使除不尽也是整数 10//3 = ",10//3);
print("求余// : 10%3 = ",10%3);

#practice quiz
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print("n ",n);
print("f ",f);
print("s1 ",s1);
print("s2 ",s2);
print("s3 ",s3);
print("s4 ",s4);

s1 = 72;
s2 = 85;
r = (s2 - s1)/ s1 * 100;
name = input("考生名字：");
print("%s 提高了 %.2f %%" % (name,r));#格式化
print("{0}提高了 {1:.2f}%".format(name,r));#format格式化