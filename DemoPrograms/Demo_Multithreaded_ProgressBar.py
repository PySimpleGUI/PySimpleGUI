import PySimpleGUI as sg
import random
import time

"""
    Demo - Multi-threaded downloader with one_line_progress_meter

    Sometimes you don't have a choice in how your data is downloaded.  In some programs
    the download happens in another thread which means you cannot call PySimpleGUI directly
    from the thread.

    Maybe you're still interested in using the one_line_progress_meter feature or perhaps
    have implemented your own progress meter in your window.

    Using the write_event_value method enables you to easily do either of these.
    
    In this demo, all thread events are a TUPLE with the first item in tuple being THREAD_KEY ---> '-THEAD-'
        This allows easy separation of all of the thread-based keys into 1 if statment:
            elif event[0] == THREAD_KEY:
    Example
        (THREAD_KEY, DL_START_KEY) indicates the download is starting and provices the Max value
        (THREAD_KEY, DL_END_KEY) indicates the downloading has completed
        
    The main window uses a relative location when making the window so that the one-line-progress-meter has room

    Copyright 2021, 2022 PySimpleGUI
"""

THREAD_KEY = '-THREAD-'
DL_START_KEY = '-START DOWNLOAD-'
DL_COUNT_KEY = '-COUNT-'
DL_END_KEY = '-END DOWNLOAD-'
DL_THREAD_EXITNG = '-THREAD EXITING-'

def the_thread(window:sg.Window):
    """
    The thread that communicates with the application through the window's events.

    Simulates downloading a random number of chinks from 50 to 100-
    """
    max_value = random.randint(50, 100)
    window.write_event_value((THREAD_KEY, DL_START_KEY), max_value)  # Data sent is a tuple of thread name and counter
    for i in range(max_value):
        time.sleep(.1)
        window.write_event_value((THREAD_KEY, DL_COUNT_KEY), i)  # Data sent is a tuple of thread name and counter
    window.write_event_value((THREAD_KEY, DL_END_KEY), max_value)  # Data sent is a tuple of thread name and counter


def main():
    layout = [  [sg.Text('My Multi-threaded PySimpleGUI Program')],
                [sg.ProgressBar(100, 'h', size=(30,20), k='-PROGRESS-', expand_x=True)],
                [sg.Text(key='-STATUS-')],
                [sg.Button('Go'), sg.Button('Exit')]  ]

    window = sg.Window('Window Title', layout, finalize=True, relative_location=(0, -300))
    downloading, max_value = False, 0

    while True:             # Event Loop
        event, values = window.read()
        # print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Go' and not downloading:
            window.start_thread(lambda: the_thread(window), (THREAD_KEY, DL_THREAD_EXITNG))
        # Events coming from the Thread
        elif event[0] == THREAD_KEY:
            if event[1] == DL_START_KEY:
                max_value = values[event]
                downloading = True
                window['-STATUS-'].update('Starting download')
                sg.one_line_progress_meter(f'Downloading {max_value} segments', 0, max_value, 1, f'Downloading {max_value} segments', )
                window['-PROGRESS-'].update(0, max_value)
            elif event[1] == DL_COUNT_KEY:
                sg.one_line_progress_meter(f'Downloading {max_value} segments', values[event]+1, max_value, 1, f'Downloading {max_value} segments')
                window['-STATUS-'].update(f'Got a new current count update {values[event]}')
                window['-PROGRESS-'].update(values[event]+1, max_value)
            elif event[1] == DL_END_KEY:
                downloading = False
                window['-STATUS-'].update('Download finished')
            elif event[1] == DL_THREAD_EXITNG:
                window['-STATUS-'].update('Last step - Thread has exited')

    window.close()

if __name__ == '__main__':
    main()
