import PySimpleGUI as sg
import random
import time
import queue

"""
    Demo - Multi-threaded "Data Pump" Design Pattern

    Send data to your PySimpleGUI program through a Python Queue, enabling integration with many
    different types of data sources.

    A thread gets data from a queue object and passes it over to the main event loop.
    The external_thread is only used here to generaate random data.  It's not part of the
    overall "Design Pattern".
    
    The thread the_thread IS part of the design pattern.  It reads data from the thread_queue and sends that
    data over to the PySimpleGUI event loop.

    Copyright 2022 PySimpleGUI
"""

gsize = (400, 400)  # size of the graph

THREAD_KEY = '-THREAD-'
THREAD_INCOMING_DATA = '-INCOMING DATA-'
THREAD_EXITNG = '-THREAD EXITING-'
THREAD_EXTERNAL_EXITNG = '-EXTERNAL THREAD EXITING-'

# This queue is where you will send your data that you want to eventually arrive as an event
thread_queue = queue.Queue()

# M""""""""M dP                                        dP
# Mmmm  mmmM 88                                        88
# MMMM  MMMM 88d888b. 88d888b. .d8888b. .d8888b. .d888b88
# MMMM  MMMM 88'  `88 88'  `88 88ooood8 88'  `88 88'  `88
# MMMM  MMMM 88    88 88       88.  ... 88.  .88 88.  .88
# MMMM  MMMM dP    dP dP       `88888P' `88888P8 `88888P8
# MMMMMMMMMM
#
# MP""""""`MM oo                     dP            dP   oo
# M  mmmmm..M                        88            88
# M.      `YM dP 88d8b.d8b. dP    dP 88 .d8888b. d8888P dP 88d888b. .d8888b.
# MMMMMMM.  M 88 88'`88'`88 88    88 88 88'  `88   88   88 88'  `88 88'  `88
# M. .MMM'  M 88 88  88  88 88.  .88 88 88.  .88   88   88 88    88 88.  .88
# Mb.     .dM dP dP  dP  dP `88888P' dP `88888P8   dP   dP dP    dP `8888P88
# MMMMMMMMMMM                                                            .88
#                                                                    d8888P
# M""""""'YMM            dP               MP""""""`MM
# M  mmmm. `M            88               M  mmmmm..M
# M  MMMMM  M .d8888b. d8888P .d8888b.    M.      `YM .d8888b. dP    dP 88d888b. .d8888b. .d8888b.
# M  MMMMM  M 88'  `88   88   88'  `88    MMMMMMM.  M 88'  `88 88    88 88'  `88 88'  `"" 88ooood8
# M  MMMM' .M 88.  .88   88   88.  .88    M. .MMM'  M 88.  .88 88.  .88 88       88.  ... 88.  ...
# M       .MM `88888P8   dP   `88888P8    Mb.     .dM `88888P' `88888P' dP       `88888P' `88888P'
# MMMMMMMMMMM                             MMMMMMMMMMM
#

def external_thread(thread_queue:queue.Queue):
    """
    Represents some external source of data.
    You would not include this code as a starting point with this Demo Program. Your data is assumed to
    come from somewhere else. The important part is that you add data to the thread_queue
    :param thread_queue:
    :return:
    """
    i = 0
    while True:
        time.sleep(.01)
        point = (random.randint(0,gsize[0]), random.randint(0,gsize[1]))
        radius = random.randint(10, 40)
        thread_queue.put((point, radius))
        i += 1


# M""""""""M dP                                        dP    MM""""""""`M
# Mmmm  mmmM 88                                        88    MM  mmmmmmmM
# MMMM  MMMM 88d888b. 88d888b. .d8888b. .d8888b. .d888b88    M'      MMMM .d8888b. 88d888b.
# MMMM  MMMM 88'  `88 88'  `88 88ooood8 88'  `88 88'  `88    MM  MMMMMMMM 88'  `88 88'  `88
# MMMM  MMMM 88    88 88       88.  ... 88.  .88 88.  .88    MM  MMMMMMMM 88.  .88 88
# MMMM  MMMM dP    dP dP       `88888P' `88888P8 `88888P8    MM  MMMMMMMM `88888P' dP
# MMMMMMMMMM                                                 MMMMMMMMMMMM
#
# MM"""""""`YM MP""""""`MM MM'"""""`MM    MM""""""""`M                              dP
# MM  mmmmm  M M  mmmmm..M M' .mmm. `M    MM  mmmmmmmM                              88
# M'        .M M.      `YM M  MMMMMMMM    M`      MMMM dP   .dP .d8888b. 88d888b. d8888P .d8888b.
# MM  MMMMMMMM MMMMMMM.  M M  MMM   `M    MM  MMMMMMMM 88   d8' 88ooood8 88'  `88   88   Y8ooooo.
# MM  MMMMMMMM M. .MMM'  M M. `MMM' .M    MM  MMMMMMMM 88 .88'  88.  ... 88    88   88         88
# MM  MMMMMMMM Mb.     .dM MM.     .MM    MM        .M 8888P'   `88888P' dP    dP   dP   `88888P'
# MMMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM    MMMMMMMMMMMM


def the_thread(window:sg.Window, thread_queue:queue.Queue):
    """
    The thread that communicates with the application through the window's events.
    Waits for data from a queue and sends that data on to the event loop
    :param window:
    :param thread_queue:
    :return:
    """

    while True:
        data = thread_queue.get()
        window.write_event_value((THREAD_KEY, THREAD_INCOMING_DATA), data)  # Data sent is a tuple of thread name and counter


def main():

    layout = [  [sg.Text('My Simulated Data Pump')],
                [sg.Multiline(size=(60, 20), k='-MLINE-')],
                [sg.Graph(gsize, (0, 0), gsize, k='-G-', background_color='gray')],
                [sg.Button('Go'), sg.Button('Exit')] ]

    window = sg.Window('Simulated Data Pump', layout, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT)

    graph = window['-G-']       # type: sg.Graph

    while True:             # Event Loop
        event, values = window.read()
        # print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Go':
            window.start_thread(lambda: the_thread(window, thread_queue), (THREAD_KEY, THREAD_EXITNG))
            window.start_thread(lambda: external_thread(thread_queue), (THREAD_KEY, THREAD_EXTERNAL_EXITNG))
        # Events coming from the Thread
        elif event[0] == THREAD_KEY:
            if event[1] == THREAD_INCOMING_DATA:
                point, radius = values[event]
                graph.draw_circle(point, radius=radius, fill_color='green')
                window['-MLINE-'].print(f'Drawing at {point} radius {radius}', c='white on red')
            elif event[1] == THREAD_EXITNG:
                window['-MLINE-'].print('Thread has exited')
            elif event[1] == THREAD_EXTERNAL_EXITNG:
                window['-MLINE-'].print('Data Pump thread has exited')
        if event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Version':
            sg.popup_scrolled(__file__, sg.get_versions(), location=window.current_location(), keep_on_top=True, non_blocking=True)

    window.close()

if __name__ == '__main__':
    main()
