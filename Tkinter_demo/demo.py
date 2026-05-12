from tkinter import *
window = Tk()
window.geometry('300x400')
window.title('first program')
window.config(bg = '#1e1e2f')

txt = Label(
    window,
    text = 'Hello world !',
    font =('Arial', 18, 'bold'),
    bg = '#1e1e2f',
    fg = 'cyan',
    pady = 20)


txt.pack()
window.mainloop()