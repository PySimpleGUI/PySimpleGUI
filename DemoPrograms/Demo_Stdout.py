#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

"""
    Demo program that reroutes stdout and stderr.
    Type something in the input box and click Print
    Whatever you typed is "printed" using a standard print statement
    Use the Output Element in your window layout to reroute stdout
    You will see the output of the print in the Output Element in the center of the window
    
"""


layout = [
            [sg.Text('Type something in input field and click print')],
            [sg.In()],
            [sg.Output()],
            [sg.Button('Print')]
         ]

window = sg.Window('Reroute stdout').Layout(layout)

while True:     # Event Loop
    event, values = window.Read()
    if event is None:
        break
    print('You typed: ', values[0])
