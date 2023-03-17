import requests
from bs4 import BeautifulSoup

def main():
    sitio = "python.org"
    agent = {'User-Agent':'Firefox'}
    response = requests.get("https://viewdns.info/reverseip/?host={}&t=1".format(sitio),headers=agent)
    html = BeautifulSoup(response.text,'html.parser')
    #tabla = html.find_all('table',attrs={'border':'1'})
    #Para cada una de las filas
    for domain in html.find_all("tr"):
        print("Dominio alojado en el mismo servidor: " + str(domain.get_text()))

if __name__ == '__main__':
    main()

