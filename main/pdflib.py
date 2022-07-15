from array import array
from urllib.error import ContentTooShortError
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import PyPDF2 as ppdf
from PIL import Image

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

##pass the PDF file path to extract PDF images 

def extract_image(file):
    if file:
        input = ppdf.PdfFileReader(open(r'{}'.format(file),'rb'))
        image_pages = []

        for i in range(input.numPages):
            image_pages.append(input.getPage(i))
        
        objects = []
        images = []

        for i in range(input.numPages):
            if verify_list(image_pages[i]):
                objects.append(image_pages[i]['/Resources']['/XObject'].getObject())
                for obj in objects[i]:
                    if objects[i][obj]['/Subtype'] == '/Image':
                        size = (objects[i][obj]['/Width'], objects[i][obj]['/Height'])
                        data = objects[i][obj].get_data()
                        
                        if objects[i][obj]['/ColorSpace'] == '/DeviceRGB':
                            mode = 'RGB'
                        else:
                            mode = 'p'
                        if objects[i][obj]['/Filter'] == '/FlateDecode':
                            img = Image.frombytes(mode,size,data)
                            img.save('/Users/joaop/Documents/PDF_auto/Arquivos Base/images/'+obj[1:]+'.png')
                            images.append(img)
                        elif objects[i][obj]['/Filter'] == '/DCTDecode':
                            img = open('/Users/joaop/Documents/PDF_auto/Arquivos Base/images/'+obj[1:]+'.jpg','wb')
                            img.write(data)
                            img.close()
                            images.append(img)
                        elif objects[i][obj]['/Filter'] == '/JPXDecode':
                            img = open('/Users/joaop/Documents/PDF_auto/Arquivos Base/images/'+obj[1:]+'jp2','wb')
                            img.write(data)
                            img.close()
                            images.append(img)
            else:
                objects.append(None)
    else: 
        print('erro')

def verify_list(list: array):
    a = 0
    for j in list['/Resources']:
        if j == '/XObject':
            a = 1
    return a
