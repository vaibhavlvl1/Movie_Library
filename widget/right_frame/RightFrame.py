import tkinter as tk
from data.colors import COLORS
from page import Home

class RightFrame:
    """
    it will hold pages on the right frame
    """

    bg_color = COLORS.ORANGE
    def __init__(self,window,name, relief=tk.SUNKEN,side=tk.LEFT):
        self.frame = tk.Frame(
            master=window,
            name=name,
            relief=relief,
            bg=RightFrame.bg_color
            )

        self.side = side
        self.add_frame()

    def add_frame(self):
        # frame content
        self.frame_content()
        self.frame.pack(side=self.side,fill=tk.BOTH,expand=True)

    def frame_content(self,page_name='home'):
        if page_name=='home':
            # add home page
            Home(self.frame, RightFrame.bg_color)
        elif page_name=="movieList":
            # add movielist
            pass
        elif page_name =='movieDetail':
            # add movie detail
            pass
