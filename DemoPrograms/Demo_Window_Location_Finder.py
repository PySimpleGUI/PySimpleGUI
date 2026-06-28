import PySimpleGUI as sg

"""
    Demo - Find window's location according to tkinter

    Drag this window around your multiple monitors.  It will show you where
    tkinter believes the corners are for the window.  Grab the squares on the sides to move
    
    You can then use this information to locate your what to pass in the location
    parameter when you want to create a window at a specific spot.
    
    This tool is particularly helpful when you have multiple monitors and want to know
        the x,y coordinates for a spot on any of your monitors
    
    The value in the center is the screen dimensions for the primary window.

    Note.... you can use Control+Arrow keys to move this window when your mouse 
        is over any of the text/graphics of the window

    Copyright 2018-2026 PySimpleGUI. All rights reserved.
"""

sg.theme('dark green 7')


layout = [[ sg.Text(key='-OUT-', ), sg.Push(), sg.Text(key='-OUT2-')],
          [ sg.T(sg.SYMBOL_SQUARE), sg.T('Screen size'),sg.Push(), sg.T(sg.Window.get_screen_size()), sg.T(sg.SYMBOL_SQUARE)],
          [ sg.Text(key='-OUT3-'),sg.Push(), sg.Text(key='-OUT4-')]]

layout = [[sg.Frame('', layout, expand_x=True, expand_y=True, border_color=sg.theme_text_color(), border_width_no_relief=6)],]

window = sg.Window('Title not seen', layout, grab_anywhere=True, no_titlebar=True, margins=(0,0), element_padding=(0,0), right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT, keep_on_top=True, font='Courier 20', finalize=True, transparent_color=sg.theme_background_color(), enable_window_config_events=True, auto_save_location=True)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Edit Me':
        sg.execute_editor(__file__)

    loc = window.current_location()

    window['-OUT-'].update(f'({loc[0]},{loc[1]})')
    window['-OUT2-'].update(f'({loc[0]+window.size[0]},{loc[1]})')
    window['-OUT3-'].update(f'({loc[0]},{loc[1]+window.size[1]})')
    window['-OUT4-'].update(f'({loc[0]+window.size[0]},{loc[1]+window.size[1]})')

window.close()
