class Customer:
    id = ""
    name = ""

    def importCus(self):
        listCus = []
        while (True):
            self = Customer()
            self.id = input("Vui lòng nhập ID Khách hàng: ")
            self.name = input("Vui lòng nhập tên Khách hàng: ")
            listCus.append(self)
            con = input("Bạn có muốn nhập tiếp không? (Y/N) ")
            if con == "N": break
        return listCus

    def removeCus(self, id, listCus):
        for cus in listCus:
            if cus.id == id: #listCus = [['001', 'Toan']]
                listCus.remove(cus)
        return listCus

c = Customer()
listCustomer = c.importCus()
c.removeCus(input("Nhập ID Khách hàng cần xóa: "), listCustomer)
for i in listCustomer:
    print("Hi", i.name)


