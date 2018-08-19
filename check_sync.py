#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("Hello，Python 123！")

# coding=utf-8
import datetime
import subprocess
import os
import time
import requestsPractice
import json
#print(datetime.datetime.now().date());

#print(subprocess);
#print(os);

if True:
    print("true")
else:
    print("false")

# 定义函数
def get_time(str):
    # /usr/bin/curl www.chinanews.com/scroll-news/news1.html | grep 'published at'|head -n1 |awk '{print $4,$5}'
    time1 = "2018"
    if time1 == "":
        print("网络不通")
    # echo "$1 network drop" >>/tmp/err
    else:
        # date +%s -d "2016-08-22 09:32:02"
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    return
# 调用函数
get_time("调用自定义函数!")

postdata = "网络故障"

sendsmsurl="http://gate.cns.com.cn:8090/api/sendsms.php"
headers = {"Content-type": "application/json"}
data= '{"apptype":"cscscs","msgtype":"1","sendto":"17310921023/amy","sendtime":"","content":"test"}'
res = requests.post(sendsmsurl,data=data,headers=headers)##post请求,
print(res.text)

print("ok")