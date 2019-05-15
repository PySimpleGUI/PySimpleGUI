#!/usr/bin/python3
import queue
import threading
import time
import PySimpleGUI as sg

"""
    Demo on how to add a long-running item to your PySimpleGUI Event Loop
    If you want to do something that takes a long time, and you do it in the 
    main event loop, you'll quickly begin to see messages from windows that your
    program has hung, asking if you want to kill it.
    
    The problem is not that your problem is hung, the problem is that you are 
    not calling Read or Refresh often enough.
    
    One way through this, shown here, is to put your long work into a thread that
    is spun off, allowed to work, and then gets back to the GUI when it's done working
    on that task.
    
    If you have multiple long tasks to run, then you'll want a more sophisticated
    format to your messages going back to the GUI so you'll know which task finished
    
    You want to look for 3 points in this code. 
    1. Where you put your call that takes a long time
    2. Where the trigger to make the call takes place in the event loop
    3. Where the completion of the call is indicated in the event loop
"""

# Put your....

 ######  ########  ##     ##
##    ## ##     ## ##     ##
##       ##     ## ##     ##
##       ########  ##     ##
##       ##        ##     ##
##    ## ##        ##     ##
 ######  ##         #######

#### ##    ## ######## ######## ##    ##  ######  #### ##     ## ########
 ##  ###   ##    ##    ##       ###   ## ##    ##  ##  ##     ## ##
 ##  ####  ##    ##    ##       ####  ## ##        ##  ##     ## ##
 ##  ## ## ##    ##    ######   ## ## ##  ######   ##  ##     ## ######
 ##  ##  ####    ##    ##       ##  ####       ##  ##   ##   ##  ##
 ##  ##   ###    ##    ##       ##   ### ##    ##  ##    ## ##   ##
#### ##    ##    ##    ######## ##    ##  ######  ####    ###    ########

 ######   #######  ########  ########
##    ## ##     ## ##     ## ##
##       ##     ## ##     ## ##
##       ##     ## ##     ## ######
##       ##     ## ##     ## ##
##    ## ##     ## ##     ## ##
 ######   #######  ########  ########

# Here in this thread

def worker_thread(thread_name, gui_queue):
    print('Starting thread - {} '.format(thread_name))
    # LOCATION 1
    # this is our "long running function call"
    time.sleep(5)  # sleep for a while
    print('Ending thread - {} '.format(thread_name))

    # at the end of the work, before exiting, send a message back to the GUI indicating end
    # in this case, we're using a simple string
    gui_queue.put('{} - done'.format(thread_name))  # put a message into queue for GUI


########  ##     ## ####
##    ##  ##     ##  ##
##        ##     ##  ##
##   #### ##     ##  ##
##    ##  ##     ##  ##
##    ##  ##     ##  ##
########  ######### ####

def the_gui():
    gui_queue = queue.Queue()  # queue used to communicate between the gui and the threads

    layout = [[sg.Text('Multithreaded Work Example')],
              [sg.Text('', size=(25, 1), key='_OUTPUT_')],
              # [sg.Output(size=(40,6))],
              [sg.Button('Go'), sg.Button('Popup'), sg.Button('Exit')], ]

    window = sg.Window('Multithreaded Window').Layout(layout)
    # --------------------- EVENT LOOP ---------------------
    count = 0
    while True:
        event, values = window.Read(timeout=100)  # wait for up to 100 ms for a GUI event
        if event is None or event == 'Exit':
            break
        if event == 'Go':           # clicking "Go" starts a long running work item by starting thread
            window.Element('_OUTPUT_').Update('Starting long work %s'%count)
            # LOCATION 2
            # STARTING long run by starting a thread
            threading.Thread(target=worker_thread, args=('Thread %s'%count, gui_queue,), daemon=True).start()
            count += 1
        # --------------- Read next message coming in from threads ---------------
        try:
            message = gui_queue.get_nowait()   # see if something has been posted to Queue
        except queue.Empty:             # get_nowait() will get exception when Queue is empty
            message = None              # nothing in queue so do nothing

        # if message received from queue, display the message in the Window
        if message is not None:
            # LOCATION 3
            # this is the place you would execute code at ENDING of long running task
            window.Element('_OUTPUT_').Update(message)

        if event == 'Popup':
            sg.Popup('This is a popup showing that the GUI is running')
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
    the_gui()
    print('Exiting Program')