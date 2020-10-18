from Other import readExcel,writeExcel
while(True):
    con=input('Would you like to to Write or Read file?: ')
    if con=='W':
        writeExcel()
    elif con=='R':
        readExcel()
    else:
        break
