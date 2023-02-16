import dns.reversename

nombre = dns.reversename.from_address("8.8.8.8")
print(nombre)
print(dns.reversename.to_address(nombre))



