import PySimpleGUI as sg

"""
    Demo - Graph Element Rescale Figures When Window Resizes

    This demo shows how you can redraw your Graph element's figures so that when
    you resize the window, all of the figures on the graph resize.

    There may be a tkinter method to help do this?

    Copyright 2022 PySimpleGUI
"""

gsize = (400,400)

layout = [  [sg.Text('Rescaling a Graph Element When Window is Resized')],
            [sg.Graph(gsize, (0,0),gsize, expand_x=True, expand_y=True, k='-G-', background_color='green')],
            [sg.Button('Exit'), sg.Sizegrip()]  ]

window = sg.Window('Graph Element Scale With Window', layout, finalize=True, resizable=True, enable_window_config_events=True)

graph = window['-G-']       #type: sg.Graph

orig_win_size = window.current_size_accurate()
# Draw the figure desired (will repeat this code later)
fig = window['-G-'].draw_circle((200, 200), 50, fill_color='blue')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == sg.WINDOW_CONFIG_EVENT:     # if get a window resized event
        # Determine how much the window was resized by and tell the Graph element the new size for the Canvas
        new_size = window.current_size_accurate()
        dx = orig_win_size[0]-new_size[0]
        dy = orig_win_size[1]-new_size[1]
        gsize = (gsize[0] - dx, gsize[1] - dy)
        orig_win_size = new_size
        graph.CanvasSize = gsize
        # Erase entire Graph and redraw all figures0
        graph.erase()
        # Redraw your figures here
        fig = window['-G-'].draw_circle((200, 200), 50, fill_color='blue')

window.close()
