import PySimpleGUI as sg
import threading
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

    Copyright 2021 PySimpleGUI
"""

DL_START_KEY = '-START DOWNLOAD-'
DL_COUNT_KEY = '-COUNT-'
DL_END_KEY = '-END DOWNLOAD-'


def the_thread(window:sg.Window):
    """
    The thread that communicates with the application through the window's events.

    Once a second wakes and sends a new event and associated value to the window
    """
    max_value = random.randint(50, 100)
    window.write_event_value(DL_START_KEY, max_value)  # Data sent is a tuple of thread name and counter
    for i in range(max_value):
        time.sleep(.1)
        window.write_event_value(DL_COUNT_KEY, i)  # Data sent is a tuple of thread name and counter
    window.write_event_value(DL_END_KEY, max_value)  # Data sent is a tuple of thread name and counter


def main():
    layout = [  [sg.Text('My Window')],
                [sg.ProgressBar(100, 'h', size=(30,20), k='-PROGRESS-')],
                [sg.Button('Go'), sg.Button('Exit')]  ]

    window = sg.Window('Window Title', layout, finalize=True)
    window.read(timeout=0)
    window.move(window.current_location()[0], window.current_location()[1]-300)
    downloading, max_value = False, 0

    while True:             # Event Loop
        event, values = window.read()
        # print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Go' and not downloading:
            threading.Thread(target=the_thread, args=(window,), daemon=True).start()
        elif event == DL_START_KEY:
            max_value = values[event]
            downloading = True
            sg.one_line_progress_meter(f'Downloading {max_value} segments', 0, max_value, 1, f'Downloading {max_value} segments', )
            window['-PROGRESS-'].update(0, max_value)
        elif event == DL_COUNT_KEY:
            sg.one_line_progress_meter(f'Downloading {max_value} segments', values[event]+1, max_value, 1, f'Downloading {max_value} segments')
            window['-PROGRESS-'].update(values[event]+1, max_value)
        elif event == DL_END_KEY:
            downloading = False

    window.close()

if __name__ == '__main__':
    main()
