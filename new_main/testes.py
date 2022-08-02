import pandas as pd
import csv
import xlrd
from matplotlib import pyplot as plt
# from openpyxl import load_workbook
import openpyxl as opp
import excel2img

excel2img.export_img('teste.xlsx','image_teste.png',"",'Página1!A1:B5')


# file = opp.load_workbook(filename=r"C:\Users\joaop\Documents\PDF_auto\Arquivos Base\Planilha de apoio para o cálculo da RCB - CPP 001_2022 - Versão 2.0_1.xlsx")

# for files in file:
#     print(files)

# f = file['Descarte']
# for x in f:
#     print(x)

# for sheet in file:
#     print(sheet)

# file = pd.ExcelFile(r"C:\Users\joaop\Documents\PDF_auto\Arquivos Base\Planilha de apoio para o cálculo da RCB - CPP 001_2022 - Versão 2.0_1(copy1).xlsx")

# data_frames{
    
# }

# df_IlumBenef = pd.read_excel(file,'IlumBenef')
# df_IlumBenef = df_IlumBenef.dropna(how='all',axis=1)
# df_IlumBenef = df_IlumBenef.dropna(how='all')

# df1 = df_IlumBenef.loc[1:20]
# print(df1)


# data = pd.read_excel(r"C:\Users\joaop\Documents\PDF_auto\Arquivos Base\Planilha de apoio para o cálculo da RCB - CPP 001_2022 - Versão 2.0_1.xlsx")
# for d in data:
#     print(d)

# for i in data:
#     print(i)
