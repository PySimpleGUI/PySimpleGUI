"""
    Demo_Close_Attempted_Event

    Catches if a window close was tried by user (click "X") and confirms with a popup.
    Requires PySimpleGUI 4.33.0 and later

    Copyright 2021-2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

import PySimpleGUI as sg

layout = [[sg.Text('Close confirmation demo')],
          [sg.Text('Try closing window with the "X"')],
          [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout, enable_close_attempted_event=True)

while True:
    event, values = window.read()
    print(event, values)
    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
        break

window.close()
