#!/usr/bin/env python3

import pysftp
import getpass

HOSTNAME = 'localhost'
PORT = 22

def sftp_getfiles(username, password, hostname=HOSTNAME,port=PORT):
    with pysftp.Connection(host=hostname, username=username, password=password) as sftp:
        print("Conexión establecida con el servidor ... ")
        # Cambiar a al directorio raiz del servidor remoto
        sftp.cwd('/')
        # Obtener estructura del directorio raiz
        list_directory = sftp.listdir_attr()
        for directory in list_directory:
            print(directory.filename, directory.longname,directory)

# conexión se cierra automaticamente al final del bloque with

if __name__ == '__main__':
	hostname = input("Introduce el nombre del host: ")
	port = input("Introduce el puerto: ")
	username = input("Introduce usuario: ")
	password = getpass.getpass(prompt="Introduce password: ")
	sftp_getfiles(username, password, hostname, port)
