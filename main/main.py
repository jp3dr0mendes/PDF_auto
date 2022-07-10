from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import PyPDF2 as ppdf

cnv_teste = canvas.Canvas("pdf_teste/teste.pdf", pagesize=A4)

cnv_clone = canvas.Canvas("pdf_teste/testeclone.pdf", pagesize=A4)
#open the pdf file
file = open(r'C:\Users\joaop\Documents\PDF_auto\Arquivos Base\Diagnóstico_CTT.pdf','rb')

#reading the pdf file content
file_content = ppdf.PdfFileReader(file)

#getting the page objects of PDF file

pages = []

for i in range(file_content.numPages):
    pages.append(file_content.getPage(i))

#extracting the content of the pages
content = []

for i in range(file_content.numPages):
    content.append(pages[i].extractText())

# for i in range(100):
#     cnv_clone.drawString(x,y,f"{i}")
#     y += 20
    
for i in range(file_content.numPages):
    cnv_clone.drawString(0,750,content[i])
    cnv_clone.showPage()



#saving the final PDF file created
cnv_clone.save()
# print(file_content.numPages)

# x = 250
# y = 450

# for i in range(100):
#     cnv.drawString(x,y,f"{i}")
#     y += 20