import tkinter as tk
import tkinter.messagebox
from email import message
from tkinter import Label, Entry, Button
from action import *
import re

def cong():
    partern = "[0-9]+"
    s1 = re.fullmatch(pattern= partern, string=entryNumber1.get())
    s2 = re.fullmatch(pattern= partern, string=entryNumber2.get())
    # print(s1)
    if s1 != None and s2 != None:
        ketQua = add(int(entryNumber1.get()), int(entryNumber2.get()))
        entryResult.insert(0, str(ketQua))
    else:
        tkinter.messagebox.showinfo(title="Warning!!!", message="Please check number 1 and 2!")
def chia():
    ketQua = dev(int(entryNumber1.get()), int(entryNumber2.get()))
    entryResult.insert(0, str(ketQua))

root = tk.Tk()
root.title("My Calculation")

#Design titel label "Calculation"
lableTitelForm = Label(text="Calculation")
lableTitelForm.config(font=("Tahoma", 20))
#Design titel label "Number 1"
lableNumber1 = Label(text="Number 1")
lableNumber1.config(font=("Tahoma", 15))
#Design Entry of number 1
entryNumber1 = Entry()
#Design titel label "Number 2"
lableNumber2 = Label(text="Number 2")
lableNumber2.config(font=("Tahoma", 15))
#Design Entry of number 2
entryNumber2 = Entry()
#Design titel label "Result"
lableResult = Label(text="Result")
lableResult.config(font=("Tahoma", 15))
#Design Entry of Result
entryResult = Entry()
#Design button

buttonAdd = Button(text = "Add", command = cong)
buttonSub = Button(text = "Sub")
buttonMulti = Button(text = "Multi")
buttonDev = Button(text = "Dev", command = chia)

lableTitelForm.grid(row=0, column=1)
lableNumber1.grid(row=1, column=0)
lableNumber2.grid(row=2, column=0)
lableResult.grid(row=3, column=0)
entryNumber1.grid(row=1, column=1)
entryNumber2.grid(row=2, column=1)
entryResult.grid(row=3, column=1)
buttonAdd.grid(row=1, column=2)
buttonSub.grid(row=2, column=2)
buttonMulti.grid(row=3, column=2)
buttonDev.grid(row=4, column=2)

# lableTitelForm.pack()
# buttonDev.pack()
# buttonMulti.pack()
# buttonSub.pack()
# buttonAdd.pack()
# entryResult.pack()
# lableResult.pack()
# entryNumber2.pack()
# entryNumber1.pack()
# lableNumber2.pack()
# lableNumber1.pack()

root.mainloop()
