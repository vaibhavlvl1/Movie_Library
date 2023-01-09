"""
This is the main file of movie library
Pages:
    1 - Home
    2 - Movie List
    3 - Movie Detail
"""

from widget import Window, LeftFrame, RightFrame

if __name__=='__main__':

    # root window
    root = Window("Movie Library - Tkinter")

    # left frame
    left_frame = LeftFrame(root.window,'leftFrame')




    # right frame
    right_frame = RightFrame(root.window,'right frame')


    # mainloop()
    root.start_method()