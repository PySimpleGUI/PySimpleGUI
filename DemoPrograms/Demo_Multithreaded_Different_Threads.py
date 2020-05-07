#!/usr/bin/python3

# Rather than importing individual classes such as threading.Thread or queue.Queue, this
#   program is doing a simple import and then indicating the package name when the functions
#   are called.  This seemed like a great way for the reader of the code to get an understanding
#   as to exactly which package is being used.  It's purely for educational and explicitness purposes
import queue
import threading
import time
import itertools
import PySimpleGUI as sg

"""
    DESIGN PATTERN - Multithreaded GUI
    One method for running multiple threads in a PySimpleGUI environment.
    The PySimpleGUI code, and thus the underlying GUI framework, runs as the primary, main thread
    Other parts of the software are implemented as threads
    
    A queue.Queue is used by the worker threads to communicate with code that calls PySimpleGUI directly.
    The PySimpleGUI code is structured just like a typical PySimpleGUI program.  A layout defined,
        a Window is created, and an event loop is executed.
    What's different is that within this otherwise normal PySimpleGUI Event Loop, there is a check for items
        in the Queue.  If there are items found, process them by making GUI changes, and continue.
    
    This design pattern works for all of the flavors of PySimpleGUI including the Web and also repl.it
    You'll find a repl.it version here: https://repl.it/@PySimpleGUI/Async-With-Queue-Communicationspy
"""


# ######## ##     ## ########  ########    ###    ########
#    ##    ##     ## ##     ## ##         ## ##   ##     ##
#    ##    ##     ## ##     ## ##        ##   ##  ##     ##
#    ##    ######### ########  ######   ##     ## ##     ##
#    ##    ##     ## ##   ##   ##       ######### ##     ##
#    ##    ##     ## ##    ##  ##       ##     ## ##     ##
#    ##    ##     ## ##     ## ######## ##     ## ########

def worker_thread1(thread_name, run_freq,  gui_queue):
    """
    A worker thread that communicates with the GUI
    These threads can call functions that block without affecting the GUI (a good thing)
    Note that this function is the code started as each thread. All threads are identical in this way
    :param thread_name: Text name used  for displaying info
    :param run_freq: How often the thread should run in milliseconds
    :param gui_queue: Queue used to communicate with the GUI
    :return:
    """
    print('Starting thread 1 - {} that runs every {} ms'.format(thread_name, run_freq))
    for i in itertools.count():                             # loop forever, keeping count in i as it loops
        time.sleep(run_freq/1000)                           # sleep for a while
        # put a message into queue for GUI
        gui_queue.put('{} - {}'.format(thread_name, i))


def worker_thread2(thread_name, run_freq,  gui_queue):
    """
    A worker thread that communicates with the GUI
    These threads can call functions that block without affecting the GUI (a good thing)
    Note that this function is the code started as each thread. All threads are identical in this way
    :param thread_name: Text name used  for displaying info
    :param run_freq: How often the thread should run in milliseconds
    :param gui_queue: Queue used to communicate with the GUI
    :return:
    """
    print('Starting thread 2 - {} that runs every {} ms'.format(thread_name, run_freq))
    for i in itertools.count():                             # loop forever, keeping count in i as it loops
        time.sleep(run_freq/1000)                           # sleep for a while
        # put a message into queue for GUI
        gui_queue.put('{} - {}'.format(thread_name, i))


def worker_thread3(thread_name, run_freq,  gui_queue):
    """
    A worker thread that communicates with the GUI
    These threads can call functions that block without affecting the GUI (a good thing)
    Note that this function is the code started as each thread. All threads are identical in this way
    :param thread_name: Text name used  for displaying info
    :param run_freq: How often the thread should run in milliseconds
    :param gui_queue: Queue used to communicate with the GUI
    :return:
    """
    print('Starting thread 3 - {} that runs every {} ms'.format(thread_name, run_freq))
    for i in itertools.count():                             # loop forever, keeping count in i as it loops
        time.sleep(run_freq/1000)                           # sleep for a while
        # put a message into queue for GUI
        gui_queue.put('{} - {}'.format(thread_name, i))



#  ######   ##     ## ####
# ##    ##  ##     ##  ##
# ##        ##     ##  ##
# ##   #### ##     ##  ##
# ##    ##  ##     ##  ##
# ##    ##  ##     ##  ##
#  ######    #######  ####


def the_gui(gui_queue):
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
              [sg.Output(size=(40, 6))],
              [sg.Button('Exit')], ]

    window = sg.Window('Multithreaded Window', layout)
    # --------------------- EVENT LOOP ---------------------
    while True:
        # wait for up to 100 ms for a GUI event
        event, values = window.read(timeout=100)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        # --------------- Loop through all messages coming in from threads ---------------
        while True:                 # loop executes until runs out of messages in Queue
            try:                    # see if something has been posted to Queue
                message = gui_queue.get_nowait()
            except queue.Empty:     # get_nowait() will get exception when Queue is empty
                break               # break from the loop if no more messages are queued up
            # if message received from queue, display the message in the Window
            if message:
                window['-OUTPUT-'].update(message)
                # do a refresh because could be showing multiple messages before next Read
                window.refresh()
                print(message)
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
    # -- Create a Queue to communicate with GUI --
    # queue used to communicate between the gui and the threads
    gui_queue = queue.Queue()
    # -- Start worker threads, each taking a different amount of time
    threading.Thread(target=worker_thread1, args=(
        'Thread 1', 500, gui_queue,),  daemon=True).start()
    threading.Thread(target=worker_thread2, args=(
        'Thread 2', 200, gui_queue,),  daemon=True).start()
    threading.Thread(target=worker_thread3, args=(
        'Thread 3', 1000, gui_queue,),  daemon=True).start()
    # -- Start the GUI passing in the Queue --
    the_gui(gui_queue)
    print('Exiting Program')
