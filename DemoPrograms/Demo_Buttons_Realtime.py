#!/usr/bin/env python
"""
    Demo - Realtime Buttons

    Realtime buttons provide a way for you to get a continuous stream of button
    events for as long as a button is held down.

    This demo is using a timeout to determine that a button has been released.
    If your application doesn't care when a button is released and only needs to know
    that it's being held down, then  you can remove the timeout on the window read call.

    Note that your reaction latency will be the same as your timeout value.  In this demo
    the timeout is 100, so there will be 100ms between releasing a button and your program detecting
    this has happened.

    Copyright 2021 PySimpleGUI
"""

import PySimpleGUI as sg

def main():
    # The Quit button is being placed in the bottom right corner and the colors are inverted, just for fun
    layout = [[sg.Text('Robotics Remote Control')],
              [sg.Text('Hold Down Button To Move')],
              [sg.Text()],
              [sg.Text('           '),
               sg.RealtimeButton(sg.SYMBOL_UP, key='-FORWARD-')],
              [sg.RealtimeButton(sg.SYMBOL_LEFT, key='-LEFT-'),
               sg.Text(size=(10,1), key='-STATUS-', justification='c', pad=(0,0)),
               sg.RealtimeButton(sg.SYMBOL_RIGHT, key='-RIGHT-')],
              [sg.Text('           '),
               sg.RealtimeButton(sg.SYMBOL_DOWN, key='-DOWN-')],
              [sg.Text()],
              [sg.Column([[sg.Quit(button_color=(sg.theme_button_color()[1], sg.theme_button_color()[0]), focus=True)]], justification='r')]]

    window = sg.Window('Robotics Remote Control', layout)

    while True:
        # This is the code that reads and updates your window
        event, values = window.read(timeout=100)
        if event in (sg.WIN_CLOSED, 'Quit'):
            break
        if event != sg.TIMEOUT_EVENT:
            # if not a timeout event, then it's a button that's being held down
            window['-STATUS-'].update(event)
        else:
            # A timeout signals that all buttons have been released so clear the status display
            window['-STATUS-'].update('')

    window.close()

if __name__ == '__main__':
    sg.theme('dark red')
    main()
