#!/usr/bin/python

import whois
import sys

if len(sys.argv) != 2:
    print("[-] uso python inforamcion_dominio.py <nombre_dominio>")
    sys.exit()

whois = whois.whois(sys.argv[1])
print(whois)
for key,value in whois.items():
    print ("%s : %s \n" %(key,value))
