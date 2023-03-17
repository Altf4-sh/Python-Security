#!/usr/bin/python

import requests
import socket
from ipwhois import IPWhois

def whois(dominio=None):
	try:
		parametros = {'domain': '562e6e5f982402da70ff199930fab7dd'}
		cabeceras = {
                "Content-Type": "application/json",
				"Accept":"application/json"
                }
		respuesta = requests.post('https://api.whoapi.com/whois/?domain=' + dominio,params=parametros, headers=cabeceras)
		print(respuesta.status_code)
		datos = respuesta.text
		return(datos)
	except Exception as exception:
		print("Error: ",exception)
		
resultado = whois('python.org')
direccion_ip = socket.gethostbyname('python.org')
whois = IPWhois(direccion_ip).lookup_whois()
for key,value in whois.items():
	print(str(key) + '<--->' + str(value))
