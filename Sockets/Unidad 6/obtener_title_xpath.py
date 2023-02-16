#!/usr/bin/env python3

import re
import requests

from lxml import etree

respuesta = requests.get('https://www.debian.org/releases/stable/index.en.html')

parser = etree.HTML(respuesta.text)

resultado = etree.tostring(parser,pretty_print=True, method="html")
#print(resultado)

obtener_texto_xpath = etree.XPath("//title/text()", smart_strings=False)
texto = obtener_texto_xpath(parser)[0]
print(texto)
