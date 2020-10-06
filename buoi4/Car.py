'''
class Car:
    color = ""
    lable = ""

    def __init__(self,c,l):
        self.color = c
        self.lable = l

    def insertNewCar(self):
        print("Insert new car")

    def deleteACar(self):
        print("Delete a car")

    def updateACar(self):
        print("Update a car")

    def findACar(self):
        print("Find a car")

mer = Car()
mer.lable = "Mercedes car"
mer.color = "Black"

bmw = Car()
bmw.lable = "BMW car"
bmw.color = "White"

audi = Car("Red", "Audi")
print(audi.lable, audi.color)

'''
