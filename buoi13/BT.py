#listSo=[1,2,3,4,5,6]
def myFunction(listSN):
    try:
        print(listSN[10])
    except IndexError:
        raise

