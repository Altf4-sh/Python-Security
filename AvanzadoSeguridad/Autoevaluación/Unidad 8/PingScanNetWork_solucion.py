#!/usr/bin/env python3
from subprocess import Popen, PIPE
import sys
import argparse

parser = argparse.ArgumentParser(description='Ping Scan Network')
    
# argumentos principales
parser.add_argument("-network", dest="network", help="NetWork segment[For example 192.168.1]", required=True)
parser.add_argument("-machines", dest="machines", help="Machines number",type=int, required=True)

parsed_args = parser.parse_args()    
    
for ip in range(0,parsed_args.machines):
    direccion_ip = parsed_args.network +'.' + str(ip)
    print("Scanning %s " %(direccion_ip))
    if sys.platform.startswith('linux'):
        # Linux
        subprocess = Popen(['/bin/ping', '-c 1 ', direccion_ip], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    elif sys.platform.startswith('win'):
        # Windows
        subprocess = Popen(['ping', direccion_ip], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr= subprocess.communicate(input=None)
    print(stdout)
    if b"Destination Host Unreachable" in stdout or stdout==b"":
        print("La dirección IP %s no está activa!" %(direccion_ip))
    else:
        print("La dirección IP %s está activa!" %(direccion_ip))
