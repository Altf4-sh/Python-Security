#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup
import sys

if len(sys.argv) !=2:
    print("uso: %s dominio" % (sys.argv[0]))
    sys.exit(0)

urls = []
dominio = sys.argv[1]

#busca los comentarios HTML en el dominio
respuesta = requests.get(dominio)
comentarios = re.compile('<!--(.*)-->',respuesta.text)

print("Comentarios en el dominio: "+dominio)

for comentario in comentarios:
    print(comentario)

#utilizamos Beautifulsoup para obtener el código html para cualquier enlace que encontramos a partir del dominio principal
#ya sea mediante enlaces absolutos (comenzando con http) y relativos (comenzando con /)

soup = BeautifulSoup(respuesta.text,"lxml")
#obtener enlaces
for link in soup.find_all('a'):
    enlace = link.get('href')
    try:
        if enlace[:4] == "http" and dominio in urls:
            urls.append(str(enlace))
        elif enlace[:1] == "/":
            urls.append(str(dominio+enlace))
    except Exception as exception:
        pass
        print("Exception",exception)

#Por cada enlace obtenido desde la página principal buscamos comentarios HTML en cada página.
for url in urls:
    print("Comentarios en la página: "+url)
    respuesta = requests.get(url)
    comentarios = re.compile('<!--(.*)-->',respuesta.text)
    for comentario in comentarios:
        print(comentario)
