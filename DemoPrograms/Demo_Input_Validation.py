import PySimpleGUI as sg

"""
    Simple field validation
    Input field should only accept digits 0-9.
    If non-digit entered, it is deleted from the field
    
    Copyright 2022-2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

layout = [[sg.Text('Enter digits:')],
          [sg.Input('', enable_events=True,  key='-INPUT-')],
          [sg.Button('Ok', key='-OK-'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    # if last char entered not a digit
    if event == '-INPUT-' and len(values['-INPUT-']) and values['-INPUT-'][-1] not in ('0123456789'):
        # delete last char from input
        window['-INPUT-'].update(values['-INPUT-'][:-1])

window.close()