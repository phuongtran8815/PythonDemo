import tkinter.messagebox

def add(number1 = 0, number2 = 0):
    return number1+number2

def sub(number1 = 0, number2 = 0):
    return number1-number2

def multi(number1 = 0, number2 = 0):
    return number1*number2

def dev(number1 = 0, number2 = 0):
    try:
        return number1/number2
    except ZeroDivisionError:
        print("Chia cho 0 roi")
        tkinter.messagebox.showinfo(title="Warning!!!", message="Number 2 must be different 0")
