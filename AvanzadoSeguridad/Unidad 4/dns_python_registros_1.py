import dns.resolver

def main(dominio):
	registros = ['A','AAAA','NS','SOA','MX','MF','MD','TXT']
	for registro in registros:
		try:
			respuestas = dns.resolver.resolve(dominio, registro)
			print("Respuestas del registro ",respuestas)
			print("-----------------------------------")
			for respuesta in respuestas:
				print(respuesta)
		except:
			print("No pude resolver la consulta para el registro ",registro)

if __name__ == '__main__':
	try:
		main('google.com')
	except KeyboardInterrupt:
		exit()
