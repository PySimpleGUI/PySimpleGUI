#!/usr/bin/env python
import PySimpleGUI as sg
import psutil

# Yet another usage of CPU data

# ----------------  Create Form  ----------------
sg.theme('Black')

layout = [[sg.Text('CPU Utilization')],
          [sg.Text('', size=(8, 2), font=('Helvetica', 20),
                justification='center', key='-text-')],
          [sg.Exit(button_color=('white', 'firebrick4'), pad=((15, 0), 0), size=(9, 1)),
           sg.Spin([x + 1 for x in range(10)], 3, key='-spin-')]]

# Layout the rows of the Window
window = sg.Window('CPU Meter',
                   layout,
                   no_titlebar=True,
                   keep_on_top=True,
                   grab_anywhere=True, finalize=True)

# ----------------  main loop  ----------------
interval = 10            # For the first one, make it quick
while True:
    # --------- Read and update window --------
    event, values = window.read(timeout=interval)
    # --------- Do Button Operations --------
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    interval = int(values['-spin-'])*1000

    cpu_percent = psutil.cpu_percent(interval=1)

    # --------- Display timer in window --------

    window['-text-'].update(f'CPU {cpu_percent:02.0f}%')

# Broke out of main loop. Close the window.
window.close()
