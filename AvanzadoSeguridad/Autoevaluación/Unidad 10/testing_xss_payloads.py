import requests
import sys

#variables iniciales
url = "http://testphp.vulnweb.com/listproducts.php?cat="
initial = "'"

#añadir payloads de inyección xss
xss_injection_payloads = ["xxx"]

response = requests.xxx(xxx+xxx)
if "MySQL" in xxx.text or "You have an error in your SQL syntax" in xxx.text or "Syntax error" in xxx.text:
	print("site vulnerable to sql injection")
	for payload in xxx:
		response = requests.xxx(url+xxx)
		if payload in response.xxx:
			print("The parameter is vulnerable")
			print("Payload string: "+xxx+"\n")
			print(xxx.text)
