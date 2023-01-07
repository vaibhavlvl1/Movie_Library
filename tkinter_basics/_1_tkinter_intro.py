"""
tkinter
GUI applications

Life cycle:
1- import tkinter
2 - main window(entry point )
3 - widgets ...
4 - Mainloop (to keep app alive)

"""
import tkinter as tk

# create main window
m = tk.Tk()



"""
after main window
Widgets are control (buttons,text,label,frame)

widget placement
1.- pack() - puts widgets one after another (top to bottom or from lef to right)
2.- grid() - widgets are put in grif ( row and column based)
3.- place() -  puts widgets in exact location on window (ex x = 100, y =300, etx)

"""




# last line main loop
m.mainloop()