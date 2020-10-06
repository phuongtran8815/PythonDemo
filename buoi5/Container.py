'''
Bài tập:
Một công ty vận tải cần quản lý thông tin danh sách các container trong cảng bao gồm:
Mã số container, ngày vào cảng, ngày dự kiến xuất khẩu, loại công là gì(công thường, công đông lạnh),
và trạng thái container(còn trong cảng hay đã xuất khẩu)
a) Xây dựng class để quản lý profile
b) cần viết hàm nhập 1 container trong class
c) Viết hàm xuất 1 container trong class
d) Từ đó cho phép nhập dữ liệu liên tục 1 danh sách container vào list.
e) Viết hàm thực hiện nhận vào danh sách container và sắp xếp theo thứ tự tăng dần đối với ngày vào cảng.
f) In ra danh sách container nào đã đến ngày xuất khẩu rồi mà vẫn còn trong cảng.
'''

from datetime import date
class Container:
    containerNumber = ""
    inTerminalDate = ""
    outTerminalEstimateDate = ""
    kindOfContainer = ""
    statusContainer = ""

    def __init__(self):
        pass

    def insertContainer(self):
        self.containerNumber = input("Please input container number: ")
        self.inTerminalDate = input("Please input terminal in date: ")
        self.outTerminalEstimateDate = input("Please input terminal estimated out date: ")
        self.kindOfContainer = input("Please input the kind of container: ")
        self.statusContainer = input("Please input container empty or full? ")

    def showContainer(self):
        print(self.containerNumber, self.inTerminalDate, self.outTerminalEstimateDate, self.kindOfContainer,self.statusContainer)

    def checkContainer(self):
        d = str(date.today())
        if(self.outTerminalEstimateDate < (d[0:4]+d[5:7]+d[8:10]) and self.statusContainer == 'Inyard'):
            return True
