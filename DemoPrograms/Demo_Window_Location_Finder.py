import PySimpleGUI as sg

"""
    Demo - Find window's location according to tkinter

    Drag this window around your multiple monitors.  It will show you where
    tkinter believes the corners are for the window.
    
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

# make the graph elements that draw squares in each corner
GSIZE = 50          # Size of the squars.  Should be large enough to cover a row-frame top to bottom to that they are in the corners firmly

graph_ul = sg.Graph((GSIZE,GSIZE), (1,GSIZE), (GSIZE,1), key='-UPPER_LEFT-', expand_x=True, expand_y=True)
graph_ur = sg.Graph((GSIZE,GSIZE), (1,GSIZE), (GSIZE,1), key='-UPPER_RIGHT-', expand_x=True, expand_y=True)
graph_ll = sg.Graph((GSIZE,GSIZE), (1,GSIZE), (GSIZE,1), key='-LOWER-LEFT-', expand_x=True, expand_y=True)
graph_lr = sg.Graph((GSIZE,GSIZE), (1,GSIZE), (GSIZE,1), key='-LOWER-RIGHT-', expand_x=True, expand_y=True)

layout = [
            [graph_ul,
             sg.T('↖', p=0, expand_x=True, expand_y=True),
             sg.Text(size=(None,1), key='-OUT-', expand_x=True, expand_y=True),
             sg.Text(size=(None,1), key='-OUT2-',  expand_x=True, expand_y=True, justification='c'),
             sg.T('↗', expand_x=True, expand_y=True),
             graph_ur],
            [sg.T('Screen size: '),sg.T(sg.Window.get_screen_size())],
            [graph_ll,
             sg.T('↙', expand_x=True, expand_y=True),
             sg.Text(size=(None,1), key='-OUT3-', expand_x=True, expand_y=True),
             sg.Text(size=(None,1), key='-OUT4-',  expand_x=True, expand_y=True, justification='r'),
             sg.T('↘', justification='r', expand_x=True, expand_y=True),
             graph_lr],
            ]

window = sg.Window('Title not seen', layout, grab_anywhere=True, no_titlebar=True, margins=(0,0), element_padding=(0,0), right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT, keep_on_top=True, font='Courier 25', finalize=True, transparent_color=sg.theme_background_color(), enable_window_config_events=True, auto_save_location=True)

# Draw the squares in the corners
graph_ul.draw_rectangle((1,1), (GSIZE, GSIZE), fill_color=sg.theme_text_color(), line_width=0)
graph_ur.draw_rectangle((1,1), (GSIZE, GSIZE), fill_color=sg.theme_text_color(), line_width=0)
graph_ll.draw_rectangle((1,1), (GSIZE, GSIZE), fill_color=sg.theme_text_color(), line_width=0)
graph_lr.draw_rectangle((1,1), (GSIZE, GSIZE), fill_color=sg.theme_text_color(), line_width=0)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Edit Me':
        sg.execute_editor(__file__)

    loc = window.current_location()
    window['-OUT-'].update(f'({loc[0]:4},{loc[1]:4})')
    window['-OUT2-'].update(f'{loc[0]+window.size[0]:4},{loc[1]:4}')
    window['-OUT3-'].update(f'{loc[0]:4},{loc[1]+window.size[1]:4}')
    window['-OUT4-'].update(f'{loc[0]+window.size[0]:4},{loc[1]+window.size[1]:4})')

window.close()
