import http.client
connection = http.client.HTTPConnection("www.google.com")
connection.request("GET", "/")
response = connection.getresponse()
print('Respuesta:',response)
print('Estado:', response.status, response.reason)
datos = response.read()
print(datos)

