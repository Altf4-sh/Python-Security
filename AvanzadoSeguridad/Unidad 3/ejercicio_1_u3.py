
# Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla el número de palabras que contiene.

"""
Escribir una función que recibe por parámetro una url de un fichero de texto y devuelve el número de palabras que contiene.
    Parámetros:
        url: Es una cadena con la url del fichero de texto.
    Devuelve:
        El número de palabras que contiene el fichero de texto dado por la url.

Paso a seguir.

1. importar el módulo requests

2.definir función y realizar la petición con el módulo requests, añadiendo también control de excepciones

3.obtener el número de palabras del contenido de la respuesta

Ejemplo de url con fichero de texto:

https://www.gutenberg.org/cache/epub/2000/pg2000.txt

 """

import requests
import sys

def main():
    try:
        url_fileText = "https://www.gutenberg.org/cache/epub/2000/pg2000.txt"
        response = requests.get(url_fileText)
        print(response.text)
    except Exception as e:
        print("Error al conectar %s (%s)" % (url_fileText,e))


if __name__ == "__main__":
    main()














