import PySimpleGUI as sg

"""
    Demo - Show an error popup with traceback information

    Copyright 2021-2024 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""


layout = [  [sg.Text('Choose the type of error to generate')],
            [sg.Button('Go'), sg.B('Key Error'), sg.B('Div 0'), sg.Button('Exit')]  ]

window = sg.Window('Exception Handling and Error Information Display', layout)

while True:             # Event Loop
    try:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        # When choice has been made, then fill in the listbox with the choices
        if event == 'Key Error':
            window['bad key']
        elif event == 'Div 0':
            a = 1/0
    except Exception as e:
        sg.popup_error_with_traceback('Error in the event loop', e, emoji=sg.EMOJI_BASE64_SCREAM)
window.close()
