import dns.resolver
 
dominios = ["google.com", "microsoft.com", "python.org"]

for dominio in dominios:
    print('Direcciones ip del dominio',dominios)
    #utilizamos el registro A para obtener direcciones ip
    direcciones = dns.resolver.resolve(dominio, 'A')
    for direccion_ip in direcciones:
        print(direccion_ip)
