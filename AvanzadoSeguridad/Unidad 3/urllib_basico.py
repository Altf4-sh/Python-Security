import urllib.request

#peticion get
try:
    response = urllib.request.urlopen("http://www.python.orgg")
    print(response.read().decode('utf-8'))
    response.close()
except Exception as error:
    print("Ocurrió un error",error)
except HTTPError as error:
    print("Ocurrió un error",error)
except URLError as error:
    print("Ocurrió un error",error)
