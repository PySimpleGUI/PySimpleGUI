#!/usr/bin/python3
import time
import PySimpleGUI as sg


"""
    Demo Program - Multithreaded Long Tasks GUI
    
    Presents one method for running long-running operations in a PySimpleGUI environment.
    
    The PySimpleGUI code, and thus the underlying GUI framework, runs as the primary, main thread
    The "long work" is contained in the thread that is being started.

    So that you don't have to import and understand the threading module, this program uses window.start_thread to run a thread.
    
    The thread is using TUPLES for its keys.  This enables you to easily find the thread events by looking at event[0].
        The Thread Keys look something like this:  ('-THREAD-', message)
        If event [0] == '-THREAD-' then you know it's one of these tuple keys.
         
    Copyright 2022 PySimpleGUI
"""


def long_operation_thread(seconds, window):
    """
    A worker thread that communicates with the GUI through a queue
    This thread can block for as long as it wants and the GUI will not be affected
    :param seconds: (int) How long to sleep, the ultimate blocking call
    :param window: (sg.Window) the window to communicate with
    :return:
    """
    window.write_event_value(('-THREAD-', 'Starting thread - will sleep for {} seconds'.format(seconds)), None)
    time.sleep(seconds)                  # sleep for a while
    window.write_event_value(('-THREAD-', '** DONE **'), 'Done!')  # put a message into queue for GUI


def the_gui():
    """
    Starts and executes the GUI
    Reads data from a Queue and displays the data to the window
    Returns when the user exits / closes the window
    """
    sg.theme('Light Brown 3')

    layout = [[sg.Text('Long task to perform example')],
              [sg.Output(size=(70, 12))],
              [sg.Text('Number of seconds your task will take'),
                  sg.Input(default_text=5, key='-SECONDS-', size=(5, 1)),
                  sg.Button('Do Long Task', bind_return_key=True)],
              [sg.Button('Click Me'), sg.Button('Exit')], ]

    window = sg.Window('Multithreaded Window', layout)

    # --------------------- EVENT LOOP ---------------------
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Do Long Task':
            seconds = int(values['-SECONDS-'])
            print('Thread ALIVE! Long work....sending value of {} seconds'.format(seconds))
            window.start_thread(lambda: long_operation_thread(seconds, window), ('-THREAD-', '-THEAD ENDED-'))
        elif event == 'Click Me':
            print('Your GUI is alive and well')
        elif event[0] == '-THREAD-':
            print('Got a message back from the thread: ', event[1])

    # if user exits the window, then close the window and exit the GUI func
    window.close()

if __name__ == '__main__':
    the_gui()
    print('Exiting Program')
