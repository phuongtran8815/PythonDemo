soBiChia=int(input("vui long nhap so bi chia:"))
soChia=int(input("vui long nhap so chia: "))
s=10
try:
    ketQua=soBiChia/soChia
    print("Ket qua cua phep chia: ",soChia,"/",soChia,"la",ketQua)
    s[0:5]
    print("code nam trong tr nhung phia duoi doan code loi")
except ZeroDivisionError:
    print("Loi toan hoc")
except ArithmeticError:
    print("Loi substring cho 1 so")
except:
    print("other errors")
finally:
    print("doan code luon duoc chay")

print("Doan code nam ngoai try")
print("Doan code nam ngoai try")
print("Doan code nam ngoai try")




