import time
import PySimpleGUI as sg


"""
    Threaded Demo - Uses Window.write_event_value communications
    
    The only PySimpleGUI call allowed from a thread is write_event_value.
    Using a tuple for thread events makes processing them easier to see and understand.

    
    Copyright 2020-2024 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""


def the_thread(window):
    """
    The thread that communicates with the application through the window's events.

    Once a second wakes and sends a new event and associated value to the window
    """

    window.write_event_value(('-THREAD-', '-STARTED-'), None)  # Tell the GUI the thread started

    for i in range(5):
        time.sleep(1)
        window.write_event_value(('-THREAD-', '-PRINT-'), i)      # Data sent is a tuple of thread name and counter
    # Note that the thread ended event is sent automatically by PySimpleGUI if you started the thread using window.start_thread

def main():
    """
    The demo will display in the multiline info about the event and values dictionary as it is being
    returned from window.read()
    Every time "Start" is clicked a new thread is started
    Try clicking "Dummy" to see that the window is active while the thread stuff is happening in the background
    """

    layout = [  [sg.Text('Output Area - cprint\'s route to here', font='Any 15')],
                [sg.Multiline(size=(65,20), key='-ML-', autoscroll=True, reroute_stdout=True, write_only=True, reroute_cprint=True)],
                [sg.T('Input so you can see data in your dictionary')],
                [sg.Input(key='-IN-', size=(30,1))],
                [sg.B('Start A Thread', key='-START-'), sg.B('Dummy'), sg.Button('Exit')]  ]

    window = sg.Window('Multithreading + Tuple Events', layout)

    while True:             # Event Loop
        event, values = window.read()
        sg.cprint(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == '-START-':
            window.start_thread(lambda : the_thread(window), ('-THREAD-', '-ENDED-'))
        if event[0] == '-THREAD-':
            if event[1] == '-PRINT-':
                sg.cprint(f'Data from the thread ', colors='white on purple', end='')
                sg.cprint(f'{values[event]}', colors='white on red')
            elif event[1] == '-ENDED-':
                sg.cprint('Thread has ended', colors='white on blue')
            elif event[1] == '-STARTED-':
                sg.cprint('Thread has started', colors='white on green')

    window.close()


if __name__ == '__main__':
    main()