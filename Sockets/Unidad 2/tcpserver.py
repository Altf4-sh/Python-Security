#!/usr/bin/python
# tcpserver.py
import socket

host = 'localhost'
puerto = 1338

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostport = (host, puerto)
s.bind(hostport)
s.listen(10)

print("Servidor tcp escuchando en el puerto", hostport)

while 1:
	cliente,addr = s.accept()
	print("Conexion desde", addr)
	buffer = cliente.recv(1024)
	print("Datos recibidos", buffer)
	if buffer == b"Hola mundo":
		cliente.send(bytes("Servidor recibe Hola Mundo\n",'utf-8'))
	cliente.close()
