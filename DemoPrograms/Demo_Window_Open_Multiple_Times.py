import PySimpleGUI as sg

"""
    Demo Restart Window (sorta reopen)
    
    Once a window is closed, you can't do anything with it.  You can't read it.  You can't "re-open" it.
    The only choice is to recreate the window.  It's important that you use a "Fresh Layout" every time.
    You can't pass the same layout from one indow to another.  You will get a popup error infomrning you
    that you've attempted to resuse a layout.

    The purpose of this demo is to show you the simple "make window" design pattern.  It simply makes a 
    window using a layout that's defined in that function and returns the Window object.  It's not a bad
    way to encapsulate windows if your applcation is gettinga little larger than the typical small data
    entry window.

    Copyright 2020 PySimpleGUI.org
"""


def make_window():
    """
    Defines a window layout and createws a indow using this layout.  The newly made Window
    is returned to the caller.

    :return: Window that is created using the layout defined in the function
    :rtype: Window
    """
    layout = [[sg.Text('My Window')],
              [sg.Input(key='-IN-'), sg.Text(size=(12, 1), key='-OUT-')],
              [sg.Button('Go'), sg.Button('Exit')]]

    return sg.Window('Window Title', layout)


def main():
    window = make_window()

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            window = make_window()
        elif event == 'Go':
            window['-OUT-'].update(values['-IN-'])


if __name__ == '__main__':
    main()