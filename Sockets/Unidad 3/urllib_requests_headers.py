import urllib.request
url = "http://www.python.org"
#https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome
headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
print('User-agent',request.get_header('User-agent'))
if response.code == 200:
    print(response.headers)
