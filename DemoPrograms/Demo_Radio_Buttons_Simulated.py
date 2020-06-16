import PySimpleGUI as sg

"""
    This demo uses buttons to simulate radio buttons.
    
    In this demo the variable active_radio_button has the key for the currently active button

    Copyright 2020 PySimpleGUI.org
"""

radio_keys = ['Play', 'Stop', 'Pause', 'Off']
selected_color = ('red', 'white')
active_radio_button = None

layout = [  [sg.Text('My Window')],
            [sg.Text('These are simulated radio buttons')],
            [sg.Button(name) for name in radio_keys],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout, use_default_focus=False)

while True:             # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event in radio_keys:
        for k in radio_keys:
            window[k].update(button_color=sg.theme_button_color())
        window[event].update(button_color=selected_color)
        active_radio_button = event

window.close()