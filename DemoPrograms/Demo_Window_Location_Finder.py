import PySimpleGUI as sg

"""
    Demo - Find window's location according to tkinter

    Drag this window around your multiple monitors.  It will show you where
    tkinter believes the upper left corner of the window is located.
    You can then use this information to locate your windows when you create them

    Copyright 2021 PySimpleGUI
"""

layout = [  [sg.T(sg.SYMBOL_UP_ARROWHEAD + ' Position')],
            [sg.Text(size=(12,1), key='-OUT-', justification='c')]]

window = sg.Window('Title not seen', layout, grab_anywhere=True, no_titlebar=True, margins=(0,0), element_padding=(0,0), right_click_menu=sg.MENU_RIGHT_CLICK_EXIT, keep_on_top=True, font='_ 25')

while True:
    event, values = window.read(timeout=100)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    window['-OUT-'].update(window.current_location())

window.close()
