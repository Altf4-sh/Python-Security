 #!/usr/bin/env python3
 
from lxml.html import fromstring
import requests
 
domain = 'domaintools.com'
url = 'https://api.domaintools.com/v1/'+domain+'/reverse-ip/?format=html'
 
headers = {'User-Agent': 'wswp'}
resp = requests.get(url, headers=headers)
html = resp.text
 
tree = fromstring(html)
 
direccion_ip = tree.xpath('/html/body/div[2]/div[2]/span[2]//text()')
print('IP address ',direccion_ip[0])
 
domain_names = tree.xpath('/html/body/div[2]/div[4]//text()')
print('domain names ',domain_names[3],domain_names[7],domain_names[11],domain_names[15])