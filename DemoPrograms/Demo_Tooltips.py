#!/usr/bin/env python
"""
    Example tooltip operations.
    Removal of tooltips feature added in version 5.0.2.11
    You disable a tooltip by using the remove_tooltip method or set the tooltip to the value None


    Copyright 2024 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
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
