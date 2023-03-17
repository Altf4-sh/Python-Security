#!/usr/bin/env python3

import requests

data_dictionary = {"id": "0123456789"}
headers = {"Content-Type" :"application/json","Accept":"application/json"}
response = requests.xxx("http://httpbin.org/post",data=xxx,headers=xxx)

print("HTTP Status Code: " + str(response.xxx))

if response.xxx == 200:
    print(response.xxx)

    print("Cabeceras de respuesta: ")
  
    print("Cabeceras de la peticion: ")

