import urllib.request
url = input("Introduce la URL:")
http_response = urllib.request.urlopen(url) # Guardamos la respuesta en un objeto resquest
print('Código de estado: '+ str(http_response.code)) 
if http_response.code == 200: # Obtenemos el estado
    print(http_response.headers)
