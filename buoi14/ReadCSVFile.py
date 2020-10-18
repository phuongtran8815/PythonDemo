import pandas as pd
import xlrd
#xl=pd.ExcelFile('D:\Reference materials\VOCAB')
excel_data_df= pd.read_excel('D:\myfile.xlsx',sheet_name='Employee')
#df=pd.read_excel(xl,0,header=None)
print(excel_data_df)
