from tkinter import *
from tkinter import messagebox

def addition():
    num1 = int(num1_entery.get())
    num2 = int(num2_entery.get())
    sum = num1 + num2
    messagebox.showinfo(message=f'Addition:{sum}')