"""
    Demo Execute Py - Using the PySimpleGUI Execute APIs

    Creating a virtual environment using PySimpleGUI & sg.execute_py_file()

    This Demo's purpose is to show the link between Execute APIs to the Global User Settings

    The function execute_py_file() uses the interpreter set in the Global Settings
    To see and change global settings, call main_global_pysimplegui_settings()
    Or you can use the "Global Settings" button found in the sg.main()

    If you have set an interpreter in your global settings, then this is what will be
        used when calling execute_py_file.  It nothing is set, then the default python
        interpreter will be used

    Demo also shows another handy function, main_get_debug_data, which returns a string with
        version numbers for Python tkinter, PySimpleGUI

    http://www.PySimpleGUI.org
    Copyright 2021 PySimpleGUI
"""

import PySimpleGUI as sg


def main():
    # --------- Define layout and create Window -------
    layout = [  [sg.Text('User Exec API Demo', font='_ 18')],
                [sg.T(sg.main_get_debug_data(True))],
                [sg.T('Python Version', text_color='yellow'),
                 sg.T(f'{sg.sys.version_info.major}.{sg.sys.version_info.minor}.{sg.sys.version_info.micro}', text_color = 'yellow')],
                [sg.B('Global Settings'), sg.B('Relaunch'), sg.B('Main'), sg.B('Refresh'), sg.Exit()],
                ]

    window = sg.Window('Execute Py File Demo', layout, keep_on_top=True, font='_ 14')

    # --------- Event Loop -------
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event.startswith('Global'):
            sg.main_global_pysimplegui_settings()
        elif event == 'Relaunch':
            sg.execute_py_file(__file__)        # Run using Global Settings to determine which python version to use
        elif event == 'Main':
            sg.main()

    # --------- After event loop ---------
    window.close()


if __name__ == '__main__':
    main()