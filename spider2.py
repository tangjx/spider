import requests
import os
from bs4 import BeautifulSoup
import json

loginName = ''
password = '03cc9b5e2f274fa0d4c99169c2abf544'
totalPage = 2
localDir = '/data/tmp/'


headers = {  
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
}  
loginUrl = 'http://pp.yanxiu.com/uc/login?loginName=' + loginName + '&password=' + password + '&appKey=f6de93f8-c589-4aa7-9eb1-92f4afb4aea5&keepCookie=0&backUrl=&crossCallback=__jsonp_10000'
url_profile = 'http://i.yanxiu.com/uft/train/index.vm'
session = requests.session()  
req1 = session.get(loginUrl, headers=headers)
#print req1.headers
#print req1.content

url_page = 'http://i.yanxiu.com/user/train/api/personal/homeworkListAjax.tc?limit=20&segment=10&projectid=1639&page='
#homework  detail view addr
viewHomework='http://i.yanxiu.com/user/train/personal/viewHomework.tc?projectid=1639&hwid='


for pageNum in range(1, totalPage + 1):
	
	homeworklistPage = session.get(url_page + str(pageNum), headers=headers).content

	hjson = json.loads(homeworklistPage)

	#print hjson['count']

	#print len(hjson['homework'])

	#print news_titles
	for i in hjson['homework']:
		print i['title']
		print i['createtimeStr']
		targetDir = localDir + i['createtimeStr']
		if(not os.path.exists(targetDir)):
			os.mkdir(targetDir) 
		url = viewHomework + str(i['id'])
		viewHomeworkHtml = session.get(url,headers=headers).content
		soup = BeautifulSoup(viewHomeworkHtml)
		downloadTag = soup.find_all("a", class_="download")
		nameTag = soup.find("span", class_="current-video")
		attachmentUrl = downloadTag[0]['href']
		attachmentFile = requests.get(attachmentUrl) 
		with open(targetDir + "/" + nameTag.contents[0][3:], "wb") as code:
			code.write(attachmentFile.content)
		print "download success" 


