import requests

ip = input("Introduce direccion ip:")

url = "https://freegeoip.app/json/"+ip

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

respuesta = requests.request("GET", url, headers=headers)

print(respuesta.json())
