#!/usr/bin/env python3

from ftplib import FTP

ftp_client=FTP('ftp.be.debian.org')
print("Server: ",ftp_client.getwelcome())
print(ftp_client.login())
print("Ficheros y directorios en el directoro raiz:")
ftp_client.dir()

#cambiar directorio
ftp_client.cwd('/pub/linux/kernel')
files=ftp_client.nlst()
files.sort()

print("%d Ficheros en el directorio /pub/linux/kernel:"%len(files))
for file in files:
	print(file)

ftp_client.quit()

