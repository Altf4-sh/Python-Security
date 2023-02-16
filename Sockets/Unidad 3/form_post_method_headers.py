#!/usr/bin/env python3

import requests

data_dictionary = {"id": "0123456789"}
headers = {"Content-Type" :"application/json","Accept":"application/json"}
response = requests.post("http://httpbin.org/post",data=data_dictionary,headers=headers)

print("HTTP Status Code: " + str(response.status_code))

if response.status_code == 200:
	print(response.text)
