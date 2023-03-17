import paramiko

host = 'localhost'
username = 'linux'
password = 'linux'

sshCliente = paramiko.SSHClient()

#La siguiente línea añade la clave del servidor automáticamente al archivo know_hosts
sshCliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print("creando conexión")
    sshCliente.connect(host, username=username, password=password)
    print("conectado")
    stdin,stdout,stderr = sshCliente.exec_command("uname -a")
    for line in stdout.readlines():
        print(line.strip())
except Exception as exception:
    print("Error al conectar: ",exception)
finally:
    print("cerrando conexión")
    sshCliente.close()
