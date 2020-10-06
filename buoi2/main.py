print("Nhập chuỗi cần cắt!")
textInput = input()
print("Ký tự dùng để cắt chuỗi!")
character = input()
list = textInput.split(character)
#count = 0
#while count < len(list):
    #print("Giá trị thứ ", count, list[count])
    #count += 1

for i in list:
    if int(i)%2 == 0:
        print(i, "là số chẵn")
    else:
        print(i, "là số lẻ")


###############################################
x = 100
temp = 0
for i in range(1,100):
    if x%i == 0:
        temp += 1

if temp > 2:
    print(x, " khong phai so nguyen to")


#############################################################

listSN = [1,5,3,7,4,29]
listSNT = []
def xacDinhSNT(x):
    temp = 0
    for j in range(2,x):
        if x%j == 0:
            temp += 1

    if temp > 0:
        return -1
    else:
        return 1

for i in listSN:
    if xacDinhSNT(i) == 1:
        listSNT.append(i)

print(listSNT)

