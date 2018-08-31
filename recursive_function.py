# -*- coding: utf-8 -*-
#递归函数 : 一个函数在内部调用自身本身
#n! = n * fact(n-1)
def fact(n):
    if n==1:
        return 1;
    else:
        return n * fact(n-1);
print("n!:",fact(5));
print("n!:",fact(10));
print("n!:",fact(100));