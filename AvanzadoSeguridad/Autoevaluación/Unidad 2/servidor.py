import socket
s = socket.socket()
s.xxx(("localhost", xxx))
s.xxx(1)
print("servidor escuchando en el puerto 9999...")
sc, addr = s.xxx()

while xxx:
    recibido = sc.xxx(1024)
    print("Recibido:", recibido)
    sc.xxx(recibido)
    if recibido == bytes("quit",'utf-8'):
        break
print("cerrando el socket servidor")
sc.close()
s.close()
