#!/usr/bin/python3
import threading
import time
import PySimpleGUI as sg

"""
    DESIGN PATTERN - Multithreaded Long Tasks GUI using shared global variables

    Presents one method for running long-running operations in a PySimpleGUI environment.
    The PySimpleGUI code, and thus the underlying GUI framework, runs as the primary, main thread
    The "long work" is contained in the thread that is being started. Communicating is done (carefully) using global variables

    There are 2 ways "progress" is being reported to the user. 
    You can simulate the 2 different scenarios that happen with worker threads.
    1.  If a the amount of time is known ahead of time or the work can be broken down into countable units, then a progress bar is used.  
    2.  If a task is one long chunk of time that cannot be broken down into smaller units, then an animated GIF is shown that spins as
    long as the task is running.
"""

total = 100     # number of units that are used with the progress bar
message = ''    # used by thread to send back a message to the main thread
progress = 0    # current progress up to a maximum of "total"


def long_operation_thread(seconds):
    """
    A worker thread that communicates with the GUI through a global message variable
    This thread can block for as long as it wants and the GUI will not be affected
    :param seconds: (int) How long to sleep, the ultimate blocking call
    """

    global message, progress

    print('Thread started - will sleep for {} seconds'.format(seconds))
    for i in range(int(seconds * 10)):
        time.sleep(.1)  # sleep for a while
        progress += total / (seconds * 10)

    message = f'*** The thread says.... "I am finished" ***'

def the_gui():
    """
    Starts and executes the GUI
    Reads data from a global variable and displays
    Returns when the user exits / closes the window
    """
    global message, progress

    sg.theme('Light Brown 3')

    layout = [[sg.Text('Long task to perform example')],
              [sg.Output(size=(80, 12))],
              [sg.Text('Number of seconds your task will take'),
               sg.Input(key='-SECONDS-', size=(5, 1)),
               sg.Button('Do Long Task', bind_return_key=True),
               sg.CBox('ONE chunk, cannot break apart', key='-ONE CHUNK-')],
              [sg.Text('Work progress'), sg.ProgressBar(total, size=(20, 20), orientation='h', key='-PROG-')],
              [sg.Button('Click Me'), sg.Button('Exit')], ]

    window = sg.Window('Multithreaded Demonstration Window', layout)

    thread = None

    # --------------------- EVENT LOOP ---------------------
    while True:
        event, values = window.read(timeout=100)
        if event in (None, 'Exit'):
            break
        elif event.startswith('Do') and not thread:
            print('Thread Starting! Long work....sending value of {} seconds'.format(float(values['-SECONDS-'])))
            thread = threading.Thread(target=long_operation_thread, args=(float(values['-SECONDS-']),), daemon=True)
            thread.start()
        elif event == 'Click Me':
            print('Your GUI is alive and well')

        if thread:                                          # If thread is running
            if values['-ONE CHUNK-']:                       # If one big operation, show an animated GIF
                sg.popup_animated(sg.DEFAULT_BASE64_LOADING_GIF, background_color='white', transparent_color='white', time_between_frames=100)
            else:                                           # Not one big operation, so update a progress bar instead
                window['-PROG-'].update_bar(progress, total)
            thread.join(timeout=0)
            if not thread.is_alive():                       # the thread finished
                print(f'message = {message}')
                sg.popup_animated(None)                     # stop animination in case one is running
                thread, message, progress = None, '', 0     # reset variables for next run
                window['-PROG-'].update_bar(0,0)            # clear the progress bar

    window.close()


if __name__ == '__main__':
    the_gui()
    print('Exiting Program')
