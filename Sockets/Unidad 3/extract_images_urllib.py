#!/usr/bin/env python3

from urllib.request import urlopen, urljoin
import re

def download_page(url):
	return urlopen(url).read()

def extract_image_locations(page):
	img_regex = re.compile('[-a-zA-Z0-9_]+.jpg',re.IGNORECASE) # Con .png también se encuentran imágenes.
	return img_regex.findall(page)

if __name__ == '__main__':
	target_url = 'http://www.adrformacion.com'
	content = download_page(target_url)
	image_locations = extract_image_locations(str(content))
	for src in image_locations:
		print(target_url, src)
