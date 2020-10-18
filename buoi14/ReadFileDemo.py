def readOnlyFunction():
    f=open(file="TextReadFile.txt",mode="r")
    try:
        a=f.read(5)
        b=f.read(5)
        print(a)
        print(b)
        print(f.read())
        print(f.readline())
        l=f.readlines()
        print(l[0],l[1])
    except:
        print("Khong cho phep ghi")
def readAndWriteFunction():
    path='D:\my_file.txt'
    mode="r+"
    try:
        f=open(file=path,mode=mode)
        f.write("Dong moi duoc them vao")
        print("Ghi noi dung thanh cong!!!")

    except FileNotFoundError:
        print("Khong tim thay duong dan file")

    finally:
        f.close()

readAndWriteFunction()
