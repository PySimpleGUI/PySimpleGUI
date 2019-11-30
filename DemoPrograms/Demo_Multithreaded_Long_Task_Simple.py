#!/usr/bin/python3
import queue
import threading
import time
import PySimpleGUI as sg

# This program has been tested on all flavors of PySimpleGUI and it works with no problems at all

"""
    DESIGN PATTERN - Multithreaded Long Tasks GUI using shared global variables
    Presents one method for running long-running operations in a PySimpleGUI environment.
    The PySimpleGUI code, and thus the underlying GUI framework, runs as the primary, main thread
    The "long work" is contained in the thread that is being started.

    The PySimpleGUI code is structured just like a typical PySimpleGUI program.  A layout defined,
        a Window is created, and an event loop is executed.
"""


thread_done = 1
message = ''
thread_counter = 0

def long_operation_thread(seconds):
    """
    A worker thread that communicates with the GUI through a global variable
    This thread can block for as long as it wants and the GUI will not be affected
    :param seconds: (int) How long to sleep, the ultimate blocking call
    :return:
    """

    global thread_done, message, thread_counter

    print('Starting thread - will sleep for {} seconds'.format(seconds))
    thread_counter += 1
    time.sleep(seconds)                  # sleep for a while
    message = f'***This is a message from the thread {thread_counter} ***'
    thread_done = True


def the_gui():
    """
    Starts and executes the GUI
    Reads data from a global variable and displays
    Returns when the user exits / closes the window
    """
    global thread_done, message

    sg.change_look_and_feel('Light Brown 3')

    layout = [[sg.Text('Long task to perform example')],
              [sg.Output(size=(70, 12))],
              [sg.Text('Number of seconds your task will take'),
                  sg.Input(key='-SECONDS-', size=(5, 1)),
                  sg.Button('Do Long Task', bind_return_key=True)],
              [sg.Button('Click Me'), sg.Button('Exit')], ]

    window = sg.Window('Multithreaded Window', layout)

    # --------------------- EVENT LOOP ---------------------
    while True:
        event, values = window.read(timeout=100)
        if event in (None, 'Exit'):
            break
        elif event.startswith('Do'):
            seconds = float(values['-SECONDS-'])
            print('Thread ALIVE! Long work....sending value of {} seconds'.format(seconds))
            threading.Thread(target=long_operation_thread, args=(seconds, ), daemon=True).start()
        elif event == 'Click Me':
            print('Your GUI is alive and well')
        # --------------- Check for incoming messages from threads  ---------------
        if thread_done is True:
            print('The thread has finished!')
            print(f'message = {message}')
            thread_done = False
            message = ''

    # if user exits the window, then close the window and exit the GUI func
    window.close()

if __name__ == '__main__':
    the_gui()
    print('Exiting Program')
