import paramiko

host = 'localhost'
username = 'linux'
password = 'linux'
comando ="uname -a"

sshTransport = paramiko.Transport(host)

try:
    print("creando conexión con la clase Transport")
    sshTransport.start_client()
    sshTransport.auth_password(username=username, password=password)
    if sshTransport.is_authenticated():
        print("conectado y autenticado el servidor sssh en el host",host)
        print("conectado y autenticado el servidor sssh en el host",sshTransport.getpeername())
        channel = sshTransport.open_session()
        channel.exec_command(comando)
        respuesta = channel.recv(1024)
        print('Comando %r/(%r)--> %s' %(comando,username,respuesta))
except Exception as exception:
    print("Error al conectar: ",exception)
finally:
    print("cerrando conexión")
    sshTransport.close()
