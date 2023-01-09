import tkinter as tk
from data.colors import COLORS
from data.geometry import GEOMETRI
class Window:
    """
    it creates tkinter main window
    """

    def __init__(self,title):
        self.window=tk.Tk()
        self.window.title(title)
        self.window.configure(bg=COLORS.BLACK)
        self.set_size()

    # start window mainloop
    def start_method(self):
        self.window.mainloop()

    # method for window height and width
    def set_size(self,):
        w, h = GEOMETRI.MAIN_WINDOW_WIDTH, GEOMETRI.MAIN_WINDOW_HEIGHT
        self.window.geometry('%dx%d'%(w,h))