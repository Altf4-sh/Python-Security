#!/usr/bin/python

import shodan

SHODAN_API_KEY= ""
shodan = shodan.Shodan(SHODAN_API_KEY)

try:
    resultados = shodan.search('apache')
    print("Numero de resultados:",resultados.items())
except Exception as exception:
    print(str(exception))
