#!/usr/bin/env python
import PySimpleGUI as sg

"""
    Demo program that reroutes stdout and stderr.
    Type something in the input box and click Print
    Whatever you typed is "printed" using a standard print statement
    Use the Output Element in your window layout to reroute stdout
    You will see the output of the print in the Output Element in the center of the window
    
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
