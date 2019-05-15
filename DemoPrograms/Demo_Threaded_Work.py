#!/usr/bin/python3
import queue
import threading
import time
import PySimpleGUI as sg

"""
    You want to look for 3 points in this code, marked with comment "LOCATION X". 
    1. Where you put your call that takes a long time
    2. Where the trigger to make the call takes place in the event loop
    3. Where the completion of the call is indicated in the event loop

    Demo on how to add a long-running item to your PySimpleGUI Event Loop
    If you want to do something that takes a long time, and you do it in the 
    main event loop, you'll quickly begin to see messages from windows that your
    program has hung, asking if you want to kill it.
    
    The problem is not that your problem is hung, the problem is that you are 
    not calling Read or Refresh often enough.
    
    One way through this, shown here, is to put your long work into a thread that
    is spun off, allowed to work, and then gets back to the GUI when it's done working
    on that task.
    
    Every time you start up one of these long-running functions, you'll give it an "ID".
    When the function completes, it will send to the GUI Event Loop a message with 
    the format:
        work_id ::: done
    This makes it easy to parse out your original work ID
    
    You can hard code these IDs to make your code more readable.  For example, maybe
    you have a function named "update_user_list()".  You can call the work ID "user list".
    Then check for the message coming back later from the work task to see if it starts
    with "user list".  If so, then that long-running task is over. 
    
"""

# ############################# User callable CPU intensive code #############################
# Put your long running code inside this "wrapper"
# NEVER make calls to PySimpleGUI from this thread (or any thread)!
# Create one of these functions for EVERY long-running call you want to make
def long_function_wrapper(work_id, gui_queue):
    # LOCATION 1
    # this is our "long running function call"
    time.sleep(5)  # sleep for a while as a simulation of a long-running computation
    # at the end of the work, before exiting, send a message back to the GUI indicating end
    gui_queue.put('{} ::: done'.format(work_id))
    # at this point, the thread exits
    return


############################# Begin GUI code #############################
def the_gui():
    gui_queue = queue.Queue()  # queue used to communicate between the gui and long-running code

    layout = [[sg.Text('Multithreaded Work Example')],
              [sg.Text('Click Go to start a long-running function call')],
              [sg.Text('', size=(25, 1), key='_OUTPUT_')],
              [sg.Text('', size=(25, 1), key='_OUTPUT2_')],
              [sg.Button('Go'), sg.Button('Popup'), sg.Button('Exit')], ]

    window = sg.Window('Multithreaded Window').Layout(layout)
    # --------------------- EVENT LOOP ---------------------
    work_id = 0
    while True:
        event, values = window.Read(timeout=100)  # wait for up to 100 ms for a GUI event
        if event is None or event == 'Exit':
            break
        if event == 'Go':           # clicking "Go" starts a long running work item by starting thread
            window.Element('_OUTPUT_').Update('Starting long work %s'%work_id)
            # LOCATION 2
            # STARTING long run by starting a thread
            threading.Thread(target=long_function_wrapper, args=(work_id, gui_queue,), daemon=True).start()
            work_id += 1
        # --------------- Read next message coming in from threads ---------------
        try:
            message = gui_queue.get_nowait()    # see if something has been posted to Queue
        except queue.Empty:                     # get_nowait() will get exception when Queue is empty
            message = None                      # nothing in queue so do nothing

        # if message received from queue, then some work was completed
        if message is not None:
            # LOCATION 3
            # this is the place you would execute code at ENDING of long running task
            # You can check the completed_work_id variable to see exactly which long-running function completed
            completed_work_id = message[:message.index(' :::')]
            window.Element('_OUTPUT2_').Update('Complete Work ID "{}"'.format(completed_work_id))
        if event == 'Popup':
            sg.Popup('This is a popup showing that the GUI is running')
    # if user exits the window, then close the window and exit the GUI func
    window.Close()

############################# Main #############################

if __name__ == '__main__':
    the_gui()
    print('Exiting Program')