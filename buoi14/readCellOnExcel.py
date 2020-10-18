import pandas as pd
columns_name=['Last Name','First Name']
index=[1,2]
try:
    data=pd.read_excel(r'D:\perfectExample\Python_Pandas_test_2.xlsx')
    df=pd.DataFrame(data,index=index,columns=columns_name)
    print(df.head())
except FileNotFoundError:
    print("Not Found")
print(data[['Country','Last Name']].head(5))
print(data[['Country','Last Name']][:5])
young_pp=data[data['Age']<30]
print(young_pp[:10])
index=pd.Index(list(range(100)),name='rows')
columns=pd.Index(['A',['B'],['C'],['D']],name='cols')
