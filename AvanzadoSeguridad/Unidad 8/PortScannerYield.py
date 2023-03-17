import nmap

portScannerYield = nmap.PortScannerYield()

for scan_yield in portScannerYield.scan('scanme.nmap.org', '21,22,23,25,80'):
    print(scan_yield[1]['nmap']['scanstats']['uphosts'])
    if scan_yield[1]['nmap']['scanstats']['uphosts'] == "1":
        print("Host ==> " + scan_yield[0])
        print(scan_yield[1]['scan'])
