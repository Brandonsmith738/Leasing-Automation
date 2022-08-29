import PyPDF2
from PyPDF2 import PdfReader


def PopulateCI():
    pdfFileObj = open('CI_Template.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    pageObj = pdfReader.getPage(0)
    pageObj.extractText()
