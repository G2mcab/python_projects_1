from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Digital Clock v.1')

label = Label(root, font = ('aerial50'), background = 'black', foreground = 'white')

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, time)

label.pack(anchor = 'center')
time()

mainloop()