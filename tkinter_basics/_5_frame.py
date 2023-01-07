import tkinter as tk
from tkinter import Frame,Button

# Frame is ciontainer that holds other widgets


window = tk.Tk()
window.title('Frames')
window.geometry('600x400')


# frame widget
frame = Frame(master=window)
#button widget
btnleft = Button(master=frame,text='Left Frame button',bg='black',fg='white')
btnright = Button(master=frame,text='Right Frame button',bg='black',fg='white')



# widgets placement
frame.pack()
btnleft.pack(side=tk.LEFT)
btnright.pack(side=tk.RIGHT)


window.mainloop()