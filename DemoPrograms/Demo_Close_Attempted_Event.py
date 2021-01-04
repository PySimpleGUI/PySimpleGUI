import PySimpleGUI as sg

"""
    Demo_Close_Attempted_Event

    Catches if a window close was tried by user (click "X") and confirms with a popup.
    Requires PySimpleGUI 4.33.0 and later

    Copyright 2021 PySimpleGUI Inc.
"""

layout = [[sg.Text('Close confirmation demo')],
          [sg.Text('Try closing window with the "X"')],
          [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout, enable_close_attempted_event=True)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
        if sg.popup_yes_no('Do yuou really want to exit?') == 'Yes':
            break
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

window.close()
