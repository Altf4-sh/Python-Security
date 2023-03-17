#!/usr/bin/env python

import shodan
import requests
import socket

"""
Hay algunas modificaciones:

    - La resolución de DNS la he hecho a través del módulo de socekt.
    - He comentado la siguiente línea -> hostIP = api.host(resolved). No es necesaria.
    - He añadido una excepcion para el manejo de errores del socket.
"""

SHODAN_API_KEY= "ydysiK0Jt21OntYOiUuR317dXHB5uI4v" 
api = shodan.Shodan(SHODAN_API_KEY)

dominio = 'www.python.org'

dnsResolve = 'https://api.shodan.io/dns/resolve?hostnames='+dominio+'&key='+SHODAN_API_KEY

try:
    # Primero necesitamos resolver nuestro dominio a una IP
    resolved = socket.gethostbyname(dominio) 
    #hostIP = api.host(resolved)

    # Entonces necesitamos hacer una busqueda de Shodan en esa IP
    host = api.host(resolved)
    print("IP: %s" % host['ip_str'])
    print("Organization: %s" % host.get('org', 'n/a'))
    print("Operating System: %s" % host.get('os', 'n/a'))


    # Imprimir todos los banners
    for item in host['data']:
        print("Port: %s" % item['port'])
        print("Banner: %s" % item['data'])

except socket.herror as error:
     print('Error: %s' %error)        
                
except shodan.APIError as exception:
        print('Error: %s' % exception)
