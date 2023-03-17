import urllib.request
import re
web = input("Introduce una url(sin http://): ")
#https://www.adrformacion.com/
#obtener la respuesta
response = urllib.request.Request('http://'+web)
#obtener el contenido de la página a partir de la respuesta
content = urllib.request.urlopen(response).read()
# expression regular para detectar emails
pattern = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
#obtener emails a partir de una expresión regular
mails = re.findall(pattern,str(content))
print(mails)

