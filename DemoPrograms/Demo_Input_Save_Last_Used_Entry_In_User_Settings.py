import PySimpleGUI as sg

"""
    Demo - Save previously entered value in Input element by using user_settings calls

    Tired of typing in the same value or entering the same filename into an Input element?
    If so, this may be exactly what you need.
    
    It simply saves the last value you entered so that the next time you start your program, that will be the default

    Copyright 2022 PySimpleGUI.org
"""


def main():
    sg.user_settings_filename(path='.')  # The settings file will be in the same folder as this program

    layout = [[sg.T('This is your layout')],
              [sg.T('Remembers last value for this:'), sg.In(sg.user_settings_get_entry('-input-', ''), k='-INPUT-')],
              [sg.OK(), sg.Button('Exit')]]

    # make a window, read it, and automatically close after 1 event happens (button or X to close window)
    event, values = sg.Window('Save Input Element Last Value', layout).read(close=True)

    # only save the value if OK was clicked
    if event == 'OK':
        sg.user_settings_set_entry('-input-', values['-INPUT-'])

if __name__ == '__main__':
    main()

