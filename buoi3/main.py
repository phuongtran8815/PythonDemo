#Bai 1: Sap xep danh sach so nguyen tang dan ve gia tri
listRandom = [1,5,3,7,4,29]
l = len(listRandom)
for i in range(0,l):
    for j in range(i+1,l):
        if listRandom[i] > listRandom[j]:
            temp = listRandom[i]
            listRandom[i] = listRandom[j]
            listRandom[j] = temp
print(listRandom)

#Bai 2: Tim ra phan tu lon thu 2 trong danh sach
setA = set(listRandom)
setA.remove(max(setA))
print(max(setA))


