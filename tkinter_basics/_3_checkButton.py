import tkinter as tk

#window creation
window = tk.Tk()
window.title('check button using tkinter')
window.geometry('600x600')

# button creation
chkBtn_1 = tk.Checkbutton(master=window, text='Correct')
chkBtn_2 = tk.Checkbutton(master=window, text='Incorrect')

# button placement
chkBtn_1.grid(row=0, column=0)
chkBtn_2.grid(row=1, column=0)


# to keep app alive
window.mainloop()