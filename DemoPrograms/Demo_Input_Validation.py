import PySimpleGUI as sg

"""
    Simple field validation
    Input field should only accept digits.
    If non-digit entered, it is deleted from the field
"""

layout = [[sg.Text('Enter digits:')],
          [sg.Input('', enable_events=True,  key='-INPUT-')],
          [sg.Button('Ok', key='-OK-'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    # if last char entered not a digit
    if len(values['-INPUT-']) and values['-INPUT-'][-1] not in ('0123456789'):
        # delete last char from input
        window['-INPUT-'].update(values['-INPUT-'][:-1])

window.close()
