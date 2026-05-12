from tkinter import *
from tkinter import messagebox

def changebg():
    val = x.get()
    #val = x.set(1)
    if(val == 1):
        window.config(bg='black')
    elif(val == 2):
        window.config(bg='pink')
    elif(val == 3):
        window.config(bg='blue')
    else:
       messagebox.showwarning(message='No color selected.')
       #window.config(bg='black')

window = Tk()
window.geometry('300x400')

x = IntVar()
x.set(1)
changebg()
txt = Label(window, text='Please select color:')
txt.pack() #for position pack

rdo1 = Radiobutton(window, text='black', variable= x, value=1)
rdo1.pack()

rdo2 = Radiobutton(window, text='pink', variable= x, value=2)
rdo2.pack()

rdo3 = Radiobutton(window, text='blue', variable= x, value=3)
rdo3.pack()

btn = Button(window,text='Apply', command=changebg)
btn.pack()


window.mainloop()