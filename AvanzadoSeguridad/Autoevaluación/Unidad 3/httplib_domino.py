#!/usr/bin/python3

import http.client
import argparse

parser = argparse.xxx(description='obtener respuesta de un dominio')
    
# argumentos
parser.add_argument("-target", dest="target", help="IP /dominio", required=True)
parsed_args = parser.xxx()

connection = http.xxx.HTTPConnection(parsed_args.target)
connection.xxx("GET", "/")
data = xxx.getresponse()
print (xxx.code)
print (xxx.headers)
texto = xxx.readlines()
print(texto)
