"""Implementar un cliente TCP con el módulo socket que se conecte a un host y un puerto introducidos por el usuario desde la consola."""

import socket

print("**** CREANDO SOCKET **** \n")
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Creamos el socket pasandole los pararametros INET -> ipv4 y STREAM -> TCP
print(" >>> Socket creado correctamente \n")

# Indicamos en dos variables el host y el puerto a donde queremos hacer la peticion.
target_host = input("DIRECCION: ") 
target_port = int(input("PUERTO: "))
print("\n")

print("**** ESTABLECIENDO CONECXION HOST REMOTO ****")
s.connect((target_host,target_port)) # Usamos el metodo connect pasandole las variables anteriores, Host y port.
print(" >>> Connection OK \n")

# Como respuesta, le pedimos una peticion GET con el protocolo v1.1 del HTTP y le concatenamos el Host al final.
request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
s.send(request.encode())  # Usamos send para enviar la peticion y encode para que el servidor pueda entender la peticion.

data=s.recv(4096) # Esta es la cantidad de bytes que vamos a leer de la respuesta.
print("DATOS: ",repr(data))   # Imprimimos datos de respuesta.
print("LONGITUD: ",len(data)) # Imprimimos longitud de respuesta.

print("**** CERRANDO CONEXION **** \n") # Por ultimo cerramos la conecxion.
s.close()
print(" >>> Connection CLOSE")