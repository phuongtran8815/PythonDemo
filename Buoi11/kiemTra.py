def kiemTraSoNguyen(number):
    if number / 10 >= 1 and number / 10 <= 9:
        return True
    else:
        return False

def kiemTraTong(numberString):
    first = numberString[0]
    last = numberString[len(numberString) - 1]
    if (int(first) + int(last)) % 2 == 0:
        return True
    else:
        return False

textInput = input("Vui lòng nhập dãy số nguyên có 2 chữ số cách nhau bởi dấu ',': ")
listInput = textInput.split(',')
listResult = []
sum = 0
for num in listInput:
    if kiemTraSoNguyen(int(num)):
        if kiemTraTong(num):
            listResult.append(int(num))
            sum = sum + int(num)
    else:
        print(num,"không đúng định dạng số 2 chữ số")

for x in range(len(listResult)):
    print(listResult[x])
print("Tổng=",sum)
