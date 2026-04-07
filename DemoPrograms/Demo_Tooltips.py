#!/usr/bin/env python
"""
    Example tooltip operations.
    Removal of tooltips feature added in version 5.0.2.11
    You disable a tooltip by using the remove_tooltip method or set the tooltip to the value None


    Copyright 2018-2026 PySimpleGUI. All rights reserved.


"""

import PySimpleGUI as sg

layout = [  [sg.Text('Tooltip Operations')],
            [sg.Input(key='-IN-', tooltip='My default tooltip')],
            [sg.Text(key='-OUT-')],
            [sg.Button('Remove'), sg.B('Add'), sg.B('Set None'), sg.Button('Exit')]  ]

window = sg.Window('Tooltip Test', layout, print_event_values=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Remove':
        window['-IN-'].remove_tooltip()
        window['-OUT-'].update('Tooltip removed')
    elif event == 'Add':
        window['-IN-'].set_tooltip(values['-IN-'])
        window['-OUT-'].update(f"Added tooltip {values['-IN-']}")
    elif event == 'Set None':
        window['-IN-'].set_tooltip(None)
        window['-OUT-'].update('Tooltip set to None')

window.close()
