import requests,json

response = requests.get("http://httpbin.org/get",timeout=5)

print("Código de estado HTTP: " + str(response.status_code))

print(response.headers)

if response.status_code == 200:
    results = response.json()
    for result in results.items():
        print(result)
    print("Cabeceras de la respuesta: ")
    for header, value in response.headers.items():
        print(header, '-->', value)
    print("Cabeceras de la petición : ")
    for header, value in response.request.headers.items():
        print(header, '-->', value)
    print("Server:" + response.headers['server'])
else:
    print("Error code %s" % response.status_code)
