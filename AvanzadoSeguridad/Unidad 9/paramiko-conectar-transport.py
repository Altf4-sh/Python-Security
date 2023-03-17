import paramiko

host = 'localhost'
username = 'linux'
password = 'linux'

sshTransport = paramiko.Transport(host)

try:
    print("creando conexión con la clase Transport")
    sshTransport.start_client()
    sshTransport.auth_password(username=username, password=password)
    if sshTransport.is_authenticated():
        print("conectado y autenticado el servidor sssh en el host",host)
except Exception as exception:
    print("Error al conectar: ",exception)
finally:
    print("cerrando conexión")
    sshTransport.close()
