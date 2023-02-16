#!usr/bin/env python

from PyPDF2 import xxx

fichero = 'pdf/XMPSpecificationPart3.pdf'

pdf = xxx(open(xxx, 'rb'))

print("[+] Pages number:",pdf.xxx())

info = pdf.xxx()

if hasattr(info,'author'):
    print("[+] Author:",info.xxx)
if hasattr(info,'creator'):
    print("[+] Creator:",info.xxx)
if hasattr(info,'producer'):
    print("[+] Producer:",info.xxx)

xmpinfo = pdf.xxx()

if hasattr(xmpinfo,'dc_contributor'):
    print ('[+] Contributor:', xmpinfo.xxx)
if hasattr(xmpinfo,'dc_identifier'):
    print ('[+] Identifier:', xmpinfo.xxx)
if hasattr(xmpinfo,'dc_date'):
    print ('[+] Date:',xmpinfo.dc_date)
if hasattr(xmpinfo,'dc_source'):
    print ('[+] Source:', xmpinfo.xxx)
if hasattr(xmpinfo,'dc_subject'):
    print ('[+] Subject:', xmpinfo.xxx)
if hasattr(xmpinfo,'xmp_modifyDate'):
    print ('[+] ModifyDate:', xmpinfo.xxx)
if hasattr(xmpinfo,'xmp_metadataDate'):
    print ('[+] MetadataDate:', xmpinfo.xxx)
if hasattr(xmpinfo,'xmpmm_documentId'):
    print ('[+] DocumentId:', xmpinfo.xxx)
if hasattr(xmpinfo,'xmpmm_instanceId'):
    print ('[+] InstanceId:', xmpinfo.xxx)
if hasattr(xmpinfo,'pdf_keywords'):
    print ('[+] PDF-Keywords:', xmpinfo.xxx)
if hasattr(xmpinfo,'pdf_pdfversion'):
    print ('[+] PDF-Version:', xmpinfo.xxx)
