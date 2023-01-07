import tkinter as tk

window = tk.Tk()   # class Tk
window.title('tkinter basics -button')   # title on screen
window.geometry('600x600')   # width x height of default screen

# button widget creation

# the unit of heigth and idth is text unit or width of one character
# fg is for font color
# command is for functionality

btn = tk.Button(master=window,
                text='Close',
                width='25',
                height='1',
                bg='red',
                fg='white',
                command=window.destroy
                )

# placing button on screen
btn.pack()


window.mainloop()