import time
import datetime
import PySimpleGUI as sg

"""
    Multithreading with signaling to thread when to stop.
    If exiting the program, waits for the thread to finish.

    In this example, the thread runs at a rate of twice a second.  It sends the time as a string
    The main GUI checks the value sent by the thread to see if it differs from what is displayed.
    If the display is different, then the GUI is updated with the new time.

    Copyright 2020-2024 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.

"""


#   dP   dP                                        dP
#   88   88                                        88
# d8888P 88d888b. 88d888b. .d8888b. .d8888b. .d888b88
#   88   88'  `88 88'  `88 88ooood8 88'  `88 88'  `88
#   88   88    88 88       88.  ... 88.  .88 88.  .88
#   dP   dP    dP dP       `88888P' `88888P8 `88888P8
#

def the_thread(window):

    while window.job_running:
        window.write_event_value('-THREAD-', datetime.datetime.now().strftime('%H:%M:%S'))
        time.sleep(0.5)


#                     oo
#
# 88d8b.d8b. .d8888b. dP 88d888b.
# 88'`88'`88 88'  `88 88 88'  `88
# 88  88  88 88.  .88 88 88    88
# dP  dP  dP `88888P8 dP dP    dP

def main():

    layout = [
        [sg.Text('00:00:00', font=('Courier New', 20, 'bold'), justification='center', expand_x=True, key='-TIME-')],
        [sg.Push(), sg.Button('Start'), sg.Button('Stop')]]

    window = sg.Window('Threading', layout, enable_close_attempted_event=True,
                       print_event_values=True,         # enable to watch the events and values print out
                       )

    window.job_running = False      # Create a member variable to signal to the thread when to stop
    exiting = False                 # Used when X is clicked

    while True:

        event, values = window.read()

        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            if window.job_running:  # if thread running, tell it to exit
                window.job_running = False
                exiting = True
            else:
                break               # if thread not running then OK to exit

        if exiting and event == '-THREAD ENDED-':  # If exiting and thread is finished then OK to exit
            break

        elif event == 'Start':
            window['Start'].update(disabled=True)
            window.job_running = True
            window.start_thread(lambda: the_thread(window), '-THREAD ENDED-')

        elif event == 'Stop':
            window.job_running = False
            window['Start'].update(disabled=False)

        elif event == '-THREAD-' and values[event] != window['-TIME-'].get():
            window['-TIME-'].update(values[event])

    window.close()

if __name__ == '__main__':
    main()