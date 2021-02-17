import threading
import time
import PySimpleGUI as sg

"""
    Threaded Demo - Uses Window.write_event_value to communicate from thread to GUI
    
    A demo specifically to show how to use write_event_value to
        "show a popup from a thread"
        
    You cannot make any direct calls into PySimpleGUI from a thread
    except for Window.write_event_value()
    Cuation - This method still has a risk of tkinter crashing
    
    Copyright 2021 PySimpleGUI
"""


def the_thread(window:sg.Window, seconds):
    """
    The thread that communicates with the application through the window's events.

    Wakes every X seconds that are provided by user in the main GUI:
        Sends an event to the main thread
        Goes back to sleep
    """
    i = 0
    while True:
        time.sleep(seconds)
        # send a message to the main GUI. It will be read using window.read()
        # the "Value" send is a tuple that contains all the things to show in the popup
        window.write_event_value('-POPUP-',
                                 ('Hello this is the thread...',
                                  f'My counter is {i}',
                                  f'Will send another message in {seconds} seconds'))
        i += 1


def main():
    """
    Every time "Start A Thread" is clicked a new thread is started
    When the event is received from the thread, a popup is shown in its behalf
    """

    layout = [  [sg.Output(size=(60,10))],
                [sg.T('How often a thread will show a popup in seconds'),
                 sg.Spin((2, 5, 10, 20), initial_value=5, k='-SPIN-')],
                [sg.B('Start A Thread'), sg.B('Dummy'), sg.Button('Exit')]  ]

    window = sg.Window('Window Title', layout, finalize=True, font='_ 15')


    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == '-POPUP-':
            sg.popup_non_blocking('This is a popup that the thread wants to show',
                     *values['-POPUP-'])
        elif event == 'Start A Thread':
            print(f'Starting thread.  You will see a new popup every {values["-SPIN-"]} seconds')
            threading.Thread(target=the_thread, args=(window, values['-SPIN-']), daemon=True).start()

    window.close()


if __name__ == '__main__':
    main()