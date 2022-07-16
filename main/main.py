from urllib.error import ContentTooShortError
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import PyPDF2 as ppdf
import abnt
import pdflib as pdf

content = pdf.extract_content(r'C:\Users\joaop\Documents\PDF_auto\Arquivos Base\Diagnóstico_CTT.pdf')

# pdf.draw_text_pdf("pdf_teste/testeclone.pdf",content)
pdf.draw_text_pdf(r'C:\Users\joaop\Documents\PDF_auto\pdfteste.docx',content)
pdf.draw_text_pdf(r'C:\Users\joaop\Documents\PDF_auto\pdfteste.pdf',content)

a = input('file path:')
pdf.extract_image(a)
