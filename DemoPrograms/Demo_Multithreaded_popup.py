import threading
import time
import PySimpleGUI as sg
import queue

"""
    Threading Demo - "Call popup from a thread"

    Can be extended to call any PySimpleGUI function by passing the function through the queue


    Safest approach to threading is to use a Queue object to communicate
    between threads and maintrhead.

    The thread calls popup, a LOCAL function that should be called with the same
    parameters that would be used to call opiup when called directly

    The parameters passed to the local popup are passed through a queue to the main thread.
    When a messages is received from the queue, sg.popup is called using the parms passed
    through the queue
    
    Copyright 2021 PySimpleGUI.org
"""

mainthread_queue:queue.Queue = None

def popup(*args, **kwargs):
    if mainthread_queue:
        mainthread_queue.put((args, kwargs))

def the_thread(count):
    """
    The thread that communicates with the application through the window's events.

    Once a second wakes and sends a new event and associated value to the window
    """
    i = 0
    while True:
        time.sleep(2)
        popup(f'Hello, this is the thread #{count}', 'My counter value', i, text_color='white', background_color='red', non_blocking=True, keep_on_top=True, location=(1000-200*count, 400))
        i += 1


def process_popup():
    try:
        queued_value = mainthread_queue.get_nowait()
        sg.popup_auto_close(*queued_value[0], **queued_value[1])
    except queue.Empty:     # get_nowait() will get exception when Queue is empty
        pass


def main():
    """
    The demo will display in the multiline info about the event and values dictionary as it is being
    returned from window.read()
    Every time "Start" is clicked a new thread is started
    Try clicking "Dummy" to see that the window is active while the thread stuff is happening in the background
    """
    global mainthread_queue

    mainthread_queue = queue.Queue()

    layout = [  [sg.Text('Output Area - cprint\'s route to here', font='Any 15')],
                [sg.Multiline(size=(65,20), key='-ML-', autoscroll=True, reroute_stdout=True, write_only=True, reroute_cprint=True)],
                [sg.T('Input so you can see data in your dictionary')],
                [sg.Input(key='-IN-', size=(30,1))],
                [sg.B('Start A Thread'), sg.B('Dummy'), sg.Button('Exit')]  ]

    window = sg.Window('Window Title', layout, finalize=True, keep_on_top=True)
    count = 0
    while True:             # Event Loop
        event, values = window.read(timeout=500)
        sg.cprint(event, values) if event != sg.TIMEOUT_EVENT else None
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        process_popup()
        if event.startswith('Start'):
            threading.Thread(target=the_thread, args=(count,), daemon=True).start()
            count += 1
    window.close()


if __name__ == '__main__':
    main()