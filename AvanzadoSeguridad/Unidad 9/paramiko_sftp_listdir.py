#!/usr/bin/env python3

import getpass
import paramiko

HOSTNAME = 'localhost'
PORT = 22

def sftp_list_files(username, password, hostname=HOSTNAME,port=PORT):
    ssh_client = paramiko.SSHClient()
    paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname, port, username, password)
    print(ssh_client)
    # Crea un objeto SFTPClient()
    sftp = ssh_client.open_sftp()
    print(sftp)
    # Obtener archivos
    dirlist = sftp.listdir('.')
    print(dirlist)
    ssh_client.close()

if __name__ == '__main__':
	hostname = input("Enter the target hostname: ")
	port = input("Enter the target port: ")
	username = input("Enter your username: ")
	password = getpass.getpass(prompt="Enter your password: ")
	sftp_list_files(username, password, hostname, port)

