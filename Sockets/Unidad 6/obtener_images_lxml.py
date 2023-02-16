#!/usr/bin/env python3

import os
import requests
from lxml import xxx

class Scraping:
   		
    def scrapingImages(self,xxx):
        print("Obtener imágenes de la url:"+ xxx)
    
        try:
            response = requests.xxx(xxx)  
            parsed_body = html.xxx(response.xxx)

            # expresion regular para obtener imagenes
            images = parsed_body.xxx(xxx)

            print('Imágenes encontradas %s' % len(images))
    
            #crear directorio para guardar las imagenes
            os.xxx("mkdir imagenes")
    
            for image in xxx:
                if xxx.startswith("http") == False:
                    download = url + "/"+ xxx
                else:
                    download = xxx
                print(download)
                # descargar las imagenes en el directorio creado
                r = requests.xxx(xxx)
                f = open('imagenes/%s' % xxx.split('/')[-1], 'wb')
                f.xxx(r.xxx)
                f.xxx()
                
        except Exception as e:
                print("Error de conexión en: " + url)
                pass
                
					
if __name__ == "__main__":
	target = "https://www.python.org"
	scraping = Scraping()
	scraping.xxx(target)
