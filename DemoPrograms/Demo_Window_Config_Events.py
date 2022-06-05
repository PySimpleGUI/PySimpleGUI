import PySimpleGUI as sg

"""
    Demo Window Config Events

    The Window object has a parameter enable_window_config_events that when set to True will
    cause sg.WINDOW_CONFIG_EVENT events to be generated when the window is moved or resized.

    Note that if you move the window using the Titlebar supplied by the operating system, then you
    will only get an event at the end of the window being moved.  If you want to receive numerous
    events during the movement, then you can achieve this using a grab_anywhere setting either
    at the window level or on a single element as shown in this demo.

    Copyright 2022 PySimpleGUI
"""

layout = [  [sg.Text('Demonstration of the enable_window_config_events')],
            [sg.Text('Grab me HERE for continuous location changed events', grab=True, text_color=sg.theme_background_color(), background_color=sg.theme_text_color())],
            [sg.Text(key='-OUT-', font='_18')],
            [sg.VPush()],
            [sg.Button('Go'), sg.Button('Exit'), sg.Sizegrip()]  ]

window = sg.Window('Window Title', layout, resizable=True, enable_window_config_events=True, finalize=True)

window.set_min_size(window.current_size_accurate())

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == sg.WINDOW_CONFIG_EVENT:
        window['-OUT-'].update(f'Size: {window.current_size_accurate()}\nLocation:{window.current_location()}')

window.close()
