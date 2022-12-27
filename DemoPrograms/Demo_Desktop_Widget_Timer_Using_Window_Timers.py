#!/usr/bin/env python
import PySimpleGUI as sg
import time

"""
    Demo Program - Timer Desktop Widget using Window.timer_start and Window.timer_stop

    This is a re-implementation of the original timer desktop widget that used window.read timeouts as
    the means of getting timer events.

    This program uses the new Window.timer_start to get timer events.  It is simpler because:
        There is only 1 call to window.read and it's in the standard location in the event loop
        The timer pause/run button uses the timer_start and timer_stop calls - perhaps more intuitive

    Note that this Demo Program requires PySimpleGUI 4.60.4.132 and greater

    Copyright 2022 PySimpleGUI
"""


def time_as_int():
    return int(round(time.time() * 100))


# ----------------  Create Form  ----------------
sg.theme('Black')

layout = [[sg.Text('')],
          [sg.Text('', size=(8, 2), font=('Helvetica', 20),
                justification='center', key='text')],
          [sg.Button('Pause', key='-RUN-PAUSE-', button_color=('white', '#001480')),
           sg.Button('Reset', button_color=('white', '#007339'), key='-RESET-'),
           sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]

window = sg.Window('Running Timer', layout,
                   no_titlebar=True,
                   auto_size_buttons=False,
                   keep_on_top=True,
                   grab_anywhere=True,
                   element_padding=(0, 0),
                   finalize=True,
                   element_justification='c',
                   right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT)

current_time, paused_time, paused = 0, 0, False
start_time = time_as_int()
timer_id = window.timer_start(10)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):        # ALWAYS give a way out of program
        break
    # --------- Handle events --------
    if event == '-RUN-PAUSE-':
        paused = not paused
        if paused:
            window.timer_stop(timer_id)
            paused_time = time_as_int()
        else:
            timer_id = window.timer_start(10)
            start_time = start_time + time_as_int() - paused_time
        window['-RUN-PAUSE-'].update('Run' if paused else 'Pause')
    elif event == sg.EVENT_TIMER:
        current_time = time_as_int() - start_time
    if event == '-RESET-':
        current_time = 0
        start_time = paused_time = time_as_int()
    elif event == 'Edit Me':
        sg.execute_editor(__file__)
    # --------- Display timer_id in window --------
    window['text'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                        (current_time // 100) % 60,
                                                        current_time % 100))
window.close()
