#!/usr/local/bin/python

import geoip2.database
import geoip
import geolite2
import json

direccion_ip = input("Introduce dirección ip:")

reader = geoip2.xxx.xxx(xxx)
respuesta = reader.city(xxx)
print(respuesta)

respuesta = geoip.geolite2.xxx(xxx)

if respuesta is not None:
    print('Pais: ',respuesta.xxx)
    print('Continente: ',respuesta.xxx)
    print('Time zone: ', respuesta.xxx)
    print('Location: ', respuesta.xxx)

reader = geolite2.geolite2.xxx()
respuesta = reader.get(xxx)
print (json.xxx(xxx,indent=4))




