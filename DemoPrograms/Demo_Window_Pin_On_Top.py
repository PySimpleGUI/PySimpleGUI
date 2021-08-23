import PySimpleGUI as sg

"""
    Demo - Pin a window on top

    Note that the PIN used requires Python 3.7+ due to a tkinter problem
    This demo uses a Window call only recently added to GitHub in Aug 2021

    4.46.0.7 of PySimpleGUI provides the methods:
        Window.keep_on_top_set
        Window.keep_on_top_clear
        
    A temporary implementation is included in case you don't have that version

    Copyright 2021 PySimpleGUI
"""

def main():
    sg.theme('dark green 7')

    PIN = '📌'

    # This custom titlebar inveses the normal text/background colors. Uses a little bigger font
    my_titlebar = [[sg.Text('Window title', expand_x=True, grab=True,
                            text_color=sg.theme_background_color(), background_color=sg.theme_text_color(), font='_ 12', pad=(0,0)),
                    sg.Text(PIN, enable_events=True, k='-PIN-',  font='_ 12', pad=(0,0),  metadata=False,
                            text_color=sg.theme_background_color(), background_color=sg.theme_text_color())]]

    layout = my_titlebar + \
             [  [sg.Text('This is my window layout')],
                [sg.Input(key='-IN-')],
                [sg.Button('Go'), sg.Button('Exit')]  ]

    window = sg.Window('Window Title', layout, no_titlebar=True, resizable=True, margins=(0,0))

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == '-PIN-':
            window['-PIN-'].metadata = not window['-PIN-'].metadata     # use metadata to store current state of pin
            if window['-PIN-'].metadata:
                window['-PIN-'].update(text_color='red')
                window.keep_on_top_set()
            else:
                window['-PIN-'].update(text_color=sg.theme_background_color())
                window.keep_on_top_clear()

    window.close()

# Temp definitions of the Window methods added to 4.46.0.7 of PySimpleGUI
def keep_on_top_set(window):
    """
    Sets keep_on_top after a window has been created.  Effect is the same
    as if the window was created with this set.  The Window is also brought
    to the front
    """
    window.KeepOnTop = True
    window.bring_to_front()
    window.TKroot.wm_attributes("-topmost", 1)


def keep_on_top_clear(window):
    """
    Clears keep_on_top after a window has been created.  Effect is the same
    as if the window was created with this set.
    """
    window.KeepOnTop = False
    window.TKroot.wm_attributes("-topmost", 0)


if __name__ == '__main__':
    if 'keep_on_top_set' not in dir(sg.Window):
        print('You do not have a PySimpleGUI version with required methods. Using the temp ones from this file.')
        sg.Window.keep_on_top_set = keep_on_top_set
        sg.Window.keep_on_top_clear = keep_on_top_clear
    main()

