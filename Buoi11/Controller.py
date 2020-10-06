from Buoi11.Student import Student

studentList=[]
while(True):
    s = Student()
    s.insertStudent()
    studentList.append(s)
    continueFlag = input('Ban co muon nhap tiep tuc Y/N? ')
    if continueFlag=='Y':
        continue
    else:
        break
for s in studentList:
    s.showStudentInfo()
