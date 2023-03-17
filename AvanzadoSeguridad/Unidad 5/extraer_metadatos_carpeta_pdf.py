#!usr/bin/env python

from PyPDF2 import PdfFileReader
import os, os.path

def get_metadatos_carpeta_pdf():
    for dirpath, dirnames, files in os.walk("pdf"):
        for data in files:
            ext = data.lower().rsplit('.', 1)[-1]
            if ext in ['pdf']:
                print("[+Metadatos: %s " %(dirpath+os.path.sep+data))
                pdf = PdfFileReader(open(dirpath+os.path.sep+data, 'rb'))
                info = pdf.getDocumentInfo()
                for metadato in info:
                    print ('[+] ' + metadato.strip( '/' ) + ': ' + info[metadato])


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


get_metadatos_carpeta_pdf()
