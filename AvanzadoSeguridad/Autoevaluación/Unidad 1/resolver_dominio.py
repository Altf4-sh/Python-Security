import socket

dominio = input()

try:
    print("Obtener ip a partir del nombre dominio:")
    ip = socket.xxx(xxx)
    print(ip)
    print("\nObtener host a partir de la direccion ip")
    print(socket.xxx(str(ip)))
    print("\nObtener nombre cualificado de un dominio")
    print(socket.xxx(dominio))

except socket.error as error:
    print (str(error))
    print ("Error de conexion")