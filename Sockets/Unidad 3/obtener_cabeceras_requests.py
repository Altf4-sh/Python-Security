import requests

response = requests.get("http://www.python.org")

print(response.content)

print("Status code: "+str(response.status_code))

print("Cabeceras de respuesta: ")
for header, value in response.headers.items():
    print(header, '-->', value)
  
print("Cabeceras de la peticion: ")
for header, value in response.request.headers.items():
    print(header, '-->', value)
