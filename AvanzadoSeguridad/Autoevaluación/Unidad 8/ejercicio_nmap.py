#!/usr/bin/python3

#importar nmap e inicializar portScanner
import xxx                       
nm = nmap.xxx()

#pedimos al usuario el host que vamos a escanear
host_scan = input('Host scan: ')

#ejecutar nmap
portlist="21,22,23,25,80,8080"	
nm.xxx(hosts=xxx, xxx='-n -p'+portlist)

#mostrar comando nmap a ejecutar
print(nm.xxx())
hosts_list = [(i, nm[i]['status']['state']) for i in nm.xxx()]

#tratamiento fichero
archivo = xxx('scan.txt', 'w')
for host, status in xxx:
    print(xxx, xxx)
    xxx.write(host+'\n')

#mostrar estado de cada puerto
array_portlist=xxx.split(',')
for port in xxx:
	state= xxx[host_scan]['tcp'][int(port)]['state']
	print("Port:"+str(xxx)+" "+"State:"+xxx)
	xxx.write("Port:"+str(xxx)+" "+"State:"+xxx+'\n')

#cierre fichero
xxx.close()
