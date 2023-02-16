#!/usr/bin/env python

import argparse
import dns.name

def main(dominio1, dominio2):
    dominio1 = dns.name.from_text(dominio1)
    dominio2 = dns.name.from_text(dominio2)
    print("dominio1 is subdomain of dominio2: ", dominio1.is_subdomain(dominio2)) 
    print("dominio1 is superdomain of dominio2: ", dominio1.is_superdomain(dominio2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Comprobar 2 dominios con dns Python')
    parser.add_argument('--dominio1', action="store", dest="dominio1",  default='www.python.org')
    parser.add_argument('--dominio2', action="store", dest="dominio2",  default='python.org')
    given_args = parser.parse_args() 
    dominio1 = given_args.dominio1
    dominio2 = given_args.dominio2
    main (dominio1, dominio2)

