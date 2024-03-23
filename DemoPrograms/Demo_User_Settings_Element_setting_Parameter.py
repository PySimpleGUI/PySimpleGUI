import PySimpleGUI as sg

"""
    Demo - User Settings

    Using the PySimpleGUI 5 setting parameter.

    New in the PSG5 release is a capability to automatically save and restore values in elements.  Each element that has the capability has a parameter called "setting"
    
    Copyright 2020-2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""


def make_window():
    layout = [[sg.Text('Window with values saved between runs')],
              [sg.Input(key='-IN-', setting='My initial value')],
              [sg.Checkbox('Checkbox', key='-CB-', setting=True)],
              [sg.Button('Re-create Window'), sg.Button('Exit')]]

    window = sg.Window('Setting Example', layout, enable_close_attempted_event=True, print_event_values=True, auto_save_location=True)

    return window


def main():

    window = make_window()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit' or event == sg.WIN_CLOSE_ATTEMPTED_EVENT:
            window.settings_save(values)
            break

        if event == 'Re-create Window':         # You can also close and re-open a window using the values previously entered
            window.settings_save(values)
            window.close()
            window = make_window()

    window.close()


if __name__ == '__main__':
    main()