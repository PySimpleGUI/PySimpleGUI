import PySimpleGUI as sg

"""
    Simple template window that saves position.

    Rather than starting in the middle of the screen, this code will save the position the window was in when it last exited.

    There are 2 ways to implement this.  
        1. The hard way is to save/recall the location yourself as shown in the manual_method func
        2. The easy way is to set the auto_save_location parm=True when creating your Window
    
    Copyright 2018-2026 PySimpleGUI. All rights reserved.
"""
def manual_method():
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


def automatic_method():
    layout = [[sg.Text('Window that Auto-saves position', font='_ 25')],
              [sg.Button('Ok'), sg.Button('Exit')]]

    window = sg.Window('Auto-saves Location', layout, auto_save_location=True)

    while True:
        event, values = window.read()
        if event in ('Exit', sg.WIN_CLOSED):
            break

    window.close()



if __name__ == '__main__':
    automatic_method()