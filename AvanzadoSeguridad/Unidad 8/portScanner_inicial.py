import nmap
portScanner = nmap.PortScanner()
resultados = portScanner.scan('scanme.nmap.org', '21,22,23,80','-sV')
print(resultados)
print(portScanner.command_line())
print(portScanner.csv())
print(portScanner.all_hosts())
print(portScanner.scaninfo())
