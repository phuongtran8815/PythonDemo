from Container import Container
containerList=[]

while(True):
    c=Container()
    c.insertContainer()
    containerList.append(c)
    continueFlag = input('Ban co muon nhap tiep tuc Y/N? ')
    if continueFlag=='Y':
        continue
    else:
        break
for c in containerList:
    c.showContainer()

def sapXepContainer(dsContainers):
    for i in range(0,len(dsContainers)):
        for j in range(i+1, len(dsContainers)):
            if (dsContainers[i].inTerminalDate>dsContainers[j].inTerminalDate):
                temp=dsContainers[i]
                dsContainers[i]=dsContainers[j]
                dsContainers[j]=temp
    return dsContainers

for i in sapXepContainer(containerList):
    i.showContainer()

for c in containerList:
    if(c.checkContainer()==True):
        print(c.containerNumber,"da bi qua han")
