#!/usr/bin/env python3

import requests

data_dictionary = {"id": "0123456789"}
headers = {"Content-Type" :"application/json","Accept":"application/json"}
response = requests.post("http://httpbin.org/post",data=data_dictionary,headers=headers)

print("HTTP Status Code: " + str(response.xxx))

if response.status_code == 200:
    print(response.text)

    print("Cabeceras de respuesta: ")
    for header, value in response.headers.items():
        print(header, '-->', value)

    print("Cabeceras de la peticion: ")
    for header, value in response.request.headers.items():
        print(header, '-->', value)
