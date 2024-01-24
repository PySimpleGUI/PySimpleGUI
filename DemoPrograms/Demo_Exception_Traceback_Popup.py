import PySimpleGUI as sg

"""
    Demo - Show an error popup with traceback information

    Copyright 2022 PySimpleGUI
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
