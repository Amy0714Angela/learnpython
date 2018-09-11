#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#一点资讯  python实现方法

import sys,os,json;
import requests;
import memcache;
#导入query_sp，使用其中的函数
import query_sp;
import re;#正则表达式
from __init__ import getRootPath;#获取项目根目录

# 项目根目录
getProjectPath = getRootPath();
#==========================一、获取上传接口access_token==============================
#mc = memcache.Client();#missing 1 required positional argument: 'servers'
mc = memcache.Client(['127.0.0.1:11211'], debug=True);#连接memcache服务器
mebkey1 = "##YIDIANZIXUNTOKEN##";
token = mc.get(mebkey1);
if token == None:
    client_id = "734809";
    client_secret = "mRRKQcNXXtAj4NDiFDkgCg";
    url = "https://open-mp.yidianzixun.com/apis/auth/token";
    r = requests.get(url, params = {"grant_type": "client_credentials", "client_id":client_id, "client_secret" : client_secret});
    print("返回值json形式:",r.json());
    rJson = r.json();
    if('access_token' in rJson and 'expires_in' in rJson):#dic类型判断是否存在某属性方法一
        expires_in = r.json().get("expires_in");  # dic类型获取属性方法一  get("属性名");
        access_token = r.json()['access_token'];  # dic类型获取属性方法二 dic["属性名"]
        mc.set(mebkey1, access_token,7200);  # 保存7200s two hours
        token = mc.get(mebkey1);
        print("if token:", token);
    elif rJson.get("error_description") != None and rJson.get("error") != None: #dic类型判断是否存在某属性方法二
        print("请求token有误，",rJson.get("error_description"));
    else:
        print("请求token发生未知错误");
print("token:",token);
#mc.delete(mebkey1);#删除
#==========================二、获取es数据，请求地址如下：==============================
#http://123.126.59.96/video/883-4/_search?q=(!sp_f139:""+AND+sp_f131:"%E4%B8%AD%E5%9B%BD%E6%96%B0%E9%97%BB%E7%BD%91")&sort=pubtime:desc
#&from=0&size=200&pretty=true&default_operator=AND&_source=d_id,title,content,sp_f158_1,sp_f139,sp_f131,sp_f123,sp_f690,keyword,pubtime,url
getquery = query_sp.getquery_sp(start=475,size=1);
searchurl = query_sp.cmdtpCurl(getquery,'video','883-4');
print("查询es地址：",searchurl);
results = requests.get(searchurl);
data = results.json().get("hits").get("hits");
print("查询es获取的数据：",data);
print("判断数据类型：",isinstance(data,list));#True

