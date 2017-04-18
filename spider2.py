import requests
# r=requests.get('http://www.baidu.com')
# print r.status_code
# print r.headers['content-type']
# print r.encoding
# print r.content

headers = {  
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',  
# 'Referer':'https://www.zhihu.com/',  
# 'X-Requested-With': 'XMLHttpRequest',  
# 'Origin':'https://www.zhihu.com'  
}  
url = 'http://pp.yanxiu.com/sso/loginNew.jsp?userid=&appid=1234&password=03cc9b5e2f274fa0d4c99169c2abf544&username=14042796&s=1492442970973&v=1&persistentcookie=false'
  
url_profile = 'http://i.yanxiu.com/uft/train/index.vm'
session = requests.session()  
print session.get(url, headers=headers).content
print session.get(url_profile, headers=headers).content