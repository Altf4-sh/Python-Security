#!/usr/local/bin/python

import geoip2.database
import geoip
import geolite2
import json

direccion_ip = input("Introduce dirección ip:")

reader = geoip2.database.Reader('GeoLite2-City.mmdb')
respuesta = reader.city(direccion_ip)
print(respuesta)

respuesta = geoip.geolite2.lookup(direccion_ip)

if respuesta is not None:
    print('Pais: ',respuesta.country)
    print('Continente: ',respuesta.continent)
    print('Time zone: ', respuesta.timezone)
    print('Location: ', respuesta.location)

reader = geolite2.geolite2.reader()
respuesta = reader.get(direccion_ip)
print (json.dumps(respuesta,indent=4))