#下一行代码去重后不能保证原有数据顺序
#data = [dict(t) for t in set([tuple(item.get('_source').items()) for item in data])];
#可使用下几行代码去重后可保证原有数据顺序
seen = set();
newData = [];
for item in data:
    #print("item类型:", isinstance(item,dict));#True
    _source = item.get('_source').items();
    # {'sp_f139': 'http://video.chinanews.com/flv/2018/08/25/400/100931_web.mp4', 'pubtime': '2018-08-26 08:55:25', 'd_id': 783219, 'sp_f158_1': 'http://i2.chinanews.com/simg/reportmanuscript/2018/08-25/100931_big.jpg', 'sp_f123': '', 'title': '周恩来与杭州纪念展杭州开幕 百余张照片追忆周总理往事', 'keyword': '周恩来 杭州 纪念展', 'sp_f690': 'gn', 'content': '<p>\u3000\u3000【解说】当地时间8月25日，“周恩来与杭州”纪念展在浙江杭州开幕。2018年是纪念周总理诞辰120周年，该展览通过100余张周恩来总理在杭州各个时期留下的珍贵照片以及照片背后的故事，全景呈现了周恩来总理在杭州的岁月往事。</p>\r\n\r\n<p>\u3000\u3000周总理生前曾来杭州30余次，本次展览通过多个板块，挖掘老照片背后的故事。许多杭州市民自发来到现场，值得一提的是几位曾和周总理同框过的人也来到了现场，沈云官曾是杭州都锦生丝织厂的一名普通工人，据她回忆1957年周总理来都锦生参观，她有幸与周总理握手、交谈，这些场景她至今还历历在目，她告诉记者，作为一名普通老百姓能够见到周总理是她一生的幸福。 【同期】(杭州市民 沈云官) 1957年，我还是个小姑娘，周总理到车间里来参观，走到我的面前指着我的手提问了，我在很顺利的操作机器，很礼貌的和他握手、谈话。心里很感动，我是一个普通的老百姓，能够见到周总理应该是我一生的幸福。</p>\r\n\r\n<p>\u3000\u3000【解说】活动当天，周恩来侄女周秉德和周秉宜也来到了现场，除了参观照片展外，周秉宜还为前来参观的市民讲述了自己1949年至1968年期间与周恩来、邓颖超一起生活，从小受他们的言传身教，带大家一起领略周总理高尚的人格品质与精神内涵。</p>\r\n\r\n<p>\u3000\u3000【同期】(中国新闻社原副社长、周恩来侄女、大鸾翔宇慈善基金会创始会长 周秉德)</p>\r\n\r\n<p>\u3000\u3000得到了很多人的支持，有些原来在镜框里的人(照片)送过来，人也来了，就说明所有的老百姓真是对总理非常有感情的，我也是非常感动的，总理的精神总是永远活在人民的心中。</p>\r\n\r\n<p>\u3000\u3000【解说】据了解，本次展览将持续到9月2日。此次展览由中国新闻社浙江分社、中共浙江省委党史研究室、中共杭州市纪委、中共杭州市委宣传部、中共杭州市委党史研究室、浙江图书馆共同举办。</p>\r\n\r\n<p>\u3000\u3000记者沈亦山 胡徐峰 杭州报道</p>\r\n', 'url': 'http://www.chinanews.com/shipin/cns/2018/08-26/news783219.shtml', 'sp_f131': '中国新闻网'}
    #print("_source:", _source);
    t = tuple(_source);
    # ('sp_f139', 'pubtime', 'd_id', 'sp_f158_1', 'sp_f123', 'title', 'keyword', 'sp_f690', 'content', 'url', 'sp_f131')
    #print("将字典列表转成元组列表:",t);
    if t not in seen:
        seen.add(t);
        newData.append(item);
