from queue import Queue
from threading import Thread
from time import sleep

import PySimpleGUI as sg

"""
    DESIGN PATTERN - Multithreaded GUI
    One method for running multiple threads in a PySimpleGUI environment.
    This design pattern works for all of the flavors of PySimpleGUI including the Web and also repl.it
    
"""


def worker_thread(thread_name, run_freq,  gui_queue):
    """
    A worker thrread that communicates with the GUI
    These threads can call functions that block withouth affecting the GUI (a good thing)
    :param thread_name: Text name used  for displaying info
    :param run_freq: How often the thread should run in milliseconds
    :param gui_queue: Queue used to communicate with the GUI
    :return:
    """
    print('Strarting thread - ', thread_name)
    i = 0
    while True:
        sleep(run_freq/1000)
        gui_queue.put('{} - {}'.format(thread_name, i))
        i += 1


def the_gui(gui_queue):
    """
    starts and executes the GUI.  Returns when the user exits / closes the window
    reads data from a Queue and displays the data
    :param gui_queue: Queue the GUI should read from
    :return:
    """
    layout = [ [sg.Text('Your GUI Window')],
               [sg.Text('', size=(15,1), key='_OUTPUT_')],
               [sg.Button('Exit')],]

    window = sg.Window('Window Title').Layout(layout)

    while True:             # Event Loop
        event, values = window.Read(timeout=200)        # wait for up to 200 ms for a GUI event
        if event is None or event == 'Exit':
            break
        #--------------- Handle stuff coming in from threads ---------------
        try:                    # see if something has been posted to Queue
            message = gui_queue.get_nowait()
        except:
            message = None      # indicate nothing posted
        # if message received from queue, display the message in the Window
        if message:
            window.Element('_OUTPUT_').Update(message)

    # if user exits the window, then close the window and exit
    window.Close()


if __name__ == '__main__':
    #-- Create a Queue to communicate with GUI --
    gui_queue = Queue()             # queue used to communicate between the gui and the worker
    #-- Start worker threads, one runs twice as often as the other
    thread = Thread(target=worker_thread, args=('Thread 1', 1000, gui_queue,),  daemon=True)
    thread.start()
    thread = Thread(target=worker_thread, args=('Thread 2', 500, gui_queue,),  daemon=True)
    thread.start()
    #-- Start the GUI passing in the Queue --
    the_gui(gui_queue)
