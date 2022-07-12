from urllib.error import ContentTooShortError
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import PyPDF2 as ppdf
import abnt

cnv_teste = canvas.Canvas("pdf_teste/teste.pdf", pagesize=A4)
#define title and name of the PDF what will be generate
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
contents = []

for i in range(file_content.numPages):
    contents.append(pages[i].extractText())

# for i in range(100):
#     cnv_clone.drawString(x,y,f"{i}")
#     y += 20
    
# for i in range(file_content.numPages):
#     cnv_clone.drawString(0,750,content[i])
#     cnv_clone.showPage()

def cursormoves1(canvas,contents):
    from reportlab.lib.units import inch
    textobject = canvas.beginText()
    textobject.setTextOrigin(0, 800)
    textobject.setFont("Helvetica-Oblique", 14)
    print(type(contents[0]))
    textobject.textLines(contents[0]) #escreve em textObject algumas linhas
    # for content in contents:
    #     textobject.textLine(content)
    #     # textobject.showPage()
    
    textobject.setFillGray(0.4)
    textobject.textLines('''
        teste
	''')
    canvas.drawText(textobject) #desenha no objeto Canva o que está escrito no objeto do tipo canva.beginText()

cursormoves1(cnv_clone,contents)

# print(abnt.a)

#saving the final PDF file created
cnv_clone.save()

# for i in range(100):
#     cnv.drawString(x,y,f"{i}")
#     y += 20