import tkinter as tk
from tkinter import Label,Entry
# label is read only text on screen
# Entry is one line text box

window = tk.Tk()
window.title('Label entry')
window.geometry('500x500')

# Lable widgets

lblName = Label(master=window,text='Name')
lblName.grid(row=0)

lblLastName = Label(window,text = 'Last Name')
lblLastName.grid(row=1)

# Entry widgets

entName = Entry(window)
entLastName = Entry(window)

entName.grid(row=0,column=1)
entLastName.grid(row=1,column=1)


window.mainloop()