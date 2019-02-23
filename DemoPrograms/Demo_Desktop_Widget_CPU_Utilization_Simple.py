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

layout = [[sg.Text('CPU Utilization')],
          [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='_text_')],
          [sg.Exit(button_color=('white', 'firebrick4'), pad=((15, 0), 0), size=(9,1)),
           sg.Spin([x + 1 for x in range(10)], 3, key='_spin_')]]

# Layout the rows of the Window
window = sg.Window('CPU Meter',
                   no_titlebar=True,
                   keep_on_top=True,
                   grab_anywhere=True).Layout(layout).Finalize()

# ----------------  main loop  ----------------
interval = 10            # For the first one, make it quick
while (True):
    # --------- Read and update window --------
    event, values = window.Read(timeout=interval)
    # --------- Do Button Operations --------
    if event is None or event == 'Exit':
        break

    interval = int(values['_spin_'])*1000



    cpu_percent = psutil.cpu_percent(interval=1)

    # --------- Display timer in window --------

    window.FindElement('_text_').Update(f'CPU {cpu_percent:02.0f}%')

# Broke out of main loop. Close the window.
window.CloseNonBlocking()