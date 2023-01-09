import tkinter as tk
from data.colors import COLORS
class Buttons:
    """
    it will create tkinter button
    """
    def __init__(self,window,name,text,
                 fg,bg,
                 width,height,
                 handle_click,
                 padx=0, pady=0,

                 side=tk.TOP):

        self.button = tk.Button(master = window, name = name,text = text,fg=fg,
                             bg=bg,width=width,height=height,
                             activebackground=COLORS.ORANGE)

        self.padx = padx
        self.pady=pady
        self.side=side
        self.add_button()
        self.bind_event(handle_click)


    def add_button(self):
        self.button.configure(font=('Arial',12))
        self.button.pack(padx=self.padx,
                         pady=self.pady,
                         side=self.side)


    # event binding to button

    def bind_event(self,handle_click):
        # in tkinter binding is done by bind()
        self.button.bind('<Button-1>',handle_click)
