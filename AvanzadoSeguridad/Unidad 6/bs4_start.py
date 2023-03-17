#!/usr/bin/env python3

import os

try:
 import requests, bs4
except:
 os.system("python3 -m pip install -U requests beautifulsoup4")

from bs4 import BeautifulSoup

url = "https://python.org"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup)
