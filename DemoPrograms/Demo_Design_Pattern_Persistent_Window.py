import PySimpleGUI as sg

"""
    The basic PySimpleGUI design pattern for a persistent window that is
    updated using data input from one of the elements.
    
    Copyright 2020 PySimpleGUI.org
"""

layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(20, 1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # change the "output" element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()
