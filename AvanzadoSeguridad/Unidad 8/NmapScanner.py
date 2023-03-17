#!/usr/bin/env python3

import nmap

class NmapScanner:
     
    def __init__(self):
        self.portScanner = nmap.PortScanner()
    
    def nmapScan(self, host, port):
        try:
            print("Comprobando el puerto "+ port +" en la máquina "+host)
            self.portScanner.scan(host, port)
            
            # Command info
            print("[*] Ejecutando el comando: %s" % self.portScanner.command_line())     
            self.state = self.portScanner[host]['tcp'][int(port)]['state']
            print(" [+] "+ host + " tcp/" + port + " " + self.state)
            print(self.portScanner[host].tcp(int(port)))
            self.server = self.portScanner[host].tcp(int(port))['product']
            self.version = self.portScanner[host].tcp(int(port))['version']
            print(" [+] "+ self.server + " " + self.version + " tcp/" + port)
            
        except Exception as exception:
            print("Error al conectar con " + host + " para escaner de puertos"+str(exception))
        

NmapScanner = NmapScanner()
NmapScanner.nmapScan("45.33.32.156","80")
