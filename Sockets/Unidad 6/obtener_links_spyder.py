#!/usr/bin/env python3

import requests
import sys
 
from bs4 import BeautifulSoup
 
# Creamos las listas 2 niveles
urls_nivel1 = []
urls_nivel2 = []
 
# Recibimos los argumentos
target_url = sys.argv[1] 
 
# Realizamos una conexión al argumento pasado y además, leemos todo el contenido del código fuente que existe en la página
url = requests.get(target_url).content
# Usamos nuestra librería de bs4 para posteriormente recatar lo que deseamos
soup = BeautifulSoup(url,'lxml')
# Mediante el for y el método de bs4 llamado find_all, recolectamos todas las etiquetas donde existe a href
for line in soup.find_all('a'):
    new_line = line.get('href')
    try: 
       # Si existe en alguna línea del código fuente el http, lo almacenamos en nuestra lista llamada urls
        if new_line[:4] == "http": 
            if target_url in new_line: 
               urls_nivel1.append(str(new_line)) 
        # Si no existe, intentamos combinar nuestro argumento(url de la página) + lo que encontramos
        elif new_line[:1] == "/": 
            try:
                comb_line = target_url+new_line 
                urls_nivel1.append(str(comb_line))  
            except: 
                pass
        # Recorremos lo que hemos guardado anteriormente en nuestra lista(urls).
        print(urls_nivel1)
        for get_this in urls_nivel1: 
           # Como dentro de urls están todos los enlaces, realizamos una conexión a dicha url y leemos el código fuente
            url = requests.get(get_this).content 
            # Usamos nuestra librería de bs4 para posteriormente obtener nuevos enlaces
            soup = BeautifulSoup(url,'lxml') 
            for line in soup.find_all('a'): 
                new_line = line.get('href') 
                try: 
                    if new_line[:4] == "http": 
                        if target_url in new_line:
                            urls_nivel2.append(str(newline)) 
                    elif new_line[:1] == "/": 
                        comb_line = target_url+new_line 
                        urls_nivel2.append(str(comb_line)) 
                except: 
                    pass
                
    except:
       pass

print(urls_nivel2)
