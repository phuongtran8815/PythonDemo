class Student():
    __name = ""
    __age = 0
    __address = ""
    __gender = ""

    def setNameStudent(self,n):
        self.__name = n
    def getNameStudent(self):
        return self.__name
    def setAgeStudent(self,a):
        self.__age = a
    def getAgeStudent(self):
        return self.__age
    def setAddressStudent(self,a):
        self.__address = a
    def getAddressStudent(self):
        return self.__address
    def setGenderStudent(self,g):
        self.__gender = g
    def getGenderStudent(self):
        return self.__gender
    def insertStudent(self):
        self.__name = input("Please input student name: ")
        self.__age = input("Please input student age: ")
        self.__address = input("Please input student address: ")
        self.__gender = input("Please input student gender (M/F): ")
    def showStudentInfo(self):
        print("Name of student:", self.__name)
        print("Age of student:", self.__age)
        print("Address of student:", self.__address)
        print("Gender of student:", self.__gender)
