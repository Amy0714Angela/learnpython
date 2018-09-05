# coding=utf-8
import requests;
r = requests.get("http://www.baidu.com");
print(r.status_code);
print(r.text);
print(r.url);
#url传入参数
r_douban = requests.get("http://www.douban.com/search", params={"q": "python", "cat": "1001"})
print(r_douban.status_code);
print(r_douban.text);
print(r_douban.url);
print(r_douban.encoding);
print(r_douban.content);
#json
r_json = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
jsonObj = r_json.json();
print("json ",jsonObj);
#header
r_header = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print("header ",r.text);
#post
r_post = requests.post("")