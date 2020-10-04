from datetime import date
class Container():
    __number = ""
    __height = 0.0
    __inTerminalDate = ""
    __outTerminalEstimateDate = ""
    __kindOfContainer = ""
    __statusContainer = ""

    def setContainerNumber(self, id):
        self.__number = id
    def getContainerNumber(self):
        return self.__number
    def setContainerHeight(self, h):
        self.__height = h
    def getContainerHeight(self):
        return self.__height
    def setContainerInTerminalDate(self, d):
        self.__inTerminalDate = d
    def getContainerInTerminalDate(self):
        return self.__inTerminalDate
    def setContainerOutTerminalEstimateDate(self, d):
        self.__outTerminalEstimateDate = d
    def getContainerOutTerminalEstimateDate(self):
        return self.__outTerminalEstimateDate
    def setContainerKindOf(self, k):
        self.__kindOfContainer = k
    def getContainerKindOf(self):
        return self.__kindOfContainer
    def setContainerStatus(self, s):
        self.__statusContainer = s
    def getContainerStatus(self):
        return self.__statusContainer

    def insertContainer(self):
        self.setContainerNumber(input("Please input container number: "))
        self.setContainerInTerminalDate(input("Please input terminal in date: "))
        self.setContainerOutTerminalEstimateDate(input("Please input terminal estimated out date: "))
        self.setContainerKindOf(input("Please input the kind of container: "))
        self.setContainerStatus(input("Please input container empty or full? "))

    def showContainer(self):
        print(self.__number, self.__inTerminalDate, self.__outTerminalEstimateDate,
              self.__kindOfContainer, self.__statusContainer)

    def checkContainer(self):
        d = str(date.today())
        if(self.__outTerminalEstimateDate < (d[0:4]+d[5:7]+d[8:10]) and self.__statusContainer == 'Inyard'):
            return True
