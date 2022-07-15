from urllib.error import ContentTooShortError
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import PyPDF2 as ppdf
import abnt
import pdflib as pdf

cnv_teste = canvas.Canvas("pdf_teste/teste.pdf", pagesize=A4)
#define title and name of the PDF what will be generate
cnv_clone = canvas.Canvas("pdf_teste/testeclone.pdf", pagesize=A4)
# #open the pdf file
# file = open(r'C:\Users\joaop\Documents\PDF_auto\Arquivos Base\Diagnóstico_CTT.pdf','rb')

# #reading the pdf file content
# file_content = ppdf.PdfFileReader(file)
content = pdf.extract_content(r'C:\Users\joaop\Documents\PDF_auto\Arquivos Base\Diagnóstico_CTT.pdf')

pdf.draw_text_pdf("pdf_teste/testeclone.pdf",content)
#saving the final PDF file created
# cnv_clone.save()

# pdf.image_extract1(1)
teste = input('file path:')
pdf.extract_image(teste)
# pdf.teste()