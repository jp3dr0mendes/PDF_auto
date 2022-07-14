from urllib.error import ContentTooShortError
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import PyPDF2 as ppdf

def draw_text_pdf(path_to_new_pdf_file,contents):
    from reportlab.lib.units import inch

    cnv = canvas.Canvas(path_to_new_pdf_file, pagesize=A4)
    textobjects = []

    for i in range(len(contents)):
        textobjects.append(cnv.beginText())
        textobjects[i].setTextOrigin(mm2p(30),mm2p(267))
        textobjects[i].setFont("Helvetica-Oblique", 12)
        textobjects[i].textLines(contents[i])
        cnv.drawText(textobjects[i])
        cnv.showPage()

    # print(textobjects[0])
    cnv.save()

def extract_content(path):
    file = open(path,'rb')
    file_content = ppdf.PdfFileReader(file)
    pages = []
    
    for i in range(file_content.numPages):
        pages.append(file_content.getPage(i))
    
    contents = []
    
    for i in range(file_content.numPages):
        contents.append(pages[i].extractText())
    
    return contents

def mm2p(mm):
    return mm/0.352777