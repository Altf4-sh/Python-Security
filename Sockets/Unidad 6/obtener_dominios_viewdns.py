import requests
from bs4 import xxx

def main():
    sitio = "python.org"
    agent = {'User-Agent':'Firefox'}
    response = requests.get("https://viewdns.info/reverseip/?host={}&t=1".format(xxx),headers=xxx)
    html = xxx(response.xxx,'html.parser')
    tabla = html.xxx('table',attrs={'border':'1'})
    #Para cada una de las filas
    for xxx in tabla.xxx("tr"):
        print("Dominio alojado en el mismo servidor: " + xxx.xxx.xxx)

if __name__ == '__main__':
    main()

