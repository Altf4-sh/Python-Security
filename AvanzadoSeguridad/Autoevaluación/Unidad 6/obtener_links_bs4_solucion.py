#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup

class Scraping:
                
    def scrapingLinks(self,url):
            print("Obtener links de la url:"+ url)
        
            try:
                response = requests.get(url)  
                bs = BeautifulSoup(response.text, 'lxml')
             
                links = bs.find_all("a")
    
                print('Links encontrados %s' % len(links))
    
                for link in links:
                    if link['href'].startswith("http") == False:
                        print(url+link['href'])
                    else:
                        print(link['href'])
                    
            except Exception as e:
                    print("Error de conexión en:  " + url)
                    pass
					
if __name__ == "__main__":
	target = "https://www.python.org"
	scraping = Scraping()
	scraping.scrapingLinks(target)
