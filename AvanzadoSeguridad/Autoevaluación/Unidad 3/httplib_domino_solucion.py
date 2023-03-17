#!/usr/bin/python3

import http.client
import argparse

parser = argparse.ArgumentParser(description='obtener respuesta de un dominio')
    
# argumentos
parser.add_argument("-target", dest="target", help="IP /dominio", required=True)
parsed_args = parser.parse_args()

connection = http.client.HTTPConnection(parsed_args.target)
connection.request("GET", "/")
data = connection.getresponse()
print (data.headers)
texto = data.readlines()
print(texto)
