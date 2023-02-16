 #!/usr/bin/env python3
 
import pygeoip
import argparse
 
def geoip_city(domain,ipaddress):
    path = 'GeoLiteCity.dat'
    geolitecity = pygeoip.GeoIP(path)
    print(geolitecity.record_by_addr(ipaddress))
    print(geolitecity.region_by_name(domain))
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get geolocation from domain and ip address')
    parser.add_argument('--domain', action="store", dest="domain",  default='www.python.org')
    parser.add_argument('--ipaddress', action="store", dest="ipaddress",  default='83.166.169.231')
    given_args = parser.parse_args()
    domain = given_args.domain
    ipaddress = given_args.ipaddress
    geoip_city(domain,ipaddress)