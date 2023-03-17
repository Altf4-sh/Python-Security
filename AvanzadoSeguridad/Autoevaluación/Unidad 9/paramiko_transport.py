#!/usr/bin/env python3

import paramiko
import getpass

def run_ssh_command(hostname, user, passwd, command):
    transport = paramiko.xxx(hostname)
    try:
        transport.xxx()
    except Exception as exception:
        print(xxx)
    
    try:
        transport.xxx(username=user,password=passwd)
    except Exception as e:
        print(e)
        
    if transport.xxx():
        print(transport.xxx())
        channel = transport.xxx()
        channel.xxx(xxx)
        response = channel.xxx(1024)
        print('Comando %r(%r)-->%s' % (xxx,xxx,xxx))

if __name__ == '__main__':
    hostname = input("Introduce el hostname: ")
    port = input("Introduce el puerto: ")
    username = input("Introduce usuario: ")
    password = getpass.xxx(prompt="Introduce password: ")
    comando = input("Introduce comando: ")
    run_ssh_command(xxx,xxx, xxx, xxx)
