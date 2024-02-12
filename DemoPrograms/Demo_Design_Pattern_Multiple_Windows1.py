import PySimpleGUI as sg

"""
    Design pattern multiple windows
    Using read_all_windows()
    
    Only 1 window at a time is visible/active on the screen.
    
    Window1 opens Window2
    When Window2 closes, Window1 reappears
    Program exits when Window1 is closed
    
    Copyright 2020-2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""


def make_window1():
    layout = [[sg.Text('Window 1'), ],
              [sg.Input(key='-IN-')],
              [sg.Text(size=(20, 1), key='-OUTPUT-')],
              [sg.Button('Launch 2'), sg.Button('Output')]]

    return sg.Window('Window 1', layout, finalize=True)

def make_window2():
    layout = [[sg.Text('Window 2')],
               [sg.Button('Exit')]]

    return sg.Window('Window 2', layout, finalize=True)


def main():
    # Design pattern 1 - First window does not remain active
    window2 = None
    window1 = make_window1()

    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED and window == window1:
            break

        if window == window1:
            window1['-OUTPUT-'].update(values['-IN-'])

        if event == 'Launch 2' and not window2:
            window1.hide()
            window2 = make_window2()

        if window == window2 and (event in (sg.WIN_CLOSED, 'Exit')):
            window2.close()
            window2 = None
            window1.un_hide()
    window1.close()


if __name__ == '__main__':
    main()