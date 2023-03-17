import requests
import sys

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def detectar_XSS_Inyection():
	#variables iniciales
	url = "http://testphp.vulnweb.com/listproducts.php?cat="

	#añadir payloads de inyección xss
	xss_injection_payloads = []

	with open('XSS-attack-vectors.txt', 'r') as filehandle:
		for line in filehandle:
			xss_inyection = line[:-1]
			xss_injection_payloads.append(xss_inyection)

	response = requests.get(url)
	if "MySQL" in response.text or "You have an error in your SQL syntax" in response.text or "Syntax error" in response.text:
		print(Color.DARKCYAN+"site vulnerable to sql injection")

		for payload in xss_injection_payloads:
			response = requests.post(url+payload)

			if payload in response.text:
				print(Color.YELLOW+"The parameter is vulnerable")
				print(Color.GREEN+"Payload string: "+payload+"\n")
				print(Color.PURPLE+response.text)

if __name__ == '__main__':
	detectar_XSS_Inyection()