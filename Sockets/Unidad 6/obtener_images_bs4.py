#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup

class Scraping:
   		
    def scrapingImages(self,url):
        print("Obtener imágenes de la url con bs4:"+ url)
    
        try:
            response = requests.get(url)  
            bs = BeautifulSoup(response.text, 'lxml')
            
            images = bs.find_all("img")

            print('Imágenes encontradas %s' % len(images))
    
            #crear directorio para guardar las imagenes
            os.system("mkdir imagenes")
    
            for tagImage in images:
                if tagImage['src'].startswith("http") == False:
                    download = url + tagImage['src']
                else:
                    download = tagImage['src']
                print(download)
                # descargar las imagenes en el directorio creado
                r = requests.get(download)
                f = open('imagenes/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
                
        except Exception as e:
                print("Error de conexión en: " + url)
                pass
                
					
if __name__ == "__main__":
	target = "https://www.python.org"
    #http://www.freeimages.co.uk/galleries/transtech/informationtechnology/index.htm
	scraping = Scraping()
	scraping.scrapingImages(target)
