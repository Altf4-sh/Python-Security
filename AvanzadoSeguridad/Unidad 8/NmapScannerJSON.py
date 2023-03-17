#!/usr/bin/env python3

import nmap
import json

class NmapScannerJSON:
     
    def __init__(self):
        self.portScanner = nmap.PortScanner()
    
    def nmapScanJSON(self, host, ports):
        try:
            print("Comprobando puertos "+ str(ports) +" en la máquina "+host)
            self.portScanner.scan(host, ports)
            
            # Info del comando ejecutado
            print("[*] Ejecutando el comando: %s" % self.portScanner.command_line())
            
            print(self.portScanner.csv())
            results = {}     
            
            for x in self.portScanner.csv().split("\n")[1:-1]:
                splited_line = x.split(";")
                host = splited_line[0]
                dns = splited_line[1]
                protocolo = splited_line[3]
                puerto = splited_line[4]
                estado = splited_line[6]
                
                results.update({'host': host,'dns': dns,'protocolo': protocolo,'puerto': puerto,'estado': estado})

            # Almacenar info en json
            file_info =  "scan_%s.json" % host
            with open(file_info, "w") as file_json:
                json.dump(results, file_json)
                
            print("[*] El fichero '%s' ha sido generado con los resultados del escaner" % file_info)            
    
        except Exception as exception:
            print("Error al conectar con " + host + " para escaner de puertos"+str(exception))

NmapScannerJSON = NmapScannerJSON()
NmapScannerJSON.nmapScanJSON("45.33.32.156","21,22,23,80")
