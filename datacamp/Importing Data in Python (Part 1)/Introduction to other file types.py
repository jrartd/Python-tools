#https://www.analyticsvidhya.com/blog/2017/03/read-commonly-used-formats-using-python/
#Pickle File
import pickle
with open("pickled_fruit.pkl","rb") as file:
	#data = pickle.load(file)

print(data)


#import excel files
""" debes intalar alguno de estos
OpenPyXL - read/write Excel 2010 xlsx/xlsm files
pandas - data import, clean-up, exploration, and analysis
xlrd - read Excel data
xlwt - write to Excel
XlsxWriter - write to Excel (xlsx) files

https://medium.com/@kasiarachuta/reading-and-writingexcel-files-in-python-pandas-8f0da449cc48
https://www.dataquest.io/blog/excel-and-pandas/

"""
import pandas as pd 
file = "battledeath.xlsx"

maindata = pd.ExcelFile(file) #forma 1
sheet1 = maindata.parse(0, skiprows=[0])	#cargar una hoja especifica del documneto

maindata2 = pd.read_excel(file,sheetname="2004") #forma 2 y el #documneto
print(maindata2)