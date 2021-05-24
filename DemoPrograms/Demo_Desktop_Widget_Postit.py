import PySimpleGUI as sg

"""
    Demo Desktop Widget Postit

    Sizegrip Element is used to make a window without a titlebar be resizable.

    There are 3 lines
    1. Make the window
    2. Set initial size of window as the minimum
    3. Read any event from the window which will close the window and return

    Note that while the window has no scrollbar, you can still use the mousewheel to scroll
    
    Copyright 2021 PySimpleGUI
"""

# ----- Make the window -----
window = sg.Window('Postit', [[sg.T('Postit Note', text_color='black', background_color='#FFFF88')],
                              [sg.ML(size=(30, 5), background_color='#FFFF88', no_scrollbar=True, k='-ML-', border_width=0, expand_y=True, expand_x=True),
                               sg.Sizegrip(background_color='#FFFF88')]],
                                no_titlebar=True, grab_anywhere=True, margins=(0, 0), background_color='#FFFF88', element_padding=(0, 0),
                                right_click_menu=sg.MENU_RIGHT_CLICK_EXIT, keep_on_top=True, font='_ 20', resizable=True, finalize=True)

# ----- Make sure it doesn't get any smaller than it is initially -----
window.set_min_size(window.size)

# ----- Read the window and wait for any event.
# ----- Any event will cause the read to return
# ----- Has a right click menu that can be used to choose exit
window.read(close=True)
