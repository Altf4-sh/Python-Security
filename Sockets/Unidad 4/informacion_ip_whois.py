#!/usr/bin/python

import sys
import socket

from ipwhois import IPWhois

if len(sys.argv) != 2:
    print("[-] uso python informacion_ip_whois.py <nombre_dominio>")
    sys.exit()

dominio = sys.argv[1]
direccion_ip = socket.gethostbyname(dominio)
print('Direccion ip:',direccion_ip)

whois = IPWhois(direccion_ip).lookup_whois()
for key,value in whois.items():
    print(key,value)
