import math

s = "java core;JEE;SQL;Python"
listSplit = s.split(";")
print(listSplit)

#################################################################################

i = input("Vui long nhap day so cach nhau boi dau ',': ")
listNumber = i.split(",")
sum = 0
for number in listNumber:
    sum = sum + int(number)
print("Sum of number array", sum)

#################################################################################

def checkPrimeNumber(number):
    if number < 2:
        return False

    for n in range(2,number):
        if number % n == 0:
            return False
    return True

sumPrime = 0
prime = input("Vui long nhap day so cach nhau boi dau ',': ")
listPrime = prime.split(",")
for numTmp in listPrime:
    numTmp = int(numTmp)
    sqrtTmp = math.sqrt(numTmp)
    if isinstance(sqrtTmp, int) and (checkPrimeNumber(sqrtTmp)):
        sumPrime = sumPrime + numTmp
print("Sum of prime number:", sumPrime)
