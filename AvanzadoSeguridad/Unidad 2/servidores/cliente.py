import socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 1338))
    while 1:
        mensaje = input("> ")
        s.send(bytes(mensaje.encode('utf-8')))
        if mensaje == "quit":
            break
except socket.error:
    print(">>> Error al conectar con el servidor!")
finally:
    print(">>> Cerrando conexión cliente. ")
    s.close()