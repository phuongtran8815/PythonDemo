import pandas as pd
import openpyxl
def readExcel():
    file=pd.read_excel(r'D:\perfectExample\Python_Pandas_test_2.xlsx',header=None)
    try:
        row=int(input('Please insert row: '))
        collumn=int(input('Please insert collumn: '))
        print('Data at [%d][%d]:'%(row,collumn),file[collumn][row])
    except:
        print('The value at index[%d][%d]:'%(row,collumn),'N/A')
def writeExcel():
    try:
        file=openpyxl.load_workbook(r'D:\perfectExample\Python_Pandas_test_2.xlsx')
        sheet=file.get_sheet_by_name('Python_Pandas_test_2')
        p=input('Please insert position to input data (Example:a1,b2...): ')
        sheet[p]=input('New content: ')
    except:
        print('Enter the wrong character')
    file.save(r'D:\perfectExample\Python_Pandas_test_2.xlsx')


