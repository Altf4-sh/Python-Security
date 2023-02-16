#!/usr/bin/env python
#--*-- coding:UTF-8 --*--

import socket,sys

host = "domain/ip_address"
port = 9999

host = "www.bing.com"
port = 80

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.settimeout(5)
except socket.error as e:
	print("socket create error: %s" %e)
	sys.exit(1)

try:
	s.connect((host,port)) # Intentamos conectar con los parámtero anteriores, si da error, contemplamos las 3 excepciones.
	print(s)
except socket.timeout as e :
	print("Timeout %s" %e)
	sys.exit(1)
except socket.gaierror as e:
	print("connection error to the server:%s" %e)
	sys.exit(1)
except socket.error as e:
	print("Connection error: %s" %e)
	sys.exit(1)



