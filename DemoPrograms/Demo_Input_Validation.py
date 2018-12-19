import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

"""
    Simple field validation
    Input field should only accept digits.
    If non-digit entered, it is deleted from the field
"""

layout = [[sg.Text('Enter digits:')],
            [sg.Input(do_not_clear=True, enable_events=True,  key='_INPUT_')],
            [sg.Button('Ok', key='_OK_'),sg.Button('Exit')]]

window = sg.Window('Window Title').Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    if event in  (None, 'Exit'):
        break
    if len(values['_INPUT_']) and values['_INPUT_'][-1] not in ('0123456789'):  # if last char entered not a digit
        window.Element('_INPUT_').Update(values['_INPUT_'][:-1])                # delete last char from input
window.Close()
