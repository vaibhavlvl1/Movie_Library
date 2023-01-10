import tkinter as tk
from data.colors import COLORS
from data.menus import MENU
# exact import to avoid circular error
from widget.button.Button import Buttons
from widget.right_frame.RightFrame import RightFrame

class LeftFrame:
    """
    class for left frame to hold menu buttons
    """

    def __init__(self,window,name):
        self.frame = tk.Frame(master = window,name=name,bg=COLORS.BLACK
                              )

        self.master = window
        self.add_frame()
        self.add_menus()

    def add_frame(self):
        self.frame.pack(side=tk.LEFT, fill=tk.Y, pady=(62,0))

    # method for click event of menu button
    def handle_click(self,event):
        self.manage_button_colors(event)
        page_name = str(event.widget).split('.')[2]
        #print('Page {} is clicked'.format(page_name))

        # self is left frame whose master is root home page
        rightFrame = self.master.children['right frame']

        # destroy children
        RightFrame.destroy_children(rightFrame)

        # add new page as page_name
        RightFrame.frame_content(rightFrame,page_name)



    def add_menus(self):
        # add menu in loop . menu is dict
        for menu_key ,menu_text in MENU.items():
            if menu_key=='about':
                button = Buttons(self.frame,menu_key,menu_text,
                                 COLORS.ORANGE,COLORS.BLACK,
                                 18, 2, handle_click=self.handle_click,
                                 side=tk.BOTTOM,)
            else:
                button = Buttons(self.frame, menu_key, menu_text,
                                 COLORS.ORANGE, COLORS.BLACK,
                                 18, 2,handle_click=self.handle_click,)

    def manage_button_colors(self,event):
        for child in event.widget.master.winfo_children():
            if child==event.widget:
                child.configure(bg=COLORS.ORANGE,fg=COLORS.WHITE)
            else:
                child.configure(bg=COLORS.BLACK,fg=COLORS.ORANGE)

