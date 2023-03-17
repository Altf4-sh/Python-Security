import socket
import sys

# Preguntamos por la IP
ip = input("Introduce IP:")

#Preguntamos por los puertos de inicio y fin
listaPuertos = list(int(num) for num in input("Introduce rango de puertos separados por comas:").strip().split(","))

print ("Escaneando IP {} en los puertos {} : ".format(xxx,xxx))

try:
    for port in xxx:
        s = socket.socket(socket.AF_INET,xxx)
        s.settimeout(5)
        if (s.connect_ex((xxx,xxx))==0):
            try:
                serv = socket.getservbyport(xxx)
            except socket.error:
                error_servidor="not-found"

            print(("El puerto %s:está abierto  Servicio:%s  "%(xxx,xxx)))
        
    print("Scanning Completed")

except KeyboardInterrupt as exception:
	print(exception)
	sys.exit()
