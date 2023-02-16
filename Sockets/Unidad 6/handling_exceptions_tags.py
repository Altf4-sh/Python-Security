#!/usr/bin/env python3

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import urllib.request

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}

url = 'http://python.org'

try:
    req = urllib.request.Request(url, headers=headers)
    with urlopen(req) as res:
        html = res.read()
except HTTPError as error:
    print("HTTPError ",error)
except URLError as error:
    print("Server down or incorrect domain ",error)
else:
    res = BeautifulSoup(html,"lxml")
    if res.title is None:
        print("Tag not found")
    else:
        print(res.title.text)
