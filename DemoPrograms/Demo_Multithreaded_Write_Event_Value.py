import threading
import time

import PySimpleGUI as sg

"""
    Threaded Demo - Uses Window.write_event_value communications
    
    Requires PySimpleGUI.py version 4.25.0 and later
    
    This is a really important demo  to understand if you're going to be using multithreading in PySimpleGUI.
    
    Older mechanisms for multi-threading in PySimpleGUI relied on polling of a queue. The management of a communications
    queue is now performed internally to PySimpleGUI.

    The importance of using the new window.write_event_value call cannot be emphasized enough.  It will hav a HUGE impact, in
    a positive way, on your code to move to this mechanism as your code will simply "pend" waiting for an event rather than polling.
    
    Copyright 2020 PySimpleGUI.org
"""

THREAD_EVENT = '-THREAD-'

def the_thread(window):
    """
    The thread that communicates with the application through the window's events.

    Once a second wakes and sends a new event and associated value to the window
    """
    i = 0
    while True:
        time.sleep(1)
        sg.cprint(f'thread info (in thread) = {threading.current_thread().name}', c='white on purple')
        window.write_event_value('-THREAD-', i)
        i += 1


def main():
    """
    The demo will display in the multiline info about the event and values dictionary as it is being
    returned from window.read()
    Every time "Start" is clicked a new thread is started
    Try clicking "go" to see that the window is active while the thread stuff is happening in the background
    """

    layout = [  [sg.Text('My Window')],
                [sg.Multiline(size=(40,20), key='-ML-', autoscroll=True, reroute_stdout=True, write_only=True, reroute_cprint=True)],
                [sg.Input(key='-IN-')],
                [sg.Button('Go'), sg.B('Start'), sg.Button('Exit')]  ]

    window = sg.Window('Window Title', layout)

    while True:             # Event Loop
        event, values = window.read()
        sg.cprint(event, values)
        sg.cprint(f'thread info = {threading.current_thread().name}')
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Start':
            thread = threading.Thread(target=the_thread, args=(window,), daemon=True)
            thread.start()
        if event == THREAD_EVENT:
            sg.cprint(f'Data from the thread = {values[THREAD_EVENT]}', colors='white on red')
    window.close()


if __name__ == '__main__':
    main()