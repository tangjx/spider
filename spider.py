#from urllib import request
import urllib.request  
import http.cookiejar  
import requests
url="http://news.qq.com" 
#req=request.Request("http://news.qq.com")
#req.add_header("user-agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")
#response=request.urlopen(req)
#print("中文".encode("utf-8").decode())
#print(response.read().decode())


url = 'http://www.baidu.com'  
decodeing="utf-8"
#直接通过url来获取网页数据  
print('第一种')  
response = urllib.request.urlopen(url)  
code = response.getcode()  
html = response.read()  
mystr = html.decode(decodeing)  
response.close()  
print(mystr)  
  
#构建request对象进行网页数据获取  
print('第二种')  
request2 = urllib.request.Request(url)  
request2.add_header('user-agent', 'Mozilla/5.0')  
response2 = urllib.request.urlopen(request2)  
html2 = response2.read()  
mystr2 = html2.decode(decodeing)  
response2.close()  
print(mystr2)  
  
#使用cookies来获取  
print('第三种')  
cj = http.cookiejar.LWPCookieJar()  
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))  
urllib.request.install_opener(opener)  
response3 = urllib.request.urlopen(url)  
print(cj)  
html3 = response3.read()  
mystr3 = html3.decode(decodeing)  
response3.close()  
print(mystr3)  

