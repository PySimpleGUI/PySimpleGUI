#!/usr/bin/env python
import PySimpleGUI as sg

"""
    Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

# Example .disappear() .reappear() methods in window


layout = [[ sg.Text('My Window') ],
          [ sg.Button('Disappear')]]

window = sg.Window('My window', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Disappear':
        window.disappear()
        sg.popup('Click OK to make window reappear')
        window.reappear()

window.close()