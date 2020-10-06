print('Hello everybody!')

def myFuntion():
    x = 5
    print(x)
myFuntion()

y = 10
y = 15
y = 'a'
def myFuntion2():
    print(y)
myFuntion2()

a, b, c = 'Dog', 'Cat', 'Mouse'
print(a, '-', b, '-', c)

value = input('Vui long nhap ten nguoi dung: ')
name = 'Chao mung ban ' + value + ' den trung tam IMIC!'
print('Chao ban', value, ',')
print(name)

#Giai phuong trinh bac 1: ax + b = 0
def GiaiPhuongTrinhBac1(a, b):
    print('Ket qua = ', -int(b)/int(a))

giaTri1 = int(input("Gia tri 'a' cua phuong trinh = "))
giaTri2 = int(input("Gia tri 'b' cua phuong trinh = "))
GiaiPhuongTrinhBac1(giaTri1, giaTri2)


