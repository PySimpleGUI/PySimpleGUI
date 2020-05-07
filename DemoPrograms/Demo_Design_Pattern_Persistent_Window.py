import PySimpleGUI as sg

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
