import paramiko
import socket

host = 'localhost'
usuario = 'usuario'
password = 'password'

try:
    ssh_client = paramiko.SSHClient()
    #mostrar info debug
    paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)
    #añadir la clave del servidor al fichero know_hosts
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    response = ssh_client.connect(host, port = 22, username = usuario, password = password)
    print('conectado con el host en el puerto 22')
    transport = ssh_client.get_transport()
    security_options = transport.get_security_options()
    print(security_options.kex)
    print(security_options.ciphers)
except paramiko.BadAuthenticationType as exception:
    print("BadAuthenticationException:",exception)
except paramiko.SSHException as sshException:
    print("SSHException:",sshException)
except socket.error as  socketError:
    print("socketError:",socketError)
finally:
    print("cerrando connection")
    ssh_client.close()
