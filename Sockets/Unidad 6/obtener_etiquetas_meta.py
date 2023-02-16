#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def obtener_etiquetas_meta(url):
    cabecera = {'User-Agent':'Firefox'}
    peticion = requests.get(url=url,headers=cabecera)
    soup = BeautifulSoup(peticion.text,'lxml')
    for v in soup.find_all('meta'):
        print(v)
        if v.get('name') == 'msapplication-tooltip':
            version = v.get('content')
            print(version)

if __name__ == '__main__':
    url = input("Introduzca url:")
    obtener_etiquetas_meta("http://"+url)

