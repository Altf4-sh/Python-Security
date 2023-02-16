#!/usr/bin/env python

import dns
import dns.resolver
import dns.query 
import dns.zone 
import dns.name
import dns.reversename
import sys

if len(sys.argv) != 2:
    print("[-] uso python DNSPythonExample.py <nombre_dominio>")
    sys.exit()

dominio = sys.argv[1]

respuestaRegistroA,respuestaRegistroMX,respuestaRegistroNS,respuestaRegistroTXT=(dns.resolver.query(dominio,'A'),
                          dns.resolver.query(dominio,'MX'),
                          dns.resolver.query(dominio, 'NS'), 
                          dns.resolver.query(dominio, 'TXT'))

print("Servidores de correo")
print("--------------------")
print(respuestaRegistroMX.response.to_text())

print("\nServidores de nombre")
print("--------------------")
print(respuestaRegistroNS.response.to_text())

print("\nDirecciones IPV4")
print("--------------------")
print(respuestaRegistroA.response.to_text())

print("\nRegistros DNS")
print("--------------------")
print(respuestaRegistroTXT.response.to_text())


