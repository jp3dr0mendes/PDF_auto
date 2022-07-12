from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import PyPDF2 as ppdf
import abnt

cnv_teste = canvas.Canvas("pdf_teste/teste.pdf", pagesize=A4)

cnv_clone = canvas.Canvas("pdf_teste/testeclone.pdf", pagesize=A4)
#open the pdf file
file = open(r'C:\Users\joaop\Documents\PDF_auto\Arquivos Base\Diagnóstico_CTT.pdf','rb')

#reading the pdf file content
file_content = ppdf.PdfFileReader(file) #retorna um objeto criado pelo PDf presente no caminho passado no argumento

#getting the page objects of PDF file

def cursormoves1(canvas):
    from reportlab.lib.units import inch
    textobject = canvas.beginText()
    textobject.setTextOrigin(inch, 2.5*inch)
    textobject.setFont("Helvetica-Oblique", 14)
    
    lyrics = ["teste 1","teste 2","teste 3","teste 4","teste 5"]
    for line in lyrics:
        textobject.textLine(line)
    
    textobject.setFillGray(0.4)
    textobject.textLines('''
        ado ado ado quem ta lendo e arrombado ado ado ado 
	''')
    canvas.drawText(textobject)

cursormoves1(cnv_clone)

cnv_clone.save()