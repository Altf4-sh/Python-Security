#!/usr/bin/env python

import argparse
import dns.zone
import dns.resolver
import socket

def main(dominio):
    # Regstros DNS IPv4
    try:
        respuestaIPV4 = dns.resolver.query(dominio, 'A')
        for i in range(0, len(respuestaIPV4)):
            print("IPV4: ", respuestaIPV4[i])
    except dns.resolver.NoAnswer as error:
        print("Error al obtener los registros IPv4:", error)

    # Regstros DNS IPv6
    try:
        respuestaIPV6 = dns.resolver.query(dominio, 'AAAA')
        for i in range(0, len(respuestaIPV6)):
            print("IPV6: ", respuestaIPV6[i])
    except dns.resolver.NoAnswer as error:
        print("Error al obtener los registros IPv6:", error)

    # Registros de correo MX (Mail Exchanger)
    try:
        mx = dns.resolver.query(dominio, 'MX')
        for i in range(0, len(mx)):
            print("MX: ", mx[i])
    except dns.resolver.NoAnswer as error:
        print("Error al obtener los registros MX:", error)

    # Registros de CNAME
    try:
        cname_answer = dns.resolver.query(dominio, 'CNAME')
        print("CNAME: ", cname_answer)
    except dns.resolver.NoAnswer as error:
        print('Error al obtener los registros CNAME', error)

     # Registros de NS
    try:
        ns_answer = dns.resolver.query(dominio, 'NS')
        print(ns_answer)
    except dns.resolver.NoAnswer as error:
        print("Error al obtener los registros NS:", error)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DNS Python')
    parser.add_argument('-dominio', action="store", dest="dominio",  default='python.org')
    given_args = parser.parse_args() 
    dominio = given_args.dominio
    main(dominio)

