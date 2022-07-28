from docx import Document
from docx.shared import Inches
from docx2pdf import convert
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.units import mm
from reportlab.platypus import Image
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
import fitz
import os
import win32com.client
import PyPDF2 as ppdf

document = Document('teste_model.docx')

for paragraph in document.paragraphs:
    if '[marcação 1]' in paragraph.text:
        # paragraph.text=paragraph.text.replace('[marcação 1]',input("digite o novo texto a ser inserido:"))
        paragraph.text=paragraph.text.replace('[marcação 1]',input("digite o novo texto a ser inserido:"))

new_doc=input("Digite o nome do novo documento:")
document.save(new_doc+".docx")
#convertendo de .docx para .pdf
convert(new_doc+".docx",new_doc+".pdf")
#removendo o arquivo .docx modificado que foi gerado como auxiliar
os.remove(new_doc+".docx")

def mm2p(mm):
    return mm/0.352777

cnv=canvas.Canvas(new_doc+".pdf")

file=open(input('digite o nome do novo arquivo pdf:')+".pdf",'rb')
file_content=ppdf.PdfFileReader(file)
print('passou1')

pages = []
for i in range(file_content.numPages):
    pages.append(file_content.getPage(i))
print('passou2')

contents=[]
for i in range(file_content.numPages):
    contents.append(pages[i].extractText())
print('passou3')

text_object=[]
for i in range(len(contents)):
    # text_object.append(cnv.beginText())
    # text_object[i].setTextOrigin(mm2p(30),mm2p(267))
    print(contents[i])
    if '[imagem 1]' in contents[i]:
        doc = fitz.open(new_doc+".pdf")
        print('passou aqui')
        for page in doc:
            text='[Imagem 1]'
            #buscando a posição de 'Imagem1' no documento
            text_instances=page.search_for(text)
            coord=[]
            for k in text_instances:
                for j in k:
                    #guardando as coordenadas encontradas da posição de 'imagem1' no documento
                    coord.append(j)
        #printando as coordenadas
        print(coord)
        #usando as coordenadas encontradas como determinação de onde a imagem começa e onde a imaggem termina no documento
        #modelo [x0,y0,x1,y1]
        #desenvolver equação para posicionar a imagem no centro e com a dimensão original
        img_rect=fitz.Rect(coord[:])
        #inserindo a imagem no local encontrado
        doc[i].insert_image(img_rect,filename=r"C:\Users\joaop\Documents\PDF_auto\Imagens\Image13.png")
        # cnv.drawImage(r"C:\Users\joaop\Documents\PDF_auto\Imagens\Image13.png",coord[0],coord[2],mask='auto')
        print('passou imagem')
        #salvando o documento com a imagem inserida
        doc.save('teste2.pdf')
        #fechando o documento
        doc.close()
        # doc.save('teste.pdf',garbage=4, deflate=True, clean=True)
        print('passou aqui também')
print('passou4')

cnv.save()

# workbook = [
#     r"C:\Users\joaop\Documents\PDF_auto\Arquivos_Base\Lev. Atualizado 2022_Equatorial.xlsm",
#     r"C:\Users\joaop\Documents\PDF_auto\Arquivos_Base\Historico de Consumo.xlsx"
#     r"C:\Users\joaop\Documents\PDF_auto\Arquivos_Base\Planilha de apoio para o cálculo da RCB - CPP 001_2022 - Versão 2.0_1 - Copia.xlsx",
#     r"C:\Users\joaop\Documents\PDF_auto\Arquivos_Base\Mapeamento Equatorial.xlsx",
#     r"C:\Users\joaop\Documents\PDF_auto\Arquivos_Base\Lev. Atualizado 2022_Equatorial.xlsm",
# ]

# # excel = win32com.client.Dispatch('Excel.Application')

# for w in workbook:
#     excel = win32com.client.Dispatch('Excel.Application')
#     sheets = excel.Workbooks.Open(w)
#     # work_sheet = sheets.WorkSheets(0).Select()
#     # work_sheet.ExportAsFixedFormat(0,'excel_pdfs/example1.pdf')
#     sheets.WorkSheets(1).Select()
#     sheets.ActiveSheet.ExportASFixedFormat(0,'excel_pdfs/example{w}.pdf')
#     sheets.Close()
#     excel.Quit()

# for workbook in workbooks:
#     w = workbook
#     save_option = PdfSaveOptions()
#     save_option.setOnePagePerSheet(True)
#     w.save('excel_pdfs/example.pdf',save_option)