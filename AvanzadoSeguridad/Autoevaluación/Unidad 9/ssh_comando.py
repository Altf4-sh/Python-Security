import paramiko

def ssh_comando(ip, user, passwd, comando):
    client = paramiko.xxx()
    #Se puede registrar en un fichero de log todas las conexiones que se produzcan.
    paramiko.util.xxx('paramiko.log')
    #Cargar las claves almacenadas del sistema
    client.xxx()
    client.xxx(paramiko.xxx())
    client.connect(ip, username=xxx, password=xxx)
    ssh_session = client.xxx().xxx()
    if xxx.active:
        ssh_session.xxx(comando)
        print(ssh_session.xxx(1024))
        client.close()

ssh_comando('localhost', 'usuario', 'password','ls -la')
