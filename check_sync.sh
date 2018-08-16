#!/bin/bash


### get the difference of two numbers ###
my_diff(){
    d=$[$1-$2]
    echo $d
}

### get published time ###
get_time(){
    #/usr/bin/curl www.chinanews.com/scroll-news/news1.html | grep 'published at'|head -n1 |awk '{print $4,$5}'
    time=`/usr/bin/curl $1 2> /dev/null |grep 'published at'|head -n1 |awk '{print $4,$5}'`
    if [ "$time" == "" ];then
       echo "$1 网络不通" >>/tmp/err
	   #echo "$1 network drop" >>/tmp/err
    else
       #date +%s -d "2016-08-22 09:32:02"
       date +%s -d "$time"
    fi
}


#mob=mob.cns.hk

#美国207.254.179.52
ny=ny.cns.hk

#sj=sj.cns.hk
#dxt=dxt.cns.hk

#香港192.254.93.52
hk=hk.cns.hk

#皂君庙61.135.137.62【20161215暂时去掉】
zjm=backend.chinanews.com

#酒仙桥58.68.149.52
jxq=www.chinanews.com


n_url=http://pub.cns.com.cn:8080/document/Np_CnNew/default/scroll-news/news1.html
#s_url=http://pub.cns.com.cn:8080/document/video/default/shipin/scroll/index.shtml


k2="iiwoai@126.com"
zy1="5841497@qq.com"
zy2="zhengziyu@chinanews.com.cn"
zqian1="racat@139.com"
zqian2="zhaoqian@chinanews.com.cn"


sendsmsurl="http://gate.cns.com.cn:8090/api/sendsms.php"





#t是存放邮件信息的，比如
#hk.cns.hk/scroll-news/news1.html update delayed 121s
#ny.cns.hk/scroll-news/news1.html update delayed 240s
#mail from  61.135.142.211 
t="/usr/local/nagios/libexec/tt.txt"

#mfile是存放延迟站点的域名的比如
#hk
#ny
mfile="/usr/local/nagios/libexec/t1.txt"

[ -f $t ] || touch $t
>$t
>$mfile
for url  in $n_url  ;do
    
    for i in  $jxq $zjm $hk $ny;do
        if [ $url == "$n_url" ];then
            Curl=$i"/scroll-news/news1.html"
	    e="news"
        elsegate.cns.com.cn
            Curl=$i"/shipin/scroll/index.shtml"
            e="shipin"
        fi
        >/tmp/err
        
	echo ""  
	ctime=`get_time $Curl`
	echo $Curl
	echo $ctime

        ttime=`get_time $url`
	echo $url
	echo $ttime
	

        n=`wc -l /tmp/err|awk '{print $1}'`
	#-gt 大于,如:if [ "$a" -gt "$b" ]   
	#网络异常取不到文件的时间戳
        if [ $n -gt "0" ] ; then
            cat /tmp/err >>$t
        mail_title=" $e network drop"
        else
            ctm=`my_diff $ttime $ctime`
	    echo "delay"${ctm}"s"
	    #延迟大于20分钟报警
            if [ $ctm -ge "1200" ]; then
                #echo $Curl" update delayed $ctm""s"  >>$t   
				#echo $Curl" renew delayed $ctm""s"  >>$t
				echo $Curl" 更新延迟" $ctm"s"  >>$t
                #echo $Curl" update delayed $ctm""s"
				#echo $Curl" renew delayed $ctm""s"
				echo $Curl" 更新延迟" $ctm"s"  				
                echo "$i"|awk -F'.' '{print $1}' >>$mfile
                echo "$i"|awk -F'.' '{print $1}' 
                mail_title="`cat $mfile |xargs ` $e update delayed"
            fi
        fi
        >/tmp/err
    done
    #cat $t
    a=`cat $t|wc -l`
    if [ $a -gt 0 ];then
	#echo "" >>$t
	echo "报警来自 61.135.137.211 " >>$t
	#echo "mail from  61.135.137.211 " >>$t
        #mail_title="`cat $mfile |xargs ` $e update delayed"
        #20160822不再发邮件改成发短信
	#/bin/mail -s "$mail_title" $zy1 $zy2 $k2 $zqian1 $zqian2 <$t
	echo "send warn message..."
	#post json
	postdata=""
	for line in `cat $t`
	do
	#echo $line
	postdata=${postdata}" "${line}
	done
	echo $postdata
        curl -H "Content-type: application/json" -X POST -d "{\"apptype\":\"PV\",\"msgtype\":\"1\",\"sendto\":\"13611046415/zhaoqian,17310921023/limin,17703175720/yanzhaoyu,13810157572/wangwenzheng,18515099200/yangwenjie,15652615322/rendi\",\"content\":\"$postdata\"}" $sendsmsurl
        #>$t
        #>$mfile
	
    fi
date
echo '---------------'
done

