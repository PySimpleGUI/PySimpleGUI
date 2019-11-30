#!/usr/bin/python3
import threading
import time
import PySimpleGUI as sg

"""
    DESIGN PATTERN - Multithreaded Long Tasks GUI using shared global variables
    
    Presents one method for running long-running operations in a PySimpleGUI environment.
    The PySimpleGUI code, and thus the underlying GUI framework, runs as the primary, main thread
    The "long work" is contained in the thread that is being started. Communicating is done (carefully) using global variables

    There are 2 ways "progress" is being reported to the user. If a the amount of time is known ahead of time and
    the work can be broek down into countable units, then a progress bar is used.  If a task is one long chunk
    of time that cannot be broken down into smaller units, then an animated GIF is shown that spins as
    long as the task is running. 
"""

thread_done = 1
message = ''
thread_counter = 0
total = 100
progress = 0

def long_operation_thread(seconds):
    """
    A worker thread that communicates with the GUI through a global variable
    This thread can block for as long as it wants and the GUI will not be affected
    :param seconds: (int) How long to sleep, the ultimate blocking call
    :return:
    """

    global thread_done, message, thread_counter, progress

    print('Thread started - will sleep for {} seconds'.format(seconds))
    thread_counter += 1
    for i in range(int(seconds*10)):
        time.sleep(.1)                  # sleep for a while
        progress += total/(seconds*10)

    message = f'***This is a message from the thread {thread_counter} ***'
    thread_done = True


def the_gui():
    """
    Starts and executes the GUI
    Reads data from a global variable and displays
    Returns when the user exits / closes the window
    """
    global thread_done, message, progress

    sg.change_look_and_feel('Light Brown 3')

    layout = [[sg.Text('Long task to perform example')],
              [sg.Output(size=(80, 12))],
              [sg.Text('Number of seconds your task will take'),
                  sg.Input(key='-SECONDS-', size=(5, 1)),
                  sg.Button('Do Long Task', bind_return_key=True),
                  sg.CBox('ONE chunk, cannot break apart', key='-ONE CHUNK-')],
              [sg.Text('Work progress'), sg.ProgressBar(total, size=(20,20), orientation='h', key='-PROG-')],
              [sg.Button('Click Me'), sg.Button('Exit')], ]

    window = sg.Window('Multithreaded Window', layout)

    one_chunk = False
    sg.popup_animated(None)

    # --------------------- EVENT LOOP ---------------------
    while True:
        event, values = window.read(timeout=400)
        if event in (None, 'Exit'):
            break
        elif event.startswith('Do'):
            seconds = float(values['-SECONDS-'])
            one_chunk = values['-ONE CHUNK-']
            print('Thread Starting! Long work....sending value of {} seconds'.format(seconds))
            threading.Thread(target=long_operation_thread, args=(seconds, ), daemon=True).start()
        elif event == 'Click Me':
            print('Your GUI is alive and well')
        # --------------- Check for incoming messages from threads  ---------------
        if thread_done is True:
            print('The thread has finished!')
            print(f'message = {message}')
            # reset everything for the next run
            sg.popup_animated(None)     # just in case one's running, stop it
            thread_done = one_chunk = False
            message, progress = '', 0
            window['-PROG-'].update_bar(total, total)       # show the bar as maxed out
        if one_chunk:                                       # flag signifies the thread is taking to take one big chunk of time
            sg.popup_animated(sg.DEFAULT_BASE64_LOADING_GIF, background_color='white', transparent_color='white', time_between_frames=100)
        elif progress != 0:
            window['-PROG-'].update_bar(progress, total)    # update the progress bar if non-zero

    # if user exits the window, then close the window and exit the GUI func
    window.close()

if __name__ == '__main__':
    the_gui()
    print('Exiting Program')
