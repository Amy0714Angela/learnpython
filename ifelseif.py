birth = input("输入出生年份:");
if int(birth)>2000:
    print("00后");
else:
    print("00前");


height = 1.75
weight = 80.5
bmi = weight/(height*height);
if bmi<18.5:
    print("过经");
elif bmi<25:
    print("正常");
elif bmi<28:
    print("过重");
elif bmi<32:
    print("肥胖");
else:
    print("严重肥胖");