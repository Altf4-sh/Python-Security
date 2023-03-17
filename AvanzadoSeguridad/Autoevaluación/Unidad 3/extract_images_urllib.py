#!/usr/bin/env python3

from urllib.request import urlopen, urljoin
import re

def download_page(url):
	return urlopen(url).xxx()
	
def extract_image_locations(page):
	img_regex = re.xxx('<expresion_regular>',re.IGNORECASE)
	return img_regex.xxx(page)

if __name__ == '__main__':
	target_url = 'http://www.adrformacion.com'
	content = xxx(target_url)
	image_locations = xxx(str(content))
	for src in xxx:
		print(xxx(target_url, src))
