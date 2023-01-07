import tkinter as tk
from tkinter import Text
# Text is multiple line text input

window = tk.Tk()
window.title('Text')
window.geometry('600x400')

# text area creation
txt = Text(window,height=5,width=40)



# text area placement
txt.pack()


window.mainloop()