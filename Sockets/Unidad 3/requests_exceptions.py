import requests

url_ok = "http://www.python.org"
url_error  = "http://www.python.org/incorrecta"
url_exception  = "http://url_not_exists"

headers  = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"

response = requests.get(url_ok,headers=headers)

if response.status_code == 200:
    print(response.content)
else:
    print("Error al conectar %s (%d)" % (url_ok,response.status_code))
    
response = requests.get(url_error,headers=headers)

if response.status_code == 200:
    print(response.content)
else:
    #print(response.raise_for_status())
    print("Error al conectar %s (%d)" % (url_error,response.status_code))
    
try:
    response = requests.get(url_exception,headers=headers)
except Exception as exception:
    
    print("Error al conectar %s (%s)" % (url_exception,exception))