#print("seen：",seen);
#print("去重后数据：",newData);
for index,item in enumerate(newData):
    if(index >1):
        break;
    #itemInfo = item["_source"];# list类型，其中每一项为dict类型
    #print("元素信息:",item);
    # ==========================  三、获取上传接口token  ==============================
    #1、上传视频文件前需先获取文件上传文件接口的信息
    getUploadInterfaceUrl = "https://open-mp.yidianzixun.com/apis/video/get_secretkey";
    _sourceList = item.get('_source');
    d_id = _sourceList['d_id'];#d_id
    title = _sourceList['title'];  # title
    print("视频标题：", title);
    catagory = _sourceList['sp_f690'];  # catagory
    videoPic = _sourceList['sp_f158_1'];#视频缩略图
    print("视频缩略图地址：",videoPic);
    videoUrl = _sourceList.get("sp_f139");#视频地址
    print("视频地址：", videoUrl);
    pubdate = _sourceList.get("pubtime").split(" ")[0].replace("-","");
    # 将正则表达式编译成Pattern对象
    pattern_video = re.compile("http(s)?:\/\/(.+)\.(mp4|mkv|flv|f4v|swf|wmv|avi|mov|rmvb|3gp|vob)$", re.I);#re.I : re.IGNORECASE
    # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
    match_video = pattern_video.match(videoUrl);
    print("match:",match_video);
    if match_video:
        print("filename:", videoUrl);
        print("access_token:", token);
        getUploadInterfaceInfo = requests.get(getUploadInterfaceUrl, params = {"filename":videoUrl, "access_token":token});
        getUploadInterfaceInfoJson = getUploadInterfaceInfo.json();
        print("getUploadInterfaceInfo:", getUploadInterfaceInfoJson);
        if 'status' in getUploadInterfaceInfoJson:
            uploadInterStatus = getUploadInterfaceInfoJson['status'];
            if uploadInterStatus == 'success':
                videoYiDianUrl = getUploadInterfaceInfoJson['url'];
                authorization = getUploadInterfaceInfoJson['Authorization'];
                contentType = getUploadInterfaceInfoJson['Content-Type'];
                date = getUploadInterfaceInfoJson['Date'];
            else:
                print("获取文件上传文件接口信息失败：","返回值中status不为success" ,getUploadInterfaceInfoJson.json());
                break;
        else:
            # {'error_code': 2, 'status': 'failed'}
            print("获取文件上传文件接口信息失败：","返回值中status为failed",getUploadInterfaceInfoJson.json());
            break;
    else:
        print("id为 %s 的稿件，视频格式不匹配" % d_id);
        break;
    print("videoYiDianUrl:",videoYiDianUrl);
    print("date:",date);
    # ==========================  四、上传视频文件 ==============================
    ########   下载视频文件至本地 ######
    # 创建存在图片的文件夹，所有图片放至videoDownloaded
    # 在项目根目录下创建picsDownloaded
    videoFilename = videoYiDianUrl.split("/")[-1];
    print("生成视频文件路径videoFilename：", videoFilename);
    videoOuterDir = getProjectPath + "/videoDownloaded";
    os.makedirs(videoOuterDir,exist_ok=True);
    # 在videoDownloaded下根据日期创建文件夹
    videosPubdateDir = os.path.join(videoOuterDir,pubdate);#兼容各系统
    os.makedirs(videosPubdateDir,exist_ok=True);
    # 请求远程视频
    #downloadVideoRes = requests.get(videoYiDianUrl);
    #print("下载视频是否成功status_code：", downloadVideoRes.status_code); #404
    downloadVideoRes = requests.get(videoUrl);#下载从es中查出的视频，而非上传到一点资讯后生成的新视频（生成的新视频不能访问）
    #videoCon = downloadVideoRes.content;
    if downloadVideoRes.status_code == 200:
        videoCon = downloadVideoRes.content;
        videoPath = videosPubdateDir + "/" + videoFilename;
        print("生成视频文件路径videPath：", videoPath);
        with open(videoPath,'wb') as writeVideo:
            writeVideo.write(videoCon);
    else:
        print("下载远程视频失败：", downloadVideoRes.status_code);
        break;
    headers = {};
    headers['Date'] = date;
    headers['Content-Type'] = contentType;
    headers['Authorization'] = authorization;
    video_file = open(videoPath, 'rb');
    req = requests.put(videoYiDianUrl, data=video_file, headers=headers);
    print("上传视频接口返回值：",req.status_code);  # req.status_code==200 表示上传成功
    if(req.status_code == 200):
        print("视频文档id为 %s ,视频上传成功" % d_id);
    else:
        print("视频文档id为 %s ,视频上传失败" % d_id);
        break;
    # ==========================  五、上传封面图 ================================
    #videoPic = "https://www.apowersoft.cn/wp-content/uploads/2017/09/combine-gifs-5.gif";
    #图片文件名
    filename = videoPic .split("/")[-1];
    # 将正则表达式编译成Pattern对象
    pattern_pic = re.compile("(.+)\.(jpeg|png|jpg)$", re.I);  # re.I : re.IGNORECASE
    # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
    match_pic = pattern_pic.match(videoPic);
    print("匹配图片格式成功：",match_pic);
    if match_pic:
        #videoPic = "https://www.apowersoft.cn/wp-content/uploads/2017/09/combine-gifs-5.gif";
        # 2、视频封面图上传接口
        postVideoThumbUrl = "https://open-mp.yidianzixun.com/apis/video/upload_picture?access_token=" + token;
        postVideoThumb_thumb = {"access_token": token};
        ###### 下载文件到本地  ######
        # 创建存在图片的文件夹，所有图片放至picsDownloaded
        # 在项目根目录下创建picsDownloaded
        picsOuterDir = getProjectPath + "/picsDownloaded";
        os.makedirs(picsOuterDir, exist_ok=True);
        # 在picsDownloaded下根据日期创建文件夹
        picPubdateDir = os.path.join(picsOuterDir, pubdate);
        os.makedirs(picPubdateDir, exist_ok=True);
        # 请求远程图片
        downloadPicRes = requests.get(videoPic);
        if downloadPicRes.status_code == 200:
            picCon = downloadPicRes.content;
            picPath = picPubdateDir + "/" + filename;
            # 将远程文件写入本地文件夹
            with open(picPath, 'wb') as fileWrite:
                fileWrite.write(picCon);
            pic_file = {'pic': (videoPic, open(picPath, 'rb'))};
            # pic_file = {'pic': (videoPic, open(pubdateDir + "/" + filename, 'rb'))};
            print("pic_file:", pic_file);
        else:
            print("下载视频缩略图失败:", downloadPicRes);
            break;

        getVideoPicRes = requests.post(postVideoThumbUrl, files=pic_file).json();
        print("getVideoPicRes:", getVideoPicRes);#{"status":"success","url":"http:\\/\\/si1.go2yd.com\\/get-image\\/0QFgFRfMPSK","format":"JPEG"}
        print("判断返回值是否有status","status" in getVideoPicRes);
        if 'status' in getVideoPicRes:
            uploadPicStatus = getVideoPicRes.get("status");
            if uploadPicStatus == 'success':
                uploadPicUrl = getVideoPicRes.get("url");
                print("上传后图片链接success：", uploadPicUrl);
            else:
                # b'{"error":"pic ext invalid","error_description":"pic ext only support: Set(jpeg, png, jpg)"}'
                print("视频封面图上传接口：","返回值中status值为failed",getVideoPicRes.json());
                break;
        else:
            print("视频封面图上传接口：","返回值没有status", getVideoPicRes.json());
            break;
    else:
        print("id为 %s 的稿件，图片格式不匹配，格式为%s" % (d_id,filename.split(".")[-1]));
        break;

    print("上传视频缩略图后返回的图片链接：",uploadPicUrl);
    # ==========================  六、发布视频信息 ================================
    # 视频频道列表（新增 新视野）
    spChannelNameList = ["国际新闻", "文娱前线", "中新访谈", "体育", "微视界","新视野","社会", "国内", "财经", "军事", "热点新闻", "港澳台侨"];
    spChannelList = ["gj", "wy", "ft", "tt", "wsj","xsy", "sh", "gn", "cj", "jq", "rd", "ga"];
    channelNameYidianzixun = ["国际","娱乐","社会","体育","社会","社会","社会","社会","财经","军事","社会","社会"];
    print("频道名称：",catagory);
    #转换为一点资讯频道名称
    for index,catName in enumerate(spChannelList):
        if catName == catagory:
            channelName = channelNameYidianzixun[index];
        else:
            channelName = "社会";
    print("转换为一点资讯后频道名称：",channelName);
    uploadVideoUrl = "https://open-mp.yidianzixun.com/apis/video/post_video_info?access_token=" + token;
    headers = {"Content-Type": "application/json"};
    body = {
        "video_url": videoYiDianUrl,
        "title": title,
        "cate_b": channelName,
        "cate_a": channelName,
        "poster_url": uploadPicUrl,
    }
    res = requests.post(uploadVideoUrl, data=json.dumps(body), headers=headers).json();
    print("发布视频信息返回值：",res);
    #{"status": "success", "code": 0}
    if 'status' in res:
        if res["status"] == 'success':
            print("发布视频信息成功");
        else:
            print("id为 %s 的稿件，发布视频信息失败" % d_id);
            break;
    else:
        print("id为 %s 的稿件，发布视频信息失败:%s" % (d_id,res));
        break;




