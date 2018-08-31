# -*- coding: utf-8 -*-
#python 函数参数类型：必选参数、默认参数、可变参数、关键字参数
######1、必选参数#########
def pow(x):
    return x * x;
print("pow(x) 1个位置参数:",pow(5));#25
#上述函数只能计算平方，若未立方，则不再可用，修改函数
def pow(x,n):
    s = 1;
    while n>=1:
        n = n - 1;
        s = s * x;
    return s;
print("pow(x,n) 2个位置参数：",pow(5,3));#125
########2、默认参数 ：必须指向不变对象 ######
########可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple #######
#是必选参数在前，默认参数在后
#二是如何设置默认参数。
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
def pow(x,n=2):
    s = 1;
    while n>0:
        n = n - 1;
        s = s * x;
    return s;
print("pow(x,n=2) 默认参数:",pow(5));#25
print("pow(x,n=2) 默认参数:",pow(5,3));#125
def encroll(name,gender,age = 6,city="beijing"):
    print("name:",name);
    print("gender:",gender);
    print("age:",age);
    print("city:",city);
print("使用两个默认参数:",encroll("Amy","girl"));
print("改变第一个默认参数age:",encroll("Amy1","girl",7));
print("改变第二个默认参数city:",encroll("Amy2","girl",city="tianjin"));
#######3、可变参数 ######
#计算如下:a*a + b*b + c*c + ……
#不使用可变参数时方法定义及调用如下:
def calc(numbers):
    print("numbers:",numbers);
    sum = 0;
    for n in numbers:
        sum = sum + n * n;
    return sum;
print("不使用可变参数时调用时参数需组合成一个list:",calc([1,2,3]));#14
print("不使用可变参数时调用时参数需组合成一个tuple：",calc((1,2,3)));#14
print("不使用可变参数时调用时不传参数：",calc([]));#0
print("不使用可变参数时调用时不传参数：",calc(()));#0
#使用可变参数时方法定义及调用如下：
def calc(*numbers):
    print("numbers:",numbers);#(1,2,3)
    print("可变参数类型",isinstance(numbers,tuple));#True
    sum = 0;
    for n in numbers:
        sum = sum + n * n;
    return sum;
print("使用可变参数时调用时参数形式", calc(1, 2, 3));  # 14
print("使用可变参数时调用时参数形式", calc(1, 2, 3));  # 14
print("使用可变参数时调用时不传参数：",calc());#0
#如果已经有一个list或者tuple，要调用一个可变参数:
nums = [1,2,3];
print("已存在list，调用一个可变参数：",calc(nums[0],nums[1],nums[2]));#14
print("已存在list，把list的元素变成可变参数传进去:",calc(*nums));#14
nums = (1,2,3);
print("已存在tuple，调用一个可变参数：",calc(nums[0],nums[1],nums[2]));#14
print("已存在tuple，把tuple的元素变成可变参数传进去:",calc(*nums));#14
########3、关键字参数: 可传入0或者任意个数参数，函数内部自动组装成一个dict ######
def person(name,age,**kw):
    #name,age为必选参数,other为关键字参数
    print("name:",name,"age:",age,"other:",kw);
print("只输入必选参数时：",person("amy",25));#name: amy age: 25 other: {}
print("传入任意关键字参数时：",person("amy",25,city="tianjin"));#name: amy age: 25 other: {'city': 'tianjin'}
print("传入任意关键字参数时：",person("amy",25,gender="M",job="Engineer"));#name: amy age: 25 other: {'gender': 'M', 'job': 'Engineer'}
extra = {'city': 'Beijing', 'job': 'Engineer'};
print("已存在一个dict,转变成关键字参数传入函数：",person("amy",25,city=extra['city'],job=extra['job']));
print("已存在一个dict,传入函数简化方式：",person("amy",25,**extra));

##########命名关键字参数：限制关键字参数的名字######
#查看传入哪些关键字参数，需在函数内部通过kw来判断
def person(name,age,**kw):
    if 'city' in kw:
        print("存在city");
    if 'job' in kw:
        print("存在job");
    print("name:",name,"age:",age,"other:",kw);
print("判断传入了哪些关键字参数，未传入关键字参数：",person('amy',25));
print("判断传入了哪些关键字参数，传入一个关键字参数city：",person('amy',25,city="beijing"));
print("判断传入了哪些关键字参数，传入两个关键字参数city,job：",person('amy',25,city="beijing",job="Engineer"));
print("判断传入了哪些关键字参数,不传city,job，仍可传入不受限制的关键字参数：",person('amy',25,gender="M"));
#要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
def person(name,age,*,city,job):
    #和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
    print("name:",name,"age:",age,"city:",city,"job:",job);
print("限制只接收city和job两个关键字参数,不能只传入一个关键字参数:",person("amy",25,city="beijing",job="Engineer"));
#函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name,age,*args,city,job):
    print("name:",name,"age:",age,"agrs:",args,"city:",city,"job:",job);
personality = ["elegant","caring"];
print("传入一个可变参数及命名关键字参数:",person("amy",25,*personality,city="langfang",job="web coder"))
#命名关键字参数可以有缺省值，简化调用
def person(name,age,*,city="Beijing",job="Engineer"):
    print("name:", name, "age:", age,"city:", city, "job:", job);
print("命名关键字参数可设置默认值:",person("amy","25"));
print("命名关键字参数可设置默认值:",person("amy","25",city="tianjing"));

############参数组合定义的顺序：必选参数、默认参数、可变参数、命名关键字参数和关键字参数 ########################
def f1(a,b,c=0,*args,city,job,**kw):
    print("a:",a,",b:",b,",c:",c,",agrs:",args,',city:',city,',job:',job,',kw:',kw);
print("5种参数：",f1(1,2,3,*[4,5,6],city="beijing",job="Engineer",**{"name":"amy","age":25}));
def f2(a,b,c=0,*args,**kw):
    print("a:",a,",b:",b,",c:",c,",agrs:",args,',kw:',kw);
print("5种参数，前2个位置参数:",f2(1,2));#a: 1 ,b: 2 ,c: 0 ,agrs: () ,kw: {}
print("5种参数，前2个位置参数,第3个默认参数:",f2(1,2,3));#a: 1 ,b: 2 ,c: 3 ,agrs: () ,kw: {}
print("5种参数，前2个位置参数,第3个默认参数c=3:",f2(1,2,c=3));#a: 1 ,b: 2 ,c: 3 ,agrs: () ,kw: {}
print("5种参数，位置参数,默认参数,可变参数:",f2(1,2,3,'a','b'));#a: 1 ,b: 2 ,c: 3 ,agrs: ('a','b') ,kw: {}
print("5种参数，位置参数,默认参数,可变参数,关键字参数:",f2(1,2,3,'a','b',x=99,y=100));#a: 1 ,b: 2 ,c: 3 ,agrs: ('a', 'b') ,kw: {'x': 99, 'y': 100}
def f2(a,b,c=0,*,d,**kw):
    print("a:", a, ",b:", b, ",c:", c, ",d:", d, ',kw:', kw);
print("5种参数:位置参数，默认参数，命名关键字参数，关键字参数:",f2(1,2,d=24,x=99,y=100));#a: 1 ,b: 2 ,c: 0 ,d: 24 ,kw: {'x': 99, 'y': 100}


#practice
def product(x,*L):
    sum = x;
    for n in L:
        sum = sum * n;
    return sum;
# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')