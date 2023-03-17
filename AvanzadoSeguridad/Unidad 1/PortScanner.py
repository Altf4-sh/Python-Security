import socket
import sys

# Preguntamos por la IP
ip = input("Introduce IP:")

#Preguntamos por los puertos de inicio y fin
listaPuertos = list(int(num) for num in input("Introduce rango de puertos separados por comas:").strip().split(","))

print ("Escaneando IP {} en los puertos {} : ".format(ip,listaPuertos))

try:
    for port in listaPuertos:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(5)
        if (s.connect_ex((ip,port))==0):
            try:
                serv = socket.getservbyport(port)
            except socket.error:
                error_servidor="not-found"

            print(("El puerto %s:está abierto  Servicio:%s  "%(port,serv)))
        
    print("Scanning Completed")

except KeyboardInterrupt as exception:
	print(exception)
	sys.exit()
