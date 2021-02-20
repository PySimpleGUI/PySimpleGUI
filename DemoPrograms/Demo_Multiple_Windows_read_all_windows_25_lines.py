#!/usr/bin/env python
"""
    Demo - Multiple read_all_window(timeout=20)
        A 2-window event loop run in async mode

    Super-simple, 25 lines of code.

    Copyright 2021 PySimpleGUI
"""

import PySimpleGUI as sg

sg.set_options(font='_ 18')

window1 = sg.Window('ONE', [[sg.T('Window 1',size=(30,1),k='-T-')],[sg.B('Run', k='-B-'), sg.B('Exit')]],
                    finalize=True)

window2 = sg.Window('TWO', [[sg.T('Window 2',k='-T-')],[sg.B('Run', k='-B-'),sg.B('Exit')]], finalize=True,
                    location=(window1.current_location()[0]-250,window1.current_location()[1]))

i, paused = 0, [False, False]

while True:             # Event Loop
    window, event, values = sg.read_all_windows(timeout=10)
    print(window, event, values) if event != sg.TIMEOUT_EVENT else None
    if window == sg.WIN_CLOSED and event == sg.WIN_CLOSED:
        window1.close()
        window2.close()
        sg.popup_auto_close('Exiting...')
        break
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        window.close()
    if not paused[0]:
        window1['-T-'].update('{:02d}:{:02d}.{:02d}'.format((i // 100) // 60, (i // 100) % 60, i % 100))
    if not paused[1]:
        window2['-T-'].update('{:02d}:{:02d}.{:02d}'.format((i // 100) // 60, (i // 100) % 60, i % 100))
    if event == '-B-':
        paused[0 if window == window1 else 1] = not paused[0 if window == window1 else 1]
        window['-B-'].update('Run' if not paused[0 if window == window1 else 1] else 'Pause')
    i += 1