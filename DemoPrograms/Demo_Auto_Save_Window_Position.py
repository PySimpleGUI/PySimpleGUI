import PySimpleGUI as sg

"""
    Simple template window that saves position.

    Rather than starting in the middle of the screen, this code will save the position the window was in when it last exited.

    To pull this off it's going to be.... super.....?hard?
    No... of course it's going to be... SIMPLE

    There is one added line of code.  When the user attempts to close the window, that's when the position is saved.
    When the program starts, it reads the previously saved position as part of the window creation.  User Settings APIs rock!

    Copyright 2021 PySimpleGUI
"""

layout = [[sg.Text('Window that Auto-saves position', font='_ 25')],
          [sg.Button('Ok'), sg.Button('Exit')]]

window = sg.Window('Auto-saves Location', layout, enable_close_attempted_event=True, location=sg.user_settings_get_entry('-location-', (None, None)))

while True:
    event, values = window.read()
    print(event, values)
    if event in ('Exit', sg.WINDOW_CLOSE_ATTEMPTED_EVENT):
        sg.user_settings_set_entry('-location-', window.current_location())  # The line of code to save the position before exiting
        break

window.close()
