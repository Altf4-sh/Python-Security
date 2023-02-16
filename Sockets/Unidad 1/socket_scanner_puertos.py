# Escaner de puertos con sockets
 
# Importamos modulo socket
from socket import * 
 
# Preguntamos por la IP                
ip = input("Introduce IP : ")
 
# Preguntamos por el puertos          
puerto_inicio = input("Introduce puerto de inicio : ")
puerto_fin = input("Introduce puerto de fin : ")
 
print ("Escaneando IP {} : ".format(ip))
 
#recorrer cada uno de los puertos
for port in range(int(puerto_inicio),int(puerto_fin) + 1):
    print ("Probando puerto {} ...".format(port))
    # Crea el objeto socket
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(5)
 
    # Comprobar conexion e imprimimos si el puerto está abierto
    if(s.connect_ex((ip,port))==0):
        print("El puerto " , port, "está abierto")
 
    # Cierra el socket
    s.close()
 
print("Escaneo finalizado!")