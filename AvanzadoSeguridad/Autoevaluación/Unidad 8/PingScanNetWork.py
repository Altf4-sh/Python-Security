#!/usr/bin/env python3
from subprocess import Popen, PIPE
import sys
import argparse

parser = argparse.ArgumentParser(description='Ping Scan Network')
    
# argumentos principales
parser.add_argument("-network", dest="network", help="NetWork segment[For example 192.168.1]", required=True)
parser.add_argument("-machines", dest="machines", help="Machines number",type=int, required=True)

parsed_args = parser.parse_args()    
    
for ip in xxx(0,parsed_args.machines):
    direccion_ip = parsed_args.xxx +'.' + str(xxx)
    print("Scanning %s " %(xxx))
    if sys.platform.xxx('linux'):
        # Linux
        subprocess = xxx(['/bin/ping', '-c 1 ', xxx], stdin=xxx, stdout=xxx, stderr=xxx)
    elif sys.platform.xxx('win'):
        # Windows
        subprocess = xxx(['ping', xxx], stdin=xxx, stdout=xxx, stderr=xxx)
    stdout, stderr= subprocess.xxx(input=None)
    print(stdout)
    if b"Destination Host Unreachable" in xxx or stdout==b"":
        print("La dirección IP %s no está activa!" %(xxx))
    else:
        print("La dirección IP %s está activa!" %(xxx))
