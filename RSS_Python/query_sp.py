#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys,urllib.parse;
import time;
#视频查询接口

#=========  查询某时间段来源是中新网的视频稿件
#http://123.126.59.96/video/883-4/_search?q=(!sp_f139:""+AND+sp_f131:"%E4%B8%AD%E5%9B%BD%E6%96%B0%E9%97%BB%E7%BD%91"+AND+pubtime:%7B%222018-08-29+10%3A32%3A44%22+TO+%222018-08-29+11%3A02%3A44%22%7D)
# &sort=pubtime:desc&from=0&size=200&pretty=true&default_operator=AND&_source=d_id,title,content,sp_f158_1,sp_f139,sp_f131,pubtime,url,sp_f690,keyword

#=========  查询所有时间来源是中新网的视频稿件
#http://123.126.59.96/video/883-4/_search?q=(!sp_f139:""+AND+sp_f131:"%E4%B8%AD%E5%9B%BD%E6%96%B0%E9%97%BB%E7%BD%91")&sort=pubtime:desc
#&from=0&size=200&pretty=true&default_operator=AND&_source=d_id,title,content,sp_f158_1,sp_f139,sp_f131,sp_f123,sp_f690,keyword,pubtime,url
print("python:",sys.version);#3.7.0
print("系统编码:",sys.stdin.encoding);#UTF-8
#查询图集、视频、正文时使用相同es域名
domain = "http://123.126.59.96";

def getquery_sp(channelname='channel',videoType='',start=0,size=200,**pubdatetime): #默认参数channelname/channel/start/size，可变参数fields,关键字参数pubdatetime
    '视频查询es参数函数'
    #默认channel为sp  channel='sp'
    #videoType : sp_f145 是否视频通稿  趣头条只需要短视频
    print("channelname:",channelname);
    print("videoType:",videoType);
    print("start:",start);
    print("size:",size);
    print("pubdatetime:",pubdatetime);
    source = urllib.parse.quote("中国新闻网");
    if videoType!='':
        videoTypeStr = "+AND+sp_f145:\"" + videoType + "\"";
    else:
        videoTypeStr = "";
    if(pubdatetime.get("startpubtime")!=None):
        pubdatetime = "+AND+pubtime:" + urllib.parse.quote(
            "{\"" + pubdatetime.get("startpubtime") + "\" TO \"" + pubdatetime["endpubtime"] + "\"}");
    else:
        #pubdatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());#获取当前格式化时间
        pubdatetime = "";
    #print("pubdatetime:",pubdatetime);

    query = "?q=(!sp_f139:\"\"+AND+sp_f131:\"" + source + "\""  + videoTypeStr + pubdatetime + ")&";
    if(channelname!="id"):
        query = query + "sort=pubtime:desc";
        query = query + "&from=" + str(start);#int 转 str
        query = query + "&size=" + str(size);#int 转 str
        query = query + "&pretty=true&default_operator=AND";
        #           d_id，标题,正文内容,视频大图,flv地址,稿件来源,节目时长,第一大栏目类别,keyword,pubtime,url
        filedStr = "d_id,title,content,sp_f158_1,sp_f139,sp_f131,sp_f123,sp_f690,keyword,pubtime,url";#默认要取的字段
        query = query + "&_source=" + filedStr;
    return query;
def cmdtpCurl(query,dbname,dbtype):
    '通用查询es参数url：视频、图集、正文'
    searchurl = domain + "/" + dbname + "/"+ dbtype + "/_search" + query;
    return searchurl;



#==========================  函数测试  ==================================
#getquery = getquery_sp();#查询来源是中新网的所有视频
#pubdatetimeDic =  {'startpubtime': '2018-08-29 14:02:15', 'endpubtime': '2018-08-29 14:10:48'};
#getquery = getquery_sp(**pubdatetimeDic);#查询来源是中新网、某段时间的视频
#getquery = getquery_sp(videoType="duan");#查询来源是中新网、视频类型为短视频的视频
#getquery = getquery_sp(videoType="duan",**pubdatetimeDic);#查询来源是中新网、视频类型为短视频、某段时间的视频
#searchurl = cmdtpCurl(getquery,"video","883-4");
#print("es查询语句：",searchurl);