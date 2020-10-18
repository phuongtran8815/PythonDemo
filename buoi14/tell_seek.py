f = open("TextReadFile.txt",'r',encoding = 'utf-8')
a = f.read(12) # đọc 12 kí tự đầu tiên
print('Nội dung là: \n', (a))

b = f.tell() # Kiểm tra vị trí hiện tại
print ('Vị trí hiện tại: ', (b))

f.seek(0) # Đặt lại vị trí con trỏ tại vị trí đầu file
c = f.read()
print('Nội dung mới là: \n', (c))
