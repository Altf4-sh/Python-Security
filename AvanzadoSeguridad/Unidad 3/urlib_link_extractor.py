#!/usr/bin/env python3

from urllib.request import urlopen
import re

def download_page(url):
	return urlopen(url).read()

def extract_links(page):
	link_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
	return link_regex.findall(page)

if __name__ == '__main__':
	target_url = 'http://www.adrformacion.com'
	content = download_page(target_url)
	links = extract_links(str(content))
	for link in links:
		print(link)
