#!usr/bin/env python

from PyPDF2 import PdfFileReader

def get_metadatos_ruta_pdf():

    print("[+ Metadatos /pdf/TutorialPython3.pdf")
    pdf = PdfFileReader(open("pdf/TutorialPython3.pdf", 'rb'))
    info = pdf.getDocumentInfo()
    print(info)

get_metadatos_ruta_pdf()
