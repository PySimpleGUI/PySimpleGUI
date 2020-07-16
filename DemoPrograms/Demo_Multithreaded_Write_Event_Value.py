import PySimpleGUI as sg
import threading
import time

"""
    Threaded Demo - Uses Window.write_event_value communications
    
    Requires PySimpleGUI.py version 4.24.0.17

    Demo of threads using a new way of communicating with threads that is done in a non-polled way.
    No longer do you need to run your event loop with a timeout value in order to multi-thread.
    Now you can pend on your read forever and use a special call that threads can call that will add a new item to the queue
    of items

"""

THREAD_EVENT = '-THEAD-'

def the_thread(window):
    """
    The thread that communicates with the application through the window's events.

    Once a second wakes and sends a new event and associated value to the window
    """
    i = 0
    while True:
        time.sleep(1)
        window.write_event_value(THREAD_EVENT, i)
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