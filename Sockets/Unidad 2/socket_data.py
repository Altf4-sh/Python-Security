#!/usr/bin/python
#-*- coding: utf-8 -*-

import socket

print('Creando socket ...')
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Creamos el socket pasandole los pararametros INET -> ipv4 y STREAM -> TCP
print('socket creado')

# Indicamos en dos variables el host y el puerto a donde queremos hacer la peticion.
target_host = "www.google.es" 
target_port = 80

print("Conexion con el host remoto")
s.connect((target_host,target_port)) # Usamos el metodo connect pasandole las variables anteriores, Host y port.
print('connection ok')

# Como respuesta, le pedimos una peticion GET con el protocolo v1.1 del HTTP y le concatenamos el Host al final.
request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
s.send(request.encode())  # Usamos send para enviar la peticion y encode para que el servidor pueda entender la peticion.

data=s.recv(4096) # Esta es la cantidad de bytes que vamos a leer de la respuesta.
print("Datos",repr(data))   # Imprimimos datos de respuesta.
print("Longitud",len(data)) # Imprimimos longitud de respuesta.

print('Cerrando el socket') # Por ultimo cerramos la conecxion.
s.close()
