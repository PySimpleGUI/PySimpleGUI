#!/usr/bin/python3
import queue
import threading
import time

import PySimpleGUI as sg

# Put your long-running code in here
def worker_thread(thread_name, gui_queue):
    print('Starting thread - {} '.format(thread_name))
    # this is our "long running function call"
    time.sleep(5)  # sleep for a while

    # at the end of the work, before exiting, send a message back to the GUI indicating end
    gui_queue.put('{} - done'.format(thread_name))  # put a message into queue for GUI


######   ##     ## ####
##    ##  ##     ##  ##
##        ##     ##  ##
##   #### ##     ##  ##
##    ##  ##     ##  ##
##    ##  ##     ##  ##
######    #######  ####

def the_gui(gui_queue):

    layout = [[sg.Text('Multithreaded Work Example')],
              [sg.Text('', size=(25, 1), key='_OUTPUT_')],
              # [sg.Output(size=(40,6))],
              [sg.Button('Go'), sg.Button('Exit')], ]

    window = sg.Window('Multithreaded Window').Layout(layout)
    # --------------------- EVENT LOOP ---------------------
    message = None
    count = 0
    while True:
        event, values = window.Read(timeout=100)  # wait for up to 100 ms for a GUI event
        if event is None or event == 'Exit':
            break
        if event == 'Go':
            window.Element('_OUTPUT_').Update('Starting long work %s'%count)
            # simulate STARTING long run by starting a thread
            threading.Thread(target=worker_thread, args=('Thread %s'%count, gui_queue,), daemon=True).start()
            count += 1
        # --------------- Loop through all messages coming in from threads ---------------
        try:  # see if something has been posted to Queue
            message = gui_queue.get_nowait()
        except queue.Empty:  # get_nowait() will get exception when Queue is empty
            pass             # nothing in queue so do nothing

        # if message received from queue, display the message in the Window
        if message is not None:
            # this is the place you would execute code at ENDING of long running task
            window.Element('_OUTPUT_').Update(message)
            window.Refresh()  # do a refresh because could be showing multiple messages before next Read
            message = None

    # if user exits the window, then close the window and exit the GUI func
    window.Close()


##     ##    ###    #### ##    ##
###   ###   ## ##    ##  ###   ##
#### ####  ##   ##   ##  ####  ##
## ### ## ##     ##  ##  ## ## ##
##     ## #########  ##  ##  ####
##     ## ##     ##  ##  ##   ###
##     ## ##     ## #### ##    ##

if __name__ == '__main__':
    # -- Create a Queue to communicate with GUI --
    gui_queue = queue.Queue()  # queue used to communicate between the gui and the threads
    the_gui(gui_queue)
    print('Exiting Program')