import requests
# r=requests.get('http://www.baidu.com')
# print r.status_code
# print r.headers['content-type']
# print r.encoding
# print r.content
from bs4 import BeautifulSoup

headers = {  
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',  
# 'Referer':'https://www.zhihu.com/',  
# 'X-Requested-With': 'XMLHttpRequest',  
# 'Origin':'https://www.zhihu.com'  
}  
url = 'http://pp.yanxiu.com/sso/loginNew.jsp?userid=&appid=1234&password=03cc9b5e2f274fa0d4c99169c2abf544&username=14042796&s=1492442970973&v=1&persistentcookie=false'
loginUrl = 'http://pp.yanxiu.com/uc/login?loginName=&password=03cc9b5e2f274fa0d4c99169c2abf544&appKey=f6de93f8-c589-4aa7-9eb1-92f4afb4aea5&keepCookie=0&backUrl=&crossCallback=__jsonp_10000'
url_profile = 'http://i.yanxiu.com/uft/train/index.vm'
session = requests.session()  
req1 = session.get(loginUrl, headers=headers)
print req1.headers
print req1.content
url_homeworklist = 'http://i.yanxiu.com/uft/train/homeworklist.vm?projectid=1639&stageid=2181&page=1'
url_jsonHomework = 'http://i.yanxiu.com/user/train/api/personal/homeworkListAjax.tc?page=1&limit=5&segment=10&study=11&themeid=0&stageid=2181&projectid=1639'
homeworklistPage = session.get(url_jsonHomework, headers=headers).content 

soup = BeautifulSoup(homeworklistPage,'lxml')
news_titles = soup.select(".select_list")
print news_titles
for i in news_titles:
	print i.get_text()
