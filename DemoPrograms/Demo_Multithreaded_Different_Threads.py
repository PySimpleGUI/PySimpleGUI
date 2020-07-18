#!/usr/bin/python3
import threading
import time
import itertools
import PySimpleGUI as sg

"""
    DESIGN PATTERN - Multithreaded GUI
    One method for running multiple threads in a PySimpleGUI environment.
    The PySimpleGUI code, and thus the underlying GUI framework, runs as the primary, main thread
    Other parts of the software are implemented as threads
    
    While users never know the implementation details within PySimpleGUI, the mechanism is that a queue.Queue
    is used to communicate data between a thread and a PySimpleGUI window.
    The PySimpleGUI code is structured just like a typical PySimpleGUI program.  A layout defined,
        a Window is created, and an event loop is executed.

    Copyright 2020 PySimpleGUI.org
    
"""


# ######## ##     ## ########  ########    ###    ########
#    ##    ##     ## ##     ## ##         ## ##   ##     ##
#    ##    ##     ## ##     ## ##        ##   ##  ##     ##
#    ##    ######### ########  ######   ##     ## ##     ##
#    ##    ##     ## ##   ##   ##       ######### ##     ##
#    ##    ##     ## ##    ##  ##       ##     ## ##     ##
#    ##    ##     ## ##     ## ######## ##     ## ########

def worker_thread1(thread_name, run_freq,  window):
    """
    A worker thread that communicates with the GUI
    These threads can call functions that block without affecting the GUI (a good thing)
    Note that this function is the code started as each thread. All threads are identical in this way
    :param thread_name: Text name used  for displaying info
    :param run_freq: How often the thread should run in milliseconds
    :param window: window this thread will be conversing with
    :type window: sg.Window
    :return:
    """
    print('Starting thread 1 - {} that runs every {} ms'.format(thread_name, run_freq))
    for i in itertools.count():                             # loop forever, keeping count in i as it loops
        time.sleep(run_freq/1000)                           # sleep for a while
        # put a message into queue for GUI
        window.write_event_value(thread_name, f'count = {i}')


def worker_thread2(thread_name, run_freq,  window):
    """
    A worker thread that communicates with the GUI
    These threads can call functions that block without affecting the GUI (a good thing)
    Note that this function is the code started as each thread. All threads are identical in this way
    :param thread_name: Text name used  for displaying info
    :param run_freq: How often the thread should run in milliseconds
    :param window: window this thread will be conversing with
    :type window: sg.Window
    :return:
    """
    print('Starting thread 2 - {} that runs every {} ms'.format(thread_name, run_freq))
    for i in itertools.count():                             # loop forever, keeping count in i as it loops
        time.sleep(run_freq/1000)                           # sleep for a while
        # put a message into queue for GUI
        window.write_event_value(thread_name, f'count = {i}')


def worker_thread3(thread_name, run_freq,  window):
    """
    A worker thread that communicates with the GUI
    These threads can call functions that block without affecting the GUI (a good thing)
    Note that this function is the code started as each thread. All threads are identical in this way
    :param thread_name: Text name used  for displaying info
    :param run_freq: How often the thread should run in milliseconds
    :param window: window this thread will be conversing with
    :type window: sg.Window
    :return:
    """
    print('Starting thread 3 - {} that runs every {} ms'.format(thread_name, run_freq))
    for i in itertools.count():                             # loop forever, keeping count in i as it loops
        time.sleep(run_freq/1000)                           # sleep for a while
        # put a message into queue for GUI
        window.write_event_value(thread_name, f'count = {i}')



#  ######   ##     ## ####
# ##    ##  ##     ##  ##
# ##        ##     ##  ##
# ##   #### ##     ##  ##
# ##    ##  ##     ##  ##
# ##    ##  ##     ##  ##
#  ######    #######  ####


def the_gui():
    """
    Starts and executes the GUI
    Reads data from a Queue and displays the data to the window
    Returns when the user exits / closes the window
        (that means it does NOT return until the user exits the window)
    :param gui_queue: Queue the GUI should read from
    :return:
    """
    layout = [[sg.Text('Multithreaded Window Example')],
              [sg.Text('', size=(15, 1), key='-OUTPUT-')],
              [sg.Multiline(size=(40, 26), key='-ML-', autoscroll=True)],
              [sg.Button('Exit')], ]

    window = sg.Window('Multithreaded Window', layout, finalize=True)

    # -- Create a Queue to communicate with GUI --
    # queue used to communicate between the gui and the threads
    # -- Start worker threads, each taking a different amount of time
    threading.Thread(target=worker_thread1, args=('Thread 1', 500, window,),  daemon=True).start()
    threading.Thread(target=worker_thread2, args=('Thread 2', 200, window,),  daemon=True).start()
    threading.Thread(target=worker_thread3, args=('Thread 3', 1000, window,), daemon=True).start()
    # -- Start the GUI passing in the Queue --

    sg.cprint_set_output_destination(window, '-ML-')

    colors = {'Thread 1':('white', 'red'), 'Thread 2':('white', 'purple'), 'Thread 3':('white', 'blue')}
    # --------------------- EVENT LOOP ---------------------
    while True:
        # wait for up to 100 ms for a GUI event
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        # --------------- Loop through all messages coming in from threads ---------------
        sg.cprint(event, values[event], c=colors[event])
    # if user exits the window, then close the window and exit the GUI func
    window.close()


##     ##    ###    #### ##    ##
###   ###   ## ##    ##  ###   ##
#### ####  ##   ##   ##  ####  ##
## ### ## ##     ##  ##  ## ## ##
##     ## #########  ##  ##  ####
##     ## ##     ##  ##  ##   ###
##     ## ##     ## #### ##    ##

if __name__ == '__main__':
    the_gui()

