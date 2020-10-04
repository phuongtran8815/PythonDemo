from abc import ABC,abstractmethod

class Person(ABC):
    name = ""
    age=0

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    @abstractmethod
    def calculationAge(self):
        pass

class Employee(Person):
    employeeID = ""
    def calculationAge(self):
        print("Calculation age from abstract class")

e=Employee()
#p=Person()# Khong the khoi tao doi tuong p tu class abstract
