import dns.resolver
respuestas = dns.resolver.query('google.com', 'MX')
for respuesta in respuestas:
    print('Host', respuesta.exchange, 'tiene una preferencia de ', respuesta.preference)
