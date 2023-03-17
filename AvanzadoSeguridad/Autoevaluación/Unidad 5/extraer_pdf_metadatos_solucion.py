#!usr/bin/env python

# Estoy usando estos metodos y modulos porque al parecer el modulo PdfFileReader esta obsoleto.
# No funciona.

from PyPDF2 import PdfReader
import os, os.path

fichero = 'XMPSpecificationPart3.pdf'

pdf = PdfReader(open(fichero, 'rb'))

print("[+] Pages number:",len(pdf.pages))

info = pdf.documentInfo()

if hasattr(info,'author'):
    print("[+] Author:",info.author)
if hasattr(info,'creator'):
    print("[+] Creator:",info.creator)
if hasattr(info,'producer'):
    print("[+] Producer:",info.producer)

xmpinfo = pdf.getXmpMetadata()

if hasattr(xmpinfo,'dc_contributor'):
    print ('[+] Contributor:', xmpinfo.dc_contributor)
if hasattr(xmpinfo,'dc_identifier'):
    print ('[+] Identifier:', xmpinfo.dc_identifier)
if hasattr(xmpinfo,'dc_date'):
    print ('[+] Date:',xmpinfo.dc_date)
if hasattr(xmpinfo,'dc_source'):
    print ('[+] Source:', xmpinfo.dc_source)
if hasattr(xmpinfo,'dc_subject'):
    print ('[+] Subject:', xmpinfo.dc_subject)
if hasattr(xmpinfo,'xmp_modifyDate'):
    print ('[+] ModifyDate:', xmpinfo.xmp_modifyDate)
if hasattr(xmpinfo,'xmp_metadataDate'):
    print ('[+] MetadataDate:', xmpinfo.xmp_metadataDate)
if hasattr(xmpinfo,'xmpmm_documentId'):
    print ('[+] DocumentId:', xmpinfo.xmpmm_documentId)
if hasattr(xmpinfo,'xmpmm_instanceId'):
    print ('[+] InstanceId:', xmpinfo.xmpmm_instanceId)
if hasattr(xmpinfo,'pdf_keywords'):
    print ('[+] PDF-Keywords:', xmpinfo.pdf_keywords)
if hasattr(xmpinfo,'pdf_pdfversion'):
    print ('[+] PDF-Version:', xmpinfo.pdf_pdfversion)
