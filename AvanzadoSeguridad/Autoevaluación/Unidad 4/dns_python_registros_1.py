import dns.resolver

def main(xxx):
	registros = ['A','AAAA','NS','SOA','MX','MF','MD','TXT']
	for registro in xxx:
		try:
			respuestas = dns.xxx.xxx(xxx, xxx)
			print("Respuestas del registro ",xxx)
			print("-----------------------------------")
			for respuesta in xxx:
				print(xxx)
		except:
			print("No pude resolver la consulta para el registro ",xxx)

if __name__ == '__main__':
	try:
		main('google.com')
	except KeyboardInterrupt:
		exit()
