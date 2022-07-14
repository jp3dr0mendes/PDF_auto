from urllib.error import ContentTooShortError
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import PyPDF2 as ppdf

def draw_text_pdf(canvas,contents):
    from reportlab.lib.units import inch
    textobjects = []
    for i in range(len(contents)):
        textobjects.append(canvas.beginText())
        textobjects[i].setTextOrigin(0, 800)
        textobjects[i].setFont("Helvetica-Oblique", 12)
        textobjects[i].textLines(contents[i])
        canvas.drawText(textobjects[i])
        canvas.showPage()
    print(textobjects[0])
    canvas.save()

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