import socket
try:
    s = socket.socket()
    s.bind(("localhost", 1338))
    s.listen(1)
    print(">>> Servidor escuchando puerto 1338...")
    sc, addr = s.accept()

    while 1:
        recibido = sc.recv(4096)
        print("Recibido:", recibido)
        sc.send(recibido)
        if recibido == bytes("quit",'utf-8'):
            break
except Exception:
    print("Se ha forzado la interrupción de una conexión existente por el host remoto.")
finally:
    print(">>> Cerrando conexión servidor.")
    sc.close()
    s.close()
