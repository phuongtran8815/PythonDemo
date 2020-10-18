import pandas as pd
# columns_name = ['Employee ID', 'Name', '']
excel_data_df = ""
try:
    excel_data_df = pd.read_excel('D:\myfile.xlsx', header=None)
except FileNotFoundError:
    print("not found")
# print whole sheet data

print(excel_data_df[2][1])
