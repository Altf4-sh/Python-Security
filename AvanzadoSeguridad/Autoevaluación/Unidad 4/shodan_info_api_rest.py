#!/usr/bin/env python

import shodan
import requests

SHODAN_API_KEY= "xxx"
api = shodan.xxx(SHODAN_API_KEY)

dominio = 'www.python.org'

dnsResolve = 'https://api.shodan.io/dns/resolve?hostnames=' + xxx + '&key=' + xxx


try:
    # Primero necesitamos resolver nuestro dominio a una IP
    resolved = requests.get(xxx)
    hostIP = xxx.xxx()[xxx]
   

    # Entonces necesitamos hacer una busqueda de Shodan en esa IP
    host = api.xxx(xxx)
    print("IP: %s" % xxx['ip_str'])
    print("Organization: %s" % xxx.get('org', 'n/a'))
    print("Operating System: %s" % xxx.get('os', 'n/a'))


    # Imprimir todos los banners
    for item in xxx['data']:
        print("Port: %s" % xxx['port'])
        print("Banner: %s" % xxx['data'])
        
                
except shodan.APIError as exception:
        print('Error: %s' % exception)
