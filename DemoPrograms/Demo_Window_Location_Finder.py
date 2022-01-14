import PySimpleGUI as sg

"""
    Demo - Find window's location according to tkinter

    Drag this window around your multiple monitors.  It will show you where
    tkinter believes the corners are for the window.
    
    You can then use this information to locate your what to pass in the location
    parameter when you want to create a window at a specific spot.
    
    The value in the center is the screen dimensions for the primary window.

    Copyright 2021, 2022 PySimpleGUI
"""

sg.theme('dark green 7')
layout = [
            [sg.T(sg.SYMBOL_UP_ARROWHEAD),
             sg.Text(size=(None,1), key='-OUT-'),
             sg.Text(size=(None,1), key='-OUT2-',  expand_x=True, expand_y=True, justification='c'), sg.T(sg.SYMBOL_UP_ARROWHEAD)],
            [sg.T('Screen size: '),sg.T(sg.Window.get_screen_size()), sg.T(sg.SYMBOL_SQUARE)],
            [sg.T(sg.SYMBOL_DOWN_ARROWHEAD),
             sg.Text(size=(None,1), key='-OUT4-'),
             sg.Text(size=(None,1), key='-OUT3-',  expand_x=True, expand_y=True, justification='r'), sg.T(sg.SYMBOL_DOWN_ARROWHEAD, justification='r')],
            ]

window = sg.Window('Title not seen', layout, grab_anywhere=True, no_titlebar=True, margins=(0,0), element_padding=(0,0), right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT, keep_on_top=True, font='_ 25', finalize=True, transparent_color=sg.theme_background_color())

while True:
    event, values = window.read(timeout=100)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Edit Me':
        sg.execute_editor(__file__)

    loc = window.current_location()
    window['-OUT-'].update(loc)
    window['-OUT2-'].update((loc[0]+window.size[0], loc[1]))
    window['-OUT3-'].update((loc[0]+window.size[0], loc[1]+window.size[1]))
    window['-OUT4-'].update((loc[0], loc[1]+window.size[1]))

window.close()
