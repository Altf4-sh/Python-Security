#!/usr/bin/env python3

import nmap
import argparse

def callbackFTP(host, result):
    try:
        script = result['scan'][xxx]['tcp'][21]['script']
        print("Command line"+ xxx['nmap']['command_line'])
        for key, value in script.xxx():
            print('Script {0} --> {1}'.format(xxx, xxx))
    except KeyError:
        pass
        

class NmapScannerAsyncFTP:
    def __init__(self):
        self.portScanner = nmap.xxx()
        self.portScannerAsync = nmap.xxx()

    def scanning(self):
        while self.xxx.xxx():
            print("Scanning >>>")
            self.xxx.xxx(10)    

    def nmapScanAsync(self, hostname, port):
        try:
            print("Checking port "+ port +" ..........")
            self.portScanner.xxx(xxx, xxx)
            self.state = self.xxx[hostname]['tcp'][int(port)]['state']
            print(" [+] "+ hostname + " tcp/" + port + " " + self.state)
            #checking FTP service
            if (port=='21') and self.xxx[hostname]['tcp'][int(port)]['state']=='open':
                print('Checking ftp port with nmap scripts......')
                print('Checking ftp-anon.nse .....')
                self.xxx.xxx(hostname,arguments="-A -sV -p21 --script ftp-anon.nse",callback=xxx)
                self.scanning()
                print('Checking ftp-bounce.nse  .....')
                self.xxx.xxx(hostname,arguments="-A -sV -p21 --script ftp-bounce.nse",callback=xxx)
                self.scanning()
                print('Checking ftp-libopie.nse  .....')
                self.xxx.xxx(hostname,arguments="-A -sV -p21 --script ftp-libopie.nse",callback=xxx)
                self.scanning()
                print('Checking ftp-proftpd-backdoor.nse  .....')
                self.xxx.xxx(hostname,arguments="-A -sV -p21 --script ftp-proftpd-backdoor.nse",callback=xxx)
                self.scanning()
                print('Checking ftp-vsftpd-backdoor.nse   .....')
                self.xxx.xxx(hostname,arguments="-A -sV -p21 --script ftp-vsftpd-backdoor.nse",callback=xxx)
                self.scanning()

        except Exception as exception:
            print("Error to connect with " + hostname + " for port scanning",str(exception))
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Nmap scanner async')
    parser.add_argument("--host", dest="host", help="target IP / domain", required=True)
    parser.add_argument("--ports", dest="ports", help="Please, specify the target port(s) separated by comma[80,8080 by default]", default="80,8080")
    parsed_args = parser.parse_args()
    port_list = parsed_args.ports.split(',')
    ip_address = parsed_args.host
    for port in port_list:
        NmapScannerAsyncFTP().xxx(xxx, xxx)
        
