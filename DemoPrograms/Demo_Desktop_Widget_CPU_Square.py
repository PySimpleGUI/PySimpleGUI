import PySimpleGUI as sg
import psutil

"""
    Another simple Desktop Widget using PySimpleGUI
    This time a RAM indicator.  The Widget is square.  
    The bottom section will be shaded to 
    represent the total amount CPU currently in use.
    Uses the theme's button color for colors.

    Copyright 2020 PySimpleGUI.org
"""

ALPHA = 0.5
THEME = 'Dark purple 6 '
GSIZE = (160, 160)
UPDATE_FREQUENCY_MILLISECONDS = 2 * 1000


def human_size(bytes, units=(' bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB')):
    """ Returns a human readable string reprentation of bytes"""
    return str(bytes) + ' ' + units[0] if bytes < 1024 else human_size(bytes >> 10, units[1:])


sg.theme(THEME)

graph = sg.Graph(GSIZE, (0, 0), GSIZE, key='-GRAPH-', enable_events=True)
layout = [[graph]]

window = sg.Window('CPU Usage', layout, no_titlebar=True, grab_anywhere=True, margins=(0, 0), element_padding=(0, 0), alpha_channel=ALPHA, finalize=True)

text_id2 = graph.draw_text(f'CPU', (GSIZE[0] // 2, GSIZE[1] // 4), font='Any 20', text_location=sg.TEXT_LOCATION_CENTER,                               color=sg.theme_button_color()[0])


while True:  # Event Loop
    # ----------- update the graphics and text in the window ------------
    cpu_percent = psutil.cpu_percent(interval=1)
    # Draw the filled rectangle
    rect_height = int(GSIZE[1] * float(cpu_percent) / 100)
    rect_id = graph.draw_rectangle((0, rect_height), (GSIZE[0], 0), fill_color=sg.theme_button_color()[1], line_width=0)
    # Draw the % used text and the close "X" on bottom
    text_id1 = graph.draw_text(f'{int(cpu_percent)}%', (GSIZE[0] // 2, GSIZE[1] // 2), font='Any 40', text_location=sg.TEXT_LOCATION_CENTER, color=sg.theme_button_color()[0])
    text_id3 = graph.draw_text('❎', (0, 0), font='Any 8', text_location=sg.TEXT_LOCATION_BOTTOM_LEFT, color=sg.theme_button_color()[0])
    # put the bar behind everything else
    graph.send_figure_to_back(rect_id)

    # update the window, wait for a while, then check for exit
    event, values = window.read(timeout=UPDATE_FREQUENCY_MILLISECONDS)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == '-GRAPH-':  # exit if clicked in the bottom left 20 x 20 pixel area
        if values['-GRAPH-'][0] < 20 and values['-GRAPH-'][1] < 20:
            break
    # erase figures so they can be redrawn
    graph.delete_figure(rect_id)
    graph.delete_figure(text_id1)
    graph.delete_figure(text_id3)
window.close()
