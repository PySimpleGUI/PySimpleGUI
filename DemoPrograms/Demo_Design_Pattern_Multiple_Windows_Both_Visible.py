import PySimpleGUI as sg
"""
    Demo - 2 simultaneous windows using read_all_window

    Both windows are immediately visible.  Each window updates the other.
    
    There's an added capability to "re-open" window 2 should it be closed.  This is done by simply calling the make_win2 function
    again when the button is pressed in window 1.
    
    The program exits when both windows have been closed
        
    Copyright 2020 PySimpleGUI.org
"""

def make_win1():
    layout = [[sg.Text('Window 1')],
              [sg.Text('Enter something to output to Window 2')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text(size=(25,1), key='-OUTPUT-')],
              [sg.Button('Reopen')],
              [sg.Button('Exit')]]
    return sg.Window('Window Title', layout, finalize=True)


def make_win2():
    layout = [[sg.Text('Window 2')],
              [sg.Text('Enter something to output to Window 1')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text(size=(25,1), key='-OUTPUT-')],
              [sg.Button('Exit')]]
    return sg.Window('Window Title', layout, finalize=True)


def main():
    window1, window2 = make_win1(), make_win2()

    window2.move(window1.current_location()[0], window1.current_location()[1]+220)

    while True:             # Event Loop
        window, event, values = sg.read_all_windows()

        if window == sg.WIN_CLOSED:     # if all windows were closed
            break
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            if window == window2:       # if closing win 2, mark as closed
                window2 = None
            elif window == window1:     # if closing win 1, mark as closed
                window1 = None
        elif event == 'Reopen':
            if not window2:
                window2 = make_win2()
                window2.move(window1.current_location()[0], window1.current_location()[1] + 220)
        elif event == '-IN-':
            output_window = window2 if window == window1 else window1
            if output_window:           # if a valid window, then output to it
                output_window['-OUTPUT-'].update(values['-IN-'])
            else:
                window['-OUTPUT-'].update('Other window is closed')


if __name__ == '__main__':
    main()