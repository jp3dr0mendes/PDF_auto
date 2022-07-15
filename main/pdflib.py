from array import array
from urllib.error import ContentTooShortError
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import PyPDF2 as ppdf
from PIL import Image
# import filtz

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

def image_extract1(a):
    if a:
        input = ppdf.PdfFileReader(open(r'C:\Users\joaop\Documents\PDF_auto\Arquivos Base\Diagnóstico_CTT.pdf','rb'))
        image_pages = []

        for i in range(input.numPages):
            image_pages.append(input.getPage(i))
        
        objects = []
        images = []

        print(input.numPages)

        for i in range(input.numPages):
            #a imagem 2 não possui imagem, achar condicional para apenas passar o laço for quando a pagina em questão possuir imagens
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
                    elif objects[i]['/Filter'] == '/DCTDecode':
                        img = open('/Users/joaop/Documents/PDF_auto/Arquivos Base/images/'+obj[1:]+'.jpg','wb')
                        img.write(data)
                        img.close()
                        images.append(img)
                    elif objects[i]['/Filter'] == '/JPXDecode':
                        img = open('/Users/joaop/Documents/PDF_auto/Arquivos Base/images/'+obj[1:]+'jp2','wb')
                        img.write(data)
                        img.close()
                        images.append(img)

        print(len(images))

def extract_test(a):
    if a:
        input = ppdf.PdfFileReader(open(r'C:\Users\joaop\Documents\PDF_auto\Arquivos Base\Diagnóstico_CTT.pdf','rb'))
        image_pages = []

        for i in range(input.numPages):
            image_pages.append(input.getPage(i))
        
        objects = []
        images = []

        print(input.numPages)

        for i in range(input.numPages):
            #a pagina 2 não possui imagem, achar condicional para apenas passar o laço for quando a pagina em questão possuir imagens
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
                        if objects[i]['/Filter'] == '/DCTDecode':
                            img = open('/Users/joaop/Documents/PDF_auto/Arquivos Base/images/'+obj[1:]+'.jpg','wb')
                            img.write(data)
                            img.close()
                            images.append(img)
                        elif objects[i]['/Filter'] == '/JPXDecode':
                            img = open('/Users/joaop/Documents/PDF_auto/Arquivos Base/images/'+obj[1:]+'jp2','wb')
                            img.write(data)
                            img.close()
                            images.append(img)
            else:
                objects.append(None)
        print(len(images))


def teste():
    input = ppdf.PdfFileReader(open(r'C:\Users\joaop\Documents\PDF_auto\Arquivos Base\Diagnóstico_CTT.pdf','rb'))
    image_pages = []

    for i in range(input.numPages):
        image_pages.append(input.getPage(i))
        
    objects = []
    images = []

    print(input.numPages)
    # print(image_pages[0]['/Resources'][0])
    for i in image_pages[0]['/Resources']:
        print(i)
    # for i in range(input.numPages):
    #     if image_pages[i]['/Resources']['/XObject']:
    #         objects.append(image_pages[i]['/Resources']['/XObject'])
    #     else:
    #         objects.append(None)


def verify_list(list: array):
    a = 0
    for j in list['/Resources']:
        if j == '/XObject':
            a = 1
    return a

# def image_extract2():
#     doc = fitz.open('C:\Users\joaop\Documents\PDF_auto\Arquivos Base\Diagnóstico_CTT.pdf')
#     for i in range(len(doc)):
