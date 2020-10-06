import pyodbc

server = 'ADMIN'
database = 'QUAN_LY_NHAN_VIEN'
username = 'PHUONGTRAN'
password = 'abc*123'

driver = '{SQL Server}' # Driver you need to connect to the database
port = '1433'

cnn = pyodbc.connect('DRIVER='+driver+';PORT=port;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+password)

cursor = cnn.cursor()
cursor.execute("SELECT * FROM PHONG_BAN")
rows = cursor.fetchone()
while rows:
    print(rows[0], '---', rows[1], '---', rows[2])
    rows = cursor.fetchone()

cursor.execute("UPDATE PHONG_BAN SET TEN_PHONG_BAN = 'PHONG NHAN SU HANH CHINH' WHERE MA_PHONG_BAN = 'PNS'")
cursor.commit()

maPhongBan = input("Vui long nhap ma phong ban muon them: ")
tenPhongBan = input("Vui long nhap ten phong ban muon them: ")
truongPhong = input("Vui long nhap ma nhan vien truong phong moi: ")

sql = "INSERT INTO PHONG_BAN(MA_PHONG_BAN, TEN_PHONG_BAN, TRUONG_PHONG) VALUES('" + maPhongBan + "', '" + tenPhongBan + "', '" + truongPhong + "')"
cursor.execute(sql)
cursor.commit()

