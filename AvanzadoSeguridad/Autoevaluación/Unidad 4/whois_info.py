#!/usr/bin/python

import requests

def whois(dominio=None):
	try:
		parametros = {'domain': xxx}
		cabeceras = {
                "Host": "api.whoapi.com"
                }
		respuesta = requests.xxx('https://api.whoapi.com/whois/?domain=' + xxx,params=xxx, headers=xxx)
		print(xxx.status_code)
		datos = xxx.text
		return(xxx)
	except Exception as exception:
		print("Error: ",exception)
		
resultado = xxx('python.org')
for xxx, xxx in xxx.items():
    print(str(xxx) + '<--->' + str(xxx))
