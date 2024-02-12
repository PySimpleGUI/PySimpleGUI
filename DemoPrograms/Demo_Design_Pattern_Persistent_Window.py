import PySimpleGUI as sg

"""
    Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

layout = [
    [sg.Text('Your typed chars appear here:'),
     sg.Text(size=(20, 1), key='-OUTPUT-')],
    [sg.Input('', key='-IN-')],
    [sg.Button('Show'), sg.Button('Exit')]
]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Show':
        # change the "output" element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()
