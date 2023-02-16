#!/usr/bin/env python3

import os
import xxx
from bs4 import xxx

class Scraping:
                
    def scrapingLinks(self,xxx):
            print("Obtener links de la url:"+ xxx)
        
            try:
                response = requests.xxx(url)  
                bs = xxx(xxx.text, 'lxml')
             
                links = bs.xxx("a")
    
                print('Links encontrados %s' % len(xxx))
    
                for xxx in links:
                    if xxx['href'].startswith("http") == False:
                        print(xxx+xxx['href'])
                    else:
                        print(xxx['href'])
                    
            except Exception as e:
                    print("Error de conexión en:  " + xxx)
                    pass
					
if __name__ == "__main__":
	target = "https://www.python.org"
	scraping = Scraping()
	scraping.xxx(xxx)
