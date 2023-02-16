import socket

dominio = input("Ingresa un dominio: ")

try:
    print("Obtener ip a partir del nombre dominio:")
    ip = socket.gethostbyname(dominio)
    print(ip)
    print("\nObtener host a partir de la direccion ip")
    print(socket.gethostbyaddr(str(ip)))
    print("\nObtener nombre cualificado de un dominio")
    print(socket.gethostbyname_ex(dominio))

except socket.error as error:
    print (str(error))
    print ("Error de conexion")