from urllib import request
req=request.Request("https://en.wikipedia.org")
req.add_header("user-agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")
response=request.urlopen(req)
print(response.read())
