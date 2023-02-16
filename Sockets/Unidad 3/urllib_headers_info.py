import urllib.request
url = input("Introduce la URL:")
http_response = urllib.request.urlopen(url)
print('Código de estado: '+ str(http_response.code))
if http_response.code == 200:
    print(http_response.info())
