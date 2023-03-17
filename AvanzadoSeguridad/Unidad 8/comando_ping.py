#!/usr/bin/env python3
from subprocess import Popen, PIPE
import sys
import argparse

parser = argparse.ArgumentParser(description='Ping Scan Network')
    
# argumentos principales
parser.add_argument("--host", dest="host", help="Host o direccion ip", required=True)

parsed_args = parser.parse_args()
direccion_ip = parsed_args.host

print("Scanning %s " %(direccion_ip))
if sys.platform.startswith('linux'):
    # Linux
    subprocess = Popen(['/bin/ping', '-c 1 ', direccion_ip], stdin=PIPE, stdout=PIPE, stderr=PIPE)
elif sys.platform.startswith('win'):
    # Win
    subprocess = Popen(['ping', direccion_ip], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	
stdout, stderr= subprocess.communicate(input=None)
print(stdout)

if b"Destination Host Unreachable" in stdout or b"100% packet loss" in stdout or stdout==b"":
    print("La dirección IP %s no está activa!" %(direccion_ip))
else:
    print("La dirección IP %s está activa!" %(direccion_ip))
