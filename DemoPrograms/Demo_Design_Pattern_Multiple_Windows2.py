import PySimpleGUI as sg

"""
    Multiple Window Design Pattern
    
    Two windows - both remain active and visible
    Window 1 launches Window 2
    Window 1 remains visible and active while Window 2 is active
    Closing Window 1 exits application
    
    Copyright 2020 PySimpleGUI.org
"""


def make_window1():
    layout = [[ sg.Text('Window 1'),],
              [sg.Input(enable_events=True, k='-IN-')],
              [sg.Text(size=(20,1), k='-OUTPUT-')],
              [sg.Button('Launch 2'), sg.Button('Exit')]]

    return sg.Window('Window 1', layout, finalize=True)


def make_window2():
    layout = [[sg.Text('Window 2')],
              [sg.Button('Exit')]]

    return sg.Window('Window 2', layout, finalize=True)


def main():
    window1, window2 = make_window1(), None
    while True:
        window, event, values = sg.read_all_windows()
        if window == window1 and event in (sg.WIN_CLOSED, 'Exit'):
            break
        # Window 1 stuff
        if event == '-IN-':
            window['-OUTPUT-'].update(values['-IN-'])
        elif event == 'Launch 2' and not window2:
            window2 = make_window2()

        # Window 2 stuff
        if window == window2 and event in(sg.WIN_CLOSED, 'Exit'):
            window2.close()
            window2 = None

    window1.close()
    if window2 is not None:
        window2.close()


if __name__ == '__main__':
    main()