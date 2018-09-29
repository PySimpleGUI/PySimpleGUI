#!/usr/bin/env python
import sys
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

import psutil

# ----------------  Create Form  ----------------
sg.ChangeLookAndFeel('Black')
layout = [[sg.Text('')],
             [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
             [sg.Exit(button_color=('white', 'firebrick4'), pad=((15, 0), 0)),
              sg.Spin([x + 1 for x in range(10)], 1, key='spin')]]
# Layout the rows of the form and perform a read. Indicate the form is non-blocking!
window = sg.Window('CPU Meter', no_titlebar=True, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True).Layout(layout)

# ----------------  main loop  ----------------
while (True):
    # --------- Read and update window --------
    button, values = window.ReadNonBlocking()

    # --------- Do Button Operations --------
    if values is None or button == 'Exit':
        break
    try:
        interval = int(values['spin'])
    except:
        interval = 1

    cpu_percent = psutil.cpu_percent(interval=interval)

    # --------- Display timer in window --------

    window.FindElement('text').Update(f'CPU {cpu_percent:02.0f}%')

# Broke out of main loop. Close the window.
window.CloseNonBlocking()