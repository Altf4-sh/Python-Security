import paramiko

host = 'localhost'
username = 'username'
password = 'password'

sshCliente = paramiko.SSHClient()

#La siguiente línea añade la clave del servidor automáticamente al archivo know_hosts
sshCliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print("creando conexión")
    sshCliente.connect(host, username=username, password=password)
    print("conectado")
except Exception as exception:
    print("Error al conectar: ",exception)
finally:
    print("cerrando conexión")
    sshCliente.close()
