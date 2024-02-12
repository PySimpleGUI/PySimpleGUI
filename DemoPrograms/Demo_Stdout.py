#!/usr/bin/env python
import PySimpleGUI as sg

"""
    Demo program that reroutes stdout and stderr.
    Type something in the input box and click Print
    Whatever you typed is "printed" using a standard print statement
    Use the Output Element in your window layout to reroute stdout
    You will see the output of the print in the Output Element in the center of the window
    
    Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
    
"""


layout = [
    [sg.Text('Type something in input field and click print')],
    [sg.Input()],
    [sg.Output()],
    [sg.Button('Print')]
]

window = sg.Window('Reroute stdout', layout)

while True:     # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    print('You typed: ', values[0])
window.close()
