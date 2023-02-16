#!/usr/bin/env python3

import re
import requests

from lxml import html

respuesta = requests.get('https://www.debian.org/releases/stable/index.en.html')
elementos = html.fromstring(respuesta.text) # Parsea la respuesta de texto plano a html.
obtener_texto_xpath = elementos.xpath("//title/text()", smart_strings=False)
texto = obtener_texto_xpath[0]
print(texto)
