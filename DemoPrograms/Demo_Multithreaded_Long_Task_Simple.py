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


def long_operation_thread(seconds, window):
    """
    A worker thread that communicates with the GUI through a global message variable
    This thread can block for as long as it wants and the GUI will not be affected
    :param seconds: (int) How long to sleep, the ultimate blocking call
    """
    progress = 0
    print('Thread started - will sleep for {} seconds'.format(seconds))
    for i in range(int(seconds * 10)):
        time.sleep(.1)  # sleep for a while
        progress += 100 / (seconds * 10)
        window.write_event_value('-PROGRESS-', progress)

    window.write_event_value('-THREAD-', '*** The thread says.... "I am finished" ***')

def the_gui():
    """
    Starts and executes the GUI
    Reads data from a global variable and displays
    Returns when the user exits / closes the window
    """

    sg.theme('Light Brown 3')

    layout = [[sg.Text('Long task to perform example')],
              [sg.MLine(size=(80, 12), k='-ML-', reroute_stdout=True,write_only=True, autoscroll=True, auto_refresh=True)],
              [sg.Text('Number of seconds your task will take'),
               sg.Input(key='-SECONDS-', focus=True, size=(5, 1)),
               sg.Button('Do Long Task', bind_return_key=True),
               sg.CBox('ONE chunk, cannot break apart', key='-ONE CHUNK-')],
              [sg.Text('Work progress'), sg.ProgressBar(100, size=(20, 20), orientation='h', key='-PROG-')],
              [sg.Button('Click Me'), sg.Button('Exit')], ]

    window = sg.Window('Multithreaded Demonstration Window', layout, finalize=True)

    timeout = thread = None
    # --------------------- EVENT LOOP ---------------------
    while True:
        event, values = window.read(timeout=timeout)
        # print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event.startswith('Do') and not thread:
            print('Thread Starting! Long work....sending value of {} seconds'.format(float(values['-SECONDS-'])))
            timeout = 100 if values['-ONE CHUNK-'] else None
            thread = threading.Thread(target=long_operation_thread, args=(float(values['-SECONDS-']),window), daemon=True)
            thread.start()
            if values['-ONE CHUNK-']:
                sg.popup_animated(sg.DEFAULT_BASE64_LOADING_GIF, background_color='white', transparent_color='white', time_between_frames=100)
        elif event == 'Click Me':
            print('Your GUI is alive and well')
        elif event == '-PROGRESS-':
            if not values['-ONE CHUNK-']:
                window['-PROG-'].update_bar(values[event], 100)
        elif event == '-THREAD-':            # Thread has completed
            thread.join(timeout=0)
            print('Thread finished')
            sg.popup_animated(None)                     # stop animination in case one is running
            thread, message, progress, timeout = None, '', 0, None     # reset variables for next run
            window['-PROG-'].update_bar(0,0)            # clear the progress bar
        if values['-ONE CHUNK-'] and thread is not None:
            sg.popup_animated(sg.DEFAULT_BASE64_LOADING_GIF, background_color='white', transparent_color='white', time_between_frames=100)
    window.close()


if __name__ == '__main__':
    the_gui()
    print('Exiting Program')
